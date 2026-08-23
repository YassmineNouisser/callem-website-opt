# CALLEM — SPÉCIFICATION DE CONTENU (FR) — v1
> Source unique de vérité. Les 10 propositions utilisent EXACTEMENT ce contenu.
> Seuls l'art direction, la mise en page, la typographie, le mouvement et la hiérarchie changent.
> Un designer peut réordonner/condenser les sections selon son concept, mais ne doit RIEN inventer.

---

## 0. MARQUE

- **Nom** : Callem  ·  **Produit** : Callem Studio  ·  **Domaine** : callem.ai
- **Logo** : monogramme « C » blanc dans un carré arrondi, dégradé indigo→violet (#6366F1 → #A855F7). Le « C » a une ouverture — c'est un combiné/une onde.
- **Couleur produit historique** : violet `hsl(272 96% 60%)` ≈ `#A32BFA`. Accents dashboard : orange `#EB6A0A`, bleu `#0A93DE`, vert `#4A9455`.
  → **Chaque proposition est LIBRE de réinventer la palette.** Le violet n'est PAS obligatoire (il est même le cliché n°1 des sites générés par IA). S'il est utilisé, il doit l'être avec discipline.
- **Ton de voix** : précis, factuel, sûr de soi, sans superlatifs marketing. Ingénieur senior qui parle à un directeur des opérations. Zéro emoji dans les titres. Zéro « révolutionnaire », « game-changer », « unleash ».
- **Langue** : FR par défaut, EN disponible (switch FR/EN dans la nav).

---

## 1. NAVIGATION

**Gauche** : Callem (logo + wordmark)
**Centre** : Produit · Solutions · Développeurs · Tarifs · Ressources
**Droite** : FR/EN · Se connecter · **Réserver une démo** (CTA principal)

Sous-menu *Produit* : Studio d'agents · Base de connaissances · Outils & Workflows · Tests & Simulation · Canaux de déploiement · Supervision & Analytics · Sécurité & Garde-fous
Sous-menu *Solutions* : Support client · Qualification de leads · Prise de rendez-vous · Campagnes sortantes · Recouvrement · Standard téléphonique
Sous-menu *Développeurs* : Documentation · Référence API · Guide de démarrage · MCP · Statut

---

## 2. HERO

**H1** : Des agents vocaux qui **résolvent**. Pas qui répondent.

**Sous-titre** :
> Callem Studio vous permet de créer des agents vocaux IA qui qualifient vos leads, prennent vos rendez-vous, traitent les demandes et transfèrent aux humains — avec garde-fous intégrés, supervision en temps réel et souveraineté totale des données en Europe. En production en jours, pas en mois.

**CTA primaire** : Réserver une démo
**CTA secondaire** : Écouter un agent en direct  *(ou « Parler aux ventes » selon le concept)*

**Barre de preuve (4 pastilles)** :
- Datacenter à Paris
- Lauréat BPI French Tech
- ~600 ms de latence bout-en-bout
- RGPD natif — aucune donnée hors UE

**Visuel héros — options selon le concept** (choisir UNE, la faire parfaitement) :
1. Carte « Agent » montrant la structure du prompt (Identité / Missions / Garde-fous) + statut live
2. Forme d'onde audio animée + transcription qui se déroule
3. Rendu 3D d'un objet-voix
4. Capture d'écran du Studio (recréée en HTML/CSS, pas une image)
5. Chronologie d'un appel : Sonnerie → Compréhension → Outil → Résolution
6. Bandeau de télémétrie live (appels en cours, latence, taux de résolution)

**Carte Agent — contenu exact** :
- Nom : `Assistant Commercial — Acme`  ·  Statut : `● En ligne`
- **Identité** : « Vous êtes un assistant commercial professionnel pour Acme Corp. Ton chaleureux et professionnel. »
- **Missions** : « Qualifier les leads sur le budget, l'échéance et le pouvoir de décision. »
- **Garde-fous** : ⊘ Ne jamais confirmer un prix · ⊘ Aucun conseil médical · ✓ Toujours vérifier l'identité de l'appelant
- **Live** : `14 832 appels aujourd'hui` · `Durée moy. 2:34`

---

## 3. BANDEAU TECHNOLOGIES / PARTENAIRES

Intitulé : « Une couche d'orchestration au-dessus du meilleur de l'IA vocale »
Logos (wordmarks texte, pas de logos gris flous) : OpenAI · Anthropic · Mistral AI · Google Cloud · ElevenLabs · Azure · Salesforce · HubSpot · Twilio · Zapier · Cal.com · Genesys

---

## 4. CHIFFRES CLÉS (4 métriques)

| Valeur | Libellé |
|---|---|
| ~600 ms | Latence de bout en bout |
| 25+ | Langues européennes |
| 70 % | Des appels résolus sans humain |
| 24/7 | Toujours disponible, zéro attente |

---

## 5. LA STACK — « Construire · Déployer · Superviser »

**Titre** : La stack vocale, de bout en bout
**Chapeau** : Callem orchestre les meilleurs modèles IA, moteurs vocaux et infrastructures télécoms dans une seule plateforme.

### 01 — CONSTRUIRE
Architecture de prompt structurée (Identité, Missions, Garde-fous), bases de connaissances RAG, appel d'outils en temps réel (mise à jour CRM, prise de RDV, envoi d'e-mail, webhooks), workflows conversationnels visuels, générateur de prompt IA.
**Sous-blocs** : Agents · Base de connaissances · Outils · Workflows · Tests

