# Stratégie SEO complète — Callem (agents vocaux IA souverains)

**Date :** août 2026 · **Domaine :** callem.ai · **Marchés :** FR (priorité 1), UE anglophone/DACH/BENELUX (priorité 2)
**Sources projet lues :** `/Users/yassminesmachine/Desktop/callem/brief/content-spec-fr.md`, `/Users/yassminesmachine/Desktop/callem/brief/quality-bar.md`

---

## 0. Ce que la recherche révèle (et qui change la stratégie)

Quatre constats issus des SERP réelles, à lire avant le reste :

**1. Les SERP françaises sont tenues par des sites-parasites à domaine exact, pas par des éditeurs.** Sur « agent vocal IA », « callbot », « SVI IA », les positions 1-10 sont occupées par `callbot-ia.com`, `svi-ia.com`, `agent-vocal-ia.fr`, `call-bot.fr`, `voicebotfrance.fr`, `comparatif-logiciels.fr`, `lessentieldeleco.fr`, `ia-vocale.com`. Ce sont des comparateurs affiliés, DR faible, contenu mince, aucune donnée propriétaire. **Conséquence : la barrière à l'entrée est basse.** Un éditeur avec de vraies données produit (télémétrie de latence, benchmarks, captures Studio) les dépasse en 6-9 mois. Corollaire stratégique : ces mêmes sites sont le corpus que citent ChatGPT/Perplexity sur ces requêtes → **il faut à la fois les battre en SEO et être listé dessus en AEO.** Les deux, pas l'un ou l'autre.

**2. Preuve que le marché FR est SEO-conquérable.** Yelda AI a atteint **la position 1 sur « callbot » en 4 mois**, +70 % de trafic et ~10 leads organiques qualifiés/mois avec 70 articles, via l'agence Onze — sur une architecture UMSO (pas même un stack technique optimal). Callem, avec Next.js 15 et un vrai différenciateur, doit viser mieux.

**3. Fenêtre réglementaire ouverte MAINTENANT.** L'**article 50 du Règlement IA (UE) 2024/1689 est entré en application le 2 août 2026** — il y a trois semaines. Il impose que toute personne interagissant avec un agent vocal IA en soit informée, sous peine de 15 M€ ou 3 % du CA mondial. La CNIL, la DGCCRF et l'Arcom sont les autorités de contrôle en France. Chaque directeur des opérations français qui exploite un agent vocal cherche en ce moment comment se mettre en conformité. **C'est le meilleur cheval de Troie éditorial de l'année, et il expire dans ~6 mois.** À traiter en priorité absolue, semaine 1.

**4. Le créneau souveraineté est quasi vierge en anglais, et Telnyx commence à s'y installer** (`telnyx.com/europe`, `telnyx.com/resources/voice-ai-europe-data-sovereignty`). Les requêtes « GDPR compliant voice AI », « European voice AI », « voice AI data residency », « sovereign AI » ont des volumes modestes mais une intention d'achat extrême et une concurrence quasi nulle. Les acheteurs UE shortlistent aujourd'hui Cognigy, Parloa, PolyAI — tous positionnés « européen ». La distinction que Callem doit posséder éditorialement : **résidence ≠ souveraineté** (AWS Francfort donne la résidence, pas la souveraineté — le CLOUD Act s'applique toujours au parent américain). C'est l'angle exact où Callem gagne, et personne ne l'a écrit proprement en français.

**Architecture actuelle à corriger :** callem.ai est aujourd'hui **une single-page** avec ancres, EN par défaut sur `/en`, docs sur sous-domaine. Surface indexable ≈ 1 URL. C'est le point de départ. Tout ce qui suit est un plan de passage de 1 à ~900 URL utiles.

---

## 1. Cartographie de mots-clés (FR + EN) — 78 requêtes

**Méthode d'estimation :** volumes mensuels France (FR) / global anglophone (EN), calibrés sur la structure des SERP observées, la densité publicitaire et la maturité du marché. `KD` = difficulté 0-100. Ces chiffres sont des ordres de grandeur à valider dans Ahrefs/Semrush avant arbitrage budgétaire — mais l'ordre de priorité, lui, est solide.

Légende priorité : **P0** = à publier dans les 30 jours · **P1** = 90 jours · **P2** = 6 mois · **P3** = opportuniste.

### 1.1 FRANÇAIS — TOFU (problème, éducation, définition)

| # | Mot-clé | Vol/mois FR | KD | Page cible | Prio |
|---|---|---|---|---|---|
| 1 | serveur vocal interactif | 2 400 | 38 | `/fr/ressources/glossaire/serveur-vocal-interactif` | P1 |
| 2 | svi | 1 900 | 42 | glossaire + redirection contextuelle | P2 |
| 3 | assistant vocal IA | 1 300 | 34 | blog (attention : pollué Alexa/Siri, qualifier « entreprise ») | P2 |
| 4 | agent conversationnel | 1 000 | 36 | glossaire | P1 |
| 5 | IA service client | 880 | 44 | blog pilier | P1 |
| 6 | IA vocale | 880 | 30 | `/fr/ressources/guides/ia-vocale-entreprise` | P0 |
| 7 | reconnaissance vocale entreprise | 720 | 32 | blog | P2 |
| 8 | RGPD et IA | 720 | 40 | `/fr/confiance/rgpd` | P0 |
| 9 | voicebot | 590 | 26 | glossaire + comparatif | P0 |
| 10 | IA souveraine | 590 | 33 | `/fr/ressources/guides/ia-souveraine` | P0 |
| 11 | automatisation appels téléphoniques | 480 | 22 | `/fr/ressources/guides/automatiser-les-appels` | P0 |
| 12 | robot téléphonique | 320 | 20 | glossaire | P2 |
| 13 | article 50 AI Act | 320 ↗ | 24 | `/fr/confiance/ai-act` | **P0** |
| 14 | taux de décroché centre d'appel | 260 | 18 | blog | P2 |
| 15 | accueil téléphonique automatisé | 210 | 24 | blog → `/fr/solutions/standard-telephonique-ia` | P1 |
| 16 | IA souveraine France | 210 | 26 | guide souveraineté | P0 |
| 17 | agent conversationnel vocal | 110 | 18 | glossaire | P1 |
| 18 | hébergement données IA France | 90 | 20 | `/fr/confiance/hebergement-des-donnees` | P1 |
| 19 | latence agent vocal | 70 | 12 | `/fr/ressources/guides/latence-ia-vocale` | P0 |
| 20 | empreinte carbone IA | 590 | 38 | blog (angle CSRD, différenciant) | P2 |

### 1.2 FRANÇAIS — MOFU (catégorie de solution, comparaison, évaluation)

| # | Mot-clé | Vol/mois FR | KD | Page cible | Prio |
|---|---|---|---|---|---|
| 21 | **agent vocal IA** | **2 900** | **41** | **`/fr` (home)** | **P0** |
| 22 | agent vocal | 1 900 | 35 | home (secondaire) | P0 |
| 23 | callbot | 1 100 | 33 | `/fr/ressources/glossaire/callbot` + pilier | P0 |
| 24 | standard téléphonique IA | 880 | 29 | `/fr/solutions/standard-telephonique-ia` | **P0** |
| 25 | agent IA téléphonique | 590 | 30 | home / solutions hub | P0 |
| 26 | centre d'appel IA | 480 | 34 | `/fr/secteurs/bpo-centres-de-contact` | P1 |
| 27 | standard téléphonique virtuel | 480 | 31 | solutions/standard | P1 |
| 28 | meilleur agent vocal IA | 390 | 36 | `/fr/comparatifs/meilleurs-agents-vocaux-ia` | **P0** |
| 29 | secrétariat téléphonique IA | 320 | 27 | `/fr/solutions/permanence-telephonique-ia` | P1 |
| 30 | comparatif callbot | 260 | 25 | `/fr/comparatifs` (hub) | P0 |
| 31 | plateforme agent vocal IA | 210 | 22 | `/fr/produit` | P0 |
| 32 | permanence téléphonique IA | 210 | 25 | solutions/permanence | P1 |
| 33 | prospection téléphonique IA | 210 | 28 | `/fr/solutions/campagnes-sortantes` | P1 |
| 34 | serveur vocal interactif IA | 170 | 21 | `/fr/solutions/svi-intelligent` | **P0** |
| 35 | IA vocale entreprise | 170 | 19 | `/fr/produit` | P0 |
| 36 | prise de rendez-vous automatique téléphone | 140 | 20 | `/fr/solutions/prise-de-rendez-vous` | P1 |
| 37 | SVI intelligent | 140 | 17 | solutions/svi-intelligent | P0 |
| 38 | qualification de leads IA | 110 | 18 | `/fr/solutions/qualification-de-leads` | P1 |
| 39 | agent vocal IA santé | 90 | 16 | `/fr/secteurs/sante` | P1 |
| 40 | logiciel callbot | 70 | 19 | `/fr/produit` | P2 |
| 41 | callbot assurance | 70 | 15 | `/fr/secteurs/assurance` | P1 |
| 42 | trunk SIP IA | 50 | 12 | `/fr/produit/telephonie-sip` | P2 |
| 43 | recouvrement créances IA | 50 | 16 | `/fr/solutions/recouvrement` | P2 |

