---
title: "Política de privacidade"
date: 2026-07-20T09:00:00-03:00
draft: false
language: pt
description: "Política de privacidade do site do CEDIS: dados coletados, finalidade, retenção, base legal e contato."
featured_image: "../assets/images/pages/media-CEDIS.webp"
eyebrow: "Privacidade e LGPD"
translationKey: privacy
---

Esta política descreve como o site institucional do CEDIS trata dados pessoais e sinais de privacidade do navegador. O site é estático, não exige autenticação e não hospeda formulários próprios de coleta de dados pessoais.

## Controlador e contato

O site é mantido pelo **Centro de Estudos, Desenvolvimento e Inovação em Software (CEDIS)**, vinculado à Universidade de Brasília.

- Contato do CEDIS: [cedis@unb.br](mailto:cedis@unb.br)
- Encarregado institucional da UnB: consulte os canais oficiais de privacidade e proteção de dados da Universidade de Brasília.

## Dados tratados

- **Métricas agregadas de navegação** via Google Analytics 4 (identificador `G-ENMST48SB3`), com anonimização de IP. Essas métricas indicam páginas acessadas, origem agregada do acesso, dispositivo/navegador em nível estatístico e eventos técnicos de navegação.
- **Preferência de idioma e tema** (claro/escuro) armazenada localmente no navegador por `localStorage`. Esses valores não são enviados ao CEDIS.
- **Dados de contato enviados voluntariamente** quando a pessoa decide escrever para o e-mail institucional do CEDIS. Nesse caso, o tratamento ocorre no ambiente de e-mail institucional da UnB.

## Finalidade

- Entender agregadamente quais conteúdos são mais consultados para orientar a curadoria editorial.
- Manter as preferências do próprio usuário entre visitas.
- Responder mensagens enviadas voluntariamente ao CEDIS.

## Base legal

As métricas agregadas e preferências locais são tratadas para apoio à gestão editorial e melhoria do serviço público de divulgação científica. Mensagens enviadas por e-mail são tratadas para responder à solicitação feita pelo próprio titular.

## Do Not Track e Global Privacy Control

O Google Analytics só é carregado quando o navegador não sinaliza **Do Not Track (DNT)** nem **Global Privacy Control (GPC)**. Quando esses sinais estão ativos, o script de analytics não é inserido na página e nenhuma requisição ao Google Analytics é iniciada pelo site.

## Retenção

- Preferências de idioma e tema permanecem apenas no navegador do usuário até que sejam apagadas pelo próprio navegador ou pelo usuário.
- Métricas agregadas do Google Analytics 4 seguem a retenção de **14 meses** (configuração padrão da propriedade GA4 mantida pelo CEDIS) para eventos e propriedades de usuário; relatórios agregados nas dimensões padrão do GA continuam disponíveis além desse período.
- Mensagens recebidas por e-mail seguem as regras institucionais de gestão documental e segurança da informação da UnB.

## Opt-out de analytics

Além de respeitar automaticamente os sinais Do Not Track e Global Privacy Control, você pode recusar explicitamente o Google Analytics neste navegador. A escolha é armazenada apenas localmente (`localStorage`) e vale para este dispositivo/navegador.

<div id="cedis-optout-widget" class="mt-3 rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm dark:border-white/10 dark:bg-white/5">
  <p id="cedis-optout-status" class="mb-3 font-semibold" aria-live="polite" role="status">O Google Analytics está ativo neste navegador (com anonimização de IP e respeito a DNT/GPC).</p>
  <button id="cedis-optout-toggle" type="button" class="rounded-full bg-primary-700 px-4 py-2 text-sm font-semibold text-white transition-colors hover:bg-primary-800">Recusar analytics</button>
</div>
<script>
  (function () {
    var KEY = "cedis-analytics-optout";
    var widget = document.getElementById("cedis-optout-widget");
    var status = document.getElementById("cedis-optout-status");
    var btn = document.getElementById("cedis-optout-toggle");
    if (!widget || !status || !btn) return;
    function render() {
      var optedOut = false;
      try { optedOut = localStorage.getItem(KEY) === "1"; } catch (e) {}
      if (optedOut) {
        status.textContent = "Você optou por não ser rastreado pelo Google Analytics neste navegador.";
        btn.textContent = "Reativar analytics";
      } else {
        status.textContent = "O Google Analytics está ativo neste navegador (com anonimização de IP e respeito a DNT/GPC).";
        btn.textContent = "Recusar analytics";
      }
    }
    btn.addEventListener("click", function () {
      try {
        if (localStorage.getItem(KEY) === "1") { localStorage.removeItem(KEY); }
        else { localStorage.setItem(KEY, "1"); }
      } catch (e) {}
      render();
      location.reload();
    });
    render();
  })();
</script>

## Integrações externas

O site contém links para serviços externos, como GitHub, Zenodo, Spotify, LinkedIn, YouTube, SharePoint e páginas da UnB. Ao acessar esses serviços, aplicam-se as políticas de privacidade de cada plataforma.

## Direitos do titular (LGPD, art. 18)

Titulares de dados pessoais podem, a qualquer momento, solicitar confirmação, acesso, correção, anonimização, portabilidade ou eliminação de seus dados, bem como informações sobre uso compartilhado. Solicitações devem ser enviadas para [cedis@unb.br](mailto:cedis@unb.br).

## Atualizações

Esta política será revisada quando o site passar a hospedar formulários, autenticação, newsletter, comentários, pixels de marketing ou novas integrações que alterem o tratamento de dados pessoais.
