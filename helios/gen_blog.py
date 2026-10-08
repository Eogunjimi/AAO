#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the blog index page and individual blog post pages.
Run from inside the helios/ directory: python3 gen_blog.py
"""
import os

HEAD_TMPL = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>@TITLE@</title><meta name="description" content="@META_DESC@"><meta name="robots" content="index, follow, max-image-preview:large"><meta property="og:type" content="article"><meta property="og:site_name" content="Access Solar Energy"><meta property="og:locale" content="en_NG"><meta property="og:title" content="@TITLE@"><meta property="og:description" content="@META_DESC@"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="@TITLE@"><meta name="twitter:description" content="@META_DESC@"><link rel="stylesheet" href="css/style.css"></head>
<body>

<div id="preloader"><span class="pre-logo">ACCESS ENERGY</span><span id="preCount">000</span></div>
<div id="cDot"></div><div id="cRing"></div>
<div id="progress"></div>

<div class="utility" id="top">
  <span>MON\u2013SAT 08:00\u201318:00 <span class="u-dot">\u25cf</span> FESTAC, LAGOS</span>
  <span class="u-right"><a href="tel:+2349056977454">(905) 697-7454</a> &nbsp;\u00b7&nbsp; <a href="mailto:accesssolarenergy@gmail.com">accesssolarenergy@gmail.com</a></span>
</div>

<header class="nav">
  <a class="wordmark" href="index.html">ACCESS ENERGY<i>.</i></a>
  <nav class="nav-links" aria-label="Primary">
    <a href="index.html">Home</a>
    <div class="nav-item">
      <a href="about.html" class="nav-top" aria-haspopup="true" aria-expanded="false">About<span class="caret" aria-hidden="true"></span></a>
      <div class="nav-sub">
        <a href="advice.html">Advice</a>
        <a href="systems.html">Systems</a>
        <a href="blog.html"@BLOG_ACTIVE_DESKTOP@>Blog</a>
      </div>
    </div>
    <div class="nav-item">
      <a href="systems.html" class="nav-top" aria-haspopup="true" aria-expanded="false">Services<span class="caret" aria-hidden="true"></span></a>
      <div class="nav-sub">
        <a href="residential-solar-installation.html">Residential Solar Installation</a>
        <a href="commercial-solar-installation.html">Commercial Solar Installation</a>
        <a href="inverter-systems.html">Inverter Systems</a>
        <a href="lithium-battery-storage.html">Lithium Battery Storage</a>
        <a href="energy-consultation.html">Energy Consultations</a>
      </div>
    </div>
    <a href="projects.html">Projects</a>
    <a href="service-areas.html">Locations</a>
    <a href="contact.html">Contact Us</a>
  </nav>
  <div class="nav-cta">
    <a class="nav-wa" href="https://wa.me/2349056977454?text=Hi%20Helios%20%E2%80%94%20I%27d%20like%20a%20quote%20for%20solar%20%2B%20storage." target="_blank" rel="noopener noreferrer" aria-label="Chat with Helios on WhatsApp"><svg class="wa-ico" viewBox="0 0 24 24" width="17" height="17" fill="currentColor" aria-hidden="true" focusable="false"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg></a>
    <a class="pill magnet" href="contact.html#quote">Get A Quote</a>
    <button class="nav-burger" id="navBurger" type="button"
            aria-label="Open menu" aria-expanded="false" aria-controls="mobileMenu">
      <span class="burger-box" aria-hidden="true"><span></span><span></span><span></span></span>
    </button>
  </div>
  <div class="nav-drawer" id="mobileMenu">
    <nav class="md-list" aria-label="Mobile">
      <a class="md-link" href="index.html">Home</a>
    <div class="md-group">
      <div class="md-row">
        <a class="md-link" href="about.html">About</a>
        <button class="md-toggle" type="button" aria-expanded="false"
                aria-controls="mdAbout" aria-label="Show About submenu">
          <span class="caret" aria-hidden="true"></span>
        </button>
      </div>
      <div class="md-sub" id="mdAbout" hidden>
        <a href="advice.html">Advice</a>
        <a href="systems.html">Systems</a>
        <a href="blog.html"@BLOG_ACTIVE_MOBILE@>Blog</a>
      </div>
    </div>
    <div class="md-group">
      <div class="md-row">
        <a class="md-link" href="systems.html">Services</a>
        <button class="md-toggle" type="button" aria-expanded="false"
                aria-controls="mdServices" aria-label="Show Services submenu">
          <span class="caret" aria-hidden="true"></span>
        </button>
      </div>
      <div class="md-sub" id="mdServices" hidden>
        <a href="residential-solar-installation.html">Residential Solar Installation</a>
        <a href="commercial-solar-installation.html">Commercial Solar Installation</a>
        <a href="inverter-systems.html">Inverter Systems</a>
        <a href="lithium-battery-storage.html">Lithium Battery Storage</a>
        <a href="energy-consultation.html">Energy Consultations</a>
      </div>
    </div>
      <a class="md-link" href="projects.html">Projects</a>
      <a class="md-link" href="service-areas.html">Locations</a>
      <a class="md-link" href="contact.html">Contact Us</a>
    </nav>
    <div class="md-foot">
      <a class="pill md-quote" href="contact.html#quote">Get A Quote</a>
      <a class="md-wa" href="https://wa.me/2349056977454?text=Hi%20Helios%20%E2%80%94%20I%27d%20like%20a%20quote%20for%20solar%20%2B%20storage." target="_blank" rel="noopener">Chat on WhatsApp</a>
      <div class="md-contact">
        <a href="tel:+2349056977454">(905) 697-7454</a>
        <a href="mailto:accesssolarenergy@gmail.com">accesssolarenergy@gmail.com</a>
      </div>
    </div>
  </div>
</header>
<div class="nav-scrim" id="navScrim"></div>
<a class="wa-float" href="https://wa.me/2349056977454?text=Hi%20Helios%20%E2%80%94%20I%27d%20like%20a%20quote%20for%20solar%20%2B%20storage." target="_blank" rel="noopener noreferrer"
   aria-label="Chat with Helios on WhatsApp">
  <svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor" aria-hidden="true" focusable="false"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
</a>
"""

