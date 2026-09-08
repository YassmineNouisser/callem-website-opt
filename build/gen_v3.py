#!/usr/bin/env python3
"""Génère build/v3.src.html — proposition « Atelier », référence Genesys.

Blanc dominant, sans-serif épaisse, grandes captures produit, accent orange,
zéro fioriture. Le héros n'est plus une photo mais la console Callem en marche.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ── données ────────────────────────────────────────────────────────────────
SECTEURS = [
    ("Finance", "photo-1616924451835-747bd5cd08ee", "Identité vérifiée avant toute donnée.",
     "ic-lock", "100 %", "appels tracés", "Quartier d’affaires vu depuis la rue"),
    ("Santé", "photo-1578991624414-276ef23a534f", "Rendez-vous et rappels, zéro conseil médical.",
     "ic-shield", "−40 %", "de no-show", "Accueil d’un établissement de santé"),
    ("Retail", "photo-1591085686350-798c0f9faa7f", "Suivi, retours, réclamations. Pics absorbés.",
     "ic-campaign", "×3", "volume en pointe", "Cliente dans une boutique"),
    ("Assurance", "photo-1560264357-8d9202250f21", "Sinistres guidés, escalade encadrée.",
     "ic-transfer", "24/7", "déclaration", "Deux conseillers en rendez-vous"),
    ("Pouvoirs publics", "photo-1559589688-6ba6beafe1e5", "Accueil continu, 25+ langues.",
     "ic-eu", "25+", "langues", "Drapeau européen devant un bâtiment public"),
]

CHIFFRES = [("−30 %", "de coûts opérationnels"), ("70 %", "résolus sans humain"),
            ("+12 pts", "de NPS"), ("< 6 mois", "de retour sur investissement")]

USAGES = [
    ("genesys", "0 0 116 24", "Genesys", "photo-1580795479225-c50ab8c3348d",
     "Conseillère avec casque en centre de contact",
     "Le standard ne sonne plus dans le vide, la nuit.",
     [("24/7", "couverture"), ("0", "migration")]),
    ("salesforce", "0 0 136 24", "Salesforce", "photo-1516055619834-586f8c75d1de",
     "Homme au téléphone en extérieur",
     "Les leads arrivent qualifiés dans le CRM.",
     [("×3", "leads traités"), ("8/10", "score moyen")]),
    ("calcom", "0 0 106 24", "Cal.com", "photo-1525182008055-f88b95ff7980",
     "Conseiller au téléphone à son bureau",
     "Les rendez-vous se prennent pendant l’appel.",
     [("140 ms", "réservation"), ("−50 %", "no-show")]),
]

ETAPES = [
    ("Construire", "L’agent, écrit en clair",
     "Identité, missions, garde-fous. En langage clair, versionné, testable.",
     ["Prompt structuré et versionné", "RAG sur vos documents, 80 ms",
      "CRM, agenda, webhook pendant l’appel"]),
    ("Déployer", "Sur vos numéros, sans migration",
     "Nos numéros, votre SIP ou votre plateforme de contact existante.",
     ["Numéros FR et UE gérés par Callem", "Raccordement SIP à votre plateau",
      "Campagnes sortantes, 50 000 appels/jour"]),
    ("Tenir la latence", "Sous 600 ms, bout en bout",
     "L’appelant n’attend jamais son tour de parole.",
     ["VAD sémantique — l’agent attend la fin de la phrase",
      "Décomposition visible sur chaque appel", "Inférence exécutée à Paris"]),
    ("Superviser", "100 % des appels analysés",
     "Aucun échantillonnage. Alertes sur vos seuils.",
     ["Écoute live et intervention humaine", "Seuils et alertes configurables",
      "Tests A/B sur prompts et modèles"]),
]

LOGOS_HERO = ["openai", "anthropic", "mistral", "googlecloud", "elevenlabs", "azure"]
VB = {"openai": "0 0 120 24", "anthropic": "0 0 128 24", "mistral": "0 0 118 24",
      "googlecloud": "0 0 150 24", "elevenlabs": "0 0 130 24", "azure": "0 0 120 24",
      "salesforce": "0 0 136 24", "hubspot": "0 0 126 24", "twilio": "0 0 110 24",
      "zapier": "0 0 108 24", "calcom": "0 0 106 24", "genesys": "0 0 116 24",
      "zendesk": "0 0 116 24", "servicenow": "0 0 140 24", "pipedrive": "0 0 122 24",
      "zoho": "0 0 110 24", "attio": "0 0 96 24", "close": "0 0 100 24",
      "nice": "0 0 118 24", "five9": "0 0 98 24", "talkdesk": "0 0 118 24",
      "cisco": "0 0 102 24", "slack": "0 0 100 24"}
NOMS = {"openai": "OpenAI", "anthropic": "Anthropic", "mistral": "Mistral AI",
        "googlecloud": "Google Cloud", "elevenlabs": "ElevenLabs", "azure": "Microsoft Azure",
        "salesforce": "Salesforce", "hubspot": "HubSpot", "twilio": "Twilio", "zapier": "Zapier",
        "calcom": "Cal.com", "genesys": "Genesys", "zendesk": "Zendesk",
        "servicenow": "ServiceNow", "pipedrive": "Pipedrive", "zoho": "Zoho CRM",
        "attio": "Attio", "close": "Close", "nice": "NICE CXone", "five9": "Five9",
        "talkdesk": "Talkdesk", "cisco": "Cisco", "slack": "Slack"}

UNSPLASH = "https://images.unsplash.com/{}?auto=format&amp;fit=crop&amp;w={}&amp;q=72"


def logo(k, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="{VB[k]}" role="img" aria-label="{NOMS[k]}">'
            f'<use href="#lg-{k}"/></svg>')


def ic(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 24 24" aria-hidden="true"><use href="#{name}"/></svg>'


ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M5 12h13M12 5l7 7-7 7"/></svg>')
CHECK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M4 12.5 9.5 18 20 6.5"/></svg>')
CROSS = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" '
         'stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>')

# ── styles ─────────────────────────────────────────────────────────────────
CSS = r"""
/* ══════════════════════════════════════════════════════════════════════════
   CALLEM · V3 « ATELIER »
   Blanc dominant · sans-serif épaisse · grandes captures produit · un accent
   ══════════════════════════════════════════════════════════════════════════ */
:root{
  --ink:#12141A; --body:#5A6068; --muted:#8B9199;
  --white:#FFFFFF; --grey:#F5F6F8; --grey-2:#EDEFF2;
  --line:#E3E6EA; --line-2:#EFF1F4;
  --acc:#EB6A0A; --acc-h:#CF5C08; --acc-soft:#FDF2E8;
  --vio:#8B3CF7; --vio-soft:#F5EEFE;
  --ok:#1B7A45;
  --disp:"Archivo",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  --r:8px; --r-lg:12px; --r-xl:16px;
  --sh:0 1px 2px rgba(18,20,26,.04), 0 14px 30px -18px rgba(18,20,26,.18);
  --sh-lg:0 2px 6px rgba(18,20,26,.04), 0 44px 88px -44px rgba(18,20,26,.32);
  --wrap:1240px;
}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--white);color:var(--body);font-family:var(--sans);
  font-size:17px;line-height:1.62;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img,svg,video{display:block;max-width:100%}
a{color:inherit}
button{font:inherit}
h1,h2,h3,h4,p,ul,ol,dl,figure,blockquote{margin:0}
ul{padding:0;list-style:none}

.wrap{width:min(100% - 2.6rem, var(--wrap));margin-inline:auto}
.sec{padding:clamp(4.5rem,8vw,7.5rem) 0}
.sec--grey{background:var(--grey)}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

h1{font-family:var(--disp);font-weight:800;letter-spacing:-.038em;line-height:1.02;
  font-size:clamp(2.6rem,5.4vw,4.7rem);color:var(--ink)}
h2{font-family:var(--disp);font-weight:700;letter-spacing:-.032em;line-height:1.07;
  font-size:clamp(1.95rem,3.8vw,3.2rem);color:var(--ink)}
h3{font-family:var(--disp);font-weight:700;letter-spacing:-.022em;line-height:1.2;
  font-size:1.28rem;color:var(--ink)}
.lede{font-size:clamp(1.05rem,1.35vw,1.22rem);line-height:1.6;color:var(--body);max-width:56ch}
.kick{display:inline-flex;align-items:center;gap:.6rem;font-family:var(--mono);font-size:.65rem;
  font-weight:500;letter-spacing:.19em;text-transform:uppercase;color:var(--acc);margin-bottom:1.1rem}
.kick::before{content:"";width:1.6rem;height:2px;background:var(--acc);border-radius:2px}
.hd{max-width:62ch;margin-bottom:clamp(2.2rem,4vw,3.4rem)}
.hd p{margin-top:1.05rem}
.hd--mid{margin-inline:auto;text-align:center}
.hd--mid .kick{justify-content:center}

/* ── boutons ──────────────────────────────────────────────────────────── */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.55rem;text-decoration:none;
  font-weight:600;font-size:1rem;padding:.85rem 1.5rem;border-radius:var(--r);
  border:1px solid transparent;cursor:pointer;white-space:nowrap;
  transition:background .2s,border-color .2s,color .2s,box-shadow .25s,transform .2s}
