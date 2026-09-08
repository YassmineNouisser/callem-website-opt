# Callem — site vitrine (proposition « Nocturne »)

Site statique, cinq pages, sans dépendance ni étape de build.
Déploiement Vercel : rien à configurer, le dépôt se déploie tel quel.

## Pages

| URL | Fichier | Contenu |
|---|---|---|
| `/` | `index.html` | Accueil — héros « champ de voix », sommaire des cinq chapitres |
| `/produit` | `produit.html` | La stack, l’explorateur de capacités, supervision, API |
| `/solutions` | `solutions.html` | Les cinq cas d’usage, le détail d’appel #4521 |
| `/securite` | `securite.html` | Garde-fous avant / pendant / après, entreprise |
| `/souverainete` | `souverainete.html` | Hébergement France, carbone, intégrations |

`cleanUrls` est actif : `/produit.html` redirige vers `/produit`, ce qui correspond
aux balises `canonical` déjà présentes dans les pages.

## Ce que contient chaque page

- **Charte Callem** — logo officiel en SVG, dégradé `#6772E5 → #9F32FC`, violet `#8B5CF6` / `#A855F7`
- **Typographie** — Outfit (titres), Inter (corps), JetBrains Mono (données), chargées depuis Google Fonts
- **Thème clair / sombre** — sélecteur dans la nav, mémorisé en `localStorage`, script anti-FOUC en tête de `<head>`, sombre par défaut
- **Illustrations** — 23 logos partenaires vectorisés, 18 icônes duotone, mockups produit reconstruits en DOM, carte d’Europe, schémas isométriques, graphiques SVG animés
- **Animations** — champ de particules en canvas, constellation d’intégrations, scrollytelling à scène épinglée, terminal API, halo au curseur, rail de progression. Tout se met en pause hors écran et se coupe sous `prefers-reduced-motion`
- **SEO** — `<title>`, meta description, canonical, OpenGraph, Twitter Card, JSON-LD (`Organization`, `SoftwareApplication`, `BreadcrumbList`, `FAQPage`), `sitemap.xml`, `robots.txt`
- **Accessibilité** — un seul `<h1>` par page, hiérarchie de titres continue, `aria-*` sur les onglets et accordéons, `:focus-visible` dessiné, contraste AA dans les deux thèmes

## Déploiement

```bash
# Vercel CLI
npx vercel --prod

# ou : importer le dépôt sur vercel.com
#   Framework Preset : Other
#   Build Command    : (vide)
#   Output Directory : (vide, racine du dépôt)
```

Aucune variable d’environnement requise.

## Avant la mise en ligne

- **Logos partenaires** — ce sont des reconstructions vectorielles faites pour la maquette.
  Les remplacer par les fichiers officiels des marques avant toute mise en ligne publique.
- **Polices** — actuellement chargées depuis Google Fonts. Les auto-héberger améliore le LCP
  et évite une requête tierce (point RGPD).
- **Chiffres** — les métriques proviennent de `docs/content-spec-fr.md`. Les faire valider par Callem.
- **Domaine** — les `canonical` et le `sitemap.xml` pointent vers `https://callem.ai`. À ajuster
  si le déploiement se fait sur un autre domaine.

## Documentation

- `docs/content-spec-fr.md` — le contenu français de référence
- `docs/brief-final.md` — la synthèse des retours client et les deux directions retenues
- `docs/callem-assets.html` — la bibliothèque partagée : logo, logos partenaires, icônes, tokens
- `docs/02-callem-seo-audit.md` — audit SEO du site actuel
- `docs/10-seo-strategy-fr.md` — stratégie SEO (mots-clés, architecture, plan éditorial)

---

## Refonte septembre 2026 — deux propositions

Le site historique (`index.html`, `produit.html`, `solutions.html`, `securite.html`,
`souverainete.html`) est conservé tel quel. Les deux nouvelles propositions vivent à côté.

| URL | Fichier | Contenu |
|---|---|---|
| `/versions` | `versions.html` | Page de choix — les deux liens, côte à côte |
| `/v1` | `v1/index.html` | **Oracle** — éditorial, fond crème, orange Hermès dominant |
| `/v2` | `v2/index.html` | **Atlas** — technique, fond blanc, violet dominant, console sombre |

Une seule des deux sera retenue puis promue à la racine.

### Ce qui change par rapport au site historique

- **Thème clair unique.** Plus de sélecteur ni de thème sombre. Palette reprise de callem.ai :
  violet `#8B3CF7`, orange `#EB6A0A`, fond chaud `#F5F0EB`, encre `#1A1A1A`.
- **Page unique** par version, sept sections. Plus de pages internes.
- **Métriques de vanité supprimées** (compteur d'appels, disponibilité, latence p95, zone de traitement).
- **Section Tarifs supprimée.** *Ressources* pointe vers `docs.callem.ai`.
- **Secteurs ajoutés** : Finance, Santé, Retail, Assurance, Pouvoirs publics.
- **AI Act article 50** traité avec le RGPD et l'hébergement France.
- **23 intégrations** affichées, suivies de « et plusieurs autres ».
- Schémas et illustrations à la place des paragraphes. Aucun tableau.

Les décisions viennent de `docs/20-etude-marche-2026.md` (étude France + États-Unis).

### Reconstruire

Les deux pages sont autonomes mais assemblées depuis `build/` pour éviter de dupliquer
le sprite SVG (43 symboles) et la carte d'Europe :

```bash
python3 build/build.py     # build/v1.src.html + build/v2.src.html → v1/index.html + v2/index.html
```

`build/build.py` injecte le sprite (`build/sprite.html`, extrait de `docs/callem-assets.html`)
et cuit les attributs de présentation des icônes duotone — les règles CSS ne franchissent pas
la frontière d'ombre d'un `<use>`. Il génère aussi la carte d'Europe et les tracés d'appel
depuis `build/europe.json`.

**Modifier les pages dans `build/*.src.html`, jamais dans `v1/` ou `v2/`** : ces fichiers sont écrasés.

### Règle éditoriale

Une page web n'est pas une présentation. Chaque bloc porte **une idée, en une ligne** :

- pas de chapeau introductif au-dessus des sections — le titre suffit ;
- une carte secteur = un titre + une phrase de cinq mots ;
- une carte client = une affirmation + deux chiffres, pas de récit ;
- les puces de la section Contrôle sont des étiquettes, pas des phrases ;
- ce qui doit être long (transcription d'appel, contenu des maquettes produit)
  l'est parce que c'est du contenu montré, pas du discours.

Le contenu est passé de **1 103 à 758 mots** (V1). Toute nouvelle rédaction doit tenir ce cap.

### V3 « Atelier » — piste écartée

Une troisième direction a été tentée sur la référence **genesys.com/fr-fr** : blanc dominant,
Archivo en display épaisse, grandes captures produit, orange en accent unique, aucune
bibliothèque d'animation. Elle vit dans `v3/` et reste accessible depuis la page de choix, mais
elle a été **écartée** : les V1 et V2 sont jugées meilleures.

Elle garde une leçon utile : sa boucle de héros ne dépend pas de `document.hidden`. Cette garde,
courante, casse l'affichage dans tout contexte qui déclare l'onglet masqué (prévisualisations,
captures automatisées, prérendu) — et les navigateurs brident déjà les minuteries en
arrière-plan, donc elle n'apporte rien.

### Passe d'amélioration — mouvement, 3D, texte

Trois chantiers menés sur les versions existantes, sans rien restructurer.

**Le mouvement.** Le geste n'a pas été d'ajouter des effets mais de ralentir et d'adoucir ceux
qui existaient. Une courbe de sortie exponentielle partagée (`--e:cubic-bezier(.16,1,.3,1)`)
remplace l'ancienne, et les durées passent de 0,75 s à 1,05–1,20 s sur les révélations, les
cartes métiers, les fiches usages et les trois couches. Les titres se dévoilent désormais
**ligne par ligne** derrière un masque, plus mot à mot — plus éditorial, moins saccadé. Le filet
des kickers se trace, et les photos arrivent avec une échelle qui se résorbe plutôt qu'un simple
fondu.

**La 3D.** Le champ du héros ne fait plus du surplace :

- le ruban **coule** — chaque point remonte le champ et reboucle, masqué par le fondu des
  extrémités, ce qui donne un courant visible plutôt qu'une onde stationnaire ;
- les points se répartissent sur **deux nappes** séparées de 2,2 unités en profondeur ;
- les points lointains **s'effacent** (`mix(0.32, 1.0, …)` sur la distance caméra), ce qui rend
  la parallaxe lisible ;
- au défilement le champ **bascule** et la caméra avance légèrement.

**Le texte.** Cinq formulations resserrées sur la V1, trois sur la V2 :

- le sous-titre du héros portait trois participes sans verbe ; il lève maintenant l'objection
  numéro un d'un acheteur B2B — « Sur vos numéros, sans migration » ;
- « une couche d'orchestration au-dessus du meilleur de l'IA vocale » était du jargon ; devenu
  « les meilleurs modèles du marché, orchestrés et supervisés par Callem » ;
- « rien ne franchit le périmètre » ne disait pas quel périmètre ; devenu « aucune donnée ne
  sort d'Europe » ;
- « s'intègre à votre stack existante » est la phrase de tous les éditeurs ; devenu « vos outils
  restent les vôtres » ;
- le bloc démo annonce le délai et l'absence d'engagement dès la première phrase.

La ponctuation française était déjà correcte — espaces insécables avant les `%`, à l'intérieur
des guillemets — la passe n'a donc rien eu à y reprendre.

### Refonte « Maison » — annulée

Une passe de refonte visuelle (papiers neutres, accent unique, photos désaturées, rayons
resserrés) avait été appliquée aux deux versions. Elle a été **retirée** : elle éloignait le site
de la charte Callem. V1 et V2 sont revenues à leurs couleurs — violet et jaune Hermès, dégradés
de marque, photos chaudes — en gardant tout ce qui avait été validé entre-temps : les cartes des
cinq métiers, les trois couches illustrées, le formulaire à fiche d'appel vivante, les cartes du
héros, le champ 3D et la plateforme épinglée.

### Outils d'animation

La couche de mouvement s'appuie sur les bibliothèques du métier, chargées depuis jsDelivr :

| Outil | Version | Ce qu'il pilote |
|---|---|---|
| **GSAP** | 3.12.5 | toutes les animations (compteurs, révélations, relief, boutons magnétiques) |
| **ScrollTrigger** | 3.12.5 | déclenchement au défilement, parallaxe, jauge de progression, cascades |
| **Lenis** | 1.1.18 | défilement inertiel, synchronisé avec ScrollTrigger via `gsap.ticker` |
| **Swiper** | 11 | carrousel des cas clients, glissable à la souris et au doigt |
| **SplitType** | 0.3.4 | découpe des titres en mots pour la révélation en cascade |
| **Three.js** | 0.149 | le champ de voix 3D du héros (WebGL) |

Ce que ça donne concrètement :

- **champ de voix 3D** dans le héros, **cartes des cinq métiers** en cascade et
  **plateforme épinglée** qui avance d'un palier par défilement — voir plus bas ;
- **défilement inertiel** sur toute la page, et les ancres de la nav y passent aussi ;
- **jauge de progression** de lecture en haut de page ;
- **titres révélés mot par mot** derrière un masque, en cascade ;
- **parallaxe** sur chaque photo ;
- **relief au curseur** : les cas clients, les panneaux produit et le bloc démo s'inclinent
  en 3D vers la souris et se soulèvent légèrement ;
- **anneau de logos en 3D** : les intégrations tournent sur un cylindre que l'on peut
  attraper à la souris ; relâché, il repart en dérive lente ;
- **boutons magnétiques** : les CTA suivent le curseur ;
- **compteurs** animés par GSAP à l'entrée dans le champ.

Tout est désactivé d'un bloc sous `prefers-reduced-motion`.

### Le champ de voix 3D

Le héros porte une couche **WebGL** (Three.js) posée entre la vidéo et le voile clair : environ
**13 000 points** dessinent un ruban qui ondule comme une onde vocale, teinté du violet vers
l'orange de la charte.

- il **réagit au curseur** : les points s'écartent sur son passage et la caméra dérive
  légèrement en parallaxe ;
- il **se disperse au défilement** : l'avancée du héros (`window.__heroProg`) alimente
  directement le nuanceur, les points s'éparpillent et s'effacent ;
- il vit **sous le voile clair**, donc il n'atteint jamais le titre : la colonne de texte
  reste parfaitement lisible ;
- une **première image est rendue de façon synchrone** au chargement — le héros n'est jamais
  vide, même si le navigateur suspend `requestAnimationFrame` ;
- la boucle se met en pause quand l'onglet passe en arrière-plan ou que le héros sort de
  l'écran, la densité de pixels est plafonnée à 1,6, et tout est coupé sous
  `prefers-reduced-motion`.

Le rendu est fait en **un seul appel de dessin** (`THREE.Points` + nuanceur maison) : c'est la
carte graphique qui travaille, pas le fil principal. C'est ce qui remplace les anciens canevas
2D, responsables des à-coups signalés.

### La plateforme : un palier de défilement par étape

La section « Construire, déployer, superviser » ne s'ouvre plus au clic seul : elle **s'épingle**
et le défilement la fait avancer étape par étape.

- ScrollTrigger fixe le bloc et découpe 2,4 hauteurs d'écran en quatre paliers ;
- à chaque palier, l'étape suivante s'ouvre, un compteur `01 / 04` et quatre segments se
  remplissent, et l'écran de droite **se recompose ligne par ligne** (80 ms d'écart) ;
- pendant l'épinglage la section passe en **mode compact** (classe `is-pin`) : titre resserré,
  écran plafonné à 44 vh, cartes flottantes masquées ;
- **repli automatique** : si le bloc compact ne tient toujours pas dans la fenêtre, ou sous
  981 px de large, l'épinglage est abandonné et les onglets restent cliquables comme avant.

### Les trois couches du contrôle

La section « Trois couches » n'était que trois listes à puces et une citation nue. Chaque couche
porte maintenant **un écran concret**, et les trois sont reliées par un rail qui se trace de
gauche à droite quand la section entre dans le champ :

- **01 · Avant** — la règle active, puis l'identité et le numéro dont les caractères sensibles
  se font **caviarder sous vos yeux** (`Camille D████`, `+33 6 ███████ 78`) ;
- **02 · Pendant** — le bandeau « en direct » avec son point qui bat, une forme d'onde animée,
  et l'alerte « le ton monte » qui propose l'escalade ;
- **03 · Après** — le scoring : hallucination 0,4 %, résolution sans humain 70 %, barres qui se
  remplissent, et le résultat du dernier A/B.

Les trois points du rail s'allument l'un après l'autre, en même temps que les fiches montent.
La citation, elle, devient **un bloc** : panneau teinté, guillemet surdimensionné en accent,
attribution en mono.

### Trois usages : les fiches

Le carrousel Swiper — qui se verrouillait de toute façon quand les trois fiches tenaient à
l'écran — est remplacé par **trois fiches éditoriales** côte à côte :

- elles montent en cascade (130 ms d'écart) et leur **photo se dévoile par un balayage**
  (`clip-path` animé) juste après ;
- au survol, la photo reprend ses couleurs, le logo partenaire s'affirme, la fiche s'incline
  légèrement en 3D vers la souris ;
- chiffres en display sous un filet, légendes en mono.

### Les cinq métiers : le jeu de cartes

Les cinq secteurs sont **cinq cartes photo côte à côte**, pas un carrousel :

- elles **montent en cascade** quand la section entre dans le champ — chacune part de 42 px plus
  bas et pivotée de 13° sur son axe vertical, avec 95 ms d'écart d'une carte à l'autre ;
- la carte active **s'élargit** (elle occupe environ 40 % de la rangée contre 12 % pour les
  autres), sa photo se pose à l'échelle 1 et retrouve ses couleurs pendant que les autres
  restent en retrait sous le dégradé de marque ;
- son texte et son chiffre clé **se déplient** sous le titre (`grid-template-rows: 0fr → 1fr`) ;
- ça **tourne seul** toutes les 4,6 s, une ligne de progression court en haut de la carte
  active ; le survol de la rangée met en pause, le survol d'une carte la sélectionne, le clic
  la fixe, et le focus clavier suit ;
- sous 900 px les cartes **passent en grille** deux par deux, toutes ouvertes, sans rotation
  automatique — rien à survoler sur un écran tactile.

### Vidéo du héros

Comme Genesys, le héros repose sur une **vidéo en boucle** (`<video autoplay loop muted playsinline>`),
servie depuis `videos.pexels.com` :

| Version | Clip | Sujet |
|---|---|---|
| V1 | `8201569` | Un conseiller avec casque dans un bureau lumineux |
| V2 | `8865868` | Un plateau de supervision face à la baie vitrée |

Deux sources sont déclarées (720p puis 360p) et une image `poster` évite tout écran noir au chargement.
La lecture est relancée automatiquement si le navigateur la suspend, et mise en pause quand le héros
sort de l'écran ou que l'onglet passe en arrière-plan.

**Licence Pexels** : usage commercial libre, sans attribution. Mêmes réserves que pour les photos :
avant mise en ligne, remplacer par les rushes de Callem et **auto-héberger** le fichier.

### La console jouable du héros

Les bulles flottantes et la pastille d'état ont laissé place à une **console d'appel sur laquelle
on agit**. Trois choses sont cliquables :

- **le dossier** — trois onglets, trois secteurs, trois parcours réellement différents :
  *Commande en retard* (Retail, 41 s, 4 outils, résolu), *Sinistre auto* (Assurance, 68 s, se
  termine par une **escalade vers un expert** parce que l'agent ne doit pas annoncer
  d'indemnisation), *Rendez-vous* (Santé, 52 s, garde-fou « zéro conseil médical »). Le troisième
  cas ne se résout pas seul, et c'est volontaire : montrer que l'agent sait s'arrêter est plus
  crédible que trois succès d'affilée ;
- **la barre de transport** — lecture/pause, et un curseur qu'on gratte à la souris ou aux
  flèches du clavier (`role="slider"`, `aria-valuenow` tenu à jour) ;
- **chaque ligne « outil »** — au survol elle révèle ce que l'appel a **renvoyé**
  (`crm.get_order(#4521) → réexpédiée le 04/09 · 82 ms`) ; un clic l'épingle.

Le fil est **ancré en bas** et masqué en fondu sur son bord haut : les lignes s'empilent et les
plus anciennes remontent hors du cadre, comme un vrai flux. Les badges s'allument à leur seconde
exacte. La frise des quatre actes en bas du héros est devenue **l'indicateur de phase de l'appel**
— cliquable pour sauter au début d'une phase — et le champ 3D suit toujours cette phase via
`__heroAmp`.

**Adaptée au thème sans une seule couleur en dur** : la console déclare `--pa` (accent dominant)
et `--sa` (second), et prend tout le reste aux jetons existants. En V1 `--pa` vaut l'orange
Hermès, en V2 le violet — les deux s'inversent d'une version à l'autre.

Deux réglages trouvés à la mesure plutôt qu'à l'œil : les lignes non révélées gardaient leur
hauteur et poussaient les lignes visibles hors du cadre — elles sont maintenant à `max-height:0` ;
et le fil réservait sa hauteur, ce qui laissait un grand vide au début — il se remplit désormais
par le bas.

### Les cartes du héros

Le bandeau d'état et les bulles ne sont plus des notifications système :

- **la barre d'état** est une pastille fine — égaliseur à cinq barres (animé en `scaleY`, pas en
  hauteur), « EN LIGNE » en mono capitales espacées, un filet vertical d'un pixel, puis l'étape
  en cours en gris ;
- **les répliques** portent leur intitulé en mono capitales avec une pastille de couleur par
  interlocuteur et l'horodatage à droite en chiffres tabulaires ; la phrase elle-même est en
  typo display, entre **guillemets colorés à l'accent** ;
- **les appels d'outils** deviennent des bandes de télémétrie : filet accentué à gauche, puce
  d'icône, code en mono, latence alignée à droite ;
- toutes les cartes entrent **en fondu net** (`filter: blur(7px) → 0`) plutôt qu'en simple
  glissement, et les surfaces sont translucides avec un liseré de lumière en haut.

### Refonte du héros — plein cadre, centré

La composition précédente était la mise en page de tous les sites SaaS : **texte à gauche, image
à droite**, avec un voile crème posé sur la photo pour rendre le texte lisible — l'aveu d'une
composition qui ne tenait pas — et des cartes éparpillées par-dessus comme un calque ajouté
après coup.

La nouvelle :

- **la photo descend en bandeau bas**, en cinémascope, détachée des bords, coins arrondis en
  haut. Elle n'est plus un fond, elle est un objet ;
- **le voile est supprimé** : le texte est sur le fond, la photo est ailleurs ;
- **le titre passe au centre**, sur toute la largeur, posé sur un halo radial qui le détache de
  l'onde ;
- **la conversation devient une frise horizontale** posée sur le bord haut du bandeau — une
  chronologie d'appel, plus des bulles en vrac. Les cartes non révélées se replient à zéro
  largeur, ce qui garde la frise centrée et lui donne un dépliage ;
- **l'onde 3D traverse tout**, d'un bord à l'autre, derrière le titre et jusque sur le bandeau ;
- une **lueur de marque** occupe le haut, là où la photo n'est plus.

**Le budget vertical est la contrainte réelle** : sur une fenêtre de 681 px, kicker + titre +
accroche + boutons + frise + bandeau + frise des actes ne tiennent pas avec les tailles de
départ. Trois mesures successives dans le navigateur ont réglé la question — le bloc démarre à
5,5 rem pour dégager la barre flottante (68 px + gouttière), et un palier `@media(max-height:770px)`
élargit la mesure du titre pour le faire tenir sur deux lignes au lieu de trois.

L'état précédent est conservé dans `build/_sauvegarde/` : deux fichiers à recopier pour revenir
en arrière.

### La barre de navigation

- **En verre, plus en blanc.** `rgba(255,255,255,.58)` avec `backdrop-filter: saturate(1.9)
  blur(20px)`, un anneau blanc d'un pixel et un liseré de lumière en haut. La photo et le champ
  3D se lisent au travers. Un bloc `@supports` repasse en blanc à 94 % pour les navigateurs sans
  `backdrop-filter`. Le coût de composition reste faible : le flou ne s'applique qu'à une bande
  de 68 px, pas à un plein écran au-dessus d'un canevas animé — c'était le piège de la première
  version du héros.
- **Le mot « Callem » ne disparaît plus.** La règle `.nav.is-tight .brand b{max-width:0}` repliait
  la marque dès 90 px de défilement — un choix que j'avais posé et qui se lit comme un bug. Elle
  est retirée : le logo complet reste affiché du haut jusqu'au pied de page.

### Le héros passe à l'échelle

Le défaut de fond était structurel : le héros occupait **400 vh de défilement** et n'y faisait
presque rien — la photo grossissait de 9 %, le texte s'effaçait, fin. Quatre écrans de scroll
pour deux effets minuscules.

`layout(p)` pilote maintenant une vraie séquence sur toute la hauteur :

| Avancée | Ce qui se passe |
|---|---|
| 0 → 25 % | le titre tient, la photo pousse (jusqu'à ×1,30) et remonte |
| 20 → 42 % | le titre sort par le haut en reculant, avec un flou croissant |
| 26 → 64 % | la conversation grossit de 14 % et se recentre |
| 40 → 86 % | le champ 3D enfle — son amplitude est multipliée jusqu'à ×2,15 |
| 70 → 86 % | la pile se disperse |
| au-delà | la conclusion arrive en grand |

Les cartes passent de pastilles à de vraies cartes (342 px, réplique en 1,2 rem), la conclusion
de 2,1 à 3,4 rem, et le champ compte **21 000 points** au lieu de 13 000, sur une largeur de 23
unités au lieu de 17 — il traverse tout l'écran.

**Une correction en cours de route :** la première tentative agrandissait aussi le titre
(jusqu'à 6,4 rem). La colonne du héros ne fait que 365 px de large : le titre passait à cinq
lignes et débordait de la fenêtre. Taille d'origine rétablie — l'ampleur vient de la séquence,
pas de la casse.

### L'animation du héros

Quatre défauts corrigés dans une passe dédiée :

- **la pile était plate** — les cinq cartes s'affichaient toutes sur le même plan. La dernière
  posée est maintenant au premier plan et les précédentes **reculent** : chacune perd 7 px de
  hauteur, 2,4 % d'échelle et 19 % d'opacité par rang, sur trois rangs. On lit enfin un
  empilement ;
- **rien ne bougeait entre deux étapes** — chaque carte **dérive** de 7 px sur 7,4 à 11 s, avec
  un décalage par carte. Le mouvement passe par la propriété `translate`, indépendante de
  `transform`, donc il n'entre pas en conflit avec la transition de révélation ;
- **le champ 3D ignorait le récit** — son amplitude suit désormais l'acte en cours via un
  uniforme `uAmp` : 0,82 à l'écoute, 1,12 quand l'IA comprend, **1,5 pendant l'exécution des
  outils**, 0,92 à la clôture. La valeur est amenée en douceur (5 % par image), et elle joue
  aussi sur la taille des points. Le ruban s'agite quand l'agent travaille ;
- **l'entrée du titre était un fondu générique** — le H1 se lève maintenant **ligne par ligne**
  derrière un masque, comme les autres titres de la page, puis la copie suit en cascade. Au
  défilement, elle sort avec un léger flou plutôt qu'un simple fondu.

### Le récit du héros

Il **se joue tout seul, en boucle** (2,6 s par étape) — il ne dépend plus du défilement :

- les quatre actes sous le héros sont des **boutons** : un clic saute directement à l'étape ;
- le survol du héros met le récit en pause ;
- la barre de progression de chaque acte se remplit à la durée réelle de l'étape ;
- tout est gelé sous `prefers-reduced-motion`.

### Photographies

Les deux versions utilisent **11 photos** chacune, servies depuis `images.unsplash.com` :
héros, les 5 cartes sectorielles, les 3 cas clients, la souveraineté (Paris) et le bloc démo.

- **Licence Unsplash** : usage commercial libre, sans attribution obligatoire.
- Ce sont des **images de calage**. Avant mise en ligne publique, deux choses :
  1. les remplacer par la photothèque de Callem (ou une sélection validée par le client) ;
  2. les **auto-héberger** dans `img/` plutôt que de pointer vers le CDN Unsplash —
     meilleur LCP, pas de dépendance externe, et pas de requête tierce (point RGPD).
- Les formats demandés au CDN : héros 1400 px, cartes secteurs 900 px, cas clients 720 px,
  souveraineté 1200 px, démo 900 px. Toutes en `auto=format&fit=crop`, `loading="lazy"`
  sauf le héros (`eager` + `fetchpriority="high"`).

### Reste à faire

- **Formulaire de démo** : le panneau de gauche est une **fiche d'appel qui se remplit en
  direct** pendant la saisie — le nom, la société, l'objectif, le numéro et l'e-mail s'y
  inscrivent avec un bref surlignage, et la fiche passe « prête à partir » (filet accentué,
  reflet qui balaie, coche) dès que les cinq champs requis sont valides. Le formulaire lui-même
  tient en cinq champs à libellés flottants : trait de focus qui se dessine sous le champ,
  coche animée dès qu'un champ devient valide, message d'erreur sous le champ, jauge
  d'avancement « n / 5 », **téléphone mis en forme automatiquement** (`0612345678` →
  `06 12 34 56 78`, `+33612345678` → `+33 6 12 34 56 78`), bouton avec état d'attente puis
  panneau de confirmation reprenant le numéro et l'e-mail saisis. L'interface est complète et
  validée côté client, mais **l'envoi n'est pas branché**.
  fonction serverless qui poste vers `hamzaghouili@callem.ai`.
- **Logos partenaires** : toujours des reconstructions vectorielles. À remplacer par les fichiers
  officiels avant mise en ligne publique.
- **Photos** : images de calage Unsplash, à remplacer et à auto-héberger (voir ci-dessus).
- **Chiffres** : à faire valider par Callem.

## V2 — passes 18 à 22 (7 septembre 2026)

Le brief en douze points, plus la consigne finale : **aucune surface sombre, tout
en violet, orange Hermès, blanc et noir.**

### Ce qui a changé

| Point | Section | Ce qui a été fait |
|---|---|---|
| 1 | Barre | Verre **violet** (translucide, teinté, ni blanc plat ni encre) + panneau *Secteurs* déroulant : les cinq métiers Genesys avec icône et une ligne chacun. |
| 2 | Héros | « L'orbite » devient **un appel qu'on regarde se dérouler** : arc de progression autour du médaillon, minuteur `00:00 → 00:41`, six étapes qui s'allument dans l'ordre horaire, fil pointillé vers le médaillon, ruban de lecture. Survoler une étape arrête l'appel dessus. Boucle de ~13,8 s, pilotée par `setInterval`. |
| 3 | Logos | Les **17 marques de callem.ai**, et rien de plus (les 23 précédentes inventaient Azure, Slack, Zoho, Attio, Close, Pipedrive). |
| 4 | Plateforme | Inchangé — les maquettes d'écran tiennent la route. |
| 5 | Cinq métiers | Photos remplacées : une conseillère au téléphone, une médecin au téléphone, un comptoir de magasin, un rendez-vous conseil, le drapeau européen. Cadrage recentré sur les visages. |
| 6 | Résultats | Le bandeau de chiffres devient **quatre cartes** qui montent en cascade, filet violet→orange qui se trace, nombres qui défilent, barre de proportion. |
| 7 | Trois usages | Des **usages réels** avec leurs chiffres, plus de témoignages attribués à Genesys, Salesforce ou Cal.com — ce sont des intégrations, pas des clients. |
| 8 | Trois couches | Devient **un relais** : les trois couches s'allument à tour de rôle, une tête lumineuse court sur le rail, une barre de temps se remplit. Le survol immobilise la couche. |
| 9 | Souveraineté | Entièrement repensé : **le banc d'essai**. Six destinations, une frontière tracée ; le faisceau part de Callem et soit il arrive, soit il s'arrête net sur la frontière. Verdict écrit à chaque fois. |
| 10 | Intégrations | **Le hub** : Callem au centre, trois orbites de logos qui tournent en sens contraires, un fil qui se trace de l'outil vers le centre avec un point qui converge. Survol = arrêt + rôle de l'outil. |
| 11 | Formulaire | Fil des trois temps, **pastilles** au lieu du menu déroulant, fiche d'appel qui se remplit en direct, bouton pleine largeur qui s'allume. |
| 12 | Pied de page | Bandeau d'appel final, colonnes, sceau « Conçu et hébergé en Europe ». |

### Consigne de dernière minute

Toutes les surfaces d'encre (barre, souveraineté, panneau de démo, pied de page)
ont été **rebasculées en clair**. Il ne reste plus une seule zone sombre.

### Points d'attention

- Le formulaire n'envoie encore rien : `TODO` en place, à brancher sur
  `hamzaghouili@callem.ai`.
- Les photos viennent d'Unsplash en lien direct — à télécharger dans `img/`
  et à remplacer par des visuels sous licence avant mise en ligne.
- L'adresse postale inventée a été retirée du pied de page.
- Les chiffres (−30 %, 70 %, +10 pts, < 6 mois) sont annoncés comme des ordres
  de grandeur Forrester/Gartner : à valider avec Callem.

## V2 — passe 23 : la barre relookée (7 septembre 2026)

Le menu déroulant « Secteurs » était un modèle vu partout. Il a disparu.

**Trois îlots flottants** au lieu d'une barre pleine largeur : la marque, les
liens, les actions. Trois capsules rondes en verre violet, détachées les unes
des autres, qui **se rapprochent et se resserrent au défilement**.

**« Secteurs » ne déroule plus rien.** L'îlot central s'élargit et *remplace son
contenu sur place* : les cinq liens s'effacent vers le haut, les cinq métiers
Genesys arrivent en cascade avec leur icône, précédés d'une flèche de retour.
Un seul niveau, aucune ombre portée, aucun panneau. Échap ou la flèche
ramènent au menu.

**Une pastille violette suit le lien survolé** et se repose, quand on relâche,
sur la section qu'on est en train de lire — repérée par un observateur de
défilement, avec un point orange sous le libellé courant.

Le « Se connecter » perd sa bordure : dans une capsule de verre, deux contours
concentriques faisaient sale.

Corrigé au passage dans le héros : quitter une étape sans quitter l'orbite
laissait l'appel gelé pour de bon (`held` ne repassait jamais à `false`).

## V2 — passes 24 et 25 : l'entrée et les paliers (7 septembre 2026)

Deux références, une chose prise à chacune.

### De genesys.com — le héros qui retient l'écran

Le bloc du héros mesure **2,6 écrans de haut**. À l'intérieur, un panneau
collant garde la composition en place pendant qu'on défile : c'est le
défilement qui joue l'appel.

- L'arc se remplit autour du médaillon, le chrono monte de `00:00` à `00:41`.
- Les six étapes s'allument l'une après l'autre, chacune reliée au médaillon.
- À 84 % de la course, la pastille « Résolu sans humain · 41 s » se pose.
- La colonne de texte dérive et s'estompe doucement, comme chez Genesys.
- Une invite « Défilez — l'appel se joue » disparaît au premier mouvement.

Tant qu'on n'a pas défilé, l'appel tourne tout seul pour que la page soit
vivante à l'arrivée ; au premier défilement, la molette prend la main.
En dessous de 1000 px, la scène redevient un bloc normal.

### De yellow.ai — les paliers, et des schémas plutôt que des captures

Les onglets de la plateforme ont disparu. À la place, **quatre panneaux pleine
largeur** qui se redressent (`scale` + `opacity`) en arrivant au centre de
l'écran, puis se retirent.

Chacun porte un **schéma**, pas une fausse capture :

| Palier | Schéma |
|---|---|
| 01 Construire | Identité · connaissances · outils → **Agent Callem** → banc de tests → production, avec la boucle de correction |
| 02 Déployer | Numéros FR/UE · trunk SIP · CCaaS → **Callem** → entrant · sortant · campagnes |
| 03 Latence | Le budget de 600 ms découpé en barre : écoute 90, compréhension 210, décision 140, voix 160 |
| 04 Superviser | 100 % des appels → **Scoring** → alerte · escalade · rien à signaler, et le correctif qui repart en A/B |

Au passage, l'épinglage GSAP de la plateforme a été supprimé : il entrait en
conflit avec la scène collante du héros et pouvait figer la section par-dessus
le reste de la page.

## V2 — passes 26 et 27 : l'entrée (7 septembre 2026)

Avant le héros, il y a maintenant **une entrée**. Trois temps, deux secondes
et demie, et on peut couper à tout moment.

1. **Ça sonne** — le sceau Callem au centre, deux cercles qui s'écartent,
   `Appel entrant`, `+33 1 84 88 00 00`, et une jauge violet→orange qui monte.
2. **Décroché · 0,4 s** — le libellé bascule en violet, le sceau grossit d'un
   cran, la jauge se remplit, et **la couture du volet s'allume** d'un trait
   violet→orange qui s'ouvre depuis le centre.
3. **Le volet s'ouvre** — les deux moitiés glissent vers le haut et vers le bas,
   le héros apparaît, le titre monte ligne par ligne et le médaillon se pose.

### Ce qui garantit qu'on ne reste jamais bloqué

Le rideau est **écrit dans le HTML**, pas injecté : il est là au premier pixel
peint, donc pas de coup d'œil sur la page avant qu'il n'arrive.

- Trois filets de sécurité : `setTimeout` (jamais `requestAnimationFrame`, qui
  est suspendu dans certains contextes), une animation CSS qui efface le rideau
  à 3,4 s même sans JavaScript, et le verrou de défilement qui n'est posé que
  par le script — s'il ne tourne pas, rien n'est verrouillé.
- **Clic, touche ou molette : on saute directement au héros.** Un bouton
  « Passer » en bas à droite.
- `prefers-reduced-motion` : l'entrée ne s'affiche pas du tout.

Séquence relevée en direct : `intro` → `step1` → `answered` → `open` → `gone`,
verrou levé, titre découpé en trois lignes, aucune erreur console.

Pour ne la jouer qu'une fois par session, une ligne suffit dans le pilote —
un test `sessionStorage` avant `root.classList.add(...)`.

### Passe 27 — l'entrée passait pour un flash

La première version durait 2,7 s dont une seconde d'écran presque vide : on la
prenait pour un temps de chargement. Elle a été refaite en grand.

- Le mot **Callem** en 7 rem au centre, lettre par lettre derrière un masque.
- Le sceau au-dessus, avec trois cercles de sonnerie qui s'écartent jusqu'au
  bord de l'écran.
- Une ligne d'état : `● Appel entrant · +33 1 84 88 00 00` (point orange qui
  bat), qui bascule en `● Décroché · 0,4 s · agent Callem` en violet.
- Un fil violet→orange qui court **d'un bord à l'autre du bas de l'écran**
  pendant toute la durée de l'entrée.
- Puis la couture s'allume et le volet s'ouvre en deux.

Minutage : sonnerie à 70 ms, ligne d'état à 680 ms, décroché à 1,9 s, ouverture
à 2,6 s, rideau parti à 3,65 s. Le filet de sécurité sans JavaScript passe à
4,4 s.

Les trois états sont visibles en images fixes : `docs/entree-etats.html`
(`http://localhost:8777/docs/entree-etats.html`).

### Passe 28 — pourquoi « il ne se passait rien »

Trois causes possibles, les trois corrigées.

1. **L'entrée se coupait toute seule.** Le raccourci « clic / touche / molette »
   était armé dès la première milliseconde. Sur trackpad, une inertie de
   défilement résiduelle ou un clic au moment du rechargement suffisait à la
   tuer avant qu'elle n'ait commencé. **Le raccourci ne s'arme plus qu'après
   900 ms.**
2. **`prefers-reduced-motion` la supprimait complètement** (`display:none`).
   Elle affiche maintenant une version fixe, sans mouvement, ouverte à 700 ms.
3. **Tout partait de `opacity:0`** et n'apparaissait que si une classe JS
   arrivait à temps. Si le script tardait ou ne tournait pas, on voyait un
   écran vide puis la page. **L'affichage est désormais 100 % en @keyframes
   CSS** ; le script ne sert plus qu'à décrocher, ouvrir et lever le verrou.

Séquence filmée en direct : badge + première lettre à 0,1 s ; « Callem » en
entier, deux cercles de sonnerie et `● Appel entrant · +33 1 84 88 00 00`
à 1,1 s ; `● Décroché · 0,4 s · agent Callem` en violet, fil complet d'un bord
à l'autre, à 2,1 s ; puis le volet s'ouvre.

### Passe 29 — l'entrée devient une scène

L'entrée « sceau + mot » était trop sobre. Reprise dans l'esprit de
genesys.com, mais en clair :

- **Une vidéo au centre**, carte arrondie de 520 px, voile violet→orange en
  `soft-light` pour rester dans la palette. Badge `● Appel en cours · 00:41`.
  Fichier Pexels 8201569 (HD puis SD), affiche de repli en photo si la vidéo
  ne charge pas.
- **Six notifications tombent autour**, trois à gauche trois à droite, chacune
  avec son icône : appel entrant (+33 6 12 44 88 21 · 09:14), identité
  vérifiée, rappel programmé, commande #4521 retrouvée (`crm.get_order · 82 ms`),
  transporteur interrogé (`carrier.track · 179 ms`), SMS de suivi envoyé.
- **La chute** : la pastille violette « ✓ Résolu sans humain · 41 s ».
- Le fil violet→orange court d'un bord à l'autre pendant toute la scène.
- Puis la couture s'allume et le volet s'ouvre sur le héros.

Minutage : première notification à 520 ms puis une toutes les 420 ms ; chute à
2,55 s ; décroché à 2,55 s ; ouverture à 3,5 s. Filet CSS sans JavaScript à 6 s.
Sous 1080 px la scène passe en colonne, sous 680 px il ne reste que la vidéo.

### Passe 30 — la scène bouge

L'entrée assemblait une composition puis s'arrêtait. Cinq choses la rendent
vivante du début à la fin :

1. **La vidéo tourne vraiment.** `video.play()` est relancé à la main au
   chargement (certains navigateurs refusent la lecture automatique en
   silence) et le refus est ignoré. Vérifié : `readyState 4`, 1280×720.
2. **L'image respire** — un lent zoom arrière de 11 s sur la vidéo, qui
   fonctionne aussi sur l'affiche de repli si la vidéo ne charge pas.
3. **Une onde de voix** de 46 barres fines ondule en permanence sur la vidéo.
4. **Le chrono monte** de `00:00` à `00:41` pendant la scène (`setInterval`,
   jamais `requestAnimationFrame`). Sans JavaScript, il affiche `00:41`.
5. **Le fil d'événements pousse.** Chaque carte arrive dans une rangée qui
   s'ouvre de `0fr` à `1fr` : la pile se décale vers le haut à chaque arrivée,
   comme un vrai flux, au lieu de six cartes qui se posent et ne bougent plus.

## V2 — passe 33 : l'ouverture façon Genesys (8 septembre 2026)

L'overlay minuté a entièrement disparu (plus de verrou, plus de minuterie,
plus de bouton Passer). À la place, **le premier écran du site** — le pattern
genesys.com, en clair :

