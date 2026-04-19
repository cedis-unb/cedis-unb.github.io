---
author: CEDIS
title: "Nativo"
date: 2025-12-16T09:00:00-03:00
language: en
product_language: pt
weight: 4
featured_image: "../assets/images/featured/nativo-logo.png"
summary: Mobile application developed as a bachelor's thesis at the University of Brasilia to support the preservation and teaching of Brazilian Indigenous languages, initially focused on Munduruku, through translation lookup, history, and collaborative curation.
authorimage: ../assets/images/global/author.webp
categories:
- products
- project
- sergio_freitas
tags:
- app
- active_learning
- social_software
- software_products
---
## Project Description

**Nativo** is a mobile application designed to support the preservation, consultation, and teaching of Brazilian Indigenous languages, with an initial focus on **Munduruku**. The product originated in a bachelor's thesis project at the University of Brasilia, developed by **Alexia Cardoso** under the supervision of Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} and co-supervision of Prof. Célia Higawa.

The proposal emerged from contact with the Munduruku village of Braganca and aims to provide a practical tool for both everyday use and learning contexts, allowing users to look up words and expressions in Portuguese and access their written translations in the supported language. The implementation combines a **React Native** mobile app with a **Python/Flask** API, **Firestore** persistence, and role-based access control.

## Project Objectives

The main objectives of the project are:

- to contribute to the appreciation, preservation, and teaching of the Munduruku language in digital format;
- to offer a mobile experience for written translation lookup between Portuguese and the supported Indigenous language;
- to enable collaborative content evolution through translation creation, review, and moderation; and
- to provide a technical foundation that can incorporate new languages, media assets, and support resources in future versions.

## Resources and Features

Among the features offered by **Nativo** are translation lookup from words and expressions entered by the user, display of the discourse category associated with each result, and history storage so previous searches can be revisited. The application also includes informational materials and manuals that support the use of the solution and explain the cultural context that motivated the project.

Beyond the main lookup flow, the system architecture includes distinct roles such as user, moderator, professor, and administrator, enabling the registration, editing, review, and organization of translations, languages, categories, and users. The project foundation also anticipates future expansion with resources such as audio, images, and broader language coverage.

## Academic Link

- Alexia Cardoso (product development as part of the bachelor's thesis)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (academic supervision)
- Prof. Célia Higawa (co-supervision)
- Munduruku community of Braganca (origin context and problem alignment)

## Access

The source code is available on [GitHub](https://github.com/CedisUnB/Nativo).