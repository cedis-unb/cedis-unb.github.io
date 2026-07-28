"""Helpers compartilhados entre scripts do CEDIS.

Centraliza operações que estavam duplicadas em múltiplos scripts:
  · frontmatter.parse_frontmatter — leitura do bloco YAML de arquivos .md
  · slugify.strip_accents, slugify_snake — normalização de nomes/strings

Ver docs-src/data-model.md e CONVENTIONS.md para o modelo de dados.
"""
