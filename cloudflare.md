# Cloudflare (DNS/CDN) — cedis.unb.br

**Status:** o site é servido via **GitHub Pages** a partir do diretório `docs/`. Cloudflare atua apenas como camada de DNS/CDN em frente ao GitHub Pages, apontando `cedis.unb.br` para os endereços da GitHub.

Este arquivo documenta a configuração atual e serve como referência para operação.

## Deploy

- **Origin real:** GitHub Pages (branch `main`, subdiretório `docs/`). Ver `.github/workflows/site-ci.yml`.
- **CNAME:** `static/CNAME` contém `cedis.unb.br` — GitHub Pages usa esse valor para servir o domínio custom.
- **Cloudflare Pages:** **não é usado**. Se em algum momento houver migração para Cloudflare Pages, use o preset "Hugo" e comando `npm install && hugo --gc --minify` (versões atuais: Hugo `0.165+`, Node `24`). Ver `.tool-versions` para as versões canônicas.

## Cloudflare DNS

O domínio `cedis.unb.br` fica hospedado numa zona Cloudflare (gerenciada pelo administrador do domínio da UnB). Registros esperados:

- `cedis.unb.br` — `A` records para os IPs do GitHub Pages (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153) + `AAAA` equivalente IPv6.
- `www.cedis.unb.br` (se existir) — `CNAME` para `cedis-unb.github.io`.

Consulte a documentação oficial do GitHub Pages para valores atualizados: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site.

## Cache/CDN

- **Cloudflare cache:** herda os headers do GitHub Pages (varia por tipo de arquivo). Recomenda-se _não_ configurar page rules agressivas que subvertam o hash-based cache-busting do Hugo (`main.<hash>.css`, `imagem.<hash>.webp`).
- **Purga:** ao publicar mudanças críticas (correções de segurança, textos institucionais alterados), disparar "Purge Everything" no dashboard Cloudflare após confirmar que o GitHub Pages já reflete o novo commit.

## Verificação rápida

```sh
# Confirma que o site está de pé + revela CDN
curl -sI https://cedis.unb.br | head -20

# Deve mostrar cabeçalhos: 'server: cloudflare' e 'cf-ray:'
```

Se `cf-ray` desaparecer ou o TTL mudar radicalmente, verificar se a zona foi migrada.

## Emergência

- **Site fora do ar via Cloudflare:** ativar "Development Mode" no dashboard (desliga cache por 3h) e testar de novo.
- **Rollback de deploy quebrado:** reverter o último commit em `main` (o GitHub Pages republica automaticamente em 1–3 min).
- **Contatos:** administrador do domínio `unb.br` (via CPD/UnB) para mudanças na zona; owner do repo `cedis-unb/cedis-unb.github.io` para deploy.

---

*Documento atualizado em 2026-08-25 — antes: menções obsoletas a Hugo 0.111.3 e Node 18.16.0 de 2023.*