FOOTER_TMPL = """
<footer>
  <div class="foot-glow" aria-hidden="true"></div>
  <div class="giant" aria-hidden="true">ACCESS</div>
  <div class="foot-cols">
    <div class="foot-brand">
      <a class="wordmark" href="index.html" style="color:var(--paper)">ACCESS ENERGY<i>.</i></a>
      <p class="blurb">Clean, reliable solar + battery backup, thoughtfully engineered for you. From a passion for renewable energy to a growing family of satisfied homes and businesses \u2014 powered with care, and counting.</p>
      <div class="foot-clock">LAGOS <span id="lagosTime">--:--:--</span> WAT</div>
    </div>
    <div>
      <h5>Menu</h5>
      <a href="index.html">Home</a><a href="systems.html">Services</a><a href="projects.html">Projects</a><a href="service-areas.html">Locations</a><a href="about.html">About</a><a href="advice.html">Advice</a><a href="blog.html">Blog</a><a href="contact.html">Contact</a>
    </div>
    <div>
      <h5>Services</h5>
      <a href="residential-solar-installation.html">Residential Solar Installation</a><a href="commercial-solar-installation.html">Commercial Solar Installation</a><a href="inverter-systems.html">Inverter Systems</a><a href="lithium-battery-storage.html">Lithium Battery Storage</a><a href="energy-consultation.html">Energy Consultations</a>
    </div>
    <div>
      <h5>Social</h5>
      <a href="#">LinkedIn</a><a href="#">Instagram</a><a href="#">Facebook</a><a href="#">YouTube</a><a href="#">X</a>
    </div>
    <div>
      <h5>Contact</h5>
      <a href="mailto:accesssolarenergy@gmail.com">accesssolarenergy@gmail.com</a>
      <a href="tel:+2349056977454">(905) 697-7454</a>
      <a href="contact.html">56 Casco Street, Agboju, Amuwo, Festac, Lagos, 102314</a>
      <p class="foot-line">Mon&ndash;Sat, 08:00&ndash;18:00</p>
      <div class="foot-connect">
        <h5>Connect with us now</h5>
        <a class="pill orange foot-quote magnet" href="contact.html#quote">Get A Free Quote</a>
      </div>
    </div>
  </div>
  <div class="foot-base">
    <div class="fb-legal">
      <span class="foot-c" aria-hidden="true">C</span>
      <div>
        <p class="foot-legal">Unauthorized reproduction or use of our original content is prohibited. ACCESS ENERGY is a registered trading name of Access Energy Limited, Lagos, Nigeria. All system designs, yield models and survey data remain our intellectual property.</p>
        <div class="foot-policy">
          <a href="#">Privacy Policy</a><a href="#">Terms of Service</a><a href="#">Cookie Policy</a><a href="#">Warranty Terms</a>
        </div>
      </div>
    </div>
    <div class="fb-right">
      <div class="foot-meta">
        <span>&copy; 2026 ACCESS ENERGY LTD</span>
        <a href="#top">BACK TO TOP &uarr;</a>
      </div>
      <div class="foot-year" aria-hidden="true">2026</div>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
"""

