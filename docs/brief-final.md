# BRIEF FINAL — 2 VERSIONS · CALLEM
### Synthèse du retour client sur les propositions A (Aurora), B (Orbite), C (Studio)

---

## 1. LE VERDICT CLIENT, MOT POUR MOT

### ✅ CE QU'IL A AIMÉ — À REPRENDRE, PAS À RÉINVENTER

| Élément | Source | Verbatim |
|---|---|---|
| **La navbar et son animation** | A, B, C | « le navbar et son animation est parfaite », « l'animation de navbar oui bien » |
| **Le détail d'appel #4521** | A | « l'animation fixe de *Appel #4521 · +33 1 84 88 00 00 · fr-FR · 02:34 · Résolu*… » avec la timeline 00:00→02:34, la transcription horodatée, les traces d'outils `crm.get_order(#4521) 82 ms · statut : en transit` et `sms.send(tracking) 140 ms · livré`, et la conclusion `Sentiment : Positif / Issue : Résolu sans humain` |
| **« La confiance par construction »** | A, C | Aimée dans les deux. « je l'aime bien mais encore tu peux faire mieux » |
| **« Conçu en Europe. Hébergé en Europe. Reste en Europe. »** | A, B, C | « wowww ». La section la plus unanimement plébiscitée |
| **Le scroll horizontal des logos** | A | « c bien » |
| **Les animations générales** | A | « très luxueuses, attirantes, bien » |
| **« Conçu pour résoudre. »** (interstitiel typographique) | B | Cité en premier dans les points positifs |
| **Les illustrations, les captures, les schémas** | B | « les illustrations impliquées, j'aime bien », « les captures même ouii parfait », « les schémas » |
| **« Pensé pour chaque interaction »** | B | Cité |
| **« AVANT / PENDANT / APRÈS »** | B | Cité |
| **« S'intègre à votre stack existante »** | B | « parfaiteee » |
| **Le header** (carte média encastrée + Studio vivant) | C | « vraiment il est très professionnel, très attirant, très impressionnant » |
| **Les 3 cartes empilées** (citations + statistiques) | C | « j'ai vraiment apprécié la partie des 3 cartes, leurs animations, c waww » — les citations Responsable Support / « L'objectif n'est pas le risque zéro… », et les blocs `100 % Des conversations évaluées`, `3 Couches de garde-fous`, `EU Datacenter à Paris`, `0 Transit hors UE`, `~50 g` |

> Sur B : « bref tu as excellé ». Sur C : « tu as excellé ».

### ❌ CE QU'IL A REJETÉ — À SUPPRIMER OU REFAIRE

| Problème | Source | Verbatim | Correction imposée |
|---|---|---|---|
| **La sphère/présence qui tourne** | B | « la présence qui tourne non non j'aime pas » — répété sous *ce qui ne sert à rien* | **Supprimée des deux versions.** Aucun objet en rotation continue dans un héros. |
| **Tout sur une seule page** | A, B | « dans le navbar j'ai pas aimé le truc que chaque partie n'est pas dans sa propre page, ce qui fait que le homepage est très long » | **Architecture multi-pages.** L'accueil devient un sommaire riche ; chaque chapitre a sa page dédiée. |
| **Le logo Callem géant en pied de page** | A, B, C | « le logo de callem dans le footer est très gros » — répété sous *ce qui est mal fait* | **Logo à 28–32 px de haut maximum.** Le wordmark géant en filigrane est supprimé. |
| **« Recevez un appel. Jugez sur pièce. »** | C | « la partie … j'ai pas aimé » | **Remplacée** (voir §4). |
| **« Tout ce qu'il faut pour automatiser la voix »** | C | « tu peux faire mieux » | **Refaite** en explorateur illustré (voir §4). |
| **Le pied de page** | C | « c'est pas trop luxueux et professionnel » | **Refait**, voir §3.3. |

### ➕ CE QUI MANQUE

| Manque | Verbatim | À implémenter |
|---|---|---|
| **Thème sombre / thème clair** | « version sombre / version claire » | **Vrai sélecteur de thème**, sur les deux versions, sur toutes les pages. |

---

## 2. ARCHITECTURE MULTI-PAGES (les deux versions)

