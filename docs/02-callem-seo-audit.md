_Audit run 2026-08-22 against `https://callem.ai/`. Raw artifacts saved to `/private/tmp/claude-502/-Users-yassminesmachine-Desktop-callem/6d888352-dfa7-41a8-9d9d-b4dc334eee16/scratchpad/` (`home.html`, `app.js`, `app.css`, `fr.html`, `gbot.html`, `flock.js`)._

---

# Executive summary

callem.ai is a **Lovable-built Vite + React SPA with zero server-side rendering**. The entire site is one HTML file of 2,243 bytes whose `<body>` contains **0 characters of visible text**. All ~1,900 words of marketing copy, all 18 sections, the FAQ, and the entire FR translation live inside a 644 KB JavaScript bundle.

The head-level SEO (title, description, OG, Twitter) is genuinely good — better than most seed-stage sites. Everything below the `<head>` is invisible to any crawler that doesn't execute JavaScript, and several signals actively contradict each other.

**Severity ranking:**

| # | Issue | Severity |
|---|---|---|
| 1 | 100% client-rendered — empty `<div id="root">` | Critical |
| 2 | `sitemap.xml` returns 404; robots.txt has no `Sitemap:` line | Critical |
| 3 | Zero JSON-LD structured data (no Organization / SoftwareApplication / FAQPage / BreadcrumbList) | High |
| 4 | Hardcoded canonical `https://callem.ai` on every route contradicts client-injected hreflang | High |
| 5 | `www.callem.ai` serves a full 200 duplicate, no redirect | High |
| 6 | Soft 404s — every unknown URL returns HTTP 200 | High |
| 7 | Google Fonts loaded via CSS `@import` (render-blocking chain, 4 families) | Medium |
| 8 | Single-page site: no indexable URLs beyond `/` | Medium |
| 9 | Heading level skips (h2 → h4 in 4 sections; footer h4 with no parent) | Medium |
| 10 | No `loading`/`width`/`height` on images; 218 KB PNG hero asset | Medium |

---

## 1. Rendering — CRITICAL

**The entire indexable body is this:**

```html
  <body>
    <div id="root"></div>
    <!-- IMPORTANT: DO NOT REMOVE THIS SCRIPT TAG OR THIS VERY COMMENT! -->
    
  </body>
```

Measured: `visible text chars: 0`. The full document is 2,243 bytes.

Verification that this is not UA-gated — there is no prerender/dynamic-rendering layer:

```
$ curl -sL https://callem.ai/ -A "Googlebot/2.1" | wc -c
2243   → IDENTICAL to browser UA
```

Content is injected client-side by `/assets/index-BJmILOxf.js` (644 KB). Approximately **1,879 words of English marketing copy** are string literals inside that bundle, e.g.:

```js
hero:{badge:"Voice AI Stack Gen 2.0 — Made in Europe 🇪🇺",
headlinePre:"Deploy voice agents that ",headlineHighlight:"resolve",
headlinePost:", not just respond",subheadline:"Callem Studio lets you build AI voice agents that qualify leads, book appointments, process requests, and transfer to humans — with built-in guardrails, real-time oversight, and full European data sovereignty. Go live in days, not months.",...}
```

Consequences: Googlebot can render this (second-wave, delayed and budget-limited), but **Bing, LinkedIn, Slack, X/Twitter, Facebook, Perplexity, ChatGPT browse, Claude web fetch, and most AI crawlers cannot**. For a company whose buyers research via LLMs, this is the single highest-cost defect on the site. The OG/Twitter tags are static in `<head>` so social previews survive — but the page body does not.

**Fix:** switch to `vite-plugin-ssg` / prerender, or move to Next.js. Prerendering a static 18-section marketing page is a low-risk change and resolves items 1, 6, and 8 simultaneously.

---

## 2. `<head>` metadata — mostly good

| Element | Value | Verdict |
|---|---|---|
| `<title>` | `Callem.ai — Voice AI Agents That Resolve, Not Just Respond` (57 chars) | Good |
| `meta description` | 189 chars — over the ~160 display limit, will truncate | Minor fix |
| `canonical` | `https://callem.ai` | Broken for i18n, see §4 |
| `og:title` / `og:description` / `og:type` / `og:url` / `og:site_name` | present | Good |
| `og:image` | `/lovable-uploads/cc1d3209-ae43-47aa-81c5-8d14c7b223fe.png` | **Relative URL — spec requires absolute** |
| `og:image:width/height` | `1200` × `630` | Good |
| `twitter:card` | `summary_large_image` | Good |
| `twitter:site` | `@callem_ai` | Good |
| `hreflang` | **absent from HTML**, injected by JS only | Broken, see §4 |
| `viewport`, `charset`, favicon | present | Good |
| `meta author` | `callem.ai` | Harmless, no SEO value |

