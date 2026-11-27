BODY = """
<h2>Caravan or building?</h2>
<p>The Shire of Bridgetown-Greenbushes says a "tiny home" isn't its own legal category. It must be one or the other, never both:</p>
<div class="table-wrap"><table>
<thead><tr><th>If your tiny home is…</th><th>It's treated as…</th><th>Approvals usually needed</th></tr></thead><tbody>
<tr><td>On wheels and can be towed</td><td>A caravan</td><td>Public health</td></tr>
<tr><td>Fixed and permanent</td><td>A building</td><td>Planning, building and public health</td></tr>
<tr><td>Changed, such as wheels taken off</td><td>A building</td><td>Planning, building and public health</td></tr>
</tbody></table></div>
<p>Being on wheels alone doesn't make it a caravan. It must really be a vehicle used for transport. Check yours with the <a href="/caravan-or-building-checker">caravan or building checker</a>.</p>

<h2>Living in a tiny home on wheels</h2>
<ul>
<li><strong>Up to 5 nights:</strong> with the property owner's OK.</li>
<li><strong>Up to 24 months:</strong> with Shire approval. Conditions may apply.</li>
<li><strong>Permanently:</strong> no. Caravans can't be lived in permanently outside a licensed caravan park.</li>
<li><strong>One per lot:</strong> the Shire won't approve more than one caravan for living in on a single lot.</li>
<li><strong>While you build a house:</strong> often allowed for a time, with public health approval for water, wastewater and power.</li>
</ul>
<p>A caravan doesn't need a building permit, but a patio or other structure built next to it may. Plan your dates with the <a href="/tiny-home-stay-calculator">stay calculator</a>.</p>

<h2>Fixed tiny homes</h2>
<p>A fixed tiny home is a building. It must meet the National Construction Code and get a building permit, and it may need development approval depending on its use and the zoning. There's no minimum size, but it must be fit to live in. A ready-made tiny home must be approved <strong>before</strong> it's installed. See <a href="/fixed-tiny-home-permit">fixed tiny home permits</a>.</p>
<p>It may be approved as a house, a granny flat (if there's already an approved house on the lot), or short-term rental accommodation, which always needs development approval.</p>

<h2>Water, wastewater and power</h2>
<p>Every place people live, caravan or building, needs approved wastewater disposal and a safe water supply. A safe power supply is usually needed too. Tents aren't supported for any kind of accommodation.</p>
"""

FAQS = [
    ("Can I live in a tiny home on wheels in Bridgetown?",
     "For up to 5 nights with the owner's OK, or up to 24 months with Shire approval. Living in one permanently outside a caravan park isn't allowed."),
    ("Does a tiny home need a building permit in Bridgetown-Greenbushes?",
     "Only if it's treated as a building, for example fixed in place or with the wheels taken off. A genuine caravan doesn't, but a patio next to it may."),
    ("How many tiny homes on wheels can I have on one lot in Bridgetown?",
     "One. The Shire says it won't approve more than one caravan for living in on a single lot."),
    ("Can I live in a caravan while I build in Bridgetown?",
     "Usually yes, for a time, if you have public health approval for water, wastewater and power."),
]


def page(S):
    return {"path": "shire-of-bridgetown-greenbushes-tiny-homes.html", "published": "2026-11-28", "type": "Council guide", "icon": "pin",
            "card": "Shire of Bridgetown-Greenbushes tiny homes: caravan or building, the 24-month limit, one per lot and services.",
            "title": "Shire of Bridgetown-Greenbushes Tiny Home Rules (2026)",
            "desc": "Tiny home rules in the Shire of Bridgetown-Greenbushes: caravan or building, staying up to 5 nights or 24 months, one caravan per lot, fixed tiny home permits, short-term rental and services.",
            "eyebrow": "Council guide", "h1": "Shire of Bridgetown-Greenbushes tiny home rules", "crumb": "Bridgetown-Greenbushes tiny homes",
            "answer": "<p>In the Shire of Bridgetown-Greenbushes, a tiny home on wheels is a <strong>caravan</strong>. You can stay up to <strong>5 nights</strong> with the owner's OK, or up to <strong>24 months</strong> with Shire approval, and only <strong>one</strong> per lot. A fixed tiny home is a <strong>building</strong> and needs a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/caravan-or-building-checker", "Caravan or building checker"), ("/tiny-home-stay-calculator", "Tiny home stay calculator"), ("/fixed-tiny-home-permit", "Fixed tiny home permit")],
            "sources": [("Tiny homes, caravans and short-term accommodation, Shire of Bridgetown-Greenbushes", "https://www.bridgetown.wa.gov.au/tiny-homes-caravans-and-short-term-accommodation.aspx"),
                        ("Tiny house fact sheet, Government of WA", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf")]}
