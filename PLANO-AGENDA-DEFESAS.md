# Plano: agenda compacta de defesas futuras

## Objetivo

Criar uma agenda compacta para a home do CEDIS, mostrando defesas futuras marcadas por dia da semana e horário, com alternância entre visão de agenda e visão linear.

## Escopo

- Fonte real: `data/defesas.yaml`.
- Seed local de desenvolvimento: `data/dev/defesas_futuras.yaml`, com 30 defesas a partir de 2026-07-27.
- Integração visual: home, em um bloco próprio de "Próximas defesas".
- Interação:
  - visão "Agenda" por dias e horários;
  - visão "Lista" com próximas defesas em ordem cronológica;
  - popover no hover/focus com estudante(s), título, orientador(es), área CEDIS principal e começo do resumo;
  - clique em defesa real leva para a página completa da defesa.

## Segurança de dados

O seed local não deve aparecer no build normal de produção. Ele só será carregado quando a variável `HUGO_CEDIS_INCLUDE_DEV_DEFESAS=1` estiver definida, como em:

```bash
HUGO_CEDIS_INCLUDE_DEV_DEFESAS=1 npm run start:agenda-seed
```

Sem essa variável, a agenda usa apenas as defesas reais catalogadas.

## Regras de duração

Quando `scheduled_end` não existir:

- `tcc` e `tcc1`: 90 minutos.
- `qualification` e `dissertation`: 120 minutos.
- `phd_qualification` e `phd`: 180 minutos.
- `specialization`: 90 minutos.

Defesas sem horário real ou marcadas como data aproximada não entram na grade horária, mas continuam elegíveis para a visão linear.

## Qualidade e validação

- Manter o componente como partial isolado para reduzir impacto no restante da home.
- Usar i18n PT/EN para textos de interface.
- Reaproveitar `people-lookup`, `area-lookup`, `translated-label` e `defesa-type-label`.
- Rodar:
  - `npm test`
  - `npm run build`
  - build local com `HUGO_CEDIS_INCLUDE_DEV_DEFESAS=1` para confirmar que o seed aparece apenas no DEV.
