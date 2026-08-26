---
title: "Privacy policy"
date: 2026-07-20T09:00:00-03:00
draft: false
language: en
description: "CEDIS site privacy policy: data collected, purpose, retention, legal basis, and contact."
featured_image: "../assets/images/pages/media-CEDIS.webp"
eyebrow: "Privacy and Brazilian LGPD"
translationKey: privacy
---

This policy describes how the CEDIS institutional website handles personal data and browser privacy signals. The website is static, does not require authentication, and does not host its own personal-data collection forms.

## Controller and contact

The site is maintained by the **Center for Studies, Development, and Innovation in Software (CEDIS)** at the University of Brasilia.

- CEDIS contact: [cedis@unb.br](mailto:cedis@unb.br)
- UnB institutional data protection officer: see the official privacy and data protection channels of the University of Brasilia.

## Data processed

- **Aggregated navigation metrics** via Google Analytics 4 (identifier `G-ENMST48SB3`), with IP anonymization. These metrics include pages accessed, aggregated access origin, device/browser information at statistical level, and technical navigation events.
- **Language and theme preferences** (light/dark) stored locally in the user's browser through `localStorage`. These values are not sent to CEDIS.
- **Contact data voluntarily sent** when a person writes to the CEDIS institutional email address. In that case, processing occurs in UnB's institutional email environment.

## Purpose

- Understand in aggregate which content is most consulted to guide editorial curation.
- Preserve the user's own preferences across visits.
- Reply to messages voluntarily sent to CEDIS.

## Legal basis

Aggregated metrics and local preferences are processed to support editorial management and improve the public service of scientific communication. Email messages are processed to respond to the request made by the data subject.

## Do Not Track and Global Privacy Control

Google Analytics is loaded only when the browser does not signal **Do Not Track (DNT)** or **Global Privacy Control (GPC)**. When these signals are enabled, the analytics script is not inserted into the page and no Google Analytics request is initiated by the site.

## Retention

- Language and theme preferences remain only in the user's browser until the browser or user deletes them.
- Aggregated Google Analytics 4 metrics follow a retention of **14 months** (default configuration of the GA4 property maintained by CEDIS) for events and user properties; aggregated reports on GA standard dimensions remain available beyond that period.
- Email messages follow UnB's institutional records management and information security rules.

## Analytics opt-out

In addition to automatically honoring Do Not Track and Global Privacy Control signals, you can explicitly refuse Google Analytics in this browser. The choice is stored locally (`localStorage`) and only applies to this device/browser.

<div id="cedis-optout-widget" class="mt-3 rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm dark:border-white/10 dark:bg-white/5">
  <p id="cedis-optout-status" class="mb-3 font-semibold" aria-live="polite" role="status">Google Analytics is active in this browser (with IP anonymization and DNT/GPC respected).</p>
  <button id="cedis-optout-toggle" type="button" class="rounded-full bg-primary-700 px-4 py-2 text-sm font-semibold text-white transition-colors hover:bg-primary-800">Opt out of analytics</button>
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
        status.textContent = "You have opted out of Google Analytics in this browser.";
        btn.textContent = "Re-enable analytics";
      } else {
        status.textContent = "Google Analytics is active in this browser (with IP anonymization and DNT/GPC respected).";
        btn.textContent = "Opt out of analytics";
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

## External integrations

The site links to external services such as GitHub, Zenodo, Spotify, LinkedIn, YouTube, SharePoint, and UnB pages. When accessing those services, each platform's privacy policy applies.

## Data subject rights (LGPD, art. 18)

Data subjects may, at any time, request confirmation, access, correction, anonymization, portability, or elimination of their data, as well as information about shared use. Requests should be sent to [cedis@unb.br](mailto:cedis@unb.br).

## Updates

This policy will be reviewed if the site starts hosting forms, authentication, newsletters, comments, marketing pixels, or new integrations that change how personal data is processed.