```
propositions-finales/v1-atelier/          propositions-finales/v2-nocturne/
├── index.html          Accueil — sommaire riche, court
├── produit.html        La stack · Capacités · Supervision & insights · API
├── solutions.html      Les 5 cas d'usage · le détail d'appel #4521
├── securite.html       La confiance par construction · Entreprise
└── souverainete.html   Conçu en Europe · Carbone · Intégrations
```

**L'accueil ne contient plus tout.** Chaque grand chapitre devient un **bloc-teaser riche et illustré**
(un visuel fort + 3 lignes + les 3 preuves chiffrées + « Découvrir → ») qui pointe vers sa page.
Objectif : une accueil qui se parcourt en 45 secondes, pas en 5 minutes.

**Contenu de l'accueil** : Nav · Héros · Barre de preuve · Ceinture de logos · 4 chiffres clés ·
teaser Produit · teaser Solutions · **« Conçu pour résoudre. »** (interstitiel) · teaser Sécurité ·
teaser Souveraineté · **« S'intègre à votre stack existante »** (section complète, elle est aimée) ·
les 3 cartes empilées · Impact (6 chiffres) · FAQ (5 questions, les 2 autres sur les pages dédiées) ·
CTA final · Pied de page.

**Les pages internes** reprennent le contenu détaillé de `content-spec-fr.md`, avec en tête un
en-tête de page (fil d'Ariane + titre + chapeau + un visuel signature), et en pied un bloc
« Poursuivre » qui renvoie vers les deux pages voisines.

**Navigation entre pages** : les liens du méga-menu pointent vers les vraies pages. La page courante est
marquée `aria-current="page"` et signalée visuellement. Toutes les pages partagent la même nav et le même
pied de page, au pixel près.

---

## 3. LE SOCLE COMMUN AUX DEUX VERSIONS

### 3.1 Charte Callem — inchangée, non négociable
Logo officiel (`brief/callem-assets.html`) · dégradé `#6772E5 → #9F32FC` · violet `#8B5CF6` / `#A855F7` ·
**Outfit** (display) + **Inter** (corps) + **JetBrains Mono** (données).

### 3.2 Sélecteur de thème — nouveau, obligatoire
- Bouton dans la nav, à côté du sélecteur FR/EN. Icône soleil/lune dessinée en SVG, transition douce.
- `document.documentElement.dataset.theme = 'light' | 'dark'`, mémorisé dans `localStorage`.
- Trois états gérés : choix explicite clair, choix explicite sombre, et **système** par défaut.
  ```css
  :root{ /* palette CLAIRE complète — toujours définie ici */ }
  @media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){ /* tokens sombres */ } }
  :root[data-theme="dark"]{ /* tokens sombres */ }
  ```
  Aucune couleur ne doit avoir sa seule définition dans un bloc `@media` ou `[data-theme]`.
- Un script anti-FOUC en tête de `<head>` applique le thème avant le premier rendu.
- **Les deux thèmes doivent être beaux.** Le thème secondaire n'est pas une inversion mécanique :
  les halos, les ombres, les liserés et l'opacité des illustrations sont réglés pour chacun.
- V1 par défaut : **clair**. V2 par défaut : **sombre**.

### 3.3 Le pied de page — refait, luxueux
Ce qui était reproché : logo trop gros, pas assez professionnel. Le nouveau modèle :
- **Liseré de marque** de 1 px en haut, en dégradé `#6772E5 → #9F32FC`, sur toute la largeur.
- **Logo à 28 px de haut** (marque + wordmark), aligné à gauche, suivi d'une baseline d'une ligne et des
  coordonnées de la société.
- **Cinq colonnes de liens** denses et bien hiérarchisées (Produit · Solutions · Développeurs ·
  Entreprise · Légal), libellés en 13 px, titres de colonne en mono 11 px capitales espacées.
- **Bandeau de conformité** : les badges RGPD · Datacenter Paris · BPI French Tech · CSRD, dessinés en SVG,
  en 20 px de haut, alignés sur une ligne avec un filet au-dessus.
- **Barre de bas de page** : copyright · sélecteur de langue · sélecteur de thème · statut système
  (`● Tous systèmes opérationnels`) · liens réseaux sociaux en icônes SVG.
- Aucun wordmark géant. Aucune zone vide. Le pied de page est **dense et tenu**, comme celui de Stripe.

### 3.4 Composants à reprendre du code existant
Les fichiers `propositions/A-aurora.html`, `B-orbite.html`, `C-studio.html` existent. **Ouvre-les et
reprends le code** des composants listés en §1 plutôt que de les réécrire de mémoire — c'est ce que le
client a validé. Adapte-les à la palette et au thème de ta version, améliore-les, mais garde ce qui a plu.

---

## 4. LES DEUX VERSIONS

### ═══════════ V1 — « ATELIER » · Le produit d'abord, clair par défaut ═══════════

**Le pari** : c'est le produit qui vend. Chaque section montre une interface réelle, un flux réel,
une donnée réelle. Lumineux, précis, dense — un SaaS d'élite.

**Héros** — *l'élément le plus aimé du client, à amplifier.*
La **carte média encastrée** de la proposition C : `inset: 10px` du bord, `border-radius: 24px`,
`min-height: 86vh`, fond sombre même en thème clair, halo de marque en dégradé radial derrière.
Dedans, la **scène produit vivante** :
- à gauche la fenêtre Callem Studio (sidebar Construire/Déployer/Superviser, onglets Modèle · Voix ·
  Outils · Analyse d'appel · Avancé, champs Identité / Missions / Garde-fous)
- à droite la supervision live (onde audio animée, transcription qui se déroule, jauges de latence
  STT/RAG/LLM/TTS, compteur `14 832` en odomètre)
- **améliorations demandées** : plus de profondeur (les deux fenêtres à des `translateZ` différents avec
  une ombre projetée cohérente), un reflet spéculaire qui suit le curseur, un liseré lumineux de marque
  sur l'arête supérieure, et le halo qui respire très lentement.
- Titre en surimpression, Outfit 300. CTA en capsule de verre avec la miniature 72 px du visualiseur.

**Ce qui remplace « Recevez un appel. Jugez sur pièce. »** →
**« Le même appel, deux mondes. »** — un **comparateur en split animé** : à gauche un SVI classique
(arborescence « tapez 1, tapez 2 », attente, transfert, 4 min 12), à droite le même appel traité par
Callem (2 min 34, résolu sans humain). Un curseur central que l'on fait glisser révèle l'un ou l'autre.
Les deux timelines se jouent en parallèle, avec les vraies durées. C'est une démonstration, pas un formulaire.

**Ce qui remplace « Tout ce qu'il faut pour automatiser la voix » →**
**Un explorateur de capacités** : une colonne de 10 entrées à gauche (les 10 capacités du content-spec),
un **panneau illustré animé** à droite qui change à chaque sélection — schéma, mini-interface, graphique
ou séquence selon la capacité. Navigation clavier, `aria-selected`, transition douce. Fini la grille de
10 cartes identiques.

**Signature visuelle** : le produit partout · bento de vraies interfaces · cartes en profondeur
(`perspective` + `translateZ`, ≤ 8° d'inclinaison) · **diorama isométrique animé** du pipeline vocal ·
graphiques SVG qui se tracent · aucun objet en rotation.

**Palette claire** : `#FFFFFF` · surfaces `#F7F5FF` · texte `#12101C` · atténué `#5D5872` ·
filets `#E9E5F5` · cartes média sombres `#0E0D14` · accent `#7C3AED`.
**Palette sombre** : `#0B0A11` · surfaces `#16151F` · texte `#EDEBF5` · atténué `#8B87A3` ·
filets `rgba(255,255,255,.08/.12/.22)` · accent `#A855F7`.
**Ombres** (en clair) : `0 0 1px rgba(20,16,40,.24), 0 4rem 7.5rem -1.25rem rgba(0,0,0,.08)`.

---

### ═══════════ V2 — « NOCTURNE » · Cinématique et immersif, sombre par défaut ═══════════

**Le pari** : on ne présente pas le produit, on le fait vivre. La page est une descente,
avec de la lumière, de la profondeur et une caméra.

**Héros — LE CHAMP DE VOIX** *(remplace la sphère qui tourne, définitivement supprimée)*
Un canvas 2D avec ~4 000 particules, et une **narration en trois temps d'environ 4 secondes** :
1. **0 → 1,2 s** — les particules arrivent en désordre depuis les bords, en traînées.
2. **1,2 → 2,6 s** — elles s'organisent en une **onde de parole** qui traverse l'écran de gauche à droite
   (enveloppe réelle : somme de trois sinusoïdes déphasées × une enveloppe en cloche, pas un sinus plat).
3. **2,6 → 4 s** — l'onde se replie et les particules se réorganisent en **contour de l'Europe** ;
   **Paris s'illumine** en dernier, en couleur de marque.
4. **Puis ça se fige.** Reste seulement un scintillement très léger et le nœud Paris qui pulse toutes les
   2,4 s. **Aucune rotation. Aucune boucle.**
Derrière, la **corona de marque** de la proposition A (que le client a aimée) : cœur sombre, trois couches
`#6772E5` / `#8B5CF6` / `#9F32FC` très floutées, en fond fixe.
Repli `prefers-reduced-motion` : l'image finale directement, sans séquence.

**Structure narrative** : l'accueil suit un appel, de la sonnerie à la résolution. Chaque acte est un
teaser de page. Le **détail d'appel #4521** (composant le plus aimé) est la pièce maîtresse de l'accueil,
en grand, avec sa timeline scrubable.

**Signature visuelle** : **caméra pilotée au scroll** (`perspective: 1400px`, les sections avancent en Z,
flou de profondeur sur les plans lointains) · **tunnel de sécurité** (AVANT / PENDANT / APRÈS comme trois
anneaux traversés en Z) · schémas techniques illustrés et tracés · scroll horizontal des logos ·
lumière de marque comme seule source de couleur.

**Palette sombre** : `#07060B` · surfaces `#12111C` / `#1A1826` · texte `#EDEBF5` · atténué `#8B87A3` ·
filets `rgba(255,255,255,.07/.12/.22)` · accent `#A855F7` · liseré interne `inset 0 1px 0 rgba(255,255,255,.09)`.
**Palette claire** : `#FBFAFE` · surfaces `#F2EFFB` · texte `#0F0D18` · atténué `#5D5872` ·
filets `#E6E1F4` · accent `#7C3AED`. En thème clair, les coronas deviennent des halos doux et les
particules passent en violet sur fond blanc — la séquence du héros reste identique.

---

## 5. EXIGENCES TECHNIQUES (rappel)
- Fichiers `.html` autonomes, CSS et JS inline, zéro bibliothèque, zéro image externe.
  Seul `<link>` externe autorisé : `fonts.googleapis.com`.
- Coller `brief/callem-assets.html` (tokens + sprite : logo, 23 logos partenaires, 18 icônes) dans chaque page.
- Responsive 1440 / 1280 / 1024 / 768 / 390. Menu mobile fonctionnel. Aucun débordement horizontal.
- A11y : landmarks, un seul `<h1>` par page, hiérarchie continue, `aria-*`, `:focus-visible` dessiné,
  contraste AA **dans les deux thèmes**, clavier complet, `prefers-reduced-motion` global.
- SEO par page : `<title>` propre, meta description, canonical, OG + Twitter, JSON-LD
  (`Organization` + `SoftwareApplication` sur l'accueil, `BreadcrumbList` sur les pages internes,
  `FAQPage` là où il y a une FAQ).
- Perf : `content-visibility: auto` sous le pli, canvas 30 fps + DPR ≤ 2 + pause hors écran et sur
  `visibilitychange`, jamais `transition: all`, `will-change` posé puis retiré en JS.
- Français typographique : apostrophes `’`, `&nbsp;` avant `: ; ! ?` et dans `«&nbsp;»`,
  majuscules accentuées, `tabular-nums` sur les métriques.

## 6. LE TEST FINAL
1. Le client retrouve-t-il **tout ce qu'il a aimé** ?
2. A-t-il disparu **tout ce qu'il a rejeté** — la présence qui tourne, le logo géant en pied de page,
   la page unique interminable, le bloc « Recevez un appel » ?
3. Le **thème clair et le thème sombre** sont-ils tous les deux beaux ?
4. Le **pied de page** est-il enfin luxueux et dense ?
5. Les **deux versions sont-elles radicalement différentes** l'une de l'autre ?