The `og:image` bug is concrete — the OG protocol requires an absolute URL. Facebook and LinkedIn frequently fail to resolve relative OG images. The file itself resolves fine (`HTTP 200 image/png`), so the fix is one line: `https://callem.ai/lovable-uploads/cc1d3209-....png`.

The description is 189 characters. Trim to ~155: e.g. *"Deploy AI voice agents with built-in guardrails, real-time oversight, and European data sovereignty. Qualify leads, book appointments, resolve calls."*

---

## 3. Structured data — completely absent

```
$ grep -oiE 'application/ld\+json|schema\.org|"@type"|FAQPage|BreadcrumbList' app.js home.html
(no matches — zero occurrences in HTML *and* in the 644 KB bundle)
```

Not a single byte of JSON-LD anywhere. Four schema types are clearly warranted by content that already exists on the page:

- **`Organization`** — the site states Paris datacenter, BPI French Tech award, `contact@callem.ai`, `@callem_ai`. All the fields are already written; they're just not marked up.
- **`SoftwareApplication`** — "Callem Studio", category `BusinessApplication`. This is the entity type that feeds AI-assistant product comparisons.
- **`FAQPage`** — see below, this is the most valuable and most obviously missed.
- **`BreadcrumbList`** — low value here given the single-page structure; skip until real URLs exist.

### The FAQ situation is worse than "no schema"

There are 5 real Q&A pairs in the bundle:

```js
faq:{headline:"Frequently Asked Questions",items:[
 {q:"How quickly can I deploy a voice agent?",a:"Most teams go from zero to live agent in under a week..."},
 {q:"What LLMs can I use?",a:"Callem supports OpenAI, Anthropic Claude, Mistral, Google Gemini, and our own sovereign European models..."},
 {q:"Is my data processed outside Europe?",a:"Never. Callem runs entirely on Paris-based infrastructure..."},
 {q:"How do you handle AI hallucinations?",a:"Through our Trust by Design framework..."},
 {q:"Can the agent transfer to a human?",a:"Yes. Smart transfer is built-in..."}]}
```

These are excellent, high-intent answers. But the questions render inside `<button>` elements (not headings), and **the answers are conditionally mounted** — only the currently-open accordion item exists in the DOM:

```js
h.jsx(VC,{children: e===s && h.jsx(fe.div,{initial:{height:0,opacity:0},...,
  children:h.jsx("p",{...,children:r.a})})})
```

`e===s &&` means 4 of 5 answers are absent from the DOM at any moment, and on load **all 5 are absent** (`e` initialises to `null`). So even a JS-executing crawler sees zero answer text. Combined with the missing `FAQPage` schema, this content is 100% invisible.

**Fix:** render answers always-present with CSS-based collapse (`max-height`/`grid-template-rows`) instead of conditional mounting, use `<h3>` for questions, and add `FAQPage` JSON-LD.

---

## 4. i18n — hreflang and canonical contradict each other

There *is* FR/EN support, but it's wired in a way that guarantees the French version is never indexed.

The router defines a language route:

```js
h.jsx(Jl,{path:"/",element:...}), h.jsx(Jl,{path:"/:lang",element:...}), h.jsx(Jl,{path:"*",...})
```

And a full French dictionary exists with its own SEO strings:

```js
seo:{title:"Callem.ai — Agents Vocaux IA qui Résolvent, pas juste Répondent",
description:"Déployez des agents vocaux IA avec garde-fous intégrés, supervision en temps réel et souveraineté des données européenne..."}
```

hreflang is injected **client-side only**, in a `useEffect`:

```js
document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(w=>w.remove()),
[{hreflang:"en",href:"https://callem.ai/en"},
 {hreflang:"fr",href:"https://callem.ai/fr"},
 {hreflang:"x-default",href:"https://callem.ai/en"}]
.forEach(({hreflang:w,href:m})=>{const b=document.createElement("link");
  b.rel="alternate",b.hreflang=w,b.href=m,document.head.appendChild(b)})
```

