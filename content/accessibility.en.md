---
title: "Accessibility"
date: 2026-07-20T09:00:00-03:00
draft: false
language: en
description: "CEDIS site digital accessibility commitments: standards followed, available features, and channel to report barriers."
featured_image: "../assets/images/pages/media-CEDIS.png"
eyebrow: "WCAG commitment"
translationKey: accessibility
---

CEDIS works to make this site usable by people with different types of disabilities, following the [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/) at level AA.

## Features already in place

- "Skip to content" link at the top of every page.
- Color contrast tested in light and dark modes.
- Keyboard navigation with visible focus.
- ARIA labels on interactive components (menus, theme buttons, forms).
- Textual alternatives (`alt`) on content images.
- Semantic structure with proper heading hierarchy.
- Support for reduced motion (`prefers-reduced-motion`).

## Under consolidation (issue I10)

- Automated validation with axe/Pa11y integrated into CI.
- Lighthouse audit (target: score ≥ 90).
- Screen reader testing on critical flows.
- Dark mode contrast verification across all combinations.
- Behavior with 200% and 400% zoom.

## Report a barrier

Struggling to use the site? Write to [cedis@unb.br](mailto:cedis@unb.br) describing the page, what you tried to do, and what happened. Barriers identified by users take priority in the correction queue.

## Standards followed

- WCAG 2.1 level AA (international reference).
- eMAG (Brazilian Electronic Government Accessibility Model), where applicable.
- Brazilian Inclusion Law (Law 13.146/2015).