### 1.3 FRANÇAIS — BOFU (marque, prix, alternative, achat)

| # | Mot-clé | Vol/mois FR | KD | Page cible | Prio |
|---|---|---|---|---|---|
| 44 | agent vocal IA prix | 170 | 23 | `/fr/tarifs` | **P0** |
| 45 | callbot prix / tarif callbot | 90 | 18 | `/fr/tarifs` | P0 |
| 46 | Zaion avis / Zaion tarif | 140 | 14 | `/fr/alternatives/zaion` | P1 |
| 47 | alternative Twilio | 110 | 30 | `/fr/alternatives/twilio` | P1 |
| 48 | Yelda avis | 90 | 12 | `/fr/alternatives/yelda` | P1 |
| 49 | Calldesk avis | 70 | 12 | `/fr/alternatives/calldesk` | P2 |
| 50 | alternative Vapi | 70 | 16 | `/fr/alternatives/vapi` | P0 |
| 51 | Diabolocom vs Zaion | 50 | 10 | `/fr/comparatifs/diabolocom-vs-zaion` | P2 |
| 52 | agent vocal IA open source | 50 | 20 | blog (capture dev, redirige vers API) | P2 |
| 53 | démo agent vocal IA | 40 | 10 | `/fr/demo` | P0 |
| 54 | agent vocal IA on-premise | 30 | 8 | `/fr/confiance/deploiement-on-premise` | P1 |

### 1.4 ANGLAIS — TOFU / MOFU / BOFU

| # | Mot-clé | Vol/mois | KD | Intent | Page cible | Prio |
|---|---|---|---|---|---|---|
| 55 | ai voice agent | 9 900 | 62 | MOFU | `/en` | P1 |
| 56 | ai receptionist | 8 100 | 58 | MOFU | `/en/solutions/ai-receptionist` | P2 |
| 57 | voice ai agents | 6 600 | 60 | MOFU | `/en` | P1 |
| 58 | ai call center | 3 600 | 57 | TOFU | `/en/industries/bpo-contact-centers` | P2 |
| 59 | sovereign ai | 3 600 ↗ | 45 | TOFU | `/en/resources/guides/sovereign-ai` | **P0** |
| 60 | ai appointment setter | 2 900 | 48 | MOFU | `/en/solutions/appointment-booking` | P2 |
| 61 | conversational ai platform | 2 400 | 63 | MOFU | `/en/product` | P3 |
| 62 | ai phone answering service | 2 900 | 52 | MOFU | `/en/solutions/ai-phone-agent` | P2 |
| 63 | elevenlabs alternatives | 2 400 | 44 | BOFU | `/en/alternatives/elevenlabs-agents` | P1 |
| 64 | ai phone agent | 1 600 | 46 | MOFU | `/en/solutions/ai-phone-agent` | P1 |
| 65 | voice ai platform | 1 300 | 49 | MOFU | `/en/product` | P1 |
| 66 | twilio alternative | 1 300 | 51 | BOFU | `/en/alternatives/twilio` | P2 |
| 67 | vapi alternatives | 1 300 | 38 | BOFU | `/en/alternatives/vapi` | **P0** |
| 68 | outbound calling ai | 880 | 44 | MOFU | `/en/solutions/outbound-campaigns` | P2 |
| 69 | ai ivr | 880 | 40 | MOFU | `/en/solutions/ai-ivr` | P1 |
| 70 | ai lead qualification | 590 | 36 | MOFU | `/en/solutions/lead-qualification` | P1 |
| 71 | retell ai alternatives | 480 | 30 | BOFU | `/en/alternatives/retell-ai` | P0 |
| 72 | voice ai pricing | 390 | 33 | BOFU | `/en/pricing` | P0 |
| 73 | bland ai alternatives | 320 | 28 | BOFU | `/en/alternatives/bland-ai` | P0 |
| 74 | gdpr compliant voice ai | 260 ↗ | 18 | BOFU | `/en/trust/gdpr` | **P0** |
| 75 | synthflow alternatives | 210 | 24 | BOFU | `/en/alternatives/synthflow` | P0 |
| 76 | eu ai act voice agents | 170 ↗ | 16 | TOFU | `/en/trust/eu-ai-act` | **P0** |
| 77 | voice ai latency benchmark | 110 | 14 | TOFU | `/en/resources/guides/voice-ai-latency` | P0 |
| 78 | european voice ai / voice ai data residency | 90 + 70 ↗ | 12 | BOFU | `/en/trust/data-residency` | **P0** |

**Lecture stratégique du tableau.** Le volume français total exploitable est d'environ **18 000 recherches/mois** sur le cluster complet — modeste, mais avec une valeur par lead extrêmement élevée (ACV mid-market/enterprise). Ne pas courir après le volume anglais générique (`ai voice agent`, KD 62, dominé par Vapi/Retell/Synthflow avec des budgets contenus 10×) : **le ROI est dans les colonnes P0 à KD < 25**, c'est-à-dire (a) le cluster souveraineté/AI Act, (b) les pages « alternative à X », (c) les termes FR de catégorie où seuls des sites minces se battent. C'est là que Callem peut être n°1 en un trimestre.

---

## 2. Architecture du site (Next.js 15 App Router)

### 2.1 Décision i18n : sous-répertoire, préfixe systématique

**Recommandation : `callem.ai/fr/…` et `callem.ai/en/…`, préfixe toujours présent.** Pas de sous-domaine, pas de ccTLD.

Justification :
- **Consolidation d'autorité.** Un seul domaine capitalise tous les backlinks. Avec un profil de liens jeune, c'est décisif — un `fr.callem.ai` recommencerait de zéro.
- **Scalabilité UE.** L'ajout de `/de/`, `/es/`, `/it/`, `/nl/` est trivial ; c'est le plan à 12 mois pour l'Europe.
- **Pas d'ambiguïté de résolution.** `localePrefix: 'always'` évite le piège du contenu dupliqué entre `/` et `/fr`.

**Slugs traduits, pas mappés à l'identique.** `/fr/solutions/standard-telephonique-ia` ↔ `/en/solutions/ai-phone-system`. Utiliser le mapping `pathnames` de `next-intl` pour que le sélecteur de langue et les `hreflang` restent appariés correctement.

**Racine `/` :** redirection 307 (temporaire, jamais 301) avec négociation `Accept-Language`, cookie de préférence `NEXT_LOCALE`. Le 307 signale à Google que la racine n'est pas une redirection permanente vers une langue.

**Plan hreflang :** chaque page émet le jeu complet, y compris l'auto-référence.

```
<link rel="alternate" hreflang="fr-FR" href="https://callem.ai/fr/solutions/standard-telephonique-ia" />
<link rel="alternate" hreflang="fr"    href="https://callem.ai/fr/solutions/standard-telephonique-ia" />
<link rel="alternate" hreflang="en"    href="https://callem.ai/en/solutions/ai-phone-system" />
<link rel="alternate" hreflang="x-default" href="https://callem.ai/en/solutions/ai-phone-system" />
<link rel="canonical" href="https://callem.ai/fr/solutions/standard-telephonique-ia" />
```

`x-default` → **`/en/`**, pas `/fr/` : c'est le repli pour l'Allemagne, l'Espagne, les Pays-Bas, les pays nordiques — la cible d'expansion. `hreflang="fr"` sans région couvre Belgique/Suisse/Québec sans créer de pages dédiées.

**Règles non négociables :** hreflang réciproque (si A pointe B, B pointe A, sinon Google ignore tout le cluster) · URL absolues · même statut HTTP 200 des deux côtés · **si une page n'existe pas en EN, elle n'apparaît dans aucun hreflang** — ne jamais pointer vers une traduction inexistante ou machine.

### 2.2 Arborescence complète

