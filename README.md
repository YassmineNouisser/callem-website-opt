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
