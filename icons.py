"""Small line icons (24px grid, stroke) and the logo mark."""

PATHS = {
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "doc": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="m9 15 2 2 4-4"/>',
    "shed": '<path d="M3 21V9l9-6 9 6v12"/><path d="M7 21v-8h10v8"/><path d="M7 17h10"/>',
    "garage": '<path d="M3 21V8l9-5 9 5v13"/><path d="M6 21v-9h12v9"/><path d="M6 15h12M6 18h12"/>',
    "pergola": '<path d="M3 7h18"/><path d="M5 4v3M9 4v3M13 4v3M17 4v3"/><path d="M5 7v14M19 7v14"/><path d="M3 21h18"/>',
    "deck": '<path d="M3 14h18"/><path d="M3 18h18"/><path d="M5 14v6M19 14v6"/><path d="M7 10h10"/>',
    "carport": '<path d="M2 7h20"/><path d="M4 7v13M20 7v13"/><path d="M7 17h10l-1.5-4h-7z"/><circle cx="8.5" cy="18.5" r="1"/><circle cx="15.5" cy="18.5" r="1"/>',
    "granny": '<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>',
    "tiny": '<rect x="3" y="6" width="14" height="10" rx="1"/><path d="M17 12h3l1 2v2h-4"/><circle cx="7" cy="18" r="2"/><circle cx="13" cy="18" r="2"/><path d="M7 10h3"/>',
    "pool": '<path d="M2 16c2 0 2-1.5 4-1.5S8 16 10 16s2-1.5 4-1.5 2 1.5 4 1.5 2-1.5 4-1.5"/><path d="M2 20c2 0 2-1.5 4-1.5S8 20 10 20s2-1.5 4-1.5 2 1.5 4 1.5 2-1.5 4-1.5"/><path d="M8 13V5a2 2 0 0 1 4 0M16 13V5a2 2 0 0 0-4 0M8 9h8"/>',
    "retro": '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l3 2"/>',
    "flame": '<path d="M12 22c4 0 7-3 7-7 0-5-5-7-5-12-3 2-5 5-5 8-1-1-2-2-2-4-2 2-2 5-2 8 0 4 3 7 7 7z"/>',
    "wall": '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 10h18M3 14.5h18M8 5v5M15 5v5M11.5 10v4.5M6 14.5V19M17 14.5V19"/>',
    "builder": '<path d="M2 18h20"/><path d="M4 18v-2a8 8 0 0 1 16 0v2"/><path d="M10 9V5h4v4"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "pin": '<path d="M12 22s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "price": '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    "plan": '<path d="M3 3h18v18H3z"/><path d="M3 9h8v12M11 13h10"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    "question": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14"/><path d="M12 17h.01"/>',
    "handshake": '<path d="m11 17 2 2a1 1 0 0 0 1.4 0l4.6-4.6a2 2 0 0 0 0-2.8L15 7.6"/><path d="M9 7 4.6 11.4a2 2 0 0 0 0 2.8L8 17.6"/><path d="M15 7.6 12.5 5a2 2 0 0 0-2.8 0L7 7.7"/><path d="m9 13 3-3"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "car": '<path d="M5 17h14v-4l-2-5H7l-2 5z"/><circle cx="8" cy="17" r="1.6"/><circle cx="16" cy="17" r="1.6"/>',
}


def get(name, size=22):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>') % (size, size, PATHS[name])


def mark(accent, size=30):
    return ('<svg width="%d" height="%d" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#15171c"/>'
            '<path d="M11 9.5h7l4 4v9a1 1 0 0 1-1 1H11a1 1 0 0 1-1-1v-12a1 1 0 0 1 1-1z" fill="none" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/>'
            '<path d="m13 17.6 2 2 4-4" fill="none" stroke="%s" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>') % (size, size, accent)


def favicon(accent):
    """Accent tile with a white page and tick: bold enough to read at 16 px in a browser tab."""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="%s"/>'
            '<path d="M10.5 7.5h7.5l4.5 4.5v11.5a1 1 0 0 1-1 1h-11a1 1 0 0 1-1-1v-15a1 1 0 0 1 1-1z" fill="#fff"/>'
            '<path d="m12.6 17.4 2.6 2.6 4.8-5" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>\n') % (accent, accent)