```
callem.ai/
├── /fr                                          → « agent vocal IA », « agent vocal », « agent IA téléphonique »
│
├── /fr/produit                                  → « plateforme agent vocal IA », « IA vocale entreprise »
│   ├── /studio-agents                           → « créer un agent vocal IA », « générateur de prompt agent »
│   ├── /base-de-connaissances                   → « base de connaissances RAG », « agent vocal RAG »
│   ├── /outils-et-workflows                     → « workflow conversationnel IA », « function calling vocal »
│   ├── /tests-et-simulation                     → « tester un agent vocal », « simulation d'appels IA »
│   ├── /canaux-de-deploiement                   → « numéro de téléphone IA », « déployer un agent vocal »
│   ├── /telephonie-et-sip                       → « trunk SIP IA », « alternative Twilio », « CTI IA »
│   ├── /supervision-et-analytics                → « analyse des appels IA », « quality monitoring IA »
│   ├── /securite-et-garde-fous                  → « garde-fous LLM », « hallucination agent vocal »
│   ├── /voix-et-modeles                         → « synthèse vocale française », « clonage de voix RGPD »
│   └── /api                                     → « API agent vocal », « API voix » (→ docs)
│
├── /fr/solutions                                → hub, « cas d'usage agent vocal IA »
│   ├── /standard-telephonique-ia          ★     → « standard téléphonique IA » (880) — page argent n°1
│   ├── /svi-intelligent                   ★     → « SVI intelligent », « serveur vocal interactif IA »
│   ├── /support-client                          → « IA service client téléphone », « callbot support »
│   ├── /qualification-de-leads                  → « qualification de leads IA »
│   ├── /prise-de-rendez-vous                    → « prise de rendez-vous automatique téléphone »
│   ├── /campagnes-sortantes                     → « prospection téléphonique IA », « appels sortants automatisés »
│   ├── /recouvrement                            → « relance impayés IA », « recouvrement automatisé »
│   ├── /permanence-telephonique-ia              → « secrétariat téléphonique IA », « permanence téléphonique IA »
│   └── /debordement-d-appels                    → « débordement d'appels », « gestion pics d'appels »
│
├── /fr/secteurs                                 → hub
│   ├── /sante            /assurance             /mutuelle-prevoyance
│   ├── /banque-finance   /immobilier            /e-commerce-retail
│   ├── /energie-utilities /transport-logistique /telecom
│   ├── /secteur-public   /education-formation   /automobile
│   ├── /btp-et-services  /tourisme-hotellerie   /bpo-centres-de-contact
│
├── /fr/integrations                             → hub, « intégrations agent vocal IA »
│   ├── /salesforce  /hubspot  /pipedrive  /zoho-crm  /attio  /close
│   ├── /zendesk  /servicenow  /genesys  /nice-cxone  /five9  /talkdesk
│   ├── /twilio  /cisco  /cal-com  /zapier  /make  /n8n  /slack
│   ├── /google-workspace  /microsoft-teams  /doctolib  /sage  /cegid  ...
│   └── /mcp                                     → « MCP agent vocal » (différenciant technique)
│
├── /fr/alternatives                             → hub, « alternative agent vocal IA »
│   ├── /vapi  /retell-ai  /bland-ai  /elevenlabs-agents  /synthflow
│   ├── /zaion  /yelda  /calldesk  /dydu  /talkr  /diabolocom  /eloquant
│   ├── /polyai  /cognigy  /parloa  /sierra  /decagon  /thoughtly
│   ├── /twilio  /google-dialogflow-cx  /amazon-connect  /genesys-cloud-ai
│   ├── /aircall  /ringover  /nice-cxone  /five9  /vocode  /air-ai
│
├── /fr/comparatifs                              → hub, « comparatif callbot »
│   ├── /meilleurs-agents-vocaux-ia        ★     → « meilleur agent vocal IA » (390)
│   ├── /meilleurs-callbots-france
│   ├── /svi-vs-agent-vocal-ia
│   ├── /vapi-vs-retell  /retell-vs-bland  /zaion-vs-calldesk  /vapi-vs-elevenlabs …
│
├── /fr/tarifs                             ★     → « agent vocal IA prix », « callbot prix »
├── /fr/demo                                     → « démo agent vocal IA » (noindex si formulaire pur)
│
├── /fr/confiance                          ★     → Trust Center, « sécurité agent vocal IA »
│   ├── /rgpd                                    → « RGPD et IA », « callbot RGPD »
│   ├── /ai-act                            ★     → « article 50 AI Act », « conformité règlement IA »
│   ├── /hebergement-des-donnees                 → « hébergement données IA France », « souveraineté »
│   ├── /deploiement-on-premise                  → « agent vocal IA on-premise »
│   ├── /sous-traitants                          → registre sous-traitants (obligatoire RGPD, +confiance)
│   ├── /securite                                → chiffrement, SSO, RBAC, ISO/SOC2 roadmap
│   └── /empreinte-carbone                       → « empreinte carbone IA », « reporting CSRD IA »
│
├── /fr/ressources                               → hub
│   ├── /guides/[slug]                           → piliers longs (5-8 au total)
│   ├── /glossaire  et  /glossaire/[terme]       → ~120 définitions (moteur AEO)
│   ├── /calculateur-roi                         → « calculateur ROI agent vocal » (aimant à liens)
│   ├── /livres-blancs/[slug]
│   ├── /webinaires/[slug]
│   ├── /modeles-d-agents/[slug]                 → scripts prêts à l'emploi par métier
│   └── /barometre-ia-vocale                ★    → étude annuelle propriétaire (aimant à liens + citations LLM)
│
├── /fr/clients  et  /fr/clients/[slug]          → études de cas
├── /fr/blog  ·  /fr/blog/[slug]  ·  /fr/blog/categorie/[slug]  ·  /fr/blog/auteur/[slug]
├── /fr/partenaires  ·  /fr/partenaires/[slug]   → programme revendeurs/intégrateurs
├── /fr/a-propos  ·  /fr/carrieres  ·  /fr/contact  ·  /fr/presse
├── /fr/juridique/{mentions-legales, politique-de-confidentialite, cgu, cgv, dpa, cookies, accessibilite}
│
├── /en/…                                        → miroir avec slugs anglais
├── /docs                                        → proxy vers la doc (voir ci-dessous)
├── /llms.txt  ·  /llms-full.txt
├── /sitemap.xml (index)  ·  /robots.txt
```

★ = page argent prioritaire.

**Docs : rapatrier `docs.callem.ai` sur `callem.ai/docs`.** Un `rewrite` dans `next.config.js` proxifie Mintlify/Docusaurus sous le domaine principal sans migration douloureuse. Gain : l'autorité des liens développeurs (GitHub, Stack Overflow, Reddit, blogs techniques) profite au domaine commercial. Les docs sont massivement citées par les LLM sur les requêtes d'implémentation — cette autorité doit atterrir sur `callem.ai`, pas à côté. Si le proxy est bloquant techniquement, garder le sous-domaine mais imposer un maillage bidirectionnel dense et déclarer les deux dans la Search Console.

**Profondeur de clic :** toute page argent à ≤ 2 clics de `/fr`. Les hubs (`/solutions`, `/secteurs`, `/integrations`, `/alternatives`) sont de vraies pages avec du contenu unique, pas de simples annuaires de liens.

---

## 3. SEO programmatique — inventaire et volumétrie

### 3.1 Inventaire par famille

| # | Famille | Modèle d'URL | Pages/locale | ×2 locales | Vol. moyen unitaire | Phase |
|---|---|---|---|---|---|---|
| 1 | Intégrations | `/fr/integrations/[outil]` | 60 | **120** | 10-90 | Ph. 2 |
| 2 | Alternatives | `/fr/alternatives/[concurrent]` | 28 | **56** | 30-1 300 | **Ph. 1** |
| 3 | Comparatifs tiers | `/fr/comparatifs/[a]-vs-[b]` | 20 | **40** | 20-500 | Ph. 2 |
| 4 | Secteurs | `/fr/secteurs/[secteur]` | 15 | **30** | 40-200 | **Ph. 1** |
| 5 | Cas d'usage × secteur | `/fr/secteurs/[secteur]/[cas]` | 45 | **90** | 10-70 | Ph. 3 |
| 6 | Glossaire | `/fr/ressources/glossaire/[terme]` | 120 | **240** | 10-2 400 | Ph. 2 |
| 7 | Langues supportées | `/fr/langues/[langue]` | 25 | **50** | 10-90 | Ph. 3 |
| 8 | Modèles IA | `/fr/modeles/[modele]` | 8 | **16** | 20-200 | Ph. 2 |
| 9 | Modèles d'agents (scripts) | `/fr/ressources/modeles-d-agents/[slug]` | 40 | **80** | 10-140 | Ph. 3 |
| 10 | Numéros par pays UE | `/fr/numeros/[pays]` | 30 | **60** | 20-300 | Ph. 3 |
| 11 | Études de cas | `/fr/clients/[slug]` | 20 | **40** | marque | continu |
| **Total** | | | **411** | **~822** | | |

Avec les pages éditoriales (≈ 60 produit/solutions/confiance) et le blog (≈ 100 articles à 12 mois), la cible réaliste est **~950 URL indexables à 12 mois**, dont ~820 programmatiques.

### 3.2 Matrice cas d'usage × secteur (famille 5)

9 cas d'usage × 15 secteurs = 135 combinaisons théoriques. **N'en construire que 45** — celles avec une demande réelle ET une histoire produit spécifique :