POSTS = [
    dict(
        slug="how-many-solar-panels-do-i-need",
        tag="SYSTEM SIZING",
        title="How Many Solar Panels Do I Need to Power My Home in Nigeria?",
        excerpt="A practical, no-jargon walkthrough of how we size a solar array \u2014 from your appliance list to the number of panels on your roof.",
        date="OCT 2026",
        read="6 MIN READ",
        image="img/blog/panel-sizing.jpg",
        body="""
<p>It's the first question every homeowner asks, and the honest answer is: it depends on what you actually want to run, not on a fixed "package" size. Panel count is the last number we calculate, not the first \u2014 it falls out of your load, your backup goals and your roof space.</p>
<h2>Start with your load, not your roof</h2>
<p>Before we talk panels, we build a load list: fridge, freezers, lighting, fans, TVs, routers, pumps, and air conditioning if it's in scope. Each appliance has a wattage and a number of hours it typically runs per day. Multiply the two and add them up, and you get your daily energy need in kilowatt-hours (kWh) \u2014 the real number that drives system size.</p>
<h3>A rough guide we use on site</h3>
<ul>
<li>Small apartment, essentials only (lights, fans, TV, router): 3\u20134 kWh/day \u2192 roughly 6\u20138 panels</li>
<li>Standard family home with fridge, freezer and pumping: 6\u201310 kWh/day \u2192 roughly 10\u201316 panels</li>
<li>Larger home or small office with AC on solar: 12\u201320 kWh/day \u2192 roughly 18\u201330 panels</li>
<li>Commercial or industrial loads: sized individually after a full audit</li>
</ul>
<p>These ranges assume good sun hours (Lagos typically sees 4.5\u20135.5 peak sun hours a day) and standard 550\u2013600W panels. Your actual number will shift based on roof orientation, shading, and how much of your load you want to run purely on solar versus topping up from the grid or generator.</p>
<h2>Why we still visit before we quote a number</h2>
<p>Two homes with the same square footage can have wildly different energy needs \u2014 one runs three air conditioners around the clock, the other barely touches its AC. That's why every Access Solar Energy quote starts with a short load assessment, either on a call or on site, before we commit to a panel count, inverter size or battery capacity.</p>
<h2>The takeaway</h2>
<p>If someone quotes you a solar system size before asking what you actually plan to run, be cautious. The right number of panels is the one that matches your appliances, your budget and your backup expectations \u2014 everything else is guesswork.</p>
""",
    ),
    dict(
        slug="hybrid-vs-pure-sine-wave-inverter",
        tag="INVERTERS",
        title="Hybrid Inverter vs Pure Sine Wave Inverter: What's the Difference?",
        excerpt="Not all inverters do the same job. Here's how to tell them apart and which one actually belongs in your home.",
        date="OCT 2026",
        read="5 MIN READ",
        image="img/blog/inverter-types.jpg",
        body="""
<p>"Inverter" gets used as a catch-all term in Nigeria, but the inverter sitting in your passage is doing a very specific job \u2014 and the type you have changes what your system can actually do.</p>
<h2>Pure sine wave inverters</h2>
<p>A pure sine wave inverter takes DC power from a battery and converts it into clean AC power that matches what comes from the grid. It's the baseline requirement for running sensitive electronics \u2014 routers, TVs, laptop chargers, medical equipment \u2014 without the humming, overheating or early failure that cheaper modified-sine inverters can cause. If your current inverter doesn't explicitly say "pure sine wave," it's worth checking.</p>
<h2>Hybrid inverters</h2>
<p>A hybrid inverter does everything a pure sine wave inverter does, plus it manages solar input directly. It can charge your battery from solar panels, draw from the grid or generator when needed, and intelligently switch between sources \u2014 all through one unit instead of a cobbled-together inverter-plus-charge-controller setup. This is what makes a true solar-plus-storage system possible in one coordinated box.</p>
<h3>Quick comparison</h3>
<ul>
<li>Pure sine wave only: clean power, but no solar charging built in</li>
<li>Hybrid: clean power, solar charging, grid/generator management, and smarter battery control</li>
<li>Hybrid units typically support dual MPPT inputs for better solar harvest on multi-angle roofs</li>
<li>Hybrid inverters are the standard spec for any system that includes solar panels</li>
</ul>
<p>If you're only running on batteries with no solar panels planned, a quality pure sine wave inverter paired with a separate charger may be sufficient. The moment solar panels are in the picture, a hybrid inverter is almost always the better long-term choice.</p>
<h2>What we install</h2>
<p>Every Access Solar Energy system is built around a hybrid inverter with dual MPPT, sized to your panel array and battery bank, so your home runs on sunlight first and falls back to the grid only when it has to.</p>
""",
    ),
    dict(
        slug="lithium-vs-lead-acid-batteries",
        tag="BATTERY STORAGE",
        title="Lithium (LFP) vs Lead-Acid Batteries: Which Should You Choose?",
        excerpt="Upfront cost isn't the only number that matters. We break down lifespan, depth of discharge and total cost of ownership.",
        date="SEP 2026",
        read="7 MIN READ",
        image="img/blog/battery-comparison.jpg",
        body="""
<p>Lead-acid batteries are cheaper to buy. Lithium (LFP) batteries are cheaper to own. Both statements are true, and understanding why changes how you should budget for backup power.</p>
<h2>Depth of discharge is the hidden cost</h2>
<p>A lead-acid battery is typically only safe to discharge to about 50% without shortening its lifespan dramatically. An LFP (lithium iron phosphate) battery can be discharged to 80\u201390% regularly without the same damage. That means a 10kWh LFP battery gives you roughly as much usable backup as a 16\u201318kWh lead-acid bank \u2014 you simply need less lithium capacity to get the same night of power.</p>
<h2>Lifespan and replacement cost</h2>
<ul>
<li>Lead-acid (tubular/gel): typically 300\u2013600 full cycles, often needing replacement within 2\u20133 years of daily use</li>
<li>LFP lithium: typically 3,000\u20136,000+ cycles, commonly lasting 8\u201310+ years in daily backup use</li>
<li>Lead-acid requires more floor/wall space for equivalent usable capacity</li>
<li>LFP has no liquid electrolyte to top up and no acid fumes to ventilate</li>
</ul>
<h2>So which one is right for you?</h2>
<p>If your budget is tight and backup needs are occasional, a well-maintained lead-acid bank can still make sense as a starting point. But for anyone experiencing frequent outages and running a battery bank daily \u2014 which describes most of our Lagos clients \u2014 the maths consistently favours lithium once you account for replacement cycles over a 5\u201310 year horizon.</p>
<h2>What we recommend</h2>
<p>We install LFP battery storage as standard on new hybrid systems because it holds up to daily cycling, needs far less maintenance, and keeps delivering close to full capacity years after installation. We're happy to model both options against your actual usage before you decide \u2014 no pressure either way.</p>
""",
    ),
    dict(
        slug="signs-your-inverter-needs-an-upgrade",
        tag="MAINTENANCE",
        title="5 Signs Your Current Inverter System Needs an Upgrade",
        excerpt="If your inverter is doing any of these five things, it's telling you something. Here's what to listen for.",
        date="SEP 2026",
        read="5 MIN READ",
        image="img/blog/inverter-upgrade.jpg",
        body="""
<p>Inverters rarely fail without warning. Most send small signals for months before they finally give up at the worst possible time. Here are the five signs we hear about most often, right before a client calls us.</p>
<h2>1. Backup time keeps shrinking</h2>
<p>If a battery bank that used to carry you through a 4-hour outage now struggles to last 90 minutes, that's rarely the inverter's fault alone \u2014 it usually points to batteries nearing end of life. But an undersized or ageing inverter can make the problem worse by running inefficiently under load.</p>
<h2>2. It hums, clicks or overheats</h2>
<p>Pure sine wave inverters should run quietly. A loud hum, repeated clicking as it switches sources, or a unit that's hot to the touch after normal use are all signs of internal wear or a system working harder than it should.</p>
<h2>3. Sensitive electronics act up</h2>
<p>Routers rebooting, TVs flickering, or chargers behaving oddly when running off the inverter usually means you're on a modified sine wave or failing unit, not a true pure sine wave inverter.</p>
<h2>4. It can't keep up with new appliances</h2>
<p>Added an extra freezer, a pumping system, or more air conditioning since your inverter was installed? Inverters are sized for a specific load; growing your appliance list without reviewing capacity is one of the most common causes of nuisance trips.</p>
<h2>5. No solar integration</h2>
<p>If your inverter can only manage batteries and grid power \u2014 with no way to add solar charging \u2014 you're paying for storage without the free energy that makes a system pay for itself. This is the single biggest upgrade opportunity we see.</p>
<h2>What to do next</h2>
<p>Any one of these on its own might just need monitoring. Two or more together usually means it's worth a proper assessment before the system fails on you. We offer free inverter health checks as part of every energy consultation.</p>
""",
    ),
    dict(
        slug="solar-installation-cost-lagos-2026",
        tag="COSTS",
        title="How Much Does Solar Installation Cost in Lagos in 2026?",
        excerpt="A realistic look at what homeowners and businesses are actually paying for solar, inverter and battery systems this year.",
        date="OCT 2026",
        read="6 MIN READ",
        image="img/blog/cost-guide.jpg",
        body="""
<p>Solar pricing in Nigeria is often quoted as a single number, which is part of why it feels confusing. The truth is cost scales directly with three things: how much power you want to generate, how much you want to store, and the quality of components used.</p>
<h2>The three cost drivers</h2>
<ul>
<li><b>Panel capacity</b> \u2014 priced per kW of solar installed, driven by your daytime and charging load</li>
<li><b>Battery capacity</b> \u2014 priced per kWh of usable storage, driven by your backup-hours target</li>
<li><b>Inverter size and type</b> \u2014 hybrid inverters with dual MPPT cost more than basic units, but unlock solar charging and smarter source management</li>
</ul>
<h2>Realistic ranges we see in Lagos</h2>
<p>Every property is different, but as a general orientation: a small essentials-only hybrid system (lights, fans, router, TV with modest backup) sits at the entry end of the market. A standard family home system that comfortably runs a fridge, freezer, pumping and general appliances with several hours of backup sits in the mid-range. Larger homes or small commercial premises adding air conditioning on solar, or needing a full day of autonomy, move into the higher end. Full commercial and industrial installations are quoted individually after a load audit, since office towers and factories have very different profiles.</p>
<h2>What changes the number the most</h2>
<ul>
<li>Whether you want air conditioning included in your backed-up load</li>
<li>How many hours of autonomy you want without sun or grid</li>
<li>Panel and battery brand \u2014 Tier-1 panels and LFP batteries cost more but last significantly longer</li>
<li>Roof condition and mounting complexity \u2014 ground-mount or structural reinforcement adds cost</li>
</ul>
<h2>Our approach to quoting</h2>
<p>We don't believe in ballpark numbers over the phone that change once we arrive on site. Every Access Solar Energy quote follows a short load assessment, so the number you receive is the number you pay \u2014 itemised, with no surprise additions once installation begins.</p>
""",
    ),
    dict(
        slug="solar-maintenance-checklist",
        tag="MAINTENANCE",
        title="Solar Maintenance Checklist: Keeping Your System Running at Its Best",
        excerpt="A simple, seasonal checklist that keeps your panels, inverter and batteries performing the way they should.",
        date="AUG 2026",
        read="5 MIN READ",
        image="img/blog/maintenance.jpg",
        body="""
<p>Solar systems are low-maintenance compared to generators, but "low-maintenance" doesn't mean "no maintenance." A short routine twice a year keeps performance where it should be and catches small issues before they become expensive ones.</p>
<h2>Panels</h2>
<ul>
<li>Clear visible dust, harmattan haze residue, or bird droppings with a soft brush and water \u2014 avoid abrasive pads</li>
<li>Check for shading from new tree growth or nearby construction that wasn't there at installation</li>
<li>Look for cracked glass, discoloured cells or loose mounting hardware after storms</li>
</ul>
<h2>Inverter</h2>
<ul>
<li>Keep the area around the unit clear and ventilated \u2014 heat buildup shortens component life</li>
<li>Check the display or app for fault codes or repeated source-switching, which can indicate a developing issue</li>
<li>Confirm firmware is up to date if your inverter supports remote monitoring</li>
</ul>
<h2>Batteries</h2>
<ul>
<li>LFP batteries need little manual upkeep \u2014 mainly confirm ventilation and avoid extreme heat exposure</li>
<li>Older lead-acid batteries need regular terminal cleaning and, for flooded types, periodic water top-ups</li>
<li>Track backup duration over time; a noticeable drop is usually the first sign of ageing cells</li>
</ul>
<h2>When to call a professional</h2>
<p>Annual or bi-annual professional inspections catch what a visual check can't \u2014 loose connections, degrading cell balance, or a panel underperforming its rated output. Access Solar Energy clients receive guidance on their specific system at handover, and we're always available for a check-up call if something feels off.</p>
""",
    ),
]


