# Colour System → Reusable Recolour Prompt

A portable prompt that applies **only this site's colour system** to a different
existing website. Layout, type, spacing and components are explicitly left alone.

Copy everything inside the fenced block into your coding agent and fill in the two
bracketed values at the top.

> For the full visual language — type, shape, motion, component recipes — see
> `DESIGN-SYSTEM-PROMPT.md` instead. This file is the colour layer on its own.

**The one idea worth understanding before you use it.** This is not a palette of
fourteen colours. It is **two base colours and one accent**, plus a set of neutrals
*derived from those bases by alpha*. Change `--ink` and every hairline, border and
muted text colour moves with it, automatically and in tune. That derivation is the
system; the hex values are just one instance of it.

---

```
Recolour an existing website to the palette below. Fill these in first:

  SITE   = [path or URL of the site to recolour]
  ACCENT = [bright accent hex, or keep #A6E060]

=== SCOPE — READ THIS FIRST ===

Change colour only. Do not touch layout, spacing, type sizes, font families,
border-radius, shadows' geometry, breakpoints, markup structure or copy. The only
properties you may edit are: color, background, background-color, background-image
(gradient colour stops only), border-color, outline-color, fill, stroke,
text-decoration-color, caret-color, and the colour components of box-shadow and
text-shadow.

If a colour change would require restructuring markup, stop and report it instead.

=== THE SYSTEM: TWO STACKS AND ONE ACCENT ===

Every surface on the site is either LIGHT or DARK. Classify each one, then apply the
matching stack. Never mix a light-stack text colour onto a dark surface.

LIGHT STACK — page backgrounds, cards, most content
  --paper        #F1F1EC   warm off-white page background
  --card         #FFFFFF   raised surfaces sitting on paper
  --ink          #13251A   primary text, near-black with a green cast
  --mute         ink @ 68% secondary text
  --hair         ink @ 12% hairline borders and dividers
  --hair-strong  ink @ 22% outlined controls, stronger rules

DARK STACK — feature bands, footer, any deep section
  --forest       #1D3A24   the dark surface
  --forest-2     #16301D   a deeper variant for layering within dark
  --paper        #F1F1EC   primary text on dark (the same token, inverted role)
  --paper-soft   paper @ 80% body text on dark
  --paper-mute   paper @ 62% secondary text on dark
  --paper-hair   paper @ 16% hairlines on dark

ACCENT — works on both stacks
  --lime         ACCENT    the single accent
  --lime-2       #C6EF8B   a lighter tint, used only for accent hover

DERIVATION — the neutrals are not independent choices. They are:
  --hair        = ink   at 12% alpha
  --hair-strong = ink   at 22% alpha
  --mute        = ink   at 68% alpha
  --paper-hair  = paper at 16% alpha
  --paper-mute  = paper at 62% alpha
  --paper-soft  = paper at 80% alpha
Recompute all six from your own --ink and --paper. Do not hand-pick greys.

=== ROLE MAP — measured from the source site ===

Use counts show where the weight of the system actually sits. Match this
distribution; a recolour that uses the accent everywhere is not this system.

  --lime    84 uses   color 39 · background 22 · border-color 14
  --ink     69 uses   color 51 · background 9  · border 3
  --paper   47 uses   color 36 · background 10
  --mute    44 uses   color 42
  --hair    30 uses   border 13 · border-bottom 7 · border-top 5
  --paper-mute 21     color 21
  --hair-strong 17    border 9 · background 3
  --paper-hair 16     border-top 4 · border-color 3 · border 3
  --card    14 uses   background 14
  --forest  10 uses   background 10
  --lime-2   3 uses   background 3 (hover only)

Note --paper is used as a text colour far more than as a background (36 vs 10). That
is the inversion at work: on dark sections it is the type colour.

ACCENT DISCIPLINE — the accent is load-bearing but never decorative filler. Allowed:
primary button fills, the active navigation item, small dots and bullets before
eyebrows, focus rings, link and icon hover states, a single emphasised word or
terminal full stop in a heading, and thin progress or underline indicators. Not
allowed: large background panels, body text, or more than one accent element
competing inside the same card.

=== CONTRAST FLOOR — NON-NEGOTIABLE ===

Compute these, do not eyeball them. Every text pair must clear 4.5:1.

  ink / paper                14.18  AAA
  ink / card                 16.06  AAA
  paper / forest             11.01  AAA
  paper-soft(.80) / forest    7.64  AAA
  paper-mute(.62) / forest    5.25  AA
  lime / forest               7.99  AAA
  ink / lime                 10.29  AAA
  mute(.68) / paper           5.31  AA
  mute(.68) / card            5.57  AA

The alpha values are load-bearing. --mute at .60 computes to 4.12:1 on paper and
FAILS; .68 gives 5.31:1 and passes. If you change --ink or --paper, recompute every
pair above before shipping, and adjust the alpha — not the hue — to recover.

Flatten alpha against its actual backdrop before measuring. Measuring an rgba value
against white when it sits on a tinted surface gives a wrong, flattering answer.

=== COLOURS THAT MUST SURVIVE UNCHANGED ===

Do not sweep these into the palette. They are meaningful, not decorative:

1. THIRD-PARTY BRAND MARKS. Google's four-colour G (#FFC107 #FF3D00 #4CAF50
   #1976D2), Facebook blue (#1877F2), and any certification or accreditation badge
   with a fixed identity (e.g. a red shield #E31E24). Recolouring a third-party mark
   misrepresents it and in many cases breaks its usage terms.

2. RATING GOLD (#FBBC04). Star ratings are gold by universal convention. It computes
   1.71:1 on white and fails contrast on purpose, so it must stay decorative — the
   accessible rating is an adjacent numeral in full-contrast ink plus a worded
   label. Never let a gold star be the only carrier of the rating.

3. SEMANTIC STATUS COLOURS if the site has them — error red, success green, warning
   amber. Re-tint them toward the new palette's temperature if you like, but keep
   them distinguishable from each other and from the accent.

=== HANDLING HARD-CODED COLOUR ===

A real site leaks colour outside its token block. The source site had 47 distinct
literals in 54 places even after tokenising. Expect the same and handle each class
deliberately rather than find-and-replacing:

· SHADOWS — near-black tints such as rgba(8,8,10,.14). Retint toward the new ink
  hue, keep the alpha, keep the geometry. Shadows in this system are soft and low
  opacity: 0 18px 40px rgba(ink,.10) at rest, 0 30px 70px rgba(ink,.14) raised.
· IMAGE SCRIMS — gradients like rgba(14,14,12,.92) over photography. Retint to the
  new dark base but preserve every alpha stop, or text over images loses legibility.
· GLASS / TRANSLUCENT BARS — e.g. rgba(246,244,239,.90). Rebuild as the new paper
  colour at the same alpha.
· TEXT STROKE on large outlined display type — rebuild from paper at the same alpha.
· ONE-OFF TINTS that are really palette members in disguise — promote them to tokens
  rather than recolouring them in place.

After the sweep, no colour literal should remain in the stylesheet except the token
definitions, the protected brand marks above, and shadow/scrim alphas.

=== PROCEDURE ===

1. Inventory first. List every colour literal in the stylesheet with its property and
   count, and every colour in markup (inline styles, SVG fill/stroke). Report the
   inventory before changing anything.
2. Classify each surface in the site as light-stack or dark-stack.
3. Define the tokens on :root, deriving the six neutrals by alpha from ink and paper.
4. Replace literals with tokens, surface by surface, leaving the protected list
   intact.
5. Recompute the contrast table and report the numbers.
6. Sweep for leftovers and for any pair that now fails.

=== VERIFICATION — report results, do not just assert them ===

1. Zero colour literals outside :root, except protected brand marks and
   shadow/scrim alphas. Show the count.
2. Every text/background pair computes ≥ 4.5:1. Show the table.
3. No light-stack text colour appears on a dark surface, or vice versa.
4. Focus rings are visible on BOTH stacks — a ring in the accent must be checked
   against the dark surface as well as the light one.
5. Disabled and placeholder text still clears 4.5:1; these are the states most often
   left failing.
6. Third-party marks render in their original colours.
7. Nothing but colour changed: diff should show no edits to layout, spacing, type or
   markup structure.
8. Check the result in both light and dark OS settings if the site declares a
   prefers-color-scheme block.
```

---

## Adapting the palette

**To change the accent only**, replace `--lime` and recompute `--lime-2` as a lighter
tint of it (roughly 18–20% lighter). Then re-verify just two pairs: accent/forest and
ink/accent. Everything else is unaffected, because nothing else derives from the
accent.

**To change the temperature**, move `--ink` and `--paper` together — they share a hue
cast (both lean green here, which is what makes the off-white read warm rather than
grey). Then recompute all six derived neutrals and the whole contrast table.

**A token to drop.** `--ink-2` (`#1B3223`) exists in the source but has **zero uses**.
Don't carry it across; it is dead weight that invites inconsistent greys later.
`--forest-2` and `--paper-soft` are used once each — keep them only if your target
site genuinely has layered dark surfaces and long-form body copy on dark.

**Verifying contrast.** Flatten alpha onto the real backdrop first, then apply the
WCAG relative-luminance formula. Checking an rgba token against white when it
actually sits on `--paper` will over-report by roughly 0.2–0.4, which is enough to
pass something that should fail.