| Secteur | Cas d'usage à construire |
|---|---|
| Santé | prise de RDV, permanence, débordement, rappel de RDV |
| Assurance / Mutuelle | déclaration de sinistre, support, qualification, recouvrement |
| Banque / Finance | authentification, support, recouvrement |
| Immobilier | qualification, prise de RDV, campagnes sortantes |
| E-commerce / Retail | suivi de commande, support, SAV |
| Énergie / Utilities | relève, support, gestion de crise (pics d'appels) |
| Transport / Logistique | suivi de livraison, prise de RDV livraison |
| Telecom | support N1, débordement, rétention |
| Secteur public | accueil, orientation, prise de RDV |
| BPO | débordement, qualification, standard |

### 3.3 La règle qui décide du succès ou de l'échec

**Chaque page programmatique doit contenir au minimum 3 éléments impossibles à générer par template.** Sans ça, Google la classe en *scaled content abuse* (politique anti-spam de mars 2024) et le dossier entier est dévalué — c'est le mode d'échec n°1 du pSEO en 2026, et il est rétroactif sur tout le domaine.

Pour une page **intégration** (`/fr/integrations/salesforce`) :
1. **Table de mapping des champs réelle** — quel champ Callem écrit dans quel objet Salesforce (`Lead.Status`, `Task.Description`, champ custom `Callem_Sentiment__c`), avec les types.
2. **Capture d'écran authentique** du flux OAuth et de l'écran de mapping, prise dans le produit.
3. **Extrait de payload webhook réel** (anonymisé) + snippet cURL fonctionnel.
4. Bonus : latence mesurée de l'appel outil (`crm.get_order → 82 ms`, chiffre du content-spec), limites de l'API partenaire, et le cas d'usage sectoriel dominant sur cette intégration.

Pour une page **alternative** (`/fr/alternatives/vapi`) :
1. **Tableau comparatif à 12-15 lignes** en `<table>` HTML : latence mesurée, zone d'hébergement, modèles disponibles, dépendance Twilio, conformité RGPD/AI Act, garde-fous, tarification à la minute, support FR.
2. **Une section « Quand Vapi est le meilleur choix »** honnête. Les pages de comparaison qui ne concèdent rien sont ignorées par les LLM et détruisent la confiance acheteur. C'est aussi ce qui les rend citables.
3. **Un test reproductible** : même prompt, même scénario, latence et transcript des deux plateformes.
4. Guide de migration concret (export des agents, équivalences de configuration).

Pour une page **secteur** : une contrainte réglementaire propre au secteur (HDS pour la santé, DDA pour l'assurance, DSP2 pour la banque), un verbatim client réel du secteur, un chiffre de volumétrie d'appels typique.

**Garde-fous d'indexation :**
- `noindex` automatique sur toute page programmatique sous un seuil de contenu unique (mesurer le ratio texte-unique/texte-template ; seuil ≥ 40 %).
- Déploiement **par vagues de 30-50 URL**, pas 800 d'un coup. Surveiller le taux d'indexation dans la Search Console ; si < 70 % après 3 semaines, arrêter et densifier avant de continuer.
- Aucune combinaison sans demande vérifiée. Les 90 combinaisons non retenues de la matrice restent des ancres dans la page secteur parente, pas des URL.

---

## 4. Checklist technique on-page — Next.js 15 App Router

### 4.1 Metadata API

**Racine `app/[locale]/layout.tsx`** — définir `metadataBase` une fois, sinon toutes les URL OG sont relatives et cassées :

```ts
export const metadata: Metadata = {
  metadataBase: new URL('https://callem.ai'),
  title: { default: 'Callem — Agents vocaux IA souverains', template: '%s | Callem' },
  applicationName: 'Callem',
  authors: [{ name: 'Callem', url: 'https://callem.ai' }],
  robots: { index: true, follow: true,
    googleBot: { index: true, follow: true, 'max-image-preview': 'large',
                 'max-snippet': -1, 'max-video-preview': -1 } },
  formatDetection: { telephone: false },
}
```

`max-snippet: -1` et `max-image-preview: large` sont **indispensables pour l'AEO** : sans eux, Google limite l'extrait utilisable dans les AI Overviews.

**`generateMetadata` pour toute route dynamique**, avec canonical auto-référente et hreflang :

```ts
export async function generateMetadata(
  { params }: { params: Promise<{ locale: Locale; slug: string }> }
): Promise<Metadata> {
  const { locale, slug } = await params        // Next.js 15 : params est une Promise
  const page = await getPage(slug, locale)
  if (!page) return {}
  const path = getPathname({ locale, href: { pathname: '/integrations/[slug]', params: { slug } } })
  return {
    title: page.metaTitle,                      // ≤ 60 car., mot-clé en tête
    description: page.metaDescription,          // 140-155 car., verbe d'action + différenciateur
    alternates: {
      canonical: `https://callem.ai${path}`,
      languages: { 'fr-FR': `https://callem.ai/fr/...`,
                   'en': `https://callem.ai/en/...`,
                   'x-default': `https://callem.ai/en/...` },
    },
    openGraph: { type: 'website', locale: locale === 'fr' ? 'fr_FR' : 'en_US',
                 alternateLocale: locale === 'fr' ? 'en_US' : 'fr_FR',
                 siteName: 'Callem', url: `https://callem.ai${path}`,
                 title: page.ogTitle, description: page.ogDescription },
    twitter: { card: 'summary_large_image', site: '@callem_ai' },
  }
}
```

**Piège Next.js 15.2+ : le *metadata streaming*.** Si `generateMetadata` déclenche un comportement dynamique, les balises sont injectées dans le `<body>` après le streaming de l'UI. Googlebot le gère, mais **la plupart des crawlers LLM et des scrapers de partage social ne le gèrent pas**. Règle : toute page SEO-critique doit être prérendue (`generateStaticParams` + `dynamicParams = false`) pour que les métadonnées se trouvent dans le `<head>` du HTML initial. Vérifier systématiquement avec `curl -s URL | head -100`, jamais avec le DevTools (qui montre le DOM post-hydratation).

**Rendu par type de route :**

| Type | Stratégie | Config |
|---|---|---|
| Home, produit, solutions, confiance | SSG | statique par défaut |
| Programmatique (intégrations, alternatives, secteurs) | SSG + ISR | `generateStaticParams()` + `export const revalidate = 86400` + `export const dynamicParams = false` |
| Blog / ressources | ISR | `revalidate = 3600` |
| Tarifs (si dynamique) | ISR | `revalidate = 3600` — jamais SSR pur |
| Demo, login, app | dynamique | `noindex` |

### 4.2 JSON-LD — quoi émettre, où

Émettre **côté serveur** dans des Server Components via `<script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }} />`. Jamais via un `useEffect` client. Toujours des `@id` stables pour lier le graphe.

| Schéma | Pages | Points de vigilance |
|---|---|---|
| **Organization** | layout racine | `@id: https://callem.ai/#organization` · `sameAs` : LinkedIn, X, GitHub, Crunchbase, Wikidata, G2, Capterra, Product Hunt, Societe.com · `address` (Paris) · `foundingDate` · `logo` ≥ 112×112 · `contactPoint` avec `areaServed: ["FR","EU"]` et `availableLanguage: ["fr","en"]` |
| **WebSite + SearchAction** | layout racine | `potentialAction` pointant vers `/fr/recherche?q={search_term_string}` — **n'émettre que si la recherche interne existe réellement** |
| **SoftwareApplication** | `/fr`, `/fr/produit`, `/fr/tarifs` | `applicationCategory: "BusinessApplication"` · `operatingSystem: "Web"` · `offers` avec `priceCurrency: "EUR"` et `priceSpecification` (UnitPriceSpecification, `unitCode: "MIN"`) · `featureList` |
| **Product + Offer + AggregateRating** | `/fr/tarifs` | **N'émettre `aggregateRating` que sur des avis réels et vérifiables** (G2/Capterra), sinon pénalité manuelle. En l'absence d'avis, omettre — pas d'invention. |
| **FAQPage** | toute page argent, alternatives, secteurs, intégrations, blog | Google a retiré les rich results FAQ pour la plupart des sites, **mais le balisage reste parsé par les AI Overviews et les crawlers LLM** — le conserver. Une seule FAQPage par URL ; les questions doivent apparaître visiblement dans le DOM. |
| **BreadcrumbList** | toutes sauf home | Cohérent avec le fil d'Ariane visible. Nommer les segments avec les mots-clés (« Solutions › Standard téléphonique IA »). |
| **VideoObject** | démos, webinaires, écoute d'agent | `name`, `description`, `thumbnailUrl`, `uploadDate`, `duration` (ISO 8601), `contentUrl`, `embedUrl`, et surtout **`transcript`** + chapitres via `hasPart: [Clip]` — la transcription est ce qui rend une vidéo citable par un LLM |
| **Article / BlogPosting** | blog | `author` → nœud `Person` avec `@id` stable, `jobTitle`, `sameAs` LinkedIn (signal E-E-A-T fort) · `datePublished` + `dateModified` · `publisher` → `@id` de l'Organization |
| **ItemList** | `/fr/comparatifs/meilleurs-agents-vocaux-ia` | Liste ordonnée des solutions — format qu'affectionnent les LLM pour les requêtes « meilleur X » |
| **Service** | pages solutions | `serviceType`, `areaServed: "EU"`, `provider` → Organization |
| **DefinedTerm + DefinedTermSet** | glossaire | Fait du glossaire une entité structurée ; excellent pour l'AEO |
| **HowTo** | guides d'implémentation | Plus de rich result, mais parsing LLM très efficace |

