# Decisões de privacidade do site CEDIS

Data da decisão: 2026-07-20.

## Escopo

Este registro cobre o site institucional estático do CEDIS publicado em `cedis.unb.br`. Sistemas externos ou produtos próprios do CEDIS têm políticas específicas quando coletam dados diretamente.

## Google Analytics

- O site usa Google Analytics 4 para métricas agregadas de navegação.
- O script de analytics só é carregado quando o navegador não sinaliza Do Not Track (`DNT: 1`) nem Global Privacy Control (`Sec-GPC: 1`/`navigator.globalPrivacyControl`).
- Não há banner de consentimento no site institucional porque a medição é agregada, não há autenticação, não há remarketing e o carregamento é bloqueado quando o usuário expressa opt-out por DNT ou GPC.
- IP é anonimizado na configuração do Hugo e também no comando `gtag("config", ..., { "anonymize_ip": true })`.

## Dados locais

- Preferência de idioma e tema é guardada em `localStorage`.
- Esses valores permanecem no navegador e não são enviados ao CEDIS.

## Formulários e integrações externas

- O site institucional não hospeda formulários próprios de coleta de dados pessoais.
- Links de contato usam `mailto:` ou encaminham para serviços institucionais externos.
- Links para GitHub, Zenodo, Spotify, LinkedIn, YouTube, SharePoint e sites da UnB seguem as políticas de privacidade dos respectivos serviços.

## Retenção e revisão

- Dados agregados de analytics seguem a retenção configurada na propriedade Google Analytics mantida pelo CEDIS.
- Esta decisão deve ser revisada quando o site passar a hospedar formulários, autenticação, comentários, newsletter ou pixels de marketing.
