---
title: "Accessibility"
date: 2026-07-20T09:00:00-03:00
draft: false
language: en
description: "CEDIS site digital accessibility commitments: standards followed, available features, and channel to report barriers."
featured_image: "../assets/images/pages/media-CEDIS.webp"
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

## Continuous validation

- Automated validation with Pa11y integrated into CI for critical pages (WCAG 2.0 AA).
- Lighthouse CI audit on both desktop and mobile.
- Accessibility and Lighthouse reports attached as workflow artifacts.
- Complementary manual reviews on critical flows with screen readers, keyboard navigation, dark mode, and 200% and 400% zoom.

## Latest empirical measurement (2026-07-27)

- Pa11y (WCAG 2.0 AA): **0 errors across 15 representative URLs**.
- Lighthouse desktop accessibility: **100 on 8/8 pages** (average 100).
- Lighthouse mobile accessibility: **100 on 8/8 pages** (average 100).
- Lighthouse SEO: 100 on every measured page.
- Lighthouse best practices: 96 on every measured page.

These numbers are revalidated on every layout or palette change.

## Report a barrier

Struggling to use the site? Write to [cedis@unb.br](mailto:cedis@unb.br) describing the page, what you tried to do, and what happened. Barriers identified by users take priority in the correction queue.

## Standards followed

- WCAG 2.1 level AA (international reference).
- eMAG (Brazilian Electronic Government Accessibility Model), where applicable.
- Brazilian Inclusion Law (Law 13.146/2015).