**Three compounding problems:**

1. **`/fr` is byte-identical to `/` in the raw HTML** — verified: same 2,243 bytes, still `<html lang="en">`, still the English `<title>`. The FR title/description/`lang` are only swapped after hydration.

2. **The canonical is hardcoded and never updated.** `grep -c 'canonical' app.js` → **0**. `grep -c 'og:url' app.js` → **0**. The `useEffect` updates exactly 6 things (`document.title` + 5 × `setAttribute("content")` for description, og:title, og:description, twitter:title, twitter:description) and touches neither canonical nor `og:url` nor `og:image`.

   So `https://callem.ai/fr` serves `<link rel="canonical" href="https://callem.ai">`. The page tells Google "the French page is a duplicate of the English homepage" while the hreflang tags simultaneously claim they're distinct alternates. **These signals are mutually exclusive; Google resolves the conflict by honouring the canonical and dropping the entire hreflang cluster.** The French site will not rank in France.

3. **Return-link requirement fails.** hreflang must be reciprocal and crawler-visible. Since it's JS-injected and the FR page canonicalizes away, the cluster is invalid regardless.

**Fix:** prerender `/en` and `/fr` as separate documents, each with a self-referencing canonical (`https://callem.ai/fr` → itself), correct `<html lang>`, translated `<title>`/description, and static reciprocal hreflang tags in `<head>`.

---

## 5. Heading hierarchy

**Exactly one `<h1>` on the homepage** — this is correct. Note that a naive `grep '"h1"'` finds only the 404 page's h1; the real hero h1 is a framer-motion component (`fe.h1`), so it is easy to miss:

```js
h.jsxs(fe.h1,{initial:{opacity:0,y:40},animate:{opacity:1,y:0},...,
  className:"heading-serif mb-8",style:{color:"#1A1A1A",fontSize:"clamp(48px, 5.5vw, 80px)"},
  children:[e.hero.headlinePre, h.jsxs("span",{...,children:[e.hero.headlineHighlight,...]}), e.hero.headlinePost]})
```

Counts: **h1 = 1, h2 = 15, h3 = 5, h4 = 4** (h3/h4 multiply at runtime because several sit inside `.map()` over card arrays).

### Full outline in DOM order

Derived from the `<main>` composition `h.jsxs("main",{children:[zF, WF, qF, GF, YF, JF, eO, rO, sO, iO, aO, cO, uO, WV, HV, qV]})`:

```
(header — no heading, logo <img alt="Callem.ai">)
H1  Deploy voice agents that resolve, not just respond
    (logo marquee — no heading)
H2  Callem orchestrates the best AI models, speech engines and telecom
    infrastructure into one platform.
H2  One studio. Three pillars.
  H3  Build          ×3 cards (Build / Deploy / Monitor)
H2  One platform. Every call pattern.
  H3  Resolve support calls end-to-end with AI   ×5 tab panels
H2  Everything you need to automate voice
  H4  600ms End-to-End — Complete Transparency   ×6 cards      ← SKIP h3
H2  Trust by Design
  H3  Secure Before You Ship                     ×3 cards
H2  Measurable results from day one
H2  Made in Europe. Hosted in Europe. Stays in Europe.
  H3  Carbon-aware by design
H2  Use AI to improve your AI
  H4  Call Analysis                              ×4 cards      ← SKIP h3
H2  Integrates with your enterprise stack
H2  Built for teams that take security seriously
  H4  Data Protection                            ×4 cards      ← SKIP h3
H2  API-first. 100% programmable.
H2  Deploy AI voice agents at scale
  H3  Talk to our team    (contact form title)
H2  Frequently Asked Questions
H2  Resources                                                  ← should be H3
H2  Stop losing calls. Start resolving them.
(footer)
  H4  Product / Solutions / Resources / Company  ×4            ← SKIP h2+h3
```

**Issues:**
- Four h2 → h4 skips (bento, insights, security, footer). Accessibility (WCAG 1.3.1) and semantic clarity.
- `"Resources"` is an `<h2>` but is a sidebar sitting beside the FAQ `<h2>` — it's a subordinate block, should be `<h3>`.
- Footer column titles jump straight to `<h4>` with no ancestor.
- FAQ questions are `<button>` text, not headings — they should be `<h3>` inside the FAQ `<h2>`.
- Content-wise the h1 is strong (matches the title tag, contains "voice agents"), but no heading anywhere targets an obvious commercial query like "AI voice agent for customer support" — headings are brand-voice ("Trust by Design", "Use AI to improve your AI") rather than search-intent.

