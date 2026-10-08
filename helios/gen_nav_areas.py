#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Converts the plain 'Locations' navbar link into a 'Service Areas' mega
dropdown (desktop) / accordion (mobile) across every page on the site.
Run from inside helios/: python3 gen_nav_areas.py
"""
import glob
import re

LAGOS_COL1 = [
    ("festac-amuwo-solar-installation.html", "Festac &amp; Amuwo"),
    ("satellite-town-solar-installation.html", "Satellite Town"),
    ("ikeja-gra-solar-installation.html", "Ikeja GRA"),
    ("lekki-phase-1-solar-installation.html", "Lekki Phase 1"),
    ("lekki-phase-2-solar-installation.html", "Lekki Phase 2"),
    ("ikoyi-solar-installation.html", "Ikoyi"),
    ("victoria-island-solar-installation.html", "Victoria Island"),
]
LAGOS_COL2 = [
    ("surulere-solar-installation.html", "Surulere"),
    ("ajah-solar-installation.html", "Ajah"),
    ("sangotedo-solar-installation.html", "Sangotedo"),
    ("magodo-solar-installation.html", "Magodo"),
    ("yaba-solar-installation.html", "Yaba"),
    ("gbagada-solar-installation.html", "Gbagada"),
    ("epe-solar-installation.html", "Epe"),
]
NATIONWIDE = [
    ("abuja-solar-installation.html", "Abuja"),
    ("port-harcourt-solar-installation.html", "Port Harcourt"),
    ("ibadan-solar-installation.html", "Ibadan"),
    ("kano-solar-installation.html", "Kano"),
    ("enugu-solar-installation.html", "Enugu"),
    ("uyo-solar-installation.html", "Uyo"),
    ("asaba-solar-installation.html", "Asaba"),
]
ALL_AREAS = LAGOS_COL1 + LAGOS_COL2 + NATIONWIDE
ALL_SLUGS = {slug for slug, _ in ALL_AREAS}


def build_desktop(current_file):
    active = current_file in ALL_SLUGS or current_file == "service-areas.html"
    top_class = ' class="nav-top active"' if active else ' class="nav-top"'

    def col(items, label):
        links = []
        for slug, name in items:
            on = ' class="on"' if slug == current_file else ''
            links.append(f'<a href="{slug}"{on}>{name}</a>')
        return f'<div class="nav-sub-col"><span class="nav-sub-label">{label}</span>{"".join(links)}</div>'

    cols = (
        col(LAGOS_COL1, "Lagos")
        + col(LAGOS_COL2, "Lagos, cont&rsquo;d")
        + col(NATIONWIDE, "Nationwide") .replace('</div>', '<a href="service-areas.html" class="nav-sub-all">View All Service Areas &rarr;</a></div>')
    )

    return (
        '<div class="nav-item">'
        f'<a href="service-areas.html"{top_class} aria-haspopup="true" aria-expanded="false">Service Areas'
        '<span class="caret" aria-hidden="true"></span></a>'
        f'<div class="nav-sub mega">{cols}</div>'
        '</div>'
    )


def build_mobile(current_file):
    active = current_file in ALL_SLUGS or current_file == "service-areas.html"
    link_class = ' class="md-link active"' if active else ' class="md-link"'

    links = []
    for slug, name in ALL_AREAS:
        on = ' class="on" aria-current="page"' if slug == current_file else ''
        links.append(f'<a href="{slug}"{on}>{name}</a>')
    links.append('<a href="service-areas.html">View All Service Areas &rarr;</a>')

    return (
        '<div class="md-group">'
        '<div class="md-row">'
        f'<a{link_class} href="service-areas.html">Service Areas</a>'
        '<button class="md-toggle" type="button" aria-expanded="false" '
        'aria-controls="mdAreas" aria-label="Show Service Areas submenu">'
        '<span class="caret" aria-hidden="true"></span>'
        '</button>'
        '</div>'
        f'<div class="md-sub" id="mdAreas" hidden>{"".join(links)}</div>'
        '</div>'
    )


DESKTOP_OLD_RE = re.compile(r'<a href="service-areas\.html"(?: class="active")?>Locations</a>')
MOBILE_OLD_RE = re.compile(r'<a class="md-link(?: active)?" href="service-areas\.html">Locations</a>')


def process(fname):
    s = open(fname, encoding='utf-8').read()
    orig = s

    nav_start = s.find('<nav class="nav-links"')
    nav_end = s.find('</nav>', nav_start) if nav_start != -1 else -1
    if nav_start != -1 and nav_end != -1:
        segment = s[nav_start:nav_end]
        new_segment, n = DESKTOP_OLD_RE.subn(lambda m: build_desktop(fname), segment, count=1)
        if n:
            s = s[:nav_start] + new_segment + s[nav_end:]

    md_start = s.find('<nav class="md-list"')
    md_end = s.find('</nav>', md_start) if md_start != -1 else -1
    if md_start != -1 and md_end != -1:
        segment = s[md_start:md_end]
        new_segment, n = MOBILE_OLD_RE.subn(lambda m: build_mobile(fname), segment, count=1)
        if n:
            s = s[:md_start] + new_segment + s[md_end:]

    if s != orig:
        open(fname, 'w', encoding='utf-8').write(s)
        return True
    return False


def main():
    changed = 0
    missing = []
    for f in sorted(glob.glob('*.html')):
        if process(f):
            changed += 1
        else:
            missing.append(f)
    print(f"updated {changed} files")
    if missing:
        print("no change in:", missing)


if __name__ == '__main__':
    main()
