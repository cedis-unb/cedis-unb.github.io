# CEDIS — Site institucional

Site oficial do **CEDIS** — Centro de Estudos, Desenvolvimento e Inovação em Software da Universidade de Brasília.

- **Produção:** <https://cedis.unb.br/>
- **Repositório:** <https://github.com/cedis-unb/cedis-unb.github.io>
- **Stack:** Hugo Extended · Tailwind CSS · Alpine.js · Pagefind · GitHub Pages / Cloudflare

## Sumário

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Rodar localmente](#rodar-localmente)
- [Build de produção](#build-de-produção)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Scripts NPM](#scripts-npm)
- [Convenções e governança](#convenções-e-governança)
- [Publicação](#publicação)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Pré-requisitos

Versões pinadas em [`.tool-versions`](.tool-versions) (compatíveis com [asdf](https://asdf-vm.com/) e [mise](https://mise.jdx.dev/)):

- **Hugo Extended** ≥ 0.164.0
- **Node.js** ≥ 24.x (LTS recente)
- **npm** ≥ 11.x
- **Python 3** (necessário para validadores e geração de páginas de publicação)

Instalação sugerida no macOS:

```sh
brew install hugo node
# ou, com mise:
mise install
```

Confira que `hugo version` reporta `+extended` — a versão non-extended não compila o Tailwind embutido.

## Instalação

```sh
git clone https://github.com/cedis-unb/cedis-unb.github.io.git
cd cedis-unb.github.io
npm ci
```

## Rodar localmente

```sh
npm start
```

Isso executa concorrentemente:

- `tailwindcss --watch` regenerando `assets/css/style.css` a partir de `assets/css/main.css`;
- `hugo server -d .hugo-server --disableFastRender` servindo em <http://localhost:1313/>.

O idioma português é o padrão. Para navegar a versão em inglês, use <http://localhost:1313/en/>.

## Build de produção

```sh
npm run build
```

O comando:

1. Regenera `content/publications/` a partir de `data/productions.yaml`.
2. Compila o site com `hugo --minify --cleanDestinationDir` para o diretório `docs/` (configurado em `hugo.yaml` via `publishDir: docs`).
3. Gera o índice de busca com `pagefind --site docs`.

`data/productions.yaml` é a fonte canônica das publicações. Não edite
`content/publications/**/*.md` manualmente; esses arquivos são
reescritos por `scripts/build_publications.py` e checados com
`npm run check:publications`.

> **Nota:** o diretório `docs/` é versionado hoje. A auditoria 2026 (issue I01 em [`PLANO-AUDITORIA-2026.md`](PLANO-AUDITORIA-2026.md)) prevê que ele passe a ser gerado exclusivamente pelo CI. Até lá, sempre rode `npm run build` antes de commitar mudanças de layout/conteúdo se quiser que o `docs/` reflita a alteração.

## Estrutura do repositório

```
.
├── archetypes/           # Templates de novos conteúdos (hugo new)
├── assets/               # CSS, JS e imagens processados pelo Hugo Pipes
├── content/              # Markdown do site (posts, products, projects, people, areas, ...)
│   ├── posts/            # Notícias e cobertura de defesas
│   ├── products/         # Produtos do CEDIS (Contextus, Evidentia, ...)
│   ├── projects/         # Projetos de pesquisa
│   ├── people/           # Fichas de pesquisadores e alumni
│   ├── areas/            # Áreas de atuação (IA, gamification, etc.)
│   ├── publications/     # Páginas geradas a partir de data/productions.yaml
│   └── history.*.md      # Linha do tempo institucional
├── data/                 # Fontes de dados YAML (fontes canônicas — ver CONVENTIONS.md)
│   ├── areas.yaml        # Áreas de atuação
│   ├── people.yaml       # Pessoas do CEDIS (incluindo orientandos e alumni)
│   ├── productions.yaml  # Produção científica (artigos, defesas, registros)
│   └── projects.yaml     # Projetos (metadados agregados)
├── docs/                 # Saída do build (versionada hoje — ver nota acima)
├── i18n/                 # Traduções PT/EN das strings de interface
├── layouts/              # Templates Hugo (partials, single, list, section)
├── scripts/              # Utilitários (Python, Bash)
├── static/               # Ativos servidos sem processamento (robots.txt, favicon, ...)
├── hugo.yaml             # Configuração central do Hugo
├── tailwind.config.js
├── postcss.config.js
├── package.json
├── CONVENTIONS.md         # Convenções editoriais (fontes canônicas, IDs, autoria)
├── ROADMAP.md             # Roadmap de comunicação e conteúdo
├── PLANO-AUDITORIA-2026.md # Plano técnico decorrente da auditoria 2026
├── SECURITY.md
└── cloudflare.md          # Notas específicas sobre hospedagem Cloudflare
```

## Scripts NPM

| Script | O que faz |
|---|---|
| `npm start` | Roda Tailwind e Hugo server concorrentemente para desenvolvimento. |
| `npm run watch:tw` | Só o watcher do Tailwind. |
| `npm run watch:hugo` | Só o Hugo server. |
| `npm run build:publications` | Regenera `content/publications/` a partir de `data/productions.yaml`. |
| `npm run check:publications` | Falha se `content/publications/` estiver divergente de `data/productions.yaml`. |
| `npm run build` | Build de produção + Pagefind. Saída em `docs/`. |
| `npm run update-i18n` | Executa `scripts/update_i18n.py` (mantém sincronia entre `i18n/pt.yaml` e `i18n/en.yaml`). |
| `npm test` | Checa publicações geradas, dados de conteúdo e paridade PT/EN. |

## Convenções e governança

Antes de contribuir, leia:

- **[`CONVENTIONS.md`](CONVENTIONS.md)** — regras editoriais (atribuição institucional FCTE, IDs de pesquisadores, estrutura de publicações, tipos válidos, URLs canônicas).
- **[`ROADMAP.md`](ROADMAP.md)** — direção de conteúdo e comunicação (30+ ações em 6 eixos, KPIs).
- **[`PLANO-AUDITORIA-2026.md`](PLANO-AUDITORIA-2026.md)** — plano técnico de execução das 12 issues da auditoria integrada 2026 (CI, modelo de dados, publicações canônicas, i18n, a11y, LGPD).
- **[`SECURITY.md`](SECURITY.md)** — política de reporte de vulnerabilidades.

**Regra central de arquitetura de dados:** relações inversas nunca são registradas à mão. Se o projeto declara seus pesquisadores, o perfil do pesquisador deriva os projetos automaticamente — não se mantém a mesma lista em dois lugares.

## Publicação

O deploy é feito automaticamente via GitHub Pages (branch `main`, diretório `docs/`) e servido por Cloudflare em `https://cedis.unb.br/`. Ver [`cloudflare.md`](cloudflare.md) para detalhes de DNS/CDN.

Enquanto o CI de build (issue I01) não estiver ativo:

1. Rode `npm run build` localmente antes de commitar mudanças de layout ou conteúdo que devam refletir em produção.
2. Commite `docs/` junto com a mudança fonte.
3. Push para `main`.

## Contribuição

1. Crie uma branch a partir de `main`.
2. Faça a alteração respeitando `CONVENTIONS.md`.
3. Rode `npm test` e `npm run build`; valide localmente (`npm start`, ou abrindo `docs/index.html` — mas prefira o server para hot reload).
4. Abra um PR descrevendo a mudança e cite qual issue/eixo do plano ela endereça.

## Licença

Distribuído sob a licença **Apache-2.0**. Ver arquivo [`LICENSE`](LICENSE).

O projeto foi originalmente baseado no tema [TailBliss](https://github.com/nusserstudios/tailbliss) (Apache-2.0) e evoluiu para uma identidade visual e estrutura de dados específicas do CEDIS.
