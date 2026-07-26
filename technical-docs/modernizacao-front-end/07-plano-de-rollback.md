# 07 — Plano de rollback

Procedimento para interromper, descartar ou reverter a migração Tailwind 4 sem afetar produção.

## Cenário 1 — Interromper migração em andamento (branch local não integrada)

Estado: trabalhando em `dev/tailwind-v4-vite-local`, decidiu-se abortar antes de merge.

### Passos

```bash
# 1. Garantir working tree limpo (commit ou stash antes de sair da branch)
git status --short
git stash   # se houver mudanças não commitadas que valem preservar
# ou:
git checkout .   # se não valem — DESCARTA MUDANÇAS

# 2. Voltar para main
git switch main

# 3. Confirmar main intocada
git log --oneline -3     # deve estar em 13bd3e105 (HEAD antes da migração)
git status --short       # deve estar limpo

# 4. Restaurar node_modules ao estado do package-lock atual
npm ci

# 5. Deletar a branch dev
git branch -D dev/tailwind-v4-vite-local
git branch -vv           # confirmar que ela sumiu

# 6. Verificar que remoto NÃO tem essa branch
git ls-remote origin | grep tailwind-v4 || echo "OK — não existe no remoto"

# 7. (Opcional) Remover tag de backup
git tag -d pre-tailwind-v4-YYYYMMDD
```

**Verificações finais:**

- `git branch -vv` mostra apenas `main` local
- `git remote -v` mostra apenas `origin`
- `git status --short` está vazio
- Site produção não foi afetado (nunca houve push)

## Cenário 2 — Restaurar dependências

Se `npm install`, `npm update`, `npx @tailwindcss/upgrade`, ou `npm uninstall` alteraram `node_modules/`, `package.json` ou `package-lock.json`:

```bash
git checkout package.json package-lock.json
npm ci                # reinstala do lock canônico
npm ls --depth=0      # confirma versões esperadas
```

Se o `package-lock.json` local foi perdido:

```bash
git show 13bd3e105:package-lock.json > package-lock.json
npm ci
```

## Cenário 3 — Reverter parcialmente (aproveitar alguns arquivos)

Se quiser preservar certos fixes (ex.: reversão manual das opacidades) mas descartar o resto:

```bash
# 1. Estar em dev/tailwind-v4-vite-local com commits
git log --oneline -20

# 2. Identificar commit(s) desejado(s) — ex.: fix de opacity
git show <sha>

# 3. Voltar para main
git switch main

# 4. Cherry-pick apenas commits desejados
git cherry-pick <sha1> <sha2>

# 5. Continuar como se fossem commits normais
```

**Precaução:** cherry-pick NÃO é push. Push só ocorre com autorização explícita separada.

## Cenário 4 — Migração já mergeada e regressão descoberta em produção

Estado: merge para `main` já aconteceu, push já ocorreu, GitHub Pages já publicou, mas bug crítico apareceu.

### Opção A — Revert cirúrgico (preferido)

```bash
# 1. Identificar o merge commit
git log --oneline --merges -5

# 2. Reverter o merge (cria um novo commit que desfaz)
git revert -m 1 <merge-sha>
# Ou reverter commits individuais se cada um for atômico
git revert <sha1> <sha2> <sha3>

# 3. Rebuild docs/
npm run build

# 4. Commit e push (COM autorização)
git add -A
git commit -m "Revert Tailwind 4 migration por regressão em produção — ver #<issue>"
git push origin main
```

Aguardar 1-2min para GitHub Pages redeploy.

### Opção B — Reset hard (destrutivo, evitar)

```bash
# Só se revert for inviável e stakeholder aprovou.
git reset --hard pre-tailwind-v4-YYYYMMDD
git push --force-with-lease origin main   # NUNCA sem autorização
```

**Riscos:** perde histórico dos commits pós-migração; force-push em `main` é anti-pattern em repos compartilhados.

## Cenário 5 — Rollback de emergência (site quebrado)

Se produção está quebrada e não temos tempo para revert cuidadoso:

```bash
# 1. Restaurar apenas docs/ (o que serve o site)
git checkout pre-tailwind-v4-YYYYMMDD -- docs/

# 2. Commit e push
git add docs/
git commit -m "Emergency: restaura docs/ da tag pre-tailwind-v4-YYYYMMDD"
git push origin main
```

Isso volta o SITE PUBLICADO ao estado da tag, mas mantém as fontes atualizadas na branch. Cria dessincronia temporária entre fontes e site — resolver depois.

## Verificação de que produção não foi alterada durante migração local

Executar a qualquer momento durante o desenvolvimento local:

```bash
# 1. Confirmar HEAD local = último HEAD conhecido antes da migração
git rev-parse HEAD     # esperado: 13bd3e105 (ou o commit mais recente da tag pre-migration)

# 2. Confirmar remoto não recebeu push
git fetch origin
git log HEAD..origin/main --oneline    # esperado: vazio
git log origin/main..HEAD --oneline    # se em main, vazio; se em dev, pode ter commits locais

# 3. Confirmar branch dev não foi pushada
git ls-remote origin dev/tailwind-v4-vite-local   # esperado: vazio

# 4. Site produção continua no HEAD antigo
curl -sI https://cedis.unb.br/ | grep -i "last-modified\|etag"

# 5. GitHub Pages não teve deploy recente
gh api repos/cedis-unb/cedis-unb.github.io/pages/builds | head -20  # requer gh CLI logado
```

## Salvaguardas preventivas contra push acidental

### Salvaguarda 1 — Hook local `pre-push`

Instalar em `.git/hooks/pre-push` (não versionado):

```bash
#!/usr/bin/env bash
# Bloqueia push da branch dev/tailwind-v4-vite-local
protected_branches=("dev/tailwind-v4-vite-local")
while read local_ref local_sha remote_ref remote_sha; do
  for pb in "${protected_branches[@]}"; do
    if [[ "$local_ref" == "refs/heads/$pb" ]]; then
      echo "ERRO: push da branch '$pb' está bloqueado por hook pre-push local."
      echo "Se realmente quiser publicar, remova o hook ou use --no-verify (não recomendado)."
      exit 1
    fi
  done
done
exit 0
```

```bash
chmod +x .git/hooks/pre-push
```

### Salvaguarda 2 — Nunca configurar upstream

`git switch --create dev/tailwind-v4-vite-local` cria branch SEM upstream. Nunca rodar `git push -u`, nunca `git push origin dev/...`.

### Salvaguarda 3 — Verificar antes de push

Antes de qualquer `git push`, confirmar:

```bash
git branch --show-current  # deve ser 'main', NUNCA 'dev/tailwind-v4-vite-local'
```

## Restaurar Node modules e Hugo cache

Se algo em `node_modules/` ou `resources/` ficou corrompido durante experimentos:

```bash
rm -rf node_modules package-lock.json
git checkout package-lock.json
npm install

rm -rf resources/_gen
hugo --minify --cleanDestinationDir -d /tmp/cedis-rebuild
```

## Deletar tag de backup

Só quando **totalmente satisfeito** com o estado pós-migração e sem chance de precisar voltar:

```bash
git tag -d pre-tailwind-v4-YYYYMMDD
# Se tag foi pushada (não deveria — auditar!):
git push origin :refs/tags/pre-tailwind-v4-YYYYMMDD   # COM autorização
```

## Confirmação final de segurança

Ao final de qualquer rollback, confirmar:

- [ ] `git log --oneline -1 main` = commit esperado antes da migração
- [ ] `git status --short` = vazio
- [ ] `git branch -vv` = apenas `main` local (branch dev deletada)
- [ ] `git ls-remote origin | grep tailwind-v4` = vazio
- [ ] `curl -s https://cedis.unb.br/ | md5sum` = hash igual ao de antes da migração (ou compare uma página crítica)
- [ ] `docs/index.html` no filesystem = mesmo do commit `13bd3e105`
- [ ] `docs/css/*.min.*.css` fingerprints = idênticos aos de `13bd3e105`

Se todos os itens acima forem "sim", produção não foi tocada e o rollback está completo.
