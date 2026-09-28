---
title: "Accessibility"
date: 2026-07-20T09:00:00-03:00
draft: false
language: en
description: "CEDIS site digital accessibility status: the level we target, what every build checks automatically, what was verified by hand, and the gaps we already know about."
featured_image: "../assets/images/pages/media-CEDIS.webp"
eyebrow: "WCAG commitment"
translationKey: accessibility
---

CEDIS works to make this site usable by people with different types of disabilities. Our
target is the [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/)
at level AA, plus the WCAG 2.2 additions that apply to a content site. **We do not claim
full conformance with any WCAG version**: part of the site has been verified, part has not,
and the gaps we already know about are listed below.

## Features already in place

- "Skip to content" link at the top of every page, pointing at a target that exists.
- Keyboard navigation with a visible focus indicator on the header, on filters, and on the competency map.
- Main menu and dropdowns operable by keyboard: they open with Enter, report their state via `aria-expanded`, and Escape closes them and returns focus to the button that opened them.
- Competency map with a keyboard-reachable alternative: each node is focusable and can be activated with Enter or Space, and the same relationships are published as a list of ordinary links that works with JavaScript switched off.
- ARIA labels on interactive components (menus, filters, map, theme button).
- Textual alternatives (`alt`) on content images.
- Semantic structure with a proper heading hierarchy.
- Support for reduced motion (`prefers-reduced-motion`), honoured by the map animation.

## Checked automatically on every build

Every push runs these checks in CI, and a failure blocks the build:

- **Pa11y** (HTML_CodeSniffer, `WCAG2AA` standard) over **21 fixed URLs**, in both languages. This is a sample, not the whole site — the site generates more than three thousand pages.
- **Lighthouse CI on desktop** over **8 URLs**, with the accessibility category required to score **at least 0.90** (not 100). The mobile run uses the same threshold but is a local command, not part of CI.
- **Structural validation** of the generated HTML: breadcrumb trail consistent with its JSON-LD, no duplicated consecutive crumbs, no `aria-controls` pointing at an id that does not exist (this one is checked on *every* generated page), no reading-time metadata in researcher listings, and the contextual research-area cards on profiles.

Automated tools of this kind only detect a minority of the WCAG success criteria — roughly a
third, and only the machine-decidable part of those. A green build means "no known automated
failure on the sampled pages", not "accessible".

## Latest measurement (2026-09-27)

Measured on a local build of the current site, in both languages:

- Pa11y (`WCAG2AA`): **0 errors on 21/21 URLs**.
- Lighthouse accessibility (desktop and mobile, run of 2026-09-26): **1.00 on 7 of the 8 URLs** and **0.90 on the home page**, in both profiles.
- Complementary scan with axe-core over 7 pages per language, in light and dark mode: **no violation in light mode except on the home page and the map**; **38 contrast violations on the home page in dark mode** and 1 on the researcher profile page.
- Keyboard: 24 open/close cycles of the header dropdowns (6 menus x 2 languages x 2 themes) all behaved correctly, and a full Tab sweep of four pages per language found **no keyboard trap**.
- Competency map: 53 nodes, all reachable with Tab, all activatable with Enter and Space, with a visible focus ring in both themes; the zoom and filter buttons are all 34 px tall.
- Filters on Opportunities, Publications and Defences: every control reachable by keyboard, every control named by a real `<label>`, all 37 px tall.
- Target size (WCAG 2.2, 24x24 px minimum): every `<button>` and `<select>` measures at least 34 px in height. Two controls are narrower or smaller than 24 px and conform only through the standard spacing exception: the header search link (**20x40 px**) and 21 of the 53 map nodes (**20x20 px**).

## Known gaps

These are real, measured, and queued for correction. We prefer to publish them rather than imply they do not exist:

- **Dark mode has insufficient contrast in places.** Secondary text on card surfaces on the home page reaches only 2.7:1 to 3.1:1 where 4.5:1 is required, and the "Former supervisions" heading on researcher profiles drops to 1.0:1. Automated contrast checking in CI runs in light mode only, so these do not fail the build.
- **The "Former supervisions" / "Previous researchers" block cannot be opened with a keyboard.** It responds to the mouse only, which also means its state is not announced. Affected: researcher profiles and knowledge-area pages.
- **Zoom / reflow.** At 400% zoom (a 320 px viewport) the home page, Publications and Defences scroll sideways; at 200% only Defences does, because of a filter dropdown that is wider than the screen. The map and Opportunities reflow correctly.
- **Two labels are wrong in English.** The light/dark button announces itself in Portuguese on every page, and the mobile menu button announces itself only as "Main".
- **The competency map declares itself an image** while containing 53 focusable nodes, which is contradictory for assistive technology. The list of links below the map is the reliable route.
- **The home page has two ARIA errors** in the "next defences" view switcher (buttons carrying `aria-selected` without the matching role). This is what keeps that page at 0.90 instead of 1.00.
- **Dense listings and target size.** On the Defences listing, the text links in consecutive cards sit closer together than the 24 px that WCAG 2.2 asks for.
- **No screen-reader testing has been recorded.** Nothing on this page is based on a NVDA, JAWS or VoiceOver session, and we do not claim otherwise. No external audit has been commissioned.

## Report a barrier

Struggling to use the site? Write to [cedis@unb.br](mailto:cedis@unb.br) describing the page,
what you tried to do, and what happened. Barriers identified by users take priority in the
correction queue.

## Standards we work against

- WCAG 2.1 level AA as the target, plus the WCAG 2.2 additions that apply (target size, focus appearance, consistent help).
- eMAG (Brazilian Electronic Government Accessibility Model), as a reference — not verified criterion by criterion.
- Brazilian Inclusion Law (Law 13.146/2015).