---

## 6. robots.txt and sitemap.xml

**`/robots.txt` — HTTP 200, exists but is a no-op:**

```
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Twitterbot
Allow: /

User-agent: facebookexternalhit
Allow: /

User-agent: *
Allow: /
```

Four redundant per-bot blocks that say exactly what the `*` block already says. Nothing is disallowed, which is fine. **But there is no `Sitemap:` directive** (`grep -i sitemap` → no match).

**`/sitemap.xml` — HTTP 404**, body is literally `Not found`, `content-type: text/plain`.

Also checked: `sitemap_index.xml` 404, `sitemap.txt` 404, `llms.txt` 404, `.well-known/security.txt` 404.

Given the site is currently one URL, the sitemap is low-impact *today* — but it becomes essential the moment `/en` and `/fr` are prerendered, and it's the standard way to declare the hreflang cluster server-side.

**Missing `llms.txt`** is worth flagging specifically: for an AI-infrastructure company selling to technical buyers who research via LLMs, publishing `llms.txt` is cheap and on-brand.

---

## 7. Duplicate content and soft 404s

**`www` is not redirected:**

```
$ curl -sIL https://www.callem.ai/ -o /dev/null -w "%{http_code} redirects=%{num_redirects}"
200 redirects=0
```

`https://www.callem.ai/` serves a **byte-identical 200** to the apex. The only thing preventing a duplicate-content split is the hardcoded `<link rel="canonical" href="https://callem.ai">` — which does work here, but relying on canonical instead of a 301 wastes crawl budget and leaks link equity. Add a 301 `www` → apex at the Cloudflare layer.

**Every unknown URL returns HTTP 200:**

```
$ curl -sI https://callem.ai/this-page-does-not-exist-xyz
HTTP/2 200

$ curl -sL https://callem.ai/privacy | diff - home.html
(identical)
```

`/privacy`, `/terms`, `/sitemap/`, and arbitrary garbage paths all return the same 200 homepage shell. The React router does have a `path:"*"` handler that renders a client-side 404:

```js
h.jsx("h1",{className:"text-4xl font-bold mb-4",children:"404"}),
h.jsx("p",{className:"text-xl text-gray-600 mb-4",children:"Oops! Page not found"})
```

...but the *server* never sends a 404 status. Google classifies these as soft 404s. This also means an unbounded number of URLs are technically "live" and crawlable.

**Note:** `/privacy` and `/terms` returning the homepage is a compliance-adjacent problem, not just SEO. A company whose entire positioning is GDPR/European data sovereignty has **no privacy policy and no terms page**. Buyers and procurement teams will look for these.

---

## 8. Site architecture — one page, no indexable surface

Complete href inventory extracted from the bundle:

```
#contact   #product   #solutions   /
https://calendar.app.google/jtxw2mP4bcEGELNM8
https://callem.ai/en    https://callem.ai/fr
https://docs.callem.ai
https://docs.callem.ai/api-reference/introduction
https://docs.callem.ai/quickstart
https://studio.callem.ai
mailto:contact@callem.ai
```

Every internal navigation link is a hash anchor. The footer's link map confirms it:

```js
Fl={product:["#product","#product","#product","https://docs.callem.ai/api-reference/introduction"],
    solutions:["#solutions","#solutions","#solutions","#solutions","#solutions"],
    resources:["https://docs.callem.ai"],
    company:["mailto:contact@callem.ai"]}
```

Five distinct solution categories exist in the copy — **Customer Support, Lead Qualification, Appointment Scheduling, Outbound Campaigns, Collections** — each with its own written headline and stats. All five collapse into `#solutions` on one page. These are five ready-made landing pages with the content already authored; they're just not addressable. Same for the three product pillars (Build / Deploy / Monitor).

This is the largest organic-growth opportunity on the site and requires almost no new copywriting.

---

## 9. Images

Only **4 `<img>` tags** exist in the entire application:

| Location | alt | Issues |
|---|---|---|
| Header logo | `alt="Callem.ai"` | no width/height |
| Logo marquee (mapped) | `alt={n.name}` | duplicated — array is `[..._0,..._0]` for the marquee loop, so every logo appears twice in the DOM |
| Voice AI Stack diagram | `alt="Callem Voice AI Stack — orchestrating OpenAI, Anthropic, ElevenLabs, Mistral, Google and more"` | good alt; 218 KB PNG |
| Integrations grid (mapped) | `alt={r.name}` | no dimensions |

**Alt coverage is 100%** — genuinely good, and the stack-diagram alt is descriptive rather than keyword-stuffed.

**But:**
```
$ grep -oE 'loading:"[a-z]+"|decoding:"[a-z]+"' app.js
(no matches)
```
**Zero `loading="lazy"`, zero `decoding="async"`, zero explicit `width`/`height` attributes** (only inline `style:{width:n.width,height:"auto"}`, which does not reserve layout space the same way and contributes to CLS).

Asset weights:
- `voice-ai-stack-D1fj-1mi.png` — **1648 × 1582, 217,950 bytes** as PNG, rendered at `max-width:700px`. Serving a 218 KB PNG at 2.3× the display width. WebP/AVIF at correct dimensions would be roughly 15–25 KB.
- `logo-full-CiXIqMWJ.png` — 20,302 bytes for a header logo that is `h-8` (32 px tall). Should be SVG.
- 18 integration logos as individual `/logos/*.svg` requests.

---

## 10. Performance signals

| Resource | Uncompressed | Transferred (gzip) |
|---|---|---|
| HTML | 2,243 B | gzip ✓ |
| `/assets/index-BJmILOxf.js` | **659,093 B** | **~206 KB** |
| `/assets/index-D5AMzoc1.css` | 72,824 B | ~12.7 KB |
| `/~flock.js` (analytics) | 21,296 B | — |

**Scripts: 2** — the main ES module (`<script type="module" crossorigin>`) and `/~flock.js` (deferred analytics, Parcel-bundled, proxied through `/~api/analytics` to dodge ad blockers; it ships a full IANA timezone table).

**Bundle is a single monolithic chunk.** No code splitting, no route-level lazy loading, no dynamic `import()`. 206 KB gzip of JS must download, parse, and execute before *any* pixel of content paints — this is the LCP element's entire critical path. The bundle includes framer-motion, react-router, @tanstack/react-query, react-hook-form, EmailJS, and shadcn/ui components, all loaded for a static marketing page.

**Fonts — the worst-performing part of the delivery.** Four families are loaded via a CSS `@import`:

```css
@import"https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400&family=Space+Grotesk:wght@600;700&display=swap"
```

Problems, in order of impact:
1. **`@import` inside CSS creates a serial request chain**: HTML → `index.css` → `fonts.googleapis.com/css2` → actual `.woff2` files. Four sequential round trips before text renders in its real font. A `<link>` in `<head>` would parallelise; self-hosting would eliminate two hops entirely.
2. **No `<link rel="preconnect">`** to `fonts.googleapis.com` or `fonts.gstatic.com` in the HTML (verified — the `<head>` has no preconnect/preload of any kind).
3. **9 font weight/style variants** across 4 families (Instrument Serif regular+italic, Inter 400/500/600/700, JetBrains Mono 400, Space Grotesk 600/700).
4. **Google Fonts is a third-party EU-data-transfer issue** — German courts have ruled that hotlinking Google Fonts violates GDPR by transmitting visitor IPs to Google. For a company whose entire pitch is "Made in Europe. Hosted in Europe. Stays in Europe," hotlinking Google Fonts is a self-inflicted credibility problem as much as a performance one. Self-host the woff2 files.

**Caching:** correct. HTML is `no-cache, must-revalidate, max-age=0`; hashed assets are `public, max-age=31536000, immutable`.

**Headers:** `strict-transport-security: max-age=31536000; includeSubDomains`, `x-content-type-options: nosniff`, `referrer-policy: strict-origin-when-cross-origin`. Served via Cloudflare. No `x-robots-tag`. Solid.

**Expected Core Web Vitals:** LCP will be poor on mobile — empty HTML, then 206 KB JS parse, then a framer-motion entrance animation with `duration:1.1, delay:.15` on the h1 itself. The hero literally animates in from `opacity:0`, which delays LCP paint by design. CLS risk from missing image dimensions and `display:swap` on four font families.

---

## 11. "AI-generated site" tells

Unambiguous. This is a Lovable (formerly GPT Engineer) export:

1. **The orphaned marker comment** — the smoking gun:
   ```html
   <div id="root"></div>
   <!-- IMPORTANT: DO NOT REMOVE THIS SCRIPT TAG OR THIS VERY COMMENT! -->
   ```
   This comment is Lovable's boilerplate guarding its `gptengineer.js` injection script. **The script has been removed but the comment was left behind**, so it now guards nothing — a comment warning you not to delete a tag that isn't there. Nothing else in the file explains it.

2. **`/lovable-uploads/` in the OG image path** — `og:image="/lovable-uploads/cc1d3209-ae43-47aa-81c5-8d14c7b223fe.png"`. Lovable's asset-upload directory with its UUID naming, exposed in a meta tag that gets scraped and displayed by every social platform.

3. **`/~flock.js` + `/~api/analytics`** — the `~`-prefixed first-party-proxied analytics is Lovable's hosting signature.

4. **Boilerplate 404 that never got styled** — `bg-gray-100`, `text-blue-500 hover:text-blue-700 underline`, "Oops! Page not found". Default Tailwind greys and blues in a site whose actual palette is `#F5F0EB` / `#1A1A1A` / `#8B3CF7` / `#EB6A0A` with Instrument Serif. It also `console.error`s on every 404. Untouched scaffold.

5. **`meta name="author" content="callem.ai"`** — scaffold default; no SEO function.

6. **Stack fingerprint** — Vite + React + shadcn/ui + Tailwind + framer-motion + @tanstack/react-query + react-hook-form, all in one unsplit chunk, with react-query included on a page that makes no queries.

7. **Copy style** — em-dash-heavy throughout ("resolve, not just respond", "Go live in days, not months", "One studio. Three pillars.", "Made in Europe. Hosted in Europe. Stays in Europe."), triadic section labels, and heavy emoji in content strings (`"🇫🇷 Paris Datacenter","🏆 BPI French Tech","⚡ ~600ms E2E","🔒 GDPR Native"`).

**Assessment:** the design and copy are genuinely strong — this does not read as slop to a human visitor. But the markup tells any technical evaluator exactly how it was built, and `/lovable-uploads/` is visible in social previews. Cleaning up items 1, 2, and 4 costs under an hour.

---

# Prioritised remediation

**P0 — do first**
1. **Prerender to static HTML.** Add `vite-plugin-ssg` or equivalent. Resolves the rendering gap, soft 404s, and unlocks everything else. Single highest-ROI change on the site.
2. **Fix the canonical/hreflang conflict.** Prerender `/en` and `/fr` with self-referencing canonicals, correct `<html lang>`, translated titles, and static reciprocal hreflang. Currently the French site cannot rank.
3. **Publish `sitemap.xml`** and add `Sitemap: https://callem.ai/sitemap.xml` to robots.txt.
4. **301 `www` → apex.**

**P1**
5. **Add JSON-LD**: `Organization`, `SoftwareApplication`, `FAQPage`. All source data already exists in the bundle.
6. **Fix the FAQ**: render answers always-present (CSS collapse, not conditional mount), promote questions to `<h3>`.
7. **Make `og:image` absolute.**
8. **Self-host fonts as woff2**, drop the `@import` chain, add `preload` for the two above-the-fold faces. Also closes the GDPR gap that contradicts the site's own positioning.
9. **Return real 404 status codes.**

**P2**
10. **Split solutions into 5 real URLs** (`/solutions/customer-support`, `/lead-qualification`, `/appointment-scheduling`, `/outbound-campaigns`, `/collections`) — copy is already written.
11. **Images**: convert `voice-ai-stack.png` (218 KB, 1648px, displayed at 700px) to WebP at 2× display width; logo to SVG; add `width`/`height` and `loading="lazy"` below the fold.
12. **Fix heading skips** (h2→h4 in bento/insights/security/footer; "Resources" h2→h3).
13. **Trim meta description** to ~155 chars.
14. **Code-split the 206 KB bundle**; drop react-query if unused.
15. **Cleanup**: remove the orphaned Lovable comment, move assets off `/lovable-uploads/`, style the 404, simplify robots.txt to a single `User-agent: *` block.
16. **Publish `/privacy` and `/terms`** — currently both return the homepage, a real gap for a GDPR-positioned vendor.
17. **Add `llms.txt`** — cheap, on-brand for an AI-infra company whose buyers research via LLMs.