- **La vidéo occupe tout le cadre** sous un voile clair maison (dégradé blanc
  à gauche, duotone violet/orange en soft-light). Léger zoom lié au
  défilement.
- **Un fil de messages monte en continu** sur la droite, comme le fil de
  cartes du héros Genesys : six cartes en boucle parfaite (rail doublé,
  translateY −50 %), masquées en haut et en bas. Chaque carte a un cadre net
  avec un filet coloré à gauche, un avatar ou une icône, deux registres
  typographiques (nom en semi-gras / méta en mono espacé), un texte humain et
  une étiquette d'état. Le récit est celui d'UN appel : appel entrant →
  identité vérifiée → transporteur → SMS → escalade supervisée → résolu 41 s.
  Survol = pause.
- **En bas à gauche, le propos** : « Un appel vient d'être *décroché.* »
  (dégradé violet→orange sur le dernier mot), révélé ligne par ligne.
- **Un indicateur de défilement** : « DÉFILER » + fil vertical animé.
- **Le défilement efface la scène** (scène collante de 178 vh, variable --p :
  le propos et le fil s'estompent et glissent, la vidéo zoome) puis le héros
  console apparaît naturellement.

Robustesse : sans JavaScript c'est une section normale qui défile, le fil
tourne en @keyframes ; `callem:in` est émis au chargement pour le héros ;
reduced-motion fige le fil et coupe la vidéo ; sous 900 px la scène devient
un bloc normal avec le fil en bas.

## V2 — passes 34-35 : le registre (8 septembre 2026)

Trois sections passent au même langage éditorial — filets fins, ordinaux en
mono, chiffres monumentaux, presque plus de texte. Le site gagne un système.

**Résultats — le registre.** Plus de cartes ni d'anneaux : quatre colonnes
entre deux filets, comme un rapport annuel. Filet supérieur violet→orange qui
se trace, ordinal `01…04`, chiffre en 5 rem qui se compte, libellé bref.
Survol : la colonne s'éclaire, les autres tombent à 34 %, une note d'une
ligne se déploie sous le libellé. La mention Forrester/Gartner reste en pied.

**Trois usages — l'index.** Plus de fiches : trois lignes de sommaire,
cliquables vers la démo. Ordinal, intitulé en 2,15 rem qui glisse au survol,
deux mesures à droite en chiffres display, flèche ronde qui s'allume et
pivote. Un filet dégradé se trace sous la ligne survolée ; note d'une phrase
repliée.

**Trois couches — le triptyque.** Le relais (rail, tête lumineuse, barre de
temps, survol qui immobilise) est conservé à l'identique. Dans les cartes :
un chiffre fantôme au contour violet (7-10 rem) en fond, un verbe —
Sécuriser. Observer. Évaluer. — une ligne en mono, et UN témoin visuel par
couche : identité masquée qui se caviarde, onde de voix + « le ton monte »,
deux jauges fines. Les listes à puces ont disparu.

## V2 — passe 36 : les cinq métiers en duotone maison (8 septembre 2026)

Le problème n'était pas seulement le choix des photos : cinq photos de stock
auront toujours cinq lumières différentes. La réponse est un **traitement**,
pas un tri : chaque image passe en niveaux de gris puis reçoit la teinte
maison (dégradé orange→violet en `mix-blend-mode:color`, souffle soft-light
par-dessus). Les cinq cartes sont désormais exactement dans la palette,
quelle que soit la photo d'origine. La carte **ouverte** reprend 80 % de ses
couleurs réelles — le survol « allume » le métier.

Photos remplacées au passage (cadrage vertical, sujet au téléphone quand
c'est possible) : conseillère en tailleur violet (Finance), règlement au
comptoir (Retail), deux conseillers au téléphone (Assurance), drapeau
européen sur pierre (Pouvoirs publics). La médecin au téléphone (Santé) est
conservée.

## V2 — passe 37 : l'orchestration (8 septembre 2026)

Le bandeau « Les meilleurs modèles du marché… » (une phrase centrée + cinq
logos posés) devient **l'orchestration** : à gauche, « Le meilleur modèle du
marché, à chaque seconde de l'appel » ; à droite, les cinq modèles sur un
rail, et **un sélecteur violet qui circule de l'un à l'autre toutes les
2,3 s** — comme le routeur le fait pendant un appel. Le logo actif reprend
ses couleurs et se soulève, son rôle s'affiche dessous en mono (Raisonnement,
Raisonnement long, Souverain · Paris, Infrastructure UE, Voix). Les autres
restent en gris. Survol = le sélecteur vient et s'arrête. Ouverture sur
Mistral. setInterval, jamais rAF ; reduced-motion fige tout en couleurs.

## V2 — passe 38 : le fil de l'appel (8 septembre 2026)

Le rail à sélecteur n'a pas convaincu. Le bandeau des modèles devient **une
animation à part entière** : un fil violet→orange **se trace d'un bord à
l'autre de l'écran** en ondulant à travers les cinq modèles — il passe
au-dessus de l'un, en dessous du suivant. À son passage, chaque modèle
**s'allume** : la puce blanche se soulève, le logo reprend ses couleurs, un
éclat circulaire s'échappe, le rôle apparaît dessous en mono. Une fois le
fil posé, **deux impulsions lumineuses le parcourent en continu** (une
violette, une orange, en quinconce) — le bandeau reste vivant.

Technique : le tracé SVG est construit en JS à partir des positions réelles
des puces (courbes de Bézier, recalculées au redimensionnement), dessiné par
`stroke-dashoffset` en transition CSS ; les impulsions voyagent par
`offset-path`/`offset-distance` en @keyframes — aucun requestAnimationFrame.
Allumages par setTimeout calés sur la progression du fil. Reduced-motion et
mobile : état final propre, sans fil ni impulsions.