.btn svg{width:16px;height:16px}
.btn--fill{background:var(--acc);color:#fff}
.btn--fill:hover{background:var(--acc-h);box-shadow:0 12px 26px -14px rgba(235,106,10,.85);
  transform:translateY(-1px)}
.btn--line{background:var(--white);border-color:var(--line);color:var(--ink)}
.btn--line:hover{border-color:var(--ink);transform:translateY(-1px)}
.btn--lg{padding:1.02rem 1.85rem;font-size:1.05rem}
.lnk{display:inline-flex;align-items:center;gap:.45rem;color:var(--acc);font-weight:600;
  text-decoration:none;font-size:.95rem}
.lnk svg{width:15px;height:15px;transition:transform .3s cubic-bezier(.2,.8,.2,1)}
.lnk:hover svg{transform:translateX(4px)}

/* ── navigation ───────────────────────────────────────────────────────── */
.nav{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.9);
  border-bottom:1px solid var(--line-2);backdrop-filter:saturate(1.8) blur(12px)}
.nav__in{display:flex;align-items:center;gap:2.2rem;height:68px}
.nav__b{display:flex;align-items:center;gap:.6rem;text-decoration:none;font-family:var(--disp);
  font-weight:700;font-size:1.15rem;letter-spacing:-.03em;color:var(--ink)}
.nav__b svg{width:28px;height:28px;border-radius:7px}
.nav__m{display:flex;gap:1.9rem;margin-left:auto}
.nav__m a{text-decoration:none;font-size:.94rem;font-weight:500;color:var(--body);
  transition:color .2s}
.nav__m a:hover{color:var(--ink)}
.nav__c{display:flex;gap:.6rem;margin-left:2rem}
.nav__c .btn{padding:.6rem 1.15rem;font-size:.92rem}
@media(max-width:960px){.nav__m{display:none}.nav__c{margin-left:auto}}
@media(max-width:520px){.nav__c .btn--line{display:none}}

/* ── héros ────────────────────────────────────────────────────────────── */
.hero{padding:clamp(3.2rem,6vw,5.5rem) 0 0;background:var(--white);position:relative;
  overflow:hidden}
.hero::before{content:"";position:absolute;inset:-20% -10% auto -10%;height:70%;pointer-events:none;
  background:radial-gradient(48% 60% at 78% 30%,rgba(235,106,10,.09),transparent 70%),
             radial-gradient(42% 55% at 18% 10%,rgba(139,60,247,.07),transparent 72%)}
.hero__in{position:relative}
.hero h1{max-width:17ch}
.hero .lede{margin-top:1.4rem}
.hero__cta{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:2.1rem}
.hero__tag{display:flex;flex-wrap:wrap;gap:1.5rem;margin-top:1.9rem;font-size:.88rem;
  color:var(--muted)}
.hero__tag span{display:inline-flex;align-items:center;gap:.45rem}
.hero__tag svg{width:15px;height:15px;color:var(--acc)}

/* ── la console produit ───────────────────────────────────────────────── */
.scr{margin-top:clamp(2.6rem,5vw,4.2rem);border-radius:var(--r-xl);background:var(--white);
  border:1px solid var(--line);box-shadow:var(--sh-lg);overflow:hidden}