def nav(html, active):
    if active:
        html = html.replace('@BLOG_ACTIVE_DESKTOP@', ' class="on"')
        html = html.replace('@BLOG_ACTIVE_MOBILE@', ' class="on" aria-current="page"')
    else:
        html = html.replace('@BLOG_ACTIVE_DESKTOP@', '')
        html = html.replace('@BLOG_ACTIVE_MOBILE@', '')
    return html


def render_index():
    title = "Blog | Access Solar Energy"
    meta_desc = "Practical guides on solar, inverter and battery systems for Nigerian homes and businesses, from the Access Solar Energy engineering desk."
    head = HEAD_TMPL.replace('@TITLE@', title).replace('@META_DESC@', meta_desc)
    head = nav(head, active=True)

    cards = []
    for p in POSTS:
        cards.append(f'''<a class="blog-card" href="{p['slug']}.html">
        <div class="bc-img"><img src="{p['image']}" alt="{p['title']}" loading="lazy"></div>
        <div class="bc-body">
          <span class="bc-tag">{p['tag']}</span>
          <h3>{p['title']}</h3>
          <p>{p['excerpt']}</p>
          <div class="bc-meta"><span>{p['date']}</span><span>{p['read']}</span></div>
        </div>
      </a>''')

    body = f'''<main>

  <section class="page-hero">
    <span class="crumb">( HOME <i>/</i> BLOG )</span>
    <h1>Blog<span class="dot">.</span></h1>
    <p class="intro">Practical guides on solar, inverter and battery systems \u2014 written by the Access Solar Energy engineering desk for Nigerian homes and businesses.</p>
    <div class="ph-row">
      <span>WRITTEN BY THE <b>ENGINEERING DESK</b></span>
      <span>UPDATED <b>MONTHLY</b></span>
    </div>
  </section>

  <div class="blog-grid">
    {''.join(cards)}
  </div>

</main>'''
    return head + body + FOOTER_TMPL