### 02 — DÉPLOYER
Passez en production sur des numéros de téléphone avec notre infrastructure télécom européenne — sans dépendance à Twilio.
**Sous-blocs** : Numéros de téléphone · Trunk SIP · Webchat · Campagnes sortantes
**Bientôt** : WhatsApp · SMS · Messenger · Instagram

### 03 — SUPERVISER
Analyse IA de 100 % des conversations — pas d'échantillonnage.
**Sous-blocs** : Live · Transcriptions · Analytics · Alertes · Quality Review

---

## 6. CAS D'USAGE — « Pensé pour chaque interaction »

Onglets/cartes : **Support** · **Qualification** · **Rendez-vous** · **Campagnes sortantes** · **Recouvrement**

### Support (cas détaillé)
**Titre** : Résolvez les appels support de bout en bout
- ✓ 70 % de taux de résolution sur les appels entrants
- ✓ Zéro attente, disponible 24/7
**Verbatim client** : « Les agents Callem traitent les appels répétitifs pour que notre équipe se concentre sur les cas complexes. » — *Responsable Support, client Callem*

**Conversation exemple** :
- **Agent** : « Bonjour, ici le support Acme. Je vois que votre commande #4521 a pris du retard. Je vérifie le dernier statut pour vous. »
- **Client** : « Oui s'il vous plaît, ça fait trois jours que j'attends. »
- **Agent** : « Votre colis est maintenant chez le transporteur et devrait arriver demain avant 18 h. Je vous envoie le lien de suivi par SMS ? »
- *(Appel d'outil : `crm.get_order(#4521)` → 82 ms · `sms.send(tracking)` → 140 ms)*

### Qualification
Qualifier budget, échéance et pouvoir de décision, scorer le lead, pousser dans le CRM et réserver un créneau si qualifié.
### Rendez-vous
Vérifier les disponibilités, proposer des créneaux, confirmer, envoyer l'invitation, gérer les reports et annulations.
### Campagnes sortantes
Import CSV, fenêtres d'appel, limites de concurrence, logique de relance, suivi en temps réel par contact.
### Recouvrement
Relances de paiement conformes, négociation d'échéanciers, escalade encadrée vers un conseiller humain.

---

## 7. CAPACITÉS — « Tout ce qu'il faut pour automatiser la voix »

1. **Latence de bout en bout ~600 ms** — décomposition : STT 90 ms · RAG 80 ms · LLM 180 ms · TTS 150 ms · Réseau 100 ms → **~600 ms**. Comparatif : Callem ~600 ms · leaders US 500–800 ms · solutions historiques 1 200 ms+.
2. **Multi-modèles & multilingue** — GPT-4o, Claude, Gemini ou Mistral. Sélection automatique du meilleur moteur TTS par langue. 25+ langues, VAD sémantique pour des tours de parole naturels.
3. **Appel d'outils en temps réel** — vos agents réservent via Cal.com, déclenchent des workflows Zapier, interrogent vos bases et appellent n'importe quel webhook, en pleine conversation.
4. **Base de connaissances (RAG)** — importez documents, FAQ et URLs. Le vector store Callem récupère le passage pertinent pendant l'appel.
5. **Moteur de campagnes sortantes** — import CSV, fenêtres d'appel, concurrence, relances, suivi temps réel.
6. **Analyse d'appel par IA** — sentiment, score de qualification et champs personnalisés extraits de chaque appel.
7. **Voix & audio** — TTS premium ElevenLabs et Azure. Clonage de voix. Vitesse ajustable, sons d'ambiance.
8. **Modèles IA européens** — STT et LLM propriétaires exécutés sur une infrastructure parisienne. Précision de premier plan sur 25 langues européennes. Apportez votre modèle ou utilisez notre stack souveraine.
9. **Téléphonie indépendante** — infrastructure SIP propre, sans verrou Twilio ou Telnyx. Intégration CTI native avec n'importe quel CCaaS.
10. **Sécurité & observabilité** — anonymisation des données personnelles, garde-fous LLM, détection de répondeur, traçage complet via Langfuse et Langsmith.

---

## 8. SÉCURITÉ — « La confiance par construction »

**Chapeau** :
> Aucune IA n'est fiable à 100 % — c'est une certitude mathématique, pas un défaut. C'est pourquoi nous avons construit trois couches de protection. Avec Callem, vous avez le même niveau de contrôle sur vos agents vocaux que sur vos agents humains. Sinon plus.

### Phase 1 — AVANT · Sécuriser avant de livrer
Chaque agent passe une validation multi-couches avant la production.
- Garde-fous d'entrée — bloquent les injections de prompt et les tentatives de jailbreak
- Garde-fous de sortie — filtrent les hallucinations, imposent le périmètre de sujet
- Masquage des données personnelles — anonymisation automatique
- Tests de simulation — validez les cas limites avant la mise en production

### Phase 2 — PENDANT · Observer et intervenir en temps réel
Visibilité et contrôle complets sur chaque conversation en cours, comme un superviseur de centre d'appels.
- Supervision live avec score de confiance
- Alertes intelligentes sur anomalie ou motif critique
- Intervention humaine instantanée quand la situation l'exige
- Escalade fluide avec transmission complète du contexte

### Phase 3 — APRÈS · Évaluer et améliorer chaque appel
Évaluation IA systématique sur 100 % des conversations — aucun échantillonnage, aucun angle mort.
- Scoring automatisé — taux d'hallucination, complétion de tâche, pertinence
- KPI personnalisés — taux de résolution, NPS, conversion, empathie
- Expérimentations A/B — comparez prompts, modèles et configurations
- Apprentissage continu — chaque correction rend le système plus fiable

**Citation de clôture** : « L'objectif n'est pas le risque zéro — c'est d'avoir le même niveau de contrôle qu'avec vos agents humains. Ou meilleur. »

---

## 9. IMPACT — « Des résultats mesurables dès le premier jour »

| Valeur | Libellé |
|---|---|
| −30 % | Coûts opérationnels |
| ÷6 | Coût de traitement des appels courants |
| −1 min | Durée moyenne de traitement |
| +10 pts | Amélioration du NPS |
| −50 % | Transferts mal orientés |
| < 6 mois | Retour sur investissement moyen |

*Note* : D'après des déploiements en production et des benchmarks de marché (Forrester, Gartner).

---

## 10. SOUVERAINETÉ — « Conçu en Europe. Hébergé en Europe. Reste en Europe. »

> Quand chaque concurrent américain fait transiter votre voix par des serveurs américains, Callem s'exécute entièrement sur une infrastructure européenne. Nos modèles de parole et de langage propriétaires sont déployés à Paris, sur une énergie bas carbone. Vos conversations ne quittent jamais l'UE — ni pour le traitement, ni pour le stockage, ni pour l'entraînement.

- Datacenter à Paris — énergie nucléaire, bas carbone
- RGPD natif — zéro transit hors UE
- Déploiement on-premise possible
- Lauréat BPI French Tech
- IA vocale bas carbone

### Sobriété carbone native
La première plateforme d'IA vocale avec un reporting CO₂ natif. Suivez votre empreinte par agent et par conversation. Exportez des rapports prêts pour la CSRD (Scope 3).
**Preuves** : Tableau de bord CO₂ · Export CSRD · ~50 g CO₂/kWh en France contre ~400 g aux États-Unis

---

## 11. SUPERVISION & INSIGHTS

**Analyse d'appel** — exemple de sortie : `Sentiment : Positif` · `Score de lead : 8/10` · `Issue : RDV pris`
Extrayez sentiments, scores de qualification et données personnalisées de chaque conversation, automatiquement.

**Analytics** — visualisez volumes d'appels, durées, taux de réussite, concurrence et latences avec des tableaux de bord configurables.

**Alertes intelligentes** — définissez des seuils sur n'importe quelle métrique. Exemple : `⚠ Sentiment négatif > 30 % — Actif`

**Observabilité** — tracez chaque action de l'agent, de la reconnaissance vocale au raisonnement LLM jusqu'à l'exécution d'outils.
Décomposition de latence : STT 120 ms · LLM 340 ms · Outil 200 ms · TTS 180 ms

---

## 12. INTÉGRATIONS — « S'intègre à votre stack existante »

> Connectez Callem à votre CRM, votre centre de contact et votre infrastructure télécom.

- **CRM / CX** : Salesforce · HubSpot · Pipedrive · Zoho CRM · Attio · Close · Zendesk · ServiceNow
- **Centre de contact (CCaaS)** : Genesys · NICE CXone · Five9 · Talkdesk
- **Télécom / CPaaS** : Twilio · Cisco
- **Productivité** : Cal.com · Zapier · Slack · Google Workspace

*Et des centaines d'autres via API REST et protocole MCP.*
**CTA** : Voir toutes les intégrations

---

## 13. ENTREPRISE — « Construit pour les équipes qui prennent la sécurité au sérieux »

- **Protection des données** — traitement conforme RGPD, anonymisation automatique des données personnelles pendant l'appel, gestion sécurisée des contacts avec liste d'opposition.
- **Sûreté des LLM** — garde-fous intégrés contre les injections de prompt, les jailbreaks et les réponses hors sujet. Détection de répondeur pour éviter les minutes perdues.
- **Équipe & API** — gestion des rôles (owner, admin, éditeur, lecteur), authentification par token Bearer, webhooks HTTPS uniquement, accès limité par quota.
- **Flexibilité télécom** — numéros gérés par Callem, apportez votre Twilio, ou raccordez votre SIP existant.

---

## 14. DÉVELOPPEURS — « API-first. 100 % programmable. »

> Tout est exposé en API. Créez des agents, lancez des campagnes, gérez vos contacts, récupérez les transcriptions et poussez les résultats vers n'importe quel système. Construisez vos intégrations en quelques heures.

**CTA** : Explorer l'API · Voir la documentation

```bash
curl -X POST https://api.callem.ai/v1/agents \
  -H "Authorization: Bearer cal_sk_..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Qualification Leads FR",
    "language": "fr-FR",
    "model": "callem-sovereign-v2",
    "identity": "Tu es un agent commercial professionnel",
    "tasks": ["qualify_budget", "qualify_timeline", "book_if_qualified"],
    "guardrails": ["no_competitor_pricing", "verify_identity_first"],
    "tools": ["crm_update", "cal_book", "send_email"],
    "knowledge_base": "kb_catalogue_produits_2026"
  }'
```

---

## 15. FAQ

**En combien de temps puis-je déployer un agent vocal ?**
La plupart des équipes passent de zéro à un agent en production en moins d'une semaine. Notre générateur de prompt IA produit un agent prêt pour la production en quelques minutes. Testez-le dans votre navigateur, puis déployez-le sur un numéro de téléphone.

**Quels modèles de langage puis-je utiliser ?**
GPT-4o, Claude, Gemini, Mistral, ou notre modèle souverain `callem-sovereign` exécuté à Paris. Vous pouvez aussi connecter votre propre modèle avec vos propres clés. Le choix se fait agent par agent.

**Mes données sont-elles traitées hors d'Europe ?**
Non. Avec la stack souveraine Callem, le traitement de la parole, l'inférence et le stockage restent en France. Si vous choisissez un modèle tiers, nous vous indiquons explicitement la zone de traitement avant activation. Aucune donnée n'est utilisée pour entraîner des modèles.

**Comment gérez-vous les hallucinations ?**
Trois couches : des garde-fous d'entrée et de sortie qui filtrent en temps réel, un ancrage systématique sur votre base de connaissances (RAG), et une évaluation IA après chaque appel qui mesure le taux d'hallucination. Vous fixez les seuils, vous recevez les alertes.

**L'agent peut-il transférer à un humain ?**
Oui, avec transmission complète du contexte : résumé de la conversation, données extraites et historique CRM arrivent chez le conseiller au moment du transfert. Les conditions de transfert se déclarent en langage naturel.

**Puis-je conserver ma téléphonie actuelle ?**
Oui. Numéros gérés par Callem, votre compte Twilio, ou raccordement direct à votre trunk SIP et à votre CCaaS existant (Genesys, NICE, Five9, Talkdesk).

**Combien ça coûte ?**
Un tarif à la minute d'appel, dégressif au volume, sans engagement sur les premiers mois. Contactez-nous pour une estimation basée sur votre volume réel.

---

## 16. CTA FINAL

**Titre** : Arrêtez de perdre des appels. Commencez à les résoudre.
**Sous-titre** : Déployez votre premier agent vocal cette semaine. Hébergé en Europe.
**CTA** : Réserver une démo · Contacter les ventes
**Mention** : Datacenter à Paris · RGPD natif · Réponse sous 24 h

---

## 17. FORMULAIRE DE CONTACT (si le concept l'intègre)

Champs : Prénom · Nom · E-mail professionnel · Téléphone (facultatif) · Société · Volume d'appels par mois (< 1 000 / 1 000–10 000 / 10 000–100 000 / 100 000+) · Message (facultatif)
Bouton : **Demander une démo**
Mentions : Réponse sous 24 h · Sans engagement · Démo personnalisée sur votre cas d'usage

---

## 18. PIED DE PAGE

**Produit** : Studio d'agents · Base de connaissances · Outils & Workflows · Canaux · Supervision · Sécurité · Tarifs
**Solutions** : Support client · Qualification de leads · Prise de rendez-vous · Campagnes sortantes · Recouvrement · Standard téléphonique
**Développeurs** : Documentation · Référence API · Guide de démarrage · MCP · Statut · Changelog
**Entreprise** : À propos · Blog · Carrières · Contact · Partenaires
**Légal** : Mentions légales · Politique de confidentialité · CGU · DPA · Sous-traitants · Sécurité

**Bas de page** : © 2026 Callem — Voice AI Stack Gen 2.0 · Conçu et hébergé en Europe 🇪🇺 · FR / EN