.scr__bar{display:flex;align-items:center;gap:.55rem;padding:.72rem 1.1rem;
  border-bottom:1px solid var(--line-2);background:#FBFCFD}
.scr__bar i{width:9px;height:9px;border-radius:50%;background:var(--grey-2)}
.scr__bar i:first-child{background:#E5E7EB}
.scr__bar b{margin-left:.7rem;font-family:var(--mono);font-size:.7rem;font-weight:400;
  color:var(--muted)}
.scr__bar em{font-style:normal;font-family:var(--mono);font-size:.7rem;color:var(--ink)}
.scr__bar u{text-decoration:none;color:var(--muted)}
.scr__live{margin-left:auto;display:inline-flex;align-items:center;gap:.45rem;
  font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--acc)}
.scr__live s{text-decoration:none;width:6px;height:6px;border-radius:50%;background:var(--acc)}
@media (prefers-reduced-motion:no-preference){.scr__live s{animation:beat 1.9s ease-out infinite}}
@keyframes beat{0%{box-shadow:0 0 0 0 rgba(235,106,10,.5)}
  70%{box-shadow:0 0 0 8px rgba(235,106,10,0)}100%{box-shadow:0 0 0 0 rgba(235,106,10,0)}}
.scr__b{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr)}
@media(max-width:860px){.scr__b{grid-template-columns:1fr}}
.scr__l{padding:clamp(1.1rem,2vw,1.7rem);border-right:1px solid var(--line-2);min-height:380px}
.scr__r{padding:clamp(1.1rem,2vw,1.7rem);background:#FCFCFD}
@media(max-width:860px){.scr__l{border-right:0;border-bottom:1px solid var(--line-2);min-height:0}}
.scr__h{display:flex;align-items:center;font-family:var(--mono);font-size:.62rem;
  letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-bottom:1.1rem}
.scr__h b{margin-left:auto;font-weight:400;color:var(--ink);font-variant-numeric:tabular-nums}

.tr{display:grid;gap:1.05rem}
.tr li{display:grid;gap:.3rem;opacity:0;transform:translateY(10px);
  transition:opacity .45s ease,transform .5s cubic-bezier(.2,.8,.2,1)}
.tr li.on{opacity:1;transform:none}
.tr li>span{display:flex;align-items:center;gap:.5rem;font-family:var(--mono);font-size:.58rem;
  letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.tr li>span::before{content:"";width:5px;height:5px;border-radius:50%;background:#C3C7CC}
.tr li.me>span::before{background:var(--acc)}
.tr li>span em{margin-left:auto;font-style:normal;font-variant-numeric:tabular-nums}
.tr li p{font-size:1rem;line-height:1.5;color:var(--ink);max-width:44ch}
.tr li.me p{color:var(--ink);font-weight:500}

.fld{margin-bottom:1.15rem}
.fld:last-child{margin-bottom:0}
.fld>label{display:block;font-family:var(--mono);font-size:.58rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--muted);margin-bottom:.5rem}
.gl{display:grid;gap:.42rem}
.gl span{display:flex;align-items:center;gap:.5rem;font-size:.86rem;color:var(--body)}
.gl svg{width:14px;height:14px;flex:none}
.gl .no svg{color:#C2410C}
.gl .yes svg{color:var(--ok)}
.tl{display:grid;gap:.42rem}
.tl li{display:flex;align-items:center;gap:.6rem;padding:.5rem .7rem;border-radius:var(--r);
  background:var(--white);border:1px solid var(--line-2);font-family:var(--mono);font-size:.76rem;
  color:var(--ink);opacity:0;transform:translateY(8px);
  transition:opacity .4s ease,transform .45s cubic-bezier(.2,.8,.2,1)}
.tl li.on{opacity:1;transform:none}
.tl li svg{width:14px;height:14px;color:var(--vio);flex:none}
.tl li em{margin-left:auto;font-style:normal;font-size:.66rem;color:var(--muted);
  font-variant-numeric:tabular-nums}
.tl li.ok{border-color:rgba(27,122,69,.28);background:#F4FBF7}
.tl li.ok svg{color:var(--ok)}
.lat{display:grid;gap:.4rem}
.lat div{display:flex;align-items:center;gap:.7rem;font-size:.78rem}
.lat span{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);width:3.4rem;flex:none}
.lat u{text-decoration:none;flex:1;height:5px;border-radius:5px;background:var(--grey-2);
  overflow:hidden}
.lat u i{display:block;height:100%;width:0;border-radius:5px;background:var(--acc);
  transition:width .8s cubic-bezier(.2,.8,.2,1)}
.scr.on .lat u i{width:var(--w)}
.lat b{font-family:var(--mono);font-size:.68rem;font-weight:400;color:var(--ink);
  font-variant-numeric:tabular-nums;width:3.6rem;text-align:right}

/* ── bandeau de logos ─────────────────────────────────────────────────── */
.strip{padding:clamp(2.4rem,4vw,3.4rem) 0 clamp(3rem,5vw,4.4rem)}
.strip p{text-align:center;font-family:var(--mono);font-size:.63rem;letter-spacing:.17em;
  text-transform:uppercase;color:var(--muted);margin-bottom:1.6rem}
.strip__g{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;
  gap:clamp(1.8rem,4.5vw,3.6rem)}
.strip__g svg{height:22px;width:auto;opacity:.55;filter:grayscale(1);
  transition:opacity .3s,filter .3s}
.strip__g svg:hover{opacity:1;filter:none}

/* ── chiffres ─────────────────────────────────────────────────────────── */
.nums{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(1rem,2.5vw,2.6rem)}
@media(max-width:820px){.nums{grid-template-columns:repeat(2,1fr);gap:2rem 1.4rem}}
.num{padding-top:1.3rem;border-top:2px solid var(--ink)}
.num b{display:block;font-family:var(--disp);font-weight:800;letter-spacing:-.04em;
  font-size:clamp(2.3rem,4.2vw,3.4rem);line-height:1;color:var(--ink)}
.num span{display:block;margin-top:.55rem;font-size:.92rem;color:var(--body)}

/* ── plateforme ───────────────────────────────────────────────────────── */
.plat{display:grid;grid-template-columns:minmax(0,.72fr) minmax(0,1.28fr);
  gap:clamp(1.6rem,4vw,4rem);align-items:start}
@media(max-width:980px){.plat{grid-template-columns:1fr}}
.steps{display:grid;gap:0;position:relative}
.steps::before{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--line)}
.step{position:relative;text-align:left;background:none;border:0;padding:1.15rem 0 1.15rem 1.6rem;
  cursor:pointer;border-bottom:1px solid var(--line-2)}
.step:last-child{border-bottom:0}
.step::before{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--acc);
  transform:scaleY(0);transform-origin:50% 0;transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.step[aria-selected="true"]::before{transform:scaleY(1)}
.step__n{font-family:var(--mono);font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--muted);transition:color .3s}
.step[aria-selected="true"] .step__n{color:var(--acc)}
.step h3{margin-top:.3rem;color:#9AA0A7;transition:color .3s}
.step[aria-selected="true"] h3{color:var(--ink)}
.step__p{display:grid;grid-template-rows:0fr;opacity:0;
  transition:grid-template-rows .5s cubic-bezier(.2,.8,.2,1),opacity .35s ease}
.step[aria-selected="true"] .step__p{grid-template-rows:1fr;opacity:1}
.step__p>div{overflow:hidden;min-height:0}
.step__p p{padding-top:.55rem;font-size:.94rem;line-height:1.55;max-width:42ch}
.step__p ul{margin-top:.85rem;display:grid;gap:.45rem}
.step__p li{display:flex;gap:.55rem;align-items:flex-start;font-size:.86rem;color:var(--body)}
.step__p li::before{content:"";width:5px;height:5px;border-radius:50%;background:var(--acc);
  margin-top:.58rem;flex:none}
.shots{position:relative;border-radius:var(--r-xl);border:1px solid var(--line);
  background:var(--white);box-shadow:var(--sh-lg);overflow:hidden;aspect-ratio:4/3}
@media(max-width:980px){.shots{aspect-ratio:16/11}}
.shot{position:absolute;inset:0;opacity:0;pointer-events:none;
  transition:opacity .5s ease,transform .6s cubic-bezier(.2,.8,.2,1);transform:scale(1.015)}
.shot.on{opacity:1;pointer-events:auto;transform:none}
.shot__bar{display:flex;align-items:center;gap:.5rem;padding:.65rem 1rem;
  border-bottom:1px solid var(--line-2);background:#FBFCFD;font-family:var(--mono);
  font-size:.66rem;color:var(--muted)}
.shot__bar i{width:8px;height:8px;border-radius:50%;background:var(--grey-2)}
.shot__bar b{font-weight:400;color:var(--ink);margin-left:.5rem}
.shot__b{padding:clamp(1rem,2vw,1.6rem);display:grid;gap:.75rem;align-content:start}
.row{display:flex;align-items:center;gap:.65rem;padding:.62rem .8rem;border-radius:var(--r);
  border:1px solid var(--line-2);background:var(--white);font-size:.85rem;color:var(--ink)}
.row svg{width:15px;height:15px;color:var(--acc);flex:none}
.row em{margin-left:auto;font-style:normal;font-family:var(--mono);font-size:.66rem;
  color:var(--muted)}
.row--soft{background:var(--grey);border-color:transparent;color:var(--body);font-size:.83rem;
  line-height:1.5;display:block}
.row--acc{border-color:rgba(235,106,10,.3);background:var(--acc-soft)}
.bars{display:grid;gap:.5rem}
.bars div{display:flex;align-items:center;gap:.7rem;font-size:.8rem}
.bars span{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);width:3.6rem;flex:none}
.bars u{text-decoration:none;flex:1;height:6px;border-radius:6px;background:var(--grey-2);
  overflow:hidden}
.bars u i{display:block;height:100%;width:var(--w);border-radius:6px;background:var(--acc)}
.bars b{font-family:var(--mono);font-size:.68rem;font-weight:400;color:var(--ink);
  width:3.6rem;text-align:right;font-variant-numeric:tabular-nums}
.spark{display:flex;align-items:flex-end;gap:4px;height:78px}
.spark i{flex:1;border-radius:3px 3px 0 0;background:var(--acc);opacity:.75;height:var(--h)}
.spark i:nth-child(3n){background:var(--vio);opacity:.6}

/* ── secteurs ─────────────────────────────────────────────────────────── */
.cards{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:clamp(.8rem,1.5vw,1.3rem)}
@media(max-width:1100px){.cards{grid-template-columns:repeat(3,1fr)}}
@media(max-width:700px){.cards{grid-template-columns:repeat(2,1fr)}}
@media(max-width:460px){.cards{grid-template-columns:1fr}}
.card{display:flex;flex-direction:column;background:var(--white);border:1px solid var(--line-2);
  border-radius:var(--r-lg);overflow:hidden;text-decoration:none;
  transition:border-color .3s,box-shadow .35s,transform .35s cubic-bezier(.2,.8,.2,1)}
.card:hover{border-color:transparent;box-shadow:var(--sh);transform:translateY(-4px)}
.card__ph{position:relative;aspect-ratio:5/4;overflow:hidden;background:var(--grey-2)}
.card__ph img{width:100%;height:100%;object-fit:cover;
  transition:transform 1s cubic-bezier(.2,.8,.2,1)}
.card:hover .card__ph img{transform:scale(1.05)}
.card__ic{position:absolute;left:.7rem;top:.7rem;width:30px;height:30px;border-radius:8px;
  background:rgba(255,255,255,.94);display:grid;place-items:center;color:var(--acc)}
.card__ic svg{width:16px;height:16px}
.card__b{padding:1.05rem 1.05rem 1.2rem;display:flex;flex-direction:column;flex:1}
.card__b h3{font-size:1.1rem}
.card__b p{margin-top:.45rem;font-size:.87rem;line-height:1.5}
.card__k{margin-top:auto;padding-top:1rem;display:flex;align-items:baseline;gap:.45rem}
.card__k b{font-family:var(--disp);font-weight:800;font-size:1.35rem;letter-spacing:-.03em;
  color:var(--ink)}
.card__k span{font-family:var(--mono);font-size:.58rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--muted)}

/* ── contrôle ─────────────────────────────────────────────────────────── */
.tri{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(1rem,2vw,1.6rem)}
@media(max-width:900px){.tri{grid-template-columns:1fr}}
.lay{background:var(--white);border:1px solid var(--line-2);border-radius:var(--r-lg);
  padding:clamp(1.2rem,2vw,1.7rem);display:flex;flex-direction:column}
.lay__n{font-family:var(--mono);font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--acc)}
.lay h3{margin:.55rem 0 1.05rem}
.lay__s{border:1px solid var(--line-2);border-radius:var(--r);background:var(--grey);
  padding:.85rem;display:grid;gap:.5rem;margin-bottom:1.15rem}
.lay__r{display:flex;align-items:center;gap:.6rem;font-size:.79rem;color:var(--ink)}
.lay__r>span{font-family:var(--mono);font-size:.56rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--muted);width:4.4rem;flex:none}
.rd{display:inline-block;height:.72em;width:0;vertical-align:-.08em;border-radius:2px;
  background:var(--ink);opacity:.8;transition:width .55s cubic-bezier(.2,.8,.2,1) .7s}
.tri.on .rd{width:var(--w)}
.wv{display:flex;align-items:flex-end;gap:3px;height:30px}
.wv i{flex:1;height:32%;border-radius:2px;background:var(--acc);opacity:.55}
@media (prefers-reduced-motion:no-preference){.wv i{animation:wv 1.05s ease-in-out infinite alternate}}
@keyframes wv{to{height:100%;opacity:.9}}
.warn{display:flex;align-items:center;gap:.5rem;font-size:.78rem;color:#C2410C;
  background:rgba(194,65,12,.08);border-radius:var(--r);padding:.45rem .6rem}
.warn svg{width:14px;height:14px;flex:none}
.warn b{margin-left:auto;color:var(--ink);font-family:var(--mono);font-size:.57rem;
  letter-spacing:.1em;text-transform:uppercase;font-weight:400}
.lay ul{margin-top:auto;display:grid;gap:.5rem}
.lay li{display:flex;gap:.6rem;align-items:flex-start;font-size:.86rem}
.lay li svg{width:15px;height:15px;color:var(--acc);flex:none;margin-top:.16rem}

/* ── usages ───────────────────────────────────────────────────────────── */
.tales{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(1rem,2vw,1.6rem)}
@media(max-width:900px){.tales{grid-template-columns:1fr}}
.tale{background:var(--white);border:1px solid var(--line-2);border-radius:var(--r-lg);
  overflow:hidden;display:flex;flex-direction:column;
  transition:border-color .3s,box-shadow .35s,transform .35s cubic-bezier(.2,.8,.2,1)}
.tale:hover{border-color:transparent;box-shadow:var(--sh);transform:translateY(-4px)}
.tale__ph{aspect-ratio:16/10;overflow:hidden;background:var(--grey-2)}
.tale__ph img{width:100%;height:100%;object-fit:cover;
  transition:transform 1s cubic-bezier(.2,.8,.2,1)}
