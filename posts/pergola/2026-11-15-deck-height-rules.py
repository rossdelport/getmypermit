BODY = """
<h2>The 500 mm line</h2>
<p>For planning approval, the number that matters is <strong>500 mm</strong>, measured from <strong>natural ground level</strong> to the top of the deck. Natural ground is the level of the land before any digging or filling, not the height of your lawn after landscaping.</p>
<div class="table-wrap"><table>
<thead><tr><th>Deck height</th><th>Planning approval (single house)</th></tr></thead><tbody>
<tr><td>500 mm or less</td><td>Not needed</td></tr>
<tr><td>Over 500 mm, meets setbacks and privacy rules</td><td>Usually not needed</td></tr>
<tr><td>Over 500 mm, doesn't meet them</td><td>Needed</td></tr>
</tbody></table></div>

<h2>What a raised deck has to meet</h2>
<p>Once a deck is over 500 mm, it can look into your neighbours' yards, so privacy rules kick in. The City of Joondalup's rules are a good example:</p>
<ul>
<li><strong>Privacy screen:</strong> if the deck is within <strong>7.5 m</strong> of a side or rear boundary, it needs a fixed screen at least <strong>1.6 m</strong> high above the deck surface.</li>
<li><strong>Setbacks at R20:</strong> 1 m from side and rear boundaries for a deck 10 to 14 m long with a privacy screen; 1.5 m if it's longer than 14 m or has no screen.</li>
<li><strong>Higher codes</strong> (R20/25 to R20/60): 1 m.</li>
</ul>
<p>The City of Vincent uses the same 7.5 m distance or 1.6 m screen for raised floors over 0.5 m at R50 and below. Councils vary, and structure plans can add rules.</p>

<h2>Building permit: councils differ</h2>
<p>The building permit side isn't the same everywhere:</p>
<ul>
<li><strong>City of Wanneroo:</strong> every deck needs a building permit, whatever its height or size.</li>
<li><strong>City of Joondalup:</strong> a deck needs a permit if it's over <strong>20 m²</strong>, higher than <strong>500 mm</strong>, less than <strong>900 mm</strong> from a boundary, in a bushfire-prone area, or has privacy screens.</li>
</ul>
<p>So a deck that's 500 mm or higher will need a building permit in both. Check with your own council before you build.</p>

<h2>Lower is simpler</h2>
<p>If you can keep the deck at or under 500 mm, you usually avoid planning approval and privacy screens. If your block slopes, measure from natural ground at the highest point of the deck, because that's where it sits furthest above the land.</p>
<p>See what the permit will cost with <a href="/deck-permit-cost">deck permit cost</a>, or read the <a href="/city-of-joondalup-patio-rules">City of Joondalup patio rules</a>.</p>
"""

FAQS = [
    ("How high can a deck be without council approval in WA?",
     "Planning approval usually isn't needed for a deck 500 mm or less above natural ground. A building permit may still be needed: Wanneroo needs one for every deck, Joondalup for decks over 20 m², over 500 mm or within 900 mm of a boundary."),
    ("Where do you measure deck height from?",
     "From natural ground level, which is the level of the land before any excavation or fill, to the deck surface."),
    ("Does a raised deck need a privacy screen?",
     "In Joondalup, a deck over 500 mm within 7.5 m of a side or rear boundary needs a fixed screen at least 1.6 m high. Other councils use similar rules."),
    ("Can a raised deck go near the boundary?",
     "At R20 in Joondalup, a raised deck needs 1 m from side and rear boundaries if it's 10 to 14 m long with a screen, or 1.5 m if longer or unscreened. Councils vary."),
]


def page(S):
    return {"path": "deck-height-rules.html", "published": "2026-11-15", "type": "Question answer", "icon": "deck",
            "card": "The 500 mm rule for decks, privacy screens, setbacks and when a building permit is needed.",
            "title": "How High Can a Deck Be Before It Needs Approval in WA?",
            "desc": "Deck height rules in WA: no planning approval at 500 mm or less above natural ground, privacy screens and setbacks above that, and when councils need a building permit.",
            "eyebrow": "Question answer", "h1": "How high can a deck be before it needs approval?", "crumb": "Deck height rules",
            "answer": "<p>A deck <strong>500 mm or less</strong> above natural ground usually doesn't need <strong>planning approval</strong>. Above 500 mm it must meet setbacks and have a <strong>1.6 m privacy screen</strong> if it's within 7.5 m of a side or rear boundary. A <strong>building permit</strong> may be needed at any height, depending on your council.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/deck-permit-cost", "Deck permit cost"), ("/city-of-joondalup-patio-rules", "City of Joondalup patio rules"), ("/patio-approval-checker", "Patio approval checker")],
            "sources": [("Decks, City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/decks"),
                        ("Decking, City of Wanneroo", "https://www.wanneroo.wa.gov.au/directory_record/328/decking"),
                        ("Planning information sheet: patios, City of Vincent", "https://vincent.wa.gov.au/Profiles/vincent/Assets/ClientData/Planning_Information_Sheets/2024/Planning_Information_Sheet_Patios_May2024.pdf")]}