Valider en CI avec `schema-dts` (typage TS) + un test Playwright qui extrait les blocs JSON-LD et les envoie à l'API Schema Markup Validator. Un schéma cassé en production passe inaperçu pendant des mois autrement.

### 4.3 `sitemap.ts` et `robots.ts`

**Sitemap en index segmenté** (`app/sitemap.ts` avec `generateSitemaps()`), un fichier par famille : `pages`, `solutions`, `secteurs`, `integrations`, `alternatives`, `glossaire`, `blog`. Objectif : diagnostiquer le taux d'indexation **par famille** dans la Search Console. Un sitemap monolithique rend impossible de savoir que, par exemple, 80 % des pages intégrations ne sont pas indexées.

```ts
// app/sitemap.ts
export async function generateSitemaps() {
  return [{ id: 'pages' }, { id: 'solutions' }, { id: 'secteurs' },
          { id: 'integrations' }, { id: 'alternatives' }, { id: 'glossaire' }, { id: 'blog' }]
}

export default async function sitemap({ id }: { id: string }): Promise<MetadataRoute.Sitemap> {
  const entries = await getEntriesFor(id)
  return entries.map(e => ({
    url: `https://callem.ai/fr${e.path}`,
    lastModified: e.updatedAt,                 // date réelle du contenu, jamais new Date()
    changeFrequency: e.freq,
    priority: e.priority,
    alternates: { languages: { fr: `https://callem.ai/fr${e.path}`,
                               en: `https://callem.ai/en${e.pathEn}` } },
  }))
}
```

`lastModified` doit refléter une modification **substantielle** du contenu. Un `new Date()` à chaque build fait perdre toute valeur au signal et Google finit par ignorer le sitemap entier.

**`app/robots.ts`** — allowlist explicite des crawlers de réponse :

```ts
export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      { userAgent: '*', allow: '/', disallow: ['/api/', '/app/', '/*?utm_*', '/fr/demo/merci', '/en/demo/thank-you'] },
      // Crawlers de réponse — à autoriser sans hésiter, ce sont eux qui citent
      { userAgent: ['OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot', 'Perplexity-User',
                    'Claude-SearchBot', 'Claude-User', 'Google-Extended', 'Applebot-Extended',
                    'Amazonbot', 'meta-externalagent', 'Bingbot', 'DuckAssistBot'], allow: '/' },
      // Crawlers d'entraînement — décision business ; recommandation : autoriser
      { userAgent: ['GPTBot', 'ClaudeBot', 'CCBot', 'cohere-ai'], allow: '/' },
    ],
    sitemap: 'https://callem.ai/sitemap.xml',
    host: 'https://callem.ai',
  }
}
```

**Vérifier le WAF, pas seulement robots.txt.** La cause n°1 d'absence de citation par Perplexity/ChatGPT est un blocage Cloudflare/Vercel Firewall en amont — le `robots.txt` autorise, le pare-feu renvoie 403. Cloudflare active désormais par défaut le blocage des bots IA sur les nouveaux domaines : **il faut le désactiver explicitement**. Contrôle : `curl -A "PerplexityBot" -I https://callem.ai/fr` → doit renvoyer 200.

### 4.4 Génération d'images OG

`app/[locale]/opengraph-image.tsx` + surcharges par segment, via `ImageResponse` :

```ts
export const runtime = 'edge'
export const size = { width: 1200, height: 630 }
export const contentType = 'image/png'
export const alt = 'Callem — Agents vocaux IA souverains'

export default async function Image({ params }) {
  const font = await fetch(new URL('./fonts/Display.woff', import.meta.url)).then(r => r.arrayBuffer())
  return new ImageResponse(<OgTemplate … />, { ...size, fonts: [{ name: 'Display', data: font, weight: 700 }] })
}
```

Contraintes réelles : `ImageResponse` ne supporte qu'un sous-ensemble de CSS (flexbox oui, grid non), pas de `next/font` — charger le `.woff` en `arrayBuffer`. **Templates différenciés par type de page** : produit (nom de fonctionnalité + capture), alternative (logo Callem `vs` logo concurrent), blog (titre + auteur + date), glossaire (le terme en très grand). Prévoir des variantes FR/EN.

Conformément à la barre de qualité du brief : **pas de fond dégradé violet→bleu, pas de blob flou, pas de glassmorphism**. L'image OG est le premier contact visuel sur LinkedIn — c'est là que le tell « site généré par IA » se voit le plus.

### 4.5 Core Web Vitals — cibles

Cibles internes plus strictes que les seuils Google, mesurées au **p75 sur données terrain (CrUX)**, pas en laboratoire :