.tale:hover .tale__ph img{transform:scale(1.05)}
.tale__b{padding:clamp(1.1rem,2vw,1.5rem);display:flex;flex-direction:column;flex:1}
.tale__lg{height:18px;margin-bottom:1rem;opacity:.5}
.tale__lg svg{height:100%;width:auto;color:var(--ink)}
.tale__q{font-family:var(--disp);font-weight:700;letter-spacing:-.025em;line-height:1.25;
  font-size:clamp(1.15rem,1.7vw,1.4rem);color:var(--ink)}
.tale__m{margin-top:auto;padding-top:1.2rem;display:flex;gap:2rem}
.tale__m div{display:flex;flex-direction:column}
.tale__m b{font-family:var(--disp);font-weight:800;letter-spacing:-.035em;line-height:1;
  font-size:clamp(1.5rem,2.2vw,1.95rem);color:var(--ink)}
.tale__m span{margin-top:.35rem;font-family:var(--mono);font-size:.58rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--muted)}

/* ── intégrations ─────────────────────────────────────────────────────── */
.grid-lg{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));
  border-top:1px solid var(--line-2);border-left:1px solid var(--line-2)}
@media(max-width:1000px){.grid-lg{grid-template-columns:repeat(4,1fr)}}
@media(max-width:640px){.grid-lg{grid-template-columns:repeat(2,1fr)}}
.grid-lg span{display:grid;place-items:center;padding:1.9rem 1rem;background:var(--white);
  border-right:1px solid var(--line-2);border-bottom:1px solid var(--line-2);
  transition:background .25s}
.grid-lg span:hover{background:var(--grey)}
.grid-lg svg{height:21px;width:auto;opacity:.62;filter:grayscale(1);
  transition:opacity .25s,filter .25s}
.grid-lg span:hover svg{opacity:1;filter:none}
.more-line{margin-top:1.6rem;text-align:center;font-size:.92rem;color:var(--muted)}

/* ── conformité ───────────────────────────────────────────────────────── */
.conf{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);
  gap:clamp(1.6rem,4vw,4rem);align-items:center}
@media(max-width:920px){.conf{grid-template-columns:1fr}}
.conf__ph{border-radius:var(--r-xl);overflow:hidden;aspect-ratio:4/3;position:relative;
  background:var(--grey-2)}
.conf__ph img{width:100%;height:100%;object-fit:cover;filter:saturate(.9) contrast(1.05)}
.conf__pin{position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);
  font-family:var(--mono);font-size:.62rem;letter-spacing:.2em;color:#fff;
  text-shadow:0 2px 12px rgba(0,0,0,.6)}
.sheet{border:1px solid var(--line);border-radius:var(--r-lg);background:var(--white);
  box-shadow:var(--sh);overflow:hidden}
.sheet__h{display:flex;align-items:center;gap:.55rem;padding:.85rem 1.1rem;
  border-bottom:1px solid var(--line-2);font-family:var(--mono);font-size:.62rem;
  letter-spacing:.15em;text-transform:uppercase;color:var(--muted)}
.sheet__h svg{width:15px;height:15px;color:var(--acc)}
.sheet dl{margin:0;padding:.4rem 1.1rem}
.sheet dl>div{display:flex;gap:1rem;padding:.62rem 0;border-bottom:1px solid var(--line-2);
  font-size:.88rem}
.sheet dl>div:last-child{border-bottom:0}
.sheet dt{font-family:var(--mono);font-size:.58rem;letter-spacing:.13em;text-transform:uppercase;
  color:var(--muted);width:7rem;flex:none;padding-top:.2rem}
.sheet dd{margin:0;color:var(--ink)}
.sheet dd b{color:var(--acc)}
.sheet__f{padding:.95rem 1.1rem;background:var(--acc-soft);display:flex;gap:.6rem;
  align-items:flex-start;font-size:.86rem;color:var(--ink)}
.sheet__f svg{width:16px;height:16px;color:var(--acc);flex:none;margin-top:.15rem}
.sheet__f span{display:block;color:var(--body);margin-top:.2rem;font-size:.83rem}

/* ── démo ─────────────────────────────────────────────────────────────── */
.demo{display:grid;grid-template-columns:minmax(0,.92fr) minmax(0,1.08fr);
  border:1px solid var(--line);border-radius:var(--r-xl);overflow:hidden;background:var(--white);
  box-shadow:var(--sh-lg)}
@media(max-width:920px){.demo{grid-template-columns:1fr}}
.demo__l{padding:clamp(1.6rem,3vw,2.8rem);background:var(--grey);
  border-right:1px solid var(--line-2)}
.demo__l p.lede{margin-top:1rem;font-size:1rem}
.demo__r{padding:clamp(1.6rem,3vw,2.8rem)}
.brief{margin-top:1.8rem;border:1px solid var(--line);border-radius:var(--r-lg);
  background:var(--white);padding:1.1rem 1.2rem;position:relative;overflow:hidden;
  transition:border-color .5s,box-shadow .5s}
.brief.ready{border-color:var(--acc);box-shadow:0 18px 40px -26px rgba(235,106,10,.7)}
.brief__h{display:flex;align-items:center;gap:.5rem;font-family:var(--mono);font-size:.59rem;
  letter-spacing:.15em;text-transform:uppercase;color:var(--muted)}
.brief__h s{text-decoration:none;width:6px;height:6px;border-radius:50%;background:var(--acc)}
.brief__h b{margin-left:auto;font-weight:400}
.brief__s{display:flex;gap:.7rem;margin-top:.95rem}
.brief__s svg{width:28px;height:28px;border-radius:7px;flex:none}
.brief__s p{font-size:.94rem;line-height:1.5;color:var(--ink)}
.brief__s q{quotes:"«\00a0" "\00a0»"}
.brief b.v{font-weight:600;color:var(--acc);border-radius:3px;transition:background-color .5s}
.brief b.v.empty{font-weight:400;font-style:italic;color:var(--muted)}
.brief .flash{background-color:rgba(235,106,10,.16)}
.brief dl{margin:1rem 0 0;padding-top:.9rem;border-top:1px solid var(--line-2);display:grid;gap:.5rem}
.brief dl>div{display:flex;gap:.8rem;font-size:.85rem;align-items:baseline}
.brief dt{font-family:var(--mono);font-size:.58rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--muted);width:4.9rem;flex:none}
.brief dd{margin:0;color:var(--ink);overflow-wrap:anywhere;font-variant-numeric:tabular-nums}
.brief dd.empty{color:var(--muted);font-style:italic}
.brief__ok{display:flex;align-items:center;gap:.45rem;font-family:var(--mono);font-size:.59rem;
  letter-spacing:.13em;text-transform:uppercase;color:var(--acc);
  max-height:0;opacity:0;overflow:hidden;border-top:0 solid var(--line-2);padding-top:0;
  transition:max-height .5s cubic-bezier(.2,.8,.2,1),opacity .4s,padding-top .5s,border-top-width .5s}
.brief.ready .brief__ok{max-height:3rem;opacity:1;padding-top:.85rem;border-top-width:1px;
  margin-top:.95rem}
.brief__ok svg{width:13px;height:13px}

.fg{display:grid;grid-template-columns:1fr 1fr;gap:1.35rem .9rem}
@media(max-width:560px){.fg{grid-template-columns:1fr}}
.f--w{grid-column:1/-1}
.fld2{position:relative}
.fld2 input,.fld2 select{font:inherit;font-size:.97rem;color:var(--ink);width:100%;
  background:transparent;border:0;border-bottom:1px solid var(--line);border-radius:0;
  padding:1.15rem 1.6rem .55rem 0;outline:none;appearance:none}
