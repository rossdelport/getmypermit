BODY = """
<h2>It depends on the wheels</h2>
<p>In WA, a tiny home is either a <strong>caravan</strong> (on wheels and built to be towed) or a <strong>building</strong> (no wheels). They follow different laws. Not sure which yours is? Use the <a href="/caravan-or-building-checker">caravan or building checker</a>.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Tiny home on wheels</th><th>Fixed tiny home</th></tr></thead><tbody>
<tr><td>Treated as</td><td>A caravan</td><td>A granny flat (or the main house)</td></tr>
<tr><td>Building permit</td><td>Not needed</td><td>Always needed</td></tr>
<tr><td>Planning approval</td><td>Generally not needed</td><td>Not needed if it meets the R-Codes</td></tr>
<tr><td>How long you can live in it</td><td>5 nights in 28 days, or up to 24 months with council approval</td><td>Permanently</td></tr>
<tr><td>Size limit</td><td>Must still be towable</td><td>70 m² as a granny flat</td></tr>
</tbody></table></div>

<h2>Tiny home on wheels in the backyard</h2>
<p>Under the state's caravan regulations:</p>
<ul>
<li>Someone can stay in it for up to <strong>5 nights in any 28 days</strong> with the landowner's OK.</li>
<li>For longer, your <strong>council</strong> can approve up to <strong>24 months in a row</strong>. It can ask for power, water, sewage and cooking facilities. If it hasn't decided within <strong>63 days</strong>, the application is treated as refused.</li>
<li>After 24 months you need to apply again. It can't be lived in permanently outside a caravan park.</li>
<li>Only <strong>one</strong> caravan can be used for camping on a lot at a time unless approved.</li>
<li>It has to keep its wheels and be able to be moved within 24 hours of disconnecting services.</li>
</ul>

<h2>Fixed tiny home in the backyard</h2>
<p>Take the wheels off (or build it on footings) and it's a <strong>building</strong>. Behind an existing house, it's usually a <strong>granny flat</strong> (ancillary dwelling):</p>
<ul>
<li>Up to <strong>70 m²</strong>, one per lot, with <strong>no minimum lot size</strong>.</li>
<li>No planning approval if it meets all the standard R-Codes rules (setbacks, site cover, height, privacy, parking).</li>
<li>A <strong>building permit</strong> and full National Construction Code compliance.</li>
<li>It can be lived in by family, friends or tenants.</li>
</ul>
<p>Some councils add their own rules. For example, in the Rockingham city centre a granny flat must sit behind the main house and match its materials. Councils vary, so check yours, or read our <a href="/city-of-rockingham-tiny-homes">City of Rockingham tiny home guide</a>.</p>

<h2>Which is right for you?</h2>
<p>If you want it there <strong>for good</strong>, a fixed tiny home approved as a granny flat is the only permanent option. A tiny home on wheels suits a stay of up to 24 months at a time, such as while you build a house. See <a href="/live-in-caravan-on-own-land-wa">living in a caravan on your own land</a> for more on the 24-month approval.</p>
"""

FAQS = [
    ("Can I put a tiny home in my backyard in Perth?",
     "Yes. A fixed tiny home can be approved as a granny flat up to 70 m² with a building permit. A tiny home on wheels can stay up to 5 nights in 28 days, or up to 24 months with council approval."),
    ("Can someone live permanently in a tiny home on wheels in my backyard?",
     "No. A tiny home on wheels is a caravan, and caravans can't be lived in permanently outside a caravan park. Council can approve up to 24 months at a time."),
    ("Do I need a building permit for a tiny home in my backyard?",
     "A fixed tiny home always needs one. A genuine towable tiny home on wheels doesn't, because it's a caravan."),
    ("Can I rent out a tiny home in my backyard?",
     "A fixed tiny home approved as a granny flat can be rented to anyone. Ask your council about renting a tiny home on wheels, as it needs their approval to be lived in long term."),
]


def page(S):
    return {"path": "tiny-home-in-backyard-perth.html", "published": "2026-11-16", "type": "Question answer", "icon": "tiny",
            "card": "The rules for a tiny home on wheels or a fixed tiny home in a Perth backyard.",
            "title": "Can I Put a Tiny Home in My Backyard in Perth?",
            "desc": "Can you put a tiny home in your backyard in Perth? Rules for tiny homes on wheels (5 nights or 24 months) and fixed tiny homes as granny flats (70 m², building permit).",
            "eyebrow": "Question answer", "h1": "Can I put a tiny home in my backyard in Perth?", "crumb": "Tiny home in the backyard",
            "answer": "<p>Yes. A <strong>fixed</strong> tiny home can be approved as a <strong>granny flat</strong> up to 70 m², with a building permit, and lived in permanently. A tiny home <strong>on wheels</strong> is a caravan: up to <strong>5 nights in 28 days</strong> with the owner's OK, or up to <strong>24 months</strong> with council approval.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/caravan-or-building-checker", "Caravan or building checker"), ("/live-in-caravan-on-own-land-wa", "Living in a caravan on your own land"), ("/city-of-rockingham-tiny-homes", "City of Rockingham tiny homes")],
            "sources": [("Tiny houses fact sheet, December 2024 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf"),
                        ("Temporary accommodation and camping outside of caravan parks, WA Government", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks"),
                        ("Ancillary dwelling information sheet, WA Planning", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf")]}