| Métrique | Seuil Google « bon » | **Cible Callem** | Levier principal |
|---|---|---|---|
| **LCP** | ≤ 2,5 s | **≤ 1,8 s** | Hero en HTML/CSS pur (pas d'image), police auto-hébergée préchargée, HTML statique |
| **INP** | ≤ 200 ms | **≤ 130 ms** | Server Components, JS client minimal, pas d'hydratation du hero |
| **CLS** | ≤ 0,1 | **≤ 0,03** | `size-adjust` sur les polices de repli, dimensions réservées, bandeau cookies rendu serveur |
| **TTFB** | ≤ 800 ms | **≤ 300 ms** | SSG + CDN edge, région UE |
| Poids JS initial | — | **≤ 120 KB gzip** | `optimizePackageImports`, `next/dynamic` sur les composants sous la ligne de flottaison |

Le brief impose un hero riche (carte Agent, onde audio, télémétrie live). **Aucun de ces éléments ne doit être l'élément LCP.** Le LCP doit être le H1 en texte. La forme d'onde animée, le lecteur audio « Écouter un agent en direct » et le bandeau de télémétrie se chargent en `next/dynamic({ ssr: false })` après l'hydratation, avec un placeholder de dimensions identiques. L'audio est le piège le plus courant : un `<audio preload="auto">` dans le hero détruit le LCP.

Instrumenter avec `useReportWebVitals` → endpoint interne, et croiser avec les données CrUX. Budget de performance en CI via Lighthouse CI, qui **fait échouer la PR** si le budget est dépassé — sinon la dette s'accumule silencieusement.

### 4.6 Stratégie de polices

- **`next/font/local` exclusivement.** Ne jamais utiliser `next/font/google` ni un `<link>` vers `fonts.googleapis.com` : le tribunal de Munich (janv. 2022) a jugé l'appel à Google Fonts contraire au RGPD, et la CNIL suit cette ligne. Pour une entreprise dont le différenciateur est la souveraineté des données, une police servie depuis un CDN américain sur la page « RGPD natif » est une contradiction que les prospects **vont** relever.
- Deux familles maximum (cf. brief) : une display/grotesque à caractère + une neutre de lecture, plus une mono pour les blocs de code et la télémétrie.
- **Polices variables**, format `woff2` uniquement, sous-ensemble `latin` + `latin-ext` (indispensable pour l'allemand, le polonais et le tchèque en phase d'expansion UE).
- `display: 'swap'` + `preload: true` sur les graisses du hero uniquement.
- **`adjustFontFallback` / métriques `size-adjust`, `ascent-override`, `descent-override` calculées** sur la police de repli. C'est le seul moyen d'atteindre CLS ≤ 0,03 avec des polices personnalisées.
- Exposer via variables CSS (`--font-display`, `--font-body`) sur `<html>`.
- Le brief demande apostrophes typographiques françaises (’), espaces fines insécables avant `: ; ! ?` et dans les guillemets « … » : **s'assurer que le jeu de caractères sous-ensemblé contient U+2019, U+202F et U+00AB/BB**, sinon ces glyphes tombent en repli et provoquent un décalage visible.

### 4.7 Stratégie d'images

- `next/image` partout, `formats: ['image/avif', 'image/webp']`.
- Attribut `sizes` **obligatoire et exact** sur chaque image responsive. Un `sizes` absent ou erroné fait télécharger la variante 3840 px sur mobile — cause n°1 de LCP dégradé sur les sites Next.js.
- `priority` sur l'unique image LCP (si le hero en contient une), `loading="lazy"` par défaut ailleurs, `fetchPriority="high"` sur le LCP.
- `placeholder="blur"` avec `blurDataURL` généré au build (`plaiceholder`) — jamais de blur généré à la volée.
- **Loader et stockage en UE** : Scaleway Object Storage / OVHcloud / Bunny.net (région UE) plutôt que le CDN par défaut. Cohérence avec le positionnement, et argument vérifiable par le prospect.
- `alt` descriptif et unique, incluant le mot-clé quand c'est naturel. Sur les captures produit : décrire ce que l'écran montre (« Écran de mapping des champs Callem vers Salesforce »), pas « capture d'écran ».
- Les logos partenaires du bandeau : **wordmarks en texte/SVG inline**, pas des PNG gris (exigence explicite du brief, et bénéfice performance).
- Nommer les fichiers en slug sémantique : `callem-studio-garde-fous-agent.avif`.

### 4.8 Divers technique

- **Analytics** : Matomo auto-hébergé ou Plausible (UE). Google Analytics 4 est en tension permanente avec les DPA européennes (décisions CNIL/DSB/Garante) — et sur une page « aucune donnée hors UE », c'est une faille de crédibilité. Plausible est en plus sans cookie → **pas de bandeau de consentement** → pas de CLS, pas de dégradation d'INP. Double bénéfice.
- **Bandeau de consentement** (si conservé pour d'autres traceurs) : rendu serveur, hauteur réservée, jamais un overlay injecté au chargement.
- Scripts tiers : `next/script` en `strategy="lazyOnload"`, aucun GTM sur les pages argent.
- URL : minuscules, tirets, **pas de barre oblique finale**, cohérence forcée par `trailingSlash: false` + redirections 308.
- Purger tous les paramètres `?utm_*` du canonical.
- Search Console : propriété de domaine + propriétés par répertoire `/fr/` et `/en/` (indispensable pour lire les performances par langue).
- Bing Webmaster Tools et IndexNow : Bing alimente ChatGPT et Copilot — **c'est un canal AEO direct**, souvent négligé. Brancher IndexNow sur le webhook de publication.

---

## 5. AEO / GEO — être cité par ChatGPT, Perplexity et les AI Overviews

Position de Google : les AI Overviews reposent sur les systèmes de classement de la Recherche, donc « optimiser pour l'IA générative, c'est toujours du SEO ». Google déclare aussi ne pas utiliser `llms.txt`. Mais **Perplexity, ChatGPT et Claude ne sont pas Google** — et le coût marginal de `llms.txt` est de quelques heures. À faire, sans en attendre d'effet côté Google.

### 5.1 `llms.txt` et `llms-full.txt`

Servis via `app/llms.txt/route.ts` (Route Handler, `Content-Type: text/plain`), générés depuis la même source que le sitemap pour ne jamais diverger.

```markdown
# Callem

> Callem est une plateforme française d'agents vocaux IA pour les entreprises
> mid-market et grands comptes. Traitement de la parole, inférence et stockage
> s'exécutent intégralement sur une infrastructure située à Paris : aucune donnée
> ne quitte l'Union européenne. Latence bout-en-bout ~600 ms. Lauréat BPI French Tech.

## Différenciateurs
- Souveraineté : modèles STT et LLM propriétaires exécutés en France, pas seulement
  hébergement en région UE. Distinction résidence vs souveraineté : voir /fr/confiance/hebergement-des-donnees
- Télécom indépendante : infrastructure SIP propre, sans dépendance à Twilio ni Telnyx
- Garde-fous en trois phases (avant / pendant / après) — voir /fr/produit/securite-et-garde-fous
- Reporting CO₂ natif, export CSRD Scope 3

## Produit
- [Studio d'agents](https://callem.ai/fr/produit/studio-agents) : construction d'agents (Identité, Missions, Garde-fous)
- [Sécurité & garde-fous](https://callem.ai/fr/produit/securite-et-garde-fous)
…

## Conformité
- [Article 50 du Règlement IA](https://callem.ai/fr/confiance/ai-act) : obligations de transparence applicables depuis le 2 août 2026
- [RGPD](https://callem.ai/fr/confiance/rgpd)
…
```

`llms-full.txt` = concaténation markdown du contenu intégral des ~40 pages canoniques. Complément utile : servir chaque page en markdown brut via `Accept: text/markdown` ou un suffixe `.md` (`/fr/produit/studio-agents.md`) — pratique adoptée par les documentations modernes et bien exploitée par les agents.

### 5.2 Structure de contenu citable

- **Réponse en tête.** Sous chaque H2 formulé en question, les 40-60 premiers mots répondent littéralement, en une phrase autonome extractible hors contexte. Le développement vient après. C'est le format que les moteurs de réponse extraient.
- **Définition canonique.** Chaque page ouvre sur un « X est … » factuel. Le glossaire industrialise ce format sur 120 termes.
- **Tableaux HTML natifs.** `<table>` avec `<thead>`/`<th scope>`, jamais des `div` en flex ni des images de tableau. Les LLM parsent les tableaux HTML avec une fidélité élevée et les restituent presque tels quels. C'est le format le plus citable qui existe.
- **FAQ structurée** sur chaque page argent : 6-10 questions reprenant des requêtes réelles, réponses de 40-80 mots, `FAQPage` en JSON-LD, questions visibles dans le DOM.
- **Attribution explicite.** « Selon les mesures Callem sur 12 000 appels en production (T2 2026), la latence médiane bout-en-bout est de 612 ms. » Un LLM cite volontiers un chiffre attribué à une source nommée ; il ignore un chiffre orphelin.

### 5.3 Statistiques propriétaires — la munition

Les LLM citent ce que **seul Callem possède**. À produire et à maintenir :

1. **Décomposition de latence** : STT 90 ms · RAG 80 ms · LLM 180 ms · TTS 150 ms · Réseau 100 ms → ~600 ms. Comparaison : leaders US 500-800 ms, solutions historiques 1 200 ms+. Publier la méthodologie de mesure.
2. **Intensité carbone** : ~50 g CO₂/kWh en France vs ~400 g aux États-Unis. Chiffre vérifiable (RTE / EIA), avec sources, décliné en « CO₂ par minute d'appel ».
3. **Baromètre annuel de l'IA vocale en Europe** — enquête propriétaire auprès de 200+ directeurs des opérations FR/DACH/BENELUX : taux d'adoption, freins, poids de la souveraineté dans le choix, préparation à l'article 50. **C'est l'actif de link-building et de citation LLM le plus rentable du plan.** Une seule étude sérieuse génère plus de liens que 30 articles.
4. **Benchmark de conformité article 50** : combien de plateformes d'agents vocaux disposent réellement d'un mécanisme de divulgation IA natif ? Testable, publiable, repris par la presse spécialisée.
5. Métriques d'impact du content-spec (−30 % de coûts opérationnels, ÷6 sur le coût de traitement, −50 % de transferts mal orientés, ROI < 6 mois) — **toujours accompagnées de leur note de méthode**. Le brief est explicite : pas de chiffre rond sans source.

### 5.4 Cohérence d'entité

Le facteur le plus corrélé aux citations LLM est la **notoriété de marque** — les marques du quartile supérieur en mentions web obtiennent ~10× plus de visibilité IA. Cela se construit par la cohérence :

- **Une seule description canonique** de Callem (2 phrases), utilisée à l'identique partout : site, `Organization.description`, LinkedIn, Crunchbase, G2, Capterra, Product Hunt, Appvizer, Societe.com, GitHub, communiqués.
- **Créer l'élément Wikidata** (Callem, société, France, secteur IA conversationnelle) avec sources. Wikidata alimente les graphes de connaissances de plusieurs moteurs de réponse.
- `sameAs` exhaustif dans `Organization` — c'est le lien explicite entre le site et toutes ces entités.
- Nommer et exposer les auteurs : pages `/fr/blog/auteur/[slug]`, schéma `Person` avec `sameAs` LinkedIn. LinkedIn figure dans le top 10 des sources citées par les AI Overviews.
- Une seule graphie : « Callem » (jamais « CallEm », « Callem AI », « Callem.ai » en corps de texte).

### 5.5 Être présent dans le corpus source

C'est le levier le plus sous-estimé. Sur « meilleur agent vocal IA », ChatGPT et Perplexity citent `comparatif-logiciels.fr`, `lessentieldeleco.fr`, `callbot-ia.com`, `ia-insights.fr`, `voicebotfrance.fr`, plus G2, Capterra, Reddit et YouTube. **Callem doit figurer dans ces listicles.** Actions :

- Démarcher chaque éditeur de comparatif FR identifié (7 sites recensés) avec un dossier presse, un accès démo et des chiffres vérifiables. Plusieurs sont affiliés → une offre de partenariat suffit.
- Profils G2 et Capterra complets, 15+ avis clients authentiques dans les 6 premiers mois. Une soumission Gartner Digital Markets alimente Capterra, GetApp **et** Software Advice.
- Reddit : contributions substantielles et transparentes sur r/artificial, r/SaaS, r/voiceai, r/france — Reddit est massivement cité par les LLM. Jamais de faux compte : le coût d'un dévoilement dépasse tout gain.
- YouTube avec transcriptions : démos produit, extraits d'appels réels. Les transcriptions YouTube sont indexées et citées.

### 5.6 Mesure

- Suivi de part de voix LLM : Profound, Peec AI, Otterly.ai ou LLMrefs — requêtes suivies en FR et EN sur les 30 mots-clés P0.
- **Analyse des logs serveur** pour les hits `OAI-SearchBot`, `PerplexityBot`, `ClaudeBot`, `Google-Extended` : quelles pages sont crawlées, à quelle fréquence. Signal précoce et gratuit, disponible avant toute citation.
- Segment analytics sur le trafic de référence `chatgpt.com`, `perplexity.ai`, `claude.ai`, `copilot.microsoft.com` — croissance rapide, souvent invisible faute de segment configuré.
- Suivi mensuel manuel : poser 20 questions d'acheteur type aux 4 principaux moteurs, consigner les citations.

---

## 6. Plan éditorial — 20 articles en français

Ordonnés par priorité de publication. Chaque titre vise un mot-clé identifié en §1 et un moment précis du parcours d'achat.

**Vague 1 — fenêtre réglementaire (semaines 1-4, priorité absolue)**

1. **Article 50 du Règlement IA : ce que votre agent vocal doit annoncer depuis le 2 août 2026** — *article 50 AI Act* · pilier de conformité, référencé depuis toutes les pages produit, mis à jour trimestriellement
2. **Agent vocal IA et RGPD : consentement, enregistrement des appels et script légal conforme CNIL** — *RGPD et IA* · inclut un modèle de script téléphonique téléchargeable
3. **Résidence des données ou souveraineté ? Pourquoi « hébergé à Francfort » ne suffit plus** — *IA souveraine* · l'article qui pose l'angle CLOUD Act, socle de tout le positionnement
4. **Prospection téléphonique par IA en France : ce que disent réellement le RGPD, Bloctel et le Règlement IA** — *prospection téléphonique IA* · sujet à forte anxiété, très partagé

**Vague 2 — capture de catégorie (semaines 5-10)**

5. **Callbot, voicebot, agent vocal IA, SVI : le vocabulaire enfin clarifié** — *callbot* / *voicebot* · pilier de définition, tête du maillage glossaire
6. **Remplacer son SVI par un agent vocal IA : méthode en 6 étapes et budget réel** — *serveur vocal interactif IA* · le trajet de migration que cherchent les responsables de centre de contact
7. **Combien coûte vraiment un agent vocal IA ? Décomposition d'une facture à 50 000 appels/mois** — *agent vocal IA prix* · transparence tarifaire = très fort taux de conversion
8. **Latence d'un agent vocal : d'où viennent les 600 ms et pourquoi ça décide de la qualité de l'appel** — *latence agent vocal* · contenu technique propriétaire, très citable par les LLM
9. **Standard téléphonique IA : ce qui change concrètement pour une entreprise de 200 à 2 000 salariés** — *standard téléphonique IA* · soutient la page argent n°1
10. **Les 5 raisons pour lesquelles un projet de callbot échoue (et comment les éviter)** — TOFU · contenu contrarien, aimant à liens et à partages LinkedIn

**Vague 3 — évaluation et comparaison (semaines 11-18)**

11. **Comparatif 2026 : 12 plateformes d'agents vocaux IA testées sur la latence, la conformité et le coût réel** — *meilleur agent vocal IA* · **méthodologie publiée, concurrents inclus honnêtement** ; article de tête de tunnel le plus rentable
12. **Vapi, Retell, Bland, ElevenLabs : ce que les plateformes américaines impliquent pour vos données européennes** — *alternative Vapi* · relie le cluster alternatives au cluster souveraineté
13. **Grille d'évaluation d'un agent vocal IA : les 27 questions à poser en appel d'offres** — MOFU · checklist téléchargeable, aimant à leads très performant
14. **Faire ou acheter : construire son agent vocal sur GPT-4o Realtime vs adopter une plateforme** — *agent vocal IA open source* · capte l'audience technique qui évalue le build
15. **Hallucinations d'un agent vocal : comment les mesurer et les ramener sous 1 %** — MOFU · sujet d'angoisse n°1 des acheteurs enterprise, terrain où Callem est fort

**Vague 4 — verticaux et preuves (semaines 19-26)**

16. **Agent vocal IA en cabinet médical : prise de rendez-vous, HDS et réduction des rendez-vous non honorés** — *agent vocal IA santé* · alimente `/fr/secteurs/sante`
17. **Assurance : automatiser la déclaration de sinistre par téléphone sans dégrader l'expérience client** — *callbot assurance*
18. **Gérer un pic d'appels ×10 sans recruter : le débordement intelligent en pratique** — *débordement d'appels* · cas d'usage énergie/telecom/secteur public
19. **Empreinte carbone d'un agent vocal IA : méthode de calcul et reporting CSRD Scope 3** — *empreinte carbone IA* · sujet quasi vierge, différenciant, très citable
20. **Ce que 12 000 appels traités par IA nous ont appris sur le transfert vers un humain** — donnée propriétaire · le format d'article que les LLM citent le plus volontiers

**Cadence :** 4-5 articles/mois en français les 6 premiers mois, 2 000-3 000 mots chacun, avec au moins un élément de preuve original (chiffre mesuré, capture produit, verbatim, tableau). Traduction anglaise (**humaine ou révisée par un humain**, jamais brute) uniquement pour les articles 1, 3, 5, 8, 11, 12, 19, 20 — ceux dont l'angle voyage. Traduire tout le blog en anglais serait un gaspillage : la SERP anglaise est autrement plus disputée.

---

## 7. Netlinking et autorité — tactiques marché français

### 7.1 Socle d'entité (semaines 1-3, à faire une fois)

Pappers · Societe.com · **Wikidata** (créer l'élément) · Crunchbase · Dealroom · LinkedIn Company · GitHub Organization · Welcome to the Jungle (page carrières = lien DR 90) · Google Business Profile (Paris). Objectif : cohérence d'entité et fondation `sameAs`, pas le jus de lien.

### 7.2 Écosystème French Tech / BPI — la carte maîtresse

Callem est **lauréat BPI French Tech**. Cet actif est largement sous-exploité et donne accès à des domaines à très forte autorité, difficiles d'accès autrement :

- **lafrenchtech.com** — annuaire officiel de la Mission French Tech
- **bpifrance.fr** et **bpifrance-creation.fr** — pages lauréats, actualités, portraits
- **lesdeeptech.fr** (BPI) — si l'angle modèles propriétaires le permet
- **French Tech Central** / capitale French Tech locale — annuaire et événements
- **Station F**, **Wilco**, **Le Village by CA**, **Paris&Co** — si programme d'accompagnement
- **Pôles de compétitivité : Cap Digital, Systematic Paris-Region** — l'adhésion donne une fiche membre + participation aux publications sectorielles
- **France Num** (Bercy) — annuaire de solutions pour la numérisation des TPE/PME, proche du `.gouv`

### 7.3 Souveraineté numérique — l'écosystème que personne ne travaille

C'est le levier différenciant, et il est presque inexploité par les concurrents :

- **Hexatrust** — association des acteurs français du cloud et de la cybersécurité de confiance. Adhésion = fiche membre, publications communes, visibilité auprès des acheteurs grands comptes et secteur public. Alignement parfait avec le positionnement.
- **Numeum** (syndicat du numérique) — commissions IA, publications
- **Cigref** (DSI des grandes entreprises) — participation aux groupes de travail IA ; les publications Cigref sont lues et citées par exactement l'audience cible
- **Gaia-X** / **Cloud de confiance** — écosystème et annuaires
- **Annuaires des partenaires : OVHcloud, Scaleway, Outscale, Cloud Temple, NumSpot** — si l'infrastructure parisienne s'appuie sur l'un d'eux, la fiche partenaire est un lien contextuel de forte valeur

### 7.4 Annuaires et plateformes d'avis (priorité par ROI)

| Plateforme | Pourquoi | Prio |
|---|---|---|
| **Appvizer** | Le plus fort référenceur B2B francophone ; domine les SERP « logiciel X » en FR | **P0** |
| **G2** | Standard mid-market/enterprise, cité par les LLM | **P0** |
| **Capterra / GetApp / Software Advice** | Une soumission Gartner Digital Markets → trois sites | **P0** |
| **Product Hunt** | Lancement, pic de notoriété, lien DR 90 | P1 |
| **Comparatif-logiciels.fr, Logiciels.pro, Toolinbox** | Comparateurs FR déjà classés sur les requêtes cibles | P1 |
| Trustpilot | Confiance, avis vérifiés | P2 |
| Tekpon, SourceForge, Slashdot, SaaSHub, AlternativeTo | Volume, cité par les LLM sur « alternative à X » | P2 |
| Les Pépites Tech, Maddyness (Maddymap) | Écosystème startup FR | P2 |

### 7.5 Presse spécialisée et relation client (le canal le plus qualifié)

L'audience de Callem — directeurs de la relation client, responsables de centre de contact, DSI — lit une presse professionnelle précise :

- **En-Contact** — la référence des centres de contact en France, lectorat exactement ciblé
- **Relation Client Magazine** / **Le Mag des Relations Clients**
- **Journal du Net**, **L'Usine Digitale**, **Silicon.fr**, **LeMagIT**, **Alliancy**, **ITforBusiness**
- **Les Échos Entrepreneurs**, **La Tribune**, **Numerama / Next** (angle souveraineté)
- **Frenchweb**, **Maddyness**

**Angle presse à dégainer immédiatement :** le benchmark de conformité article 50. « X plateformes d'agents vocaux sur Y ne permettent pas de se conformer à l'obligation de transparence entrée en vigueur le 2 août. » C'est une histoire prête à publier, chiffrée, d'actualité, et Callem en est le protagoniste naturel. Fenêtre : environ 6 mois.

### 7.6 Marketplaces partenaires (liens + trafic qualifié)

Chaque intégration construite ouvre une fiche sur une marketplace à forte autorité, avec en prime du trafic acheteur :

Salesforce AppExchange · HubSpot App Marketplace · Zendesk Marketplace · **Genesys AppFoundry** · Zoho Marketplace · Pipedrive Marketplace · Zapier App Directory · Make · n8n · Cal.com Apps · Slack App Directory · Twilio Showcase · Mistral AI partners · Scaleway/OVHcloud marketplace.

C'est le meilleur rapport effort/rendement du plan : le travail d'intégration est déjà fait pour le produit, la fiche est un sous-produit gratuit.

### 7.7 Événements et prise de parole

**Salon Stratégie Clients / All4Customer** (Porte de Versailles) — l'événement central du secteur en France : liste des exposants, programme des conférences, comptes rendus presse, tous générateurs de liens · **VivaTech** · **Big Bpifrance** · **France is AI** · **AI Paris** · **Web2Day** · **Meetups AI Paris, Mistral AI community**. Chaque intervention produit : page programme, replay YouTube, article de compte rendu, publications LinkedIn des participants.

### 7.8 Contenus créateurs de liens (par rendement décroissant)

1. **Baromètre annuel de l'IA vocale en Europe** — l'étude propriétaire ; 30-60 liens éditoriaux attendus, et une source citée en boucle par les LLM
2. **Calculateur de ROI** `/fr/ressources/calculateur-roi` — outil interactif, très partagé et intégré en lien depuis les blogs sectoriels
3. **Baromètre de conformité article 50** — mis à jour trimestriellement
4. **Comparateur de latence des plateformes vocales** — méthodologie ouverte, résultats reproductibles ; format irrésistible pour la presse tech
5. **Modèles de scripts d'agents conformes CNIL** — 40 modèles téléchargeables, à la fois aimant à leads et pSEO

### 7.9 Ce qu'il faut éviter

Fermes de liens et achats en masse sur les places de marché netlinking FR (Semjuice, Rocketlinks, Getfluence en mode volume) : profils détectables, risque de pénalité et incohérence totale avec une marque qui vend la confiance. Le PBN est hors de question. La technique de *parasite SEO* utilisée par l'agence de Yelda fonctionne à court terme mais expose à la mise à jour *site reputation abuse* de Google — à écarter pour une marque enterprise dont la crédibilité **est** le produit.

---

## 8. Séquencement et objectifs

| Phase | Semaines | Livrables | Objectif |
|---|---|---|---|
| **0 — Fondations** | 1-4 | Migration single-page → App Router i18n · metadata + JSON-LD + sitemap + robots + llms.txt · Trust Center (7 pages) · article 50 publié · Search Console/Bing/IndexNow | ~35 URL indexées · CWV au vert |
| **1 — Pages argent** | 5-12 | 10 solutions · 11 produit · tarifs · 8 alternatives P0 · 15 secteurs · comparatif « meilleurs agents vocaux » · 10 articles | ~90 URL · premiers top 10 sur les KD < 20 · G2/Capterra/Appvizer en ligne |
| **2 — Programmatique v1** | 13-24 | 60 intégrations · 20 alternatives restantes · 120 glossaire · 20 comparatifs tiers · Baromètre · calculateur ROI · 20 articles | ~450 URL · 3 000-5 000 visites organiques/mois · top 3 sur « standard téléphonique IA », « SVI intelligent », « alternative Vapi » |
| **3 — Échelle + EN** | 25-52 | Matrice cas×secteur · langues · modèles d'agents · numéros UE · miroir EN complet · campagne de liens · presse | ~950 URL · 12 000-20 000 visites/mois · 60-100 leads organiques/mois |

**Indicateurs à piloter** (dans l'ordre d'importance) : leads organiques qualifiés > pipeline attribué à l'organique > taux d'indexation par famille de sitemap > positions sur les 30 mots-clés P0 > citations LLM sur 20 requêtes types > trafic. Le trafic est le dernier indicateur, pas le premier : sur ce marché, 3 000 visites très qualifiées valent plus que 30 000 diffuses.

**Objectif à 12 mois :** position 1-3 sur « agent vocal IA », « standard téléphonique IA », « SVI intelligent », « callbot » et l'intégralité du cluster souveraineté FR + EN ; référence citée par ChatGPT et Perplexity sur « agent vocal IA conforme RGPD » et « European voice AI »; 60-100 leads organiques qualifiés par mois.

---

## Sources

- [Yelda — 10 meilleurs agents vocaux IA](https://www.yelda.fr/blog/meilleur-agent-ia-vocal) · [Étude de cas SEO Yelda par l'agence Onze](https://agenceonze.fr/cas-client/yelda-ai/)
- [Nerolia — comparatif agents vocaux et prix réels](https://nerolia-ai.fr/blog/meilleur-agent-virtuel-vocal-ia-comparatif) · [Nerolia — RGPD et conformité légale](https://nerolia-ai.fr/blog/agent-vocal-ia-france-rgpd-conformite-legale)
- [callbot-ia.com](https://callbot-ia.com/) · [svi-ia.com](https://svi-ia.com/) · [call-bot.fr](https://call-bot.fr/) · [agent-vocal-ia.fr](https://agent-vocal-ia.fr/voicebot-ia-francais) · [comparatif-logiciels.fr](https://www.comparatif-logiciels.fr/10-meilleurs-agents-vocaux-ia-en-2026-comparatif/)
- [Synthflow](https://synthflow.ai/) · [Retell AI](https://www.retellai.com/) · [Vapi](https://vapi.ai/) — architectures d'URL relevées
- [Article 50 de l'AI Act — Données Personnelles](https://www.donneespersonnelles.fr/transparence-ia-article-50-ai-act) · [Riant Avocat — obligations et sanctions](https://riant-avocat.fr/article-50-reglement-ia-obligation-transparence-sanctions/) · [Transparia](https://www.transparia.fr/ressources/transparence-ia/article-50-ai-act)
- [Telnyx — Voice AI that never leaves the EU](https://telnyx.com/resources/voice-ai-europe-data-sovereignty) · [Softcery — EU Voice AI Regulations](https://softcery.com/lab/eu-voice-ai-regulations-founders-guide) · [Dstny — the sovereignty question](https://www.dstny.com/blog/behind-the-sovereignty-question-the-voice-deals-you-can-no-longer-win)
- [Leapd — comment ChatGPT, AI Overviews et Perplexity sourcent en 2026](https://www.leapd.ai/blog/ai-visibility/how-chatgpt-google-ai-overviews-and-perplexity-source-information-in-2026) · [LLMrefs — guide GEO 2026](https://llmrefs.com/generative-engine-optimization)
- [Next.js SEO Guide 2026 — App Router & Core Web Vitals](https://appseo.com/next-js-seo-guide-2026-app-router/) · [StackNotice — Next.js 15 metadata, OG, sitemap, structured data](https://stacknotice.com/blog/nextjs-seo-guide-2026)
- [Les Pépites Tech — collection B2B French Tech](https://lespepitestech.com/startup-collection/b2b) · [AntheDesign — netlinking B2B](https://www.anthedesign.fr/referencement/top-netlinking-b2b-usa-2026/)
