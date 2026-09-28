# Design System → Reusable Redesign Prompt

This file contains a portable, self-contained prompt that reproduces the visual
language built for this site on **a different, existing website**.

**How to use it:** copy everything inside the fenced block below into your coding
agent, then fill in the four bracketed values at the top. Nothing else needs editing.

**What it is tuned for:** restyling a site that already exists and already has its
copy, pages and information architecture settled. It is deliberately a *skin*, not a
rewrite — the whole premise is that structure and content survive untouched.

**Swappable vs structural.** The accent hue and the dark surface colour are the two
things you can change freely without the system falling apart — swap lime/forest for
any bright-accent-on-deep-neutral pair and the rest still works. The parts that carry
the character, and that you should not casually drop, are: the sentence-case headings
with one italic serif accent word, the lime pill with the dark circular arrow badge,
the dotted eyebrow, and the generous corner radii.

---

```
You are restyling an existing website. Fill these in before you start:

  SITE            = [path or URL of the site to restyle]
  ACCENT          = [bright accent hex, e.g. #A6E060]
  DEEP            = [deep surface hex, e.g. #1D3A24]
  BRAND SPECIFICS = [anything that must be preserved verbatim: logo, legal text,
                     phone numbers, registration numbers]

=== THE ONE RULE THAT OVERRIDES EVERYTHING ===

Change the UI layer only. Preserve the existing content structure and flow exactly:
the same pages, the same sections in the same order, the same copy, the same
information architecture, the same links. You are re-skinning, not rewriting or
reorganising. If a redesign idea requires deleting a section, merging two sections,
cutting copy, or inventing new content, do not do it — the constraint wins.

Never invent facts to fill a layout. No placeholder registration numbers, licence
numbers, certifications, awards, client names, or statistics. If a design pattern
seems to need one, leave it out and say so.

Apply the system across every page as one coherent pass. A page-by-page patch job
that leaves pages inconsistent with each other is a failure, even if each page looks
fine alone.

=== THE FEEL ===

Warm, rounded, confident, modern-agency. Light warm off-white pages with deep
saturated dark sections punctuating them. A single bright accent used sparingly and
always with intent. Generous whitespace, large soft corner radii, soft diffuse
shadows instead of hard borders. Medium-weight sans headings — never ultra-bold,
never thin — with a single italic serif word per heading as the signature move.

=== COLOUR TOKENS ===

Define these as CSS custom properties on :root and use them everywhere. Never
hard-code a colour outside this block.

  --paper        #F1F1EC   page background, warm off-white
  --card         #FFFFFF   raised surfaces
  --ink          #13251A   primary text, near-black with a green cast
  --ink-2        #1B3223   secondary dark
  --forest       DEEP      dark section background
  --forest-2     #16301D   deeper variant for layering
  --lime         ACCENT    the accent
  --lime-2       #C6EF8B   accent hover, a lighter tint
  --gold         #FBBC04   rating stars only

  --hair         rgba(19,37,26,.12)    hairline borders on light
  --hair-strong  rgba(19,37,26,.22)    outlined buttons on light
  --mute         rgba(19,37,26,.68)    secondary text on light
  --paper-hair   rgba(241,241,236,.16) hairline borders on dark
  --paper-mute   rgba(241,241,236,.62) secondary text on dark
  --paper-soft   rgba(241,241,236,.80) body text on dark

Derive the rgba values from your own --ink and --paper if you change them.

CONTRAST FLOOR — verify these by computing them, do not eyeball. Every text pair
must clear 4.5:1. The alpha values above are load-bearing: --mute at .60 computes to
4.12:1 on paper and fails; .68 gives 5.31:1 and passes. If you retune a token,
recompute every pair that uses it.

  ink/paper 14.18 · ink/card 16.06 · paper/forest 11.01 · paper-soft/forest 7.64
  paper-mute/forest 5.25 · lime/forest 7.99 · ink/lime 10.29
  mute/paper 5.31 · mute/card 5.57

--gold is 1.71:1 on white and fails on purpose: stars are decorative only. The
accessible rating must be an adjacent numeral in full-contrast ink plus a worded
label. Never let a gold star be the sole carrier of meaning.

=== TYPOGRAPHY ===

Three families, each with one job:

  --sans   "Inter", "Helvetica Neue", Helvetica, "Segoe UI", Arial, sans-serif
           Everything by default.
  --serif  "Iowan Old Style", "Palatino Linotype", Palatino, Georgia,
           "Times New Roman", serif
           Italic accent words inside headings. Nothing else.
  --mono   "SF Mono", "IBM Plex Mono", "JetBrains Mono", ui-monospace, Menlo,
           Consolas, monospace
           Small caps metadata: timestamps, captions, table labels, utility bars.

Body: 16px / 1.5 / letter-spacing -.005em.

Headings: font-weight 640 — medium, not bold. letter-spacing -.022em. line-height
1.02. Size with clamp() so they scale fluidly, e.g.
clamp(2.6rem, 5.8vw, 5.6rem) for section heads.

SIGNATURE MOVE — in every major heading, wrap exactly one word (occasionally two) in
<em> and style it:

  font-family: var(--serif); font-style: italic; font-weight: 400;
  letter-spacing: -.005em; color: inherit;

Apply that rule to em inside every heading class at once via a grouped selector, so
it can never drift between components. Pick a word that carries meaning — a noun or
qualifier — never an article or preposition.

CASE — headings are sentence case. Buttons are Title Case. Eyebrows are UPPERCASE.
If the existing markup is all-caps text, you must edit the markup: text-transform
cannot undo capitals baked into the source. Keep a protected list so acronyms and
proper nouns survive re-casing (brand names, country/city names, month
abbreviations, "I", unit symbols, and any all-caps product names).

WATCH OUT — a headline sized for tight uppercase will wrap and overflow once
re-cased to sentence case, because lowercase letterforms are wider in aggregate.
Re-measure every headline after re-casing.

=== SHAPE AND DEPTH ===

  --radius     14px   small: inputs, menu items, tags
  --radius-lg  24px   cards, images, media
  --radius-xl  34px   large feature panels
  pills        999px  all buttons, all chips

  --shadow     0 18px 40px rgba(19,37,26,.10)   resting cards
  --shadow-lg  0 30px 70px rgba(19,37,26,.14)   hover and floating panels

Prefer a soft shadow plus a 1px --hair border over a heavy border. Dark sections get
no shadow — separate them by colour alone.

=== LAYOUT ===

Horizontal gutter is 4vw everywhere. Use it relentlessly — it is what makes the site
feel like one system. Do not introduce a fixed max-width content column; this design
is full-bleed and breaks if you centre it in a narrow measure.

Section rhythm: padding 12vh 4vw for major sections, 8vh–9vh for tighter ones.
Twelve-column grid, gap 0 24px, for any multi-column area.

Breakpoints, in this order: 1180 · 1100 · 960 · 820 · 760 · 640 · 560 · 480 · 360.
960px is the main desktop-to-stacked switch.

Heroes and feature bands go edge-to-edge: margin 0, border-radius 0, meeting the
header directly. Keep the inner 4vw padding so text still lines up with the rest of
the page — the surface bleeds, the content does not.

=== COMPONENTS ===

PRIMARY BUTTON — accent pill with a dark circular arrow badge. This is the most
recognisable element in the system; get it exactly right.

  display:inline-flex; align-items:center; gap:14px;
  background:var(--lime); color:var(--ink);
  font:600 13.5px var(--sans); letter-spacing:-.005em;
  padding:7px 7px 7px 22px; border-radius:999px;
  transition:background .22s, color .22s, transform .22s;

  ::after { content:"\2192"; width:32px; height:32px; flex:0 0 32px;
            border-radius:50%; background:var(--ink); color:var(--lime);
            display:grid; place-items:center; font-size:14px; line-height:1;
            transition:transform .25s, background .22s, color .22s; }

  :hover { background:var(--lime-2) }
  :hover::after { transform:translateX(3px) }

Asymmetric padding (22px left, 7px right) is deliberate — it optically centres the
label against the badge.

SECONDARY BUTTON — transparent, 1.5px solid var(--hair-strong), --ink label, same
pill radius and type. On dark surfaces: border --paper-hair, colour --paper.

ICON-ONLY BUTTON — two variants, and keep them consistent if you add more:
  · secondary: transparent, 1.5px solid --hair-strong, glyph via currentColor,
    46px circle stepping to 40px ≤480px and 36px ≤360px, hover inverts to ink fill
    with paper glyph plus scale(1.09)
  · primary: solid accent 48px circle; to collapse a label+badge pill into a single
    circle, override the ::after to width/height 100% on a transparent background
    and force the glyph colour
Icon-only buttons carry an aria-label and no text span. Never attach a
cursor-following transform to a small circular button — it dodges the pointer.

EYEBROW — uppercase micro-label above headings.

  font:600 11px var(--sans); letter-spacing:.14em; text-transform:uppercase;
  color:var(--mute); display:inline-flex; align-items:center; gap:8px;
  margin-bottom:20px;
  ::before { content:""; width:7px; height:7px; flex:0 0 7px;
             border-radius:50%; background:var(--lime); }

On dark surfaces the text becomes --paper-mute; the dot stays accent. If a particular
eyebrow supplies its own leading glyph, suppress the ::before for that one rather
than showing two markers.

NAVIGATION — sentence-case links, 14px / weight 500, padding 8px 14px, radius 999px.
Hover fills with rgba(ink,.06); the active page fills with the accent. Dropdowns open
on :hover AND :focus-within so they work from the keyboard with zero JavaScript.
Include a transparent bridge strip spanning the gap between trigger and panel so the
pointer can cross without the menu closing — and render that bridge only while the
panel is open, or it will silently swallow clicks on whatever sits beneath it.

CARDS — background --card, radius --radius-lg, 1px --hair border, --shadow at rest,
--shadow-lg on hover.

FOOTER — deep surface, asymmetric column grid (roughly 1.9fr 1fr 1.15fr .85fr 1.3fr),
40px gap, collapsing 4-col at 1180 → 2-col at 820 → 1-col at 560. A giant outlined
wordmark or year sits behind the base line; it must be pointer-events:none so it
never blocks the links in front of it.

=== MOTION ===

  [data-reveal]      opacity 0, translateY(26px)
  [data-reveal].in   opacity 1, transform none
  transition         opacity .8s ease, transform .8s cubic-bezier(.2,.65,.2,1)

Hover transitions .22s. Marquees 30s linear infinite, paused on hover.

Always ship this, and mean it:

  @media (prefers-reduced-motion:reduce){
    *,*::before,*::after{ animation:none !important; transition:none !important }
    [data-reveal]{ opacity:1; transform:none }
  }

Any element whose resting state is hidden behind a transform must be forced visible
in that block, or reduced-motion users get a blank page.

=== TRAPS THAT WILL BITE YOU ===

· display:block on a descendant selector blockifies nested inline spans. Scope with >.
· A selector like `.card span:last-child` also matches nested spans that happen to be
  last children, and outranks a plain 3-class rule on specificity. Scope it with > at
  the source instead of escalating with !important.
· text-transform cannot undo capitals in the source. Edit the markup.
· Hard-coded line breaks in a headline are fine on wide screens and orphan single
  words on narrow ones. Below ~640px let the headline reflow as normal text — and if
  the reveal animation is transform-based, disable it there explicitly, because
  transforms do not apply to inline boxes and you must not leave text invisible.
· Huge decorative display numbers need pointer-events:none.
· Size radial gradients in px, not %.
· When adding a sibling to an existing button, set an explicit height and
  box-sizing:border-box or the two will not align.
· backdrop-filter on a sticky header creates a stacking context that can make
  dropdown panels composite oddly. Verify with an unclipped screenshot before
  "fixing" it — clipped screenshot tooling frequently renders this wrong and will
  send you chasing a bug that does not exist.
· body{overflow-x:clip} hides horizontal overflow from
  documentElement.scrollWidth > innerWidth. Measure children against their own
  container's rect instead.

=== ACCEPTANCE CHECKS — run these before declaring done ===

1. Every page uses the system. No page still shows the old treatment.
2. Content diff is UI-only: no section added, removed, reordered or reworded.
3. Every text colour pair computes ≥ 4.5:1. Show the numbers.
4. No horizontal overflow at 360, 390, 480, 640, 768, 960, 1180, 1440, 1920.
5. Keyboard: every interactive element reachable and visibly focused; dropdowns open
   on focus; tab order matches visual order.
6. Icon-only controls have accessible names.
7. prefers-reduced-motion leaves all content visible.
8. No console errors. No broken links, including in-page fragments — and confirm each
   fragment target actually exists rather than assuming.
9. Every heading has exactly one italic serif accent word.
```

---

## Notes on adapting this

**If the target site has a build step** (React, Vue, Tailwind, a CMS theme), the
tokens and component recipes translate directly — express them as theme variables
rather than `:root` custom properties. The rules under *Traps* and *Acceptance
checks* apply unchanged.

**If the target site is content-heavy** (a blog, docs, a store), add a body-copy
measure of `60–75ch` and a `--radius` of `10px` for inline elements; the 34px radius
is for feature panels only and looks clumsy on dense text.

**The contrast table is the part most worth keeping.** Those exact alpha values were
tuned against real measurements — `--mute` in particular sits just above the AA line
and drops below it if you lighten it even slightly.