def render_post(p, idx):
    title = f"{p['title']} | Access Solar Energy Blog"
    meta_desc = p['excerpt']
    head = HEAD_TMPL.replace('@TITLE@', title).replace('@META_DESC@', meta_desc)
    head = nav(head, active=True)

    others = [o for o in POSTS if o['slug'] != p['slug']][:3]
    related = []
    for o in others:
        related.append(f'''<a class="blog-card" href="{o['slug']}.html">
        <div class="bc-img"><img src="{o['image']}" alt="{o['title']}" loading="lazy"></div>
        <div class="bc-body">
          <span class="bc-tag">{o['tag']}</span>
          <h3>{o['title']}</h3>
          <p>{o['excerpt']}</p>
          <div class="bc-meta"><span>{o['date']}</span><span>{o['read']}</span></div>
        </div>
      </a>''')

    body = f'''<main>

  <section class="post-hero">
    <span class="crumb">( HOME <i>/</i> <a href="blog.html">BLOG</a> <i>/</i> {p['tag']} )</span>
    <span class="eyebrow">{p['tag']}</span>
    <h1>{p['title']}</h1>
    <div class="post-meta"><span>{p['date']}</span><span>{p['read']}</span><span>ACCESS SOLAR ENERGY TEAM</span></div>
    <img class="post-cover" src="{p['image']}" alt="{p['title']}">
  </section>

  <article class="post-body">
    {p['body']}
    <div class="post-cta">
      <div><h4>Ready to talk about your project?</h4><p>Get a free assessment and a clear recommendation \u2014 no pressure, no jargon.</p></div>
      <a class="pill" href="contact.html#quote">Get A Free Quote</a>
    </div>
  </article>

  <section class="related-posts">
    <h5>More from the blog</h5>
    <div class="blog-grid" style="padding:0">
      {''.join(related)}
    </div>
  </section>

</main>'''
    return head + body + FOOTER_TMPL


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(out_dir, 'blog.html'), 'w', encoding='utf-8') as f:
        f.write(render_index())
    print('wrote blog.html')
    for i, p in enumerate(POSTS):
        fname = os.path.join(out_dir, f"{p['slug']}.html")
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(render_post(p, i))
        print('wrote', fname)


if __name__ == '__main__':
    main()