.fld2 select{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1.5 6 6.5l5-5' stroke='%238B9199' stroke-width='1.6' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right .15rem center}
.fld2 label{position:absolute;left:0;top:1.15rem;font-size:.97rem;color:var(--muted);
  pointer-events:none;transform-origin:0 50%;
  transition:transform .3s cubic-bezier(.2,.8,.2,1),color .3s}
.fld2 input:focus+label,.fld2 select:focus+label,
.fld2 input:not(:placeholder-shown)+label,.fld2 select[data-filled]+label{
  transform:translateY(-1.15rem) scale(.72);color:var(--acc)}
.fld2::before{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:var(--acc);
  transform:scaleX(0);transform-origin:0 50%;pointer-events:none;
  transition:transform .45s cubic-bezier(.2,.8,.2,1)}
.fld2:focus-within::before{transform:scaleX(1)}
.fld2::after{content:"";position:absolute;right:2px;top:1.3rem;width:11px;height:6px;
  border-left:2px solid var(--acc);border-bottom:2px solid var(--acc);opacity:0;
  transform:rotate(-45deg) scale(.4);transform-origin:50% 50%;pointer-events:none;
  transition:opacity .3s,transform .45s cubic-bezier(.2,.8,.2,1)}
.fld2.ok::after{opacity:1;transform:rotate(-45deg) scale(1)}
.fld2.bad::before{background:#C2410C;transform:scaleX(1)}
.fld2 .err{position:absolute;left:0;top:100%;margin-top:.2rem;font-size:.7rem;color:#C2410C;
  opacity:0;transform:translateY(-4px);pointer-events:none;transition:.25s}
.fld2.bad .err{opacity:1;transform:none}
.fld2 .req{color:var(--vio)}
.more{border:0;background:none;padding:.4rem 0;display:inline-flex;align-items:center;gap:.45rem;
  font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--acc);cursor:pointer}
.more svg{width:13px;height:13px;transition:transform .3s}
.more[aria-expanded="true"] svg{transform:rotate(45deg)}
.extra{display:grid;grid-template-columns:1fr 1fr;gap:.9rem;overflow:hidden;max-height:0;
  transition:max-height .5s cubic-bezier(.2,.8,.2,1),margin-top .5s}
.extra.on{max-height:14rem;margin-top:1.1rem}
@media(max-width:560px){.extra{grid-template-columns:1fr}}
.gauge{display:flex;align-items:center;gap:.8rem;margin-top:1.7rem}
.gauge u{text-decoration:none;flex:1;height:3px;border-radius:3px;background:var(--grey-2);
  overflow:hidden}
.gauge u i{display:block;height:100%;width:0;border-radius:3px;background:var(--acc);
  transition:width .55s cubic-bezier(.2,.8,.2,1)}
.gauge b{font-family:var(--mono);font-size:.64rem;font-weight:400;color:var(--muted);
  font-variant-numeric:tabular-nums}
.send{display:flex;flex-wrap:wrap;align-items:center;gap:1rem;margin-top:1.5rem}
.send p{font-size:.83rem;color:var(--muted);max-width:30ch}
.btn.busy{pointer-events:none}
.btn.busy span{opacity:0}
.btn.busy::after{content:"";position:absolute;left:50%;top:50%;width:17px;height:17px;
  margin:-8.5px 0 0 -8.5px;border-radius:50%;border:2px solid rgba(255,255,255,.35);
  border-top-color:#fff;animation:spin .7s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.btn{position:relative}
.done{display:none;text-align:center;padding:clamp(2rem,5vw,3.6rem) 0}
.done.on{display:block}
.done__i{width:56px;height:56px;border-radius:50%;background:var(--acc-soft);color:var(--acc);
  display:grid;place-items:center;margin:0 auto 1.4rem}
.done__i svg{width:26px;height:26px}
.done p{margin-top:.85rem}
.done p b{color:var(--ink);font-weight:600}

/* ── pied de page ─────────────────────────────────────────────────────── */
.foot{background:var(--ink);color:#A7ADB5;padding:clamp(3.2rem,6vw,5rem) 0 2rem}
.foot__t{display:grid;grid-template-columns:1.5fr repeat(4,1fr);gap:2.2rem}
@media(max-width:900px){.foot__t{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.foot__t{grid-template-columns:1fr}}
.foot__b svg{width:30px;height:30px;border-radius:8px;margin-bottom:1rem}
.foot__b p{max-width:30ch;line-height:1.55;font-size:.92rem}
.foot__b .adr{margin-top:1rem;font-family:var(--mono);font-size:.72rem;color:#767D86;
  line-height:1.6}
.foot h4{font-family:var(--mono);font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;
  color:#767D86;font-weight:400;margin-bottom:1rem}
.foot ul{display:grid;gap:.6rem}
.foot a{text-decoration:none;font-size:.92rem;color:#C9CED4;transition:color .2s}
.foot a:hover{color:#fff}
.foot__bar{margin-top:clamp(2.4rem,5vw,3.6rem);padding-top:1.6rem;
  border-top:1px solid rgba(255,255,255,.1);display:flex;flex-wrap:wrap;gap:1rem;
  align-items:center;font-family:var(--mono);font-size:.72rem;color:#767D86}
.foot__soc{margin-left:auto;display:flex;gap:.5rem}
.foot__soc a{width:34px;height:34px;border:1px solid rgba(255,255,255,.16);border-radius:var(--r);
  display:grid;place-items:center;transition:border-color .2s,background .2s}
.foot__soc a:hover{border-color:var(--acc);background:rgba(235,106,10,.14)}
.foot__soc svg{width:15px;height:15px}

/* ── révélations ──────────────────────────────────────────────────────── */
.rv{opacity:0;transform:translateY(26px);
  transition:opacity .75s cubic-bezier(.2,.8,.2,1) var(--d,0ms),
             transform .85s cubic-bezier(.2,.8,.2,1) var(--d,0ms)}
.rv.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){
  .rv{opacity:1;transform:none}
  *{animation-duration:.01ms!important;transition-duration:.01ms!important}
}
"""

# ── fragments produit ──────────────────────────────────────────────────────
SHOTS = [
    ("Assistant Commercial — Acme", f"""
        <div class="row row--soft"><b style="color:var(--muted);font-family:var(--mono);font-size:.6rem;letter-spacing:.13em;text-transform:uppercase">Identité</b><br>
          Vous êtes un assistant commercial professionnel pour Acme Corp. Ton chaleureux, phrases courtes.</div>
        <div class="row row--acc">{ic('ic-agent')}Qualifier sur budget, échéance et décideur<em>mission</em></div>
        <div class="row">{CROSS.replace('currentColor','#C2410C')}Ne jamais confirmer un prix<em>garde-fou</em></div>
        <div class="row">{CROSS.replace('currentColor','#C2410C')}Aucun conseil médical<em>garde-fou</em></div>
        <div class="row">{CHECK.replace('currentColor','#1B7A45')}Toujours vérifier l’identité<em>garde-fou</em></div>"""),
    ("Canaux", f"""
        <div class="row">{ic('ic-phone')}+33 1 84 88 00 00<em>numéro FR</em></div>
        <div class="row">{ic('ic-sip')}Trunk SIP — actif<em>votre plateau</em></div>
        <div class="row">{ic('ic-chat')}Webchat sur votre site<em>même agent</em></div>
        <div class="row">{ic('ic-campaign')}Campagnes sortantes<em>50 000 / jour</em></div>
        <div class="row row--soft"><b style="color:var(--muted);font-family:var(--mono);font-size:.6rem;letter-spacing:.13em;text-transform:uppercase">Zone de traitement</b><br>
          eu-west-paris — aucun transit hors Union européenne</div>"""),
    ("Latence bout-en-bout", """
        <div class="bars">
          <div><span>STT</span><u><i style="--w:16%"></i></u><b>90 ms</b></div>
          <div><span>RAG</span><u><i style="--w:14%"></i></u><b>80 ms</b></div>
          <div><span>LLM</span><u><i style="--w:31%"></i></u><b>180 ms</b></div>
          <div><span>TTS</span><u><i style="--w:26%"></i></u><b>150 ms</b></div>
          <div><span>Réseau</span><u><i style="--w:17%"></i></u><b>100 ms</b></div>
        </div>
        <div class="row row--acc" style="margin-top:.4rem">Total perçu par l’appelant<em>~600 ms</em></div>"""),
    ("Analytics", f"""
        <div class="row row--soft"><b style="color:var(--muted);font-family:var(--mono);font-size:.6rem;letter-spacing:.13em;text-transform:uppercase">Appels analysés · 30 jours</b>
          <span class="spark">{''.join(f'<i style="--h:{h}%"></i>' for h in [38,62,44,78,52,70,48,86,58,40,74,54,66,46])}</span></div>
        <div class="row">{ic('ic-analytics')}Sentiment positif<em>78 %</em></div>
        <div class="row">{ic('ic-alert')}Alerte — seuil dépassé<em>30 %</em></div>
        <div class="row">{ic('ic-workflow')}Test A/B — prompt v3<em>+12 %</em></div>"""),
]


def build_html():
    steps = "".join(
        f'''<button class="step" type="button" role="tab" aria-selected="{'true' if i==0 else 'false'}" data-i="{i}">
            <span class="step__n">0{i+1} · {tab}</span>
            <h3>{titre}</h3>
            <span class="step__p"><div>
              <p>{txt}</p>
              <ul>{''.join(f'<li>{b}</li>' for b in puces)}</ul>
            </div></span>
          </button>'''
        for i, (tab, titre, txt, puces) in enumerate(ETAPES))

    shots = "".join(
        f'''<div class="shot{' on' if i==0 else ''}" data-i="{i}">
            <div class="shot__bar"><i></i><i></i><i></i>callem.ai/studio&nbsp;/&nbsp;<b>{t}</b></div>
            <div class="shot__b">{corps}</div>
          </div>'''
        for i, (t, corps) in enumerate(SHOTS))

    cartes = "".join(
        f'''<a class="card rv" style="--d:{i*70}ms" href="#demo">
            <span class="card__ph"><img src="{UNSPLASH.format(pid, 560)}" alt="{alt}" loading="lazy" decoding="async">
              <span class="card__ic">{ic(icone)}</span></span>
            <span class="card__b"><h3>{nom}</h3><p>{desc}</p>
              <span class="card__k"><b>{k}</b><span>{klab}</span></span></span>
          </a>'''
        for i, (nom, pid, desc, icone, k, klab, alt) in enumerate(SECTEURS))

    tales = "".join(
        f'''<article class="tale rv" style="--d:{i*90}ms">
            <div class="tale__ph"><img src="{UNSPLASH.format(pid, 720)}" alt="{alt}" loading="lazy" decoding="async"></div>
            <div class="tale__b">
              <span class="tale__lg">{logo(lg)}</span>
              <p class="tale__q">{cite}</p>
              <div class="tale__m">{''.join(f'<div><b>{v}</b><span>{l}</span></div>' for v,l in mets)}</div>
            </div>
          </article>'''
        for i, (lg, vb, nom, pid, alt, cite, mets) in enumerate(USAGES))

    nums = "".join(f'<div class="num rv" style="--d:{i*80}ms"><b>{v}</b><span>{l}</span></div>'
                   for i, (v, l) in enumerate(CHIFFRES))

    tous = "".join(f"<span>{logo(k)}</span>" for k in VB)
    hero_logos = "".join(logo(k) for k in LOGOS_HERO)
    wv = "".join('<i style="animation-delay:%dms"></i>' % (k * 70) for k in range(14))
    return steps, shots, cartes, tales, nums, tous, hero_logos, wv

# ── page ───────────────────────────────────────────────────────────────────
PAGE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Callem — Des agents vocaux qui résolvent vos appels, en France</title>
<meta name="description" content="Agents vocaux IA pour la finance, la santé, le retail, l'assurance et le secteur public. Supervision temps réel, garde-fous, hébergement France, conforme AI Act article 50.">
<link rel="canonical" href="https://callem.ai/">
<meta property="og:type" content="website">
<meta property="og:title" content="Callem — Des agents vocaux qui résolvent vos appels">
<meta property="og:description" content="Conçu en Europe. Hébergé en Europe. Reste en Europe. Conforme AI Act article 50.">
<meta property="og:locale" content="fr_FR">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>__CSS__</style>
</head>
<body>
<!--SPRITE-->

<header class="nav">
  <div class="wrap nav__in">
    <a class="nav__b" href="#top"><svg viewBox="0 0 127 127" aria-hidden="true"><use href="#callem-mark"/></svg>Callem</a>
    <nav class="nav__m" aria-label="Principale">
      <a href="#plateforme">Plateforme</a><a href="#secteurs">Secteurs</a>
      <a href="#controle">Contrôle</a><a href="#conformite">Conformité</a>
      <a href="https://docs.callem.ai/" target="_blank" rel="noopener">Ressources</a>
    </nav>
    <div class="nav__c">
      <a class="btn btn--line" href="https://app.callem.ai/" target="_blank" rel="noopener">Se connecter</a>
      <a class="btn btn--fill" href="#demo">Réserver une démo</a>
    </div>
  </div>
</header>

<main id="top">

<section class="hero">
  <div class="wrap hero__in">
    <p class="kick rv">Agents vocaux IA · hébergés à Paris</p>
    <h1 class="rv" style="--d:60ms">Des agents vocaux qui résolvent vos appels.</h1>
    <p class="lede rv" style="--d:120ms">Traités de bout en bout, supervisés en direct, hébergés en France.
      Sur vos numéros, sans migration.</p>
    <div class="hero__cta rv" style="--d:180ms">
      <a class="btn btn--fill btn--lg" href="#demo">Réserver une démo</a>
      <a class="btn btn--line btn--lg" href="#plateforme">Voir la plateforme</a>
    </div>
    <p class="hero__tag rv" style="--d:240ms">
      <span>__IC_LOCK__Datacenter à Paris</span>
      <span>__IC_SHIELD__Conforme AI Act article 50</span>
      <span>__IC_EU__RGPD natif</span>
    </p>

    <div class="scr rv" id="scr" style="--d:300ms">
      <div class="scr__bar"><i></i><i></i><i></i>
        <b>callem.ai/studio</b><u>&nbsp;/&nbsp;</u><em>Appel entrant — Acme</em>
        <span class="scr__live"><s></s>En direct</span></div>
      <div class="scr__b">
        <div class="scr__l">
          <div class="scr__h">Transcription<b id="clk">00:00</b></div>
          <ul class="tr" id="tr">
            <li data-at="2"><span>Appelant<em>00:02</em></span><p>Ma commande #4521 a trois jours de retard.</p></li>
            <li data-at="6" class="me"><span>Agent Callem<em>00:06</em></span><p>Je vérifie tout de suite.</p></li>
            <li data-at="19" class="me"><span>Agent Callem<em>00:19</em></span><p>Elle est repartie ce matin, livraison mardi. Je vous envoie le suivi par SMS.</p></li>
            <li data-at="38"><span>Appelant<em>00:38</em></span><p>Parfait, merci.</p></li>
          </ul>
        </div>
        <div class="scr__r">
          <div class="scr__h">Agent · Assistant Commercial</div>
          <div class="fld"><label>Garde-fous actifs</label>
            <div class="gl">
              <span class="no">__CROSS__Ne jamais confirmer un prix</span>
              <span class="no">__CROSS__Aucun conseil médical</span>
              <span class="yes">__CHECK__Toujours vérifier l’identité</span>
            </div></div>
          <div class="fld"><label>Outils appelés pendant l’appel</label>
            <ul class="tl" id="tl">
              <li data-at="9">__IC_TOOLS__crm.get_order(#4521)<em>82 ms</em></li>
              <li data-at="24">__IC_CHAT__sms.send(tracking)<em>140 ms</em></li>
              <li data-at="41" class="ok">__CHECK__Résolu sans humain<em>00:41</em></li>
            </ul></div>
          <div class="fld"><label>Latence bout en bout</label>
            <div class="lat">
              <div><span>STT</span><u><i style="--w:16%"></i></u><b>90 ms</b></div>
              <div><span>LLM</span><u><i style="--w:31%"></i></u><b>180 ms</b></div>
              <div><span>TTS</span><u><i style="--w:26%"></i></u><b>150 ms</b></div>
              <div><span>Total</span><u><i style="--w:100%"></i></u><b>580 ms</b></div>
            </div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="strip">
  <div class="wrap">
    <p>Une couche d’orchestration au-dessus du meilleur de l’IA vocale</p>
    <div class="strip__g rv">__HERO_LOGOS__</div>
  </div>
</section>

<section class="sec sec--grey" id="resultats">
  <div class="wrap">
    <div class="hd rv"><p class="kick">Résultats</p>
      <h2>Ce que ça change, dès le premier mois.</h2></div>
    <div class="nums">__NUMS__</div>
    <p class="rv" style="margin-top:2.4rem;font-family:var(--mono);font-size:.72rem;color:var(--muted)">
      Déploiements en production · benchmarks Forrester et Gartner.</p>
  </div>
</section>

<section class="sec" id="plateforme">
  <div class="wrap">
    <div class="hd rv"><p class="kick">La plateforme</p>
      <h2>Construire, déployer, superviser. Au même endroit.</h2>
      <p class="lede">Un seul socle, de la première ligne au dernier appel.</p></div>
    <div class="plat">
      <div class="steps rv" id="steps" role="tablist" aria-label="Étapes de la plateforme">__STEPS__</div>
      <div class="shots rv" id="shots" style="--d:100ms">__SHOTS__</div>
    </div>
  </div>
</section>

<section class="sec sec--grey" id="secteurs">
  <div class="wrap">
    <div class="hd rv"><p class="kick">Secteurs</p>
      <h2>Cinq métiers, un même socle.</h2>
      <p class="lede">Les garde-fous changent, la plateforme non.</p></div>
    <div class="cards">__CARTES__</div>
  </div>
</section>

<section class="sec" id="controle">
  <div class="wrap">
    <div class="hd rv"><p class="kick">Contrôle</p>
      <h2>Trois couches, parce qu’aucune IA n’est fiable à 100 %.</h2></div>
    <div class="tri" id="tri">
      <div class="lay rv"><p class="lay__n">01 · Avant</p><h3>Sécuriser avant de livrer</h3>
        <div class="lay__s">
          <div class="lay__r"><span>Règle</span>ne jamais confirmer un prix</div>
          <div class="lay__r"><span>Identité</span>Camille D<i class="rd" style="--w:2.5em"></i></div>
          <div class="lay__r"><span>Numéro</span>+33 6 <i class="rd" style="--w:3.4em"></i> 78</div>
        </div>
        <ul><li>__IC_SHIELD__Garde-fous entrée et sortie</li>
          <li>__IC_LOCK__Masquage des données personnelles</li>
          <li>__IC_TEST__Tests sur les cas limites</li></ul></div>
      <div class="lay rv" style="--d:90ms"><p class="lay__n">02 · Pendant</p><h3>Observer et intervenir</h3>
        <div class="lay__s">
          <div class="lay__r"><span>En direct</span><b style="margin-left:auto;font-family:var(--mono);font-size:.7rem;font-weight:400">00:41</b></div>
          <div class="wv">__WV__</div>
          <div class="warn">__IC_ALERT__Le ton monte<b>Escalade</b></div>
        </div>
        <ul><li>__IC_LIVE__Supervision live</li>
          <li>__IC_ALERT__Alertes sur anomalie</li>
          <li>__IC_TRANSFER__Escalade avec le contexte</li></ul></div>
      <div class="lay rv" style="--d:180ms"><p class="lay__n">03 · Après</p><h3>Évaluer chaque appel</h3>
        <div class="lay__s">
          <div class="bars">
            <div><span>Hallucin.</span><u><i style="--w:4%"></i></u><b>0,4 %</b></div>
            <div><span>Résolu</span><u><i style="--w:70%"></i></u><b>70 %</b></div>
          </div>
          <div class="lay__r"><span>A/B</span>prompt v3 → +12 %</div>
        </div>
        <ul><li>__IC_ANALYTICS__Scoring hallucination</li>
          <li>__IC_WORKFLOW__Expérimentations A/B</li>
          <li>__IC_KB__Chaque correction renforce l’agent</li></ul></div>
    </div>
  </div>
</section>

<section class="sec sec--grey">
  <div class="wrap">
    <div class="hd rv"><p class="kick">Sur le terrain</p>
      <h2>Trois usages, trois résultats.</h2></div>
    <div class="tales">__TALES__</div>
  </div>
</section>

<section class="sec" id="integrations">
  <div class="wrap">
    <div class="hd hd--mid rv"><p class="kick">Intégrations</p>
      <h2>S’intègre à votre stack existante.</h2></div>
    <div class="grid-lg rv">__TOUS__</div>
    <p class="more-line rv">et plusieurs autres — API REST et MCP pour le reste.</p>
  </div>
</section>

<section class="sec sec--grey" id="conformite">
  <div class="wrap">
    <div class="hd rv"><p class="kick">Conformité</p>
      <h2>Conçu en Europe. Hébergé en Europe. Reste en Europe.</h2></div>
    <div class="conf">
      <div class="conf__ph rv"><img src="__PARIS__" alt="Paris de nuit, pont Alexandre III" loading="lazy" decoding="async">
        <span class="conf__pin">PARIS · EU-WEST</span></div>
      <div class="sheet rv" style="--d:100ms">
        <div class="sheet__h">__IC_EU__Fiche de conformité</div>
        <dl>
          <div><dt>Traitement</dt><dd>eu-west-paris</dd></div>
          <div><dt>Transit</dt><dd><b>0</b> donnée hors Union européenne</dd></div>
          <div><dt>Entraînement</dt><dd>aucune donnée client</dd></div>
          <div><dt>RGPD</dt><dd>anonymisation · opposition · DPA</dd></div>
          <div><dt>Énergie</dt><dd>~50 g CO₂/kWh · ~400 g aux États-Unis</dd></div>
        </dl>
        <div class="sheet__f">__IC_SHIELD__<div><b style="color:var(--ink)">AI Act — article 50, applicable depuis août 2026</b>
          <span>L’agent annonce qu’il est une IA dès la première seconde. Journalisé.</span></div></div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="demo">
  <div class="wrap">
    <div class="demo rv" id="demoBox">
      <div class="demo__l">
        <p class="kick">Réserver une démo</p>
        <h2 style="font-size:clamp(1.7rem,2.8vw,2.4rem)">On vous appelle. Avec un agent.</h2>
        <p class="lede">On configure un agent sur votre cas, puis il vous appelle. Sous 24 h.</p>
        <div class="brief" id="brief">
          <div class="brief__h"><s></s>Appel de démo<b>sous 24 h</b></div>
          <div class="brief__s"><svg viewBox="0 0 127 127" aria-hidden="true"><use href="#callem-mark"/></svg>
            <p><q>Bonjour <b class="v empty" data-k="nom">votre nom</b>, ici l’assistant vocal
              de <b class="v empty" data-k="societe">votre société</b>. Je vous appelle pour votre démo Callem.</q></p></div>
          <dl>
            <div><dt>Objectif</dt><dd class="empty" data-k="objectif">à préciser</dd></div>
            <div><dt>Numéro</dt><dd class="empty" data-k="telephone">à préciser</dd></div>
            <div><dt>E-mail</dt><dd class="empty" data-k="email">à préciser</dd></div>
          </dl>
          <div class="brief__ok">__CHECK__Fiche prête à partir</div>
        </div>
      </div>
      <div class="demo__r">
        <form id="form" novalidate>
          <div class="fg">
            <div class="fld2 f--w">
              <select id="objectif" name="objectif" required>
                <option value="" disabled selected hidden></option>
                <option>Support client</option><option>Qualification de leads</option>
                <option>Prise de rendez-vous</option><option>Campagnes sortantes</option>
                <option>Recouvrement</option><option>Standard téléphonique</option>
              </select>
              <label for="objectif">Objectif de la démo <span class="req">*</span></label>
              <span class="err">Choisissez un objectif.</span></div>
            <div class="fld2"><input id="nom" name="nom" type="text" autocomplete="name" placeholder=" " required>
              <label for="nom">Nom et prénom <span class="req">*</span></label><span class="err">Indiquez votre nom.</span></div>
            <div class="fld2"><input id="societe" name="societe" type="text" autocomplete="organization" placeholder=" " required>
              <label for="societe">Société <span class="req">*</span></label><span class="err">Indiquez votre société.</span></div>
            <div class="fld2"><input id="email" name="email" type="email" autocomplete="email" placeholder=" " required>
              <label for="email">E-mail professionnel <span class="req">*</span></label><span class="err">Adresse e-mail invalide.</span></div>
            <div class="fld2"><input id="tel" name="telephone" type="tel" autocomplete="tel" inputmode="tel" maxlength="20" placeholder=" " required>
              <label for="tel">Téléphone <span class="req">*</span></label><span class="err">Numéro invalide.</span></div>
            <div class="f--w">
              <button class="more" type="button" aria-expanded="false" aria-controls="extra">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
                <span>Ajouter un détail</span></button>
              <div class="extra" id="extra">
                <div class="fld2"><select id="secteur" name="secteur">
                  <option value="" disabled selected hidden></option>
                  <option>Finance</option><option>Santé</option><option>Retail</option>
                  <option>Assurance</option><option>Pouvoirs publics</option><option>Autre</option></select>
                  <label for="secteur">Secteur</label></div>
                <div class="fld2"><input id="ctx" name="contexte" type="text" placeholder=" ">
                  <label for="ctx">Votre scénario</label></div>
              </div>
            </div>
          </div>
          <div class="gauge"><u><i id="gi"></i></u><b id="gn">0 / 5</b></div>
          <div class="send">
            <button class="btn btn--fill btn--lg" id="go" type="submit"><span>Demander l’appel de démo</span></button>
            <p>Réponse sous 24 h. Sans engagement.</p>
          </div>
        </form>
        <div class="done" id="done" role="status">
          <div class="done__i">__CHECK__</div>
          <h2 style="font-size:clamp(1.6rem,2.6vw,2.2rem)">Demande enregistrée.</h2>
          <p>Un agent vous appelle sous 24 h au <b id="doneTel">votre numéro</b>.</p>
          <p style="font-size:.88rem;color:var(--muted)">Une confirmation part vers <b id="doneMail">votre e-mail</b>.</p>
        </div>
      </div>
    </div>
  </div>
</section>

</main>

<footer class="foot">
  <div class="wrap">
    <div class="foot__t">
      <div class="foot__b">
        <svg viewBox="0 0 127 127" aria-hidden="true"><use href="#callem-mark"/></svg>
        <p>Des agents vocaux IA, construits et supervisés depuis Paris.</p>
        <p class="adr">Callem SAS · 12 rue de la Voix, 75011 Paris<br>contact@callem.ai</p>
      </div>
      <div><h4>Plateforme</h4><ul>
        <li><a href="#plateforme">Studio d’agents</a></li><li><a href="#plateforme">Base de connaissances</a></li>
        <li><a href="#plateforme">Outils &amp; Workflows</a></li><li><a href="#controle">Supervision</a></li></ul></div>
      <div><h4>Secteurs</h4><ul>
        <li><a href="#secteurs">Finance</a></li><li><a href="#secteurs">Santé</a></li>
        <li><a href="#secteurs">Retail</a></li><li><a href="#secteurs">Assurance</a></li>
        <li><a href="#secteurs">Pouvoirs publics</a></li></ul></div>
      <div><h4>Développeurs</h4><ul>
        <li><a href="https://docs.callem.ai/" target="_blank" rel="noopener">Documentation</a></li>
        <li><a href="https://docs.callem.ai/" target="_blank" rel="noopener">Référence API</a></li>
        <li><a href="https://docs.callem.ai/" target="_blank" rel="noopener">Guide de démarrage</a></li>
        <li><a href="https://docs.callem.ai/" target="_blank" rel="noopener">MCP</a></li></ul></div>
      <div><h4>Légal</h4><ul>
        <li><a href="#">Mentions légales</a></li><li><a href="#">Confidentialité</a></li>
        <li><a href="#">CGU</a></li><li><a href="#">DPA</a></li><li><a href="#">Sous-traitants</a></li></ul></div>
    </div>
    <div class="foot__bar">
      <span>© 2026 Callem — Conçu et hébergé en Europe</span>
      <span class="foot__soc">
        <a href="#" aria-label="X"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 3h3l-6.6 7.5L21.7 21h-6l-4.7-6.1L5.6 21h-3l7-8L2.5 3h6.2l4.2 5.6L17.5 3Z"/></svg></a>
        <a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9h4v12H3V9Zm7 0h3.8v1.7h.05c.53-1 1.83-2.05 3.76-2.05 4.02 0 4.76 2.6 4.76 5.98V21h-4v-5.3c0-1.26-.02-2.9-1.77-2.9-1.77 0-2.04 1.38-2.04 2.8V21h-4V9Z"/></svg></a>
      </span>
    </div>
  </div>
</footer>
__JS__
</body>
</html>
"""

JS = r"""<script>
(function(){
"use strict";
var $ = function(id){ return document.getElementById(id); };
var RM = matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ── révélations : un test de position, pas d'observateur ─────────────── */
var rv = [].slice.call(document.querySelectorAll(".rv")), tick = false;
function sweep(){
  tick = false;
  var h = innerHeight;
  for (var i = rv.length - 1; i >= 0; i--){
    var r = rv[i].getBoundingClientRect();
    if (r.top < h * 0.88 && r.bottom > 0){ rv[i].classList.add("in"); rv.splice(i, 1); }
  }
}
function onScroll(){ if (!tick){ tick = true; requestAnimationFrame(sweep); } }
addEventListener("scroll", onScroll, {passive:true});
addEventListener("resize", onScroll);
sweep(); setTimeout(sweep, 300); setTimeout(sweep, 1200);

/* ── la console du héros joue l'appel en boucle ───────────────────────── */
(function(){
  var scr = $("scr"), clk = $("clk");
  if (!scr) return;
  var lines = [].slice.call(scr.querySelectorAll("#tr li")),
      tools = [].slice.call(scr.querySelectorAll("#tl li")),
      all = lines.concat(tools).map(function(el){ return {el:el, at:+el.getAttribute("data-at")}; }),
      END = 44, t = 0, timer = null;

  function paint(){
    var m = Math.floor(t / 60), s = Math.floor(t % 60);
    clk.textContent = (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s;
    all.forEach(function(o){ o.el.classList.toggle("on", t >= o.at); });
    scr.classList.toggle("on", t >= 8);
  }
  function step(){ t += 1; if (t > END) t = 0; paint(); }
  function play(){ if (!timer && !RM) timer = setInterval(step, 260); }
  function stop(){ clearInterval(timer); timer = null; }

  if (RM){ t = END; paint(); return; }
  paint();
  scr.addEventListener("pointerenter", stop);
  scr.addEventListener("pointerleave", play);
  function check(){
    var r = scr.getBoundingClientRect();
    if (r.bottom > 0 && r.top < innerHeight) play(); else stop();
  }
  addEventListener("scroll", check, {passive:true});
  addEventListener("resize", check);
  check();
})();

/* ── plateforme : clic, clavier, et avance au défilement ──────────────── */
(function(){
  var box = $("steps"), stage = $("shots");
  if (!box || !stage) return;
  var btns = [].slice.call(box.querySelectorAll(".step")),
      shots = [].slice.call(stage.querySelectorAll(".shot")),
      cur = 0;
  function pick(n){
    if (n === cur) return;
    cur = n;
    btns.forEach(function(b, i){ b.setAttribute("aria-selected", i === n ? "true" : "false"); });
    shots.forEach(function(s, i){ s.classList.toggle("on", i === n); });
  }
  btns.forEach(function(b, i){ b.addEventListener("click", function(){ pick(i); }); });

  /* la section avance d'une étape par tiers de sa traversée */
  var sec = document.getElementById("plateforme");
  function follow(){
    if (innerWidth < 981) return;
    var r = sec.getBoundingClientRect(), span = r.height + innerHeight;
    var p = (innerHeight - r.top) / span;
    if (p < 0 || p > 1) return;
    pick(Math.max(0, Math.min(3, Math.floor((p - .18) / .16))));
  }
  addEventListener("scroll", follow, {passive:true});
})();

/* ── contrôle : le caviardage et les barres se lancent à l'arrivée ────── */
(function(){
  var t = $("tri");
  if (!t) return;
  function check(){
    var r = t.getBoundingClientRect();
    if (r.top < innerHeight * .85 && r.bottom > 0){
      t.classList.add("on"); removeEventListener("scroll", check);
    }
  }
  addEventListener("scroll", check, {passive:true}); check();
})();

/* ── formulaire ───────────────────────────────────────────────────────── */
(function(){
  var form = $("form"), brief = $("brief"), go = $("go"), done = $("done"), box = $("demoBox");
  if (!form) return;
  var REQ = ["objectif", "nom", "societe", "email", "telephone"],
      bar = $("gi"), num = $("gn");

  function ok(k, v){
    v = (v || "").trim();
    if (k === "email") return /^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v);
    if (k === "telephone") return v.replace(/[^0-9]/g, "").length >= 9;
    return v.length >= 2;
  }
  function fmt(raw){
    var s = raw.replace(/[^\d+]/g, "");
    s = s.charAt(0) + s.slice(1).replace(/\+/g, "");
    if (s.slice(0, 3) === "+33"){
      var d = s.slice(3).replace(/^0/, "").slice(0, 9);
      return ("+33 " + d.replace(/(\d)(\d{2})(\d{2})(\d{2})(\d{0,2})/, "$1 $2 $3 $4 $5")).trim();
    }
    if (s.charAt(0) === "0") return s.slice(0, 10).replace(/(\d{2})(?=\d)/g, "$1 ").trim();
    if (s.charAt(0) === "+") return ("+" + s.slice(1, 16)).replace(/(\d{3})(?=\d)/g, "$1 ").trim();
    return s.slice(0, 15);
  }
  var tel = form.elements.telephone;
  tel.addEventListener("input", function(){
    var end = tel.selectionStart === tel.value.length, f = fmt(tel.value);
    if (f === tel.value) return;
    tel.value = f;
    if (end) tel.setSelectionRange(f.length, f.length);
  });

  var slots = [].slice.call(brief.querySelectorAll("[data-k]")), PH = {};
  slots.forEach(function(s){ PH[s.getAttribute("data-k")] = s.textContent; });
  function fill(){
    slots.forEach(function(s){
      var k = s.getAttribute("data-k"), f = form.elements[k],
          v = f ? f.value.trim() : "", txt = v || PH[k];
      if (txt !== s.textContent){
        s.textContent = txt;
        s.classList.remove("flash"); void s.offsetWidth; s.classList.add("flash");
        setTimeout(function(){ s.classList.remove("flash"); }, 520);
      }
      s.classList.toggle("empty", !v);
    });
  }
  function gauge(){
    var n = 0;
    REQ.forEach(function(k){
      var f = form.elements[k], good = ok(k, f.value), fld = f.closest(".fld2");
      if (good){ n++; fld.classList.remove("bad"); }
      fld.classList.toggle("ok", good);
    });
    bar.style.width = (n / REQ.length * 100) + "%";
    num.textContent = n + " / " + REQ.length;
    var full = n === REQ.length;
    brief.classList.toggle("ready", full);
    return full;
  }
  form.addEventListener("input", function(){ fill(); gauge(); });
  form.addEventListener("change", function(){ fill(); gauge(); });
  form.querySelectorAll("select").forEach(function(s){
    var sync = function(){ s.toggleAttribute("data-filled", !!s.value); };
    s.addEventListener("change", sync); sync();
  });
  fill(); gauge();

  form.addEventListener("submit", function(e){
    e.preventDefault();
    var good = true;
    REQ.forEach(function(k){
      var f = form.elements[k], v = ok(k, f.value);
      f.closest(".fld2").classList.toggle("bad", !v);
      if (!v) good = false;
    });
    if (!good){ var b = form.querySelector(".bad input, .bad select"); if (b) b.focus(); return; }
    go.classList.add("busy"); go.setAttribute("aria-busy", "true");
    /* TODO — brancher ici l'envoi vers hamzaghouili@callem.ai (fonction serverless) */
    setTimeout(function(){
      $("doneTel").textContent = form.elements.telephone.value.trim();
      $("doneMail").textContent = form.elements.email.value.trim();
      form.style.display = "none";
      done.classList.add("on");
      box.scrollIntoView({block:"center", behavior: RM ? "auto" : "smooth"});
    }, 850);
  });
  form.querySelectorAll("input,select").forEach(function(el){
    el.addEventListener("blur", function(){
      if (REQ.indexOf(el.name) >= 0 && el.value.trim())
        el.closest(".fld2").classList.toggle("bad", !ok(el.name, el.value));
    });
  });

  var more = document.querySelector(".more"), extra = $("extra");
  more.addEventListener("click", function(){
    var open = extra.classList.toggle("on");
    more.setAttribute("aria-expanded", open ? "true" : "false");
    more.querySelector("span").textContent = open ? "Masquer" : "Ajouter un détail";
  });
})();
})();
</script>"""


def main():
    steps, shots, cartes, tales, nums, tous, hero_logos, wv = build_html()
    html = (PAGE
            .replace("__CSS__", CSS)
            .replace("__JS__", JS)
            .replace("__STEPS__", steps).replace("__SHOTS__", shots)
            .replace("__CARTES__", cartes).replace("__TALES__", tales)
            .replace("__NUMS__", nums).replace("__TOUS__", tous)
            .replace("__HERO_LOGOS__", hero_logos).replace("__WV__", wv)
            .replace("__PARIS__", UNSPLASH.format("photo-1499856871958-5b9627545d1a", 1100))
            .replace("__CHECK__", CHECK).replace("__CROSS__", CROSS).replace("__ARROW__", ARROW))
    for k in ("lock", "shield", "eu", "tools", "chat", "test", "live", "alert",
              "transfer", "analytics", "workflow", "kb"):
        html = html.replace("__IC_" + k.upper() + "__", ic("ic-" + k))
    out = ROOT / "build" / "v3.src.html"
    out.write_text(html, encoding="utf-8")
    print(f"✓ build/v3.src.html  ({len(html):,} octets)")


main()
