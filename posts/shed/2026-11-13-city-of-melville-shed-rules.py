BODY = """
<h2>When you need a building permit</h2>
<p>In Melville, a freestanding shed needs a building permit if <strong>any</strong> of these apply:</p>
<ul>
<li>The floor area is more than <strong>10 m²</strong></li>
<li>It is more than <strong>2.4 m</strong> high</li>
<li>It's in <strong>wind region C or D</strong></li>
</ul>
<p>The City says a freestanding shed can go right up to the boundary, but must be at least <strong>900 mm from a house wall</strong> or <strong>450 mm from the house eaves</strong> to meet the building code's fire rules. If that can't be done, the shed must be <strong>900 mm from the boundary</strong>.</p>

<h2>When you need planning approval</h2>
<p>In a residential zone, planning approval is usually <strong>not</strong> needed if the shed:</p>
<ul>
<li>Isn't attached to the house, and isn't lived in</li>
<li>Together with other sheds is no more than <strong>60 m² or 10%</strong> of the site, whichever is less</li>
<li>Has walls no higher than <strong>2.4 m</strong> and a ridge no higher than <strong>4.2 m</strong></li>
<li>Isn't in the front or side street setback (6 m at R15 to R25; usually 3 m to a side street)</li>
<li>Is <strong>1 m</strong> from side and rear boundaries (closer may be allowed, so ask the City)</li>
<li>Keeps enough open space (50% at R15 to R25, 45% at R30 to R40, 55% at R12.5)</li>
<li>Isn't on a heritage-listed property</li>
</ul>
<p>In other zones, planning approval is always needed.</p>

<h2>Fees and timeframes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Melville's figure</th></tr></thead><tbody>
<tr><td>Building permit, shed under $20,000</td><td>$166.65</td></tr>
<tr><td>Building permit, over $20,000</td><td>0.19% plus 0.137% levy</td></tr>
<tr><td>Verge bond, work over $20,000</td><td>$1,900 plus $100 inspection fee</td></tr>
<tr><td>Planning approval, under $50,000</td><td>$147</td></tr>
<tr><td>Written planning advice</td><td>$73</td></tr>
<tr><td>BA1 / BA2 decision</td><td>10 / 25 working days</td></tr>
<tr><td>Planning decision</td><td>60 days, or 90 with consultation</td></tr>
</tbody></table></div>
<p>Check your shed with the <a href="/shed-size-checker">shed size checker</a>, or read <a href="/garden-shed-approval">garden shed approval</a> and <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a shed in the City of Melville?",
     "A freestanding shed needs a building permit if it's over 10 m², over 2.4 m high, or in wind region C or D."),
    ("Can I build a shed on the boundary in Melville?",
     "The City says a freestanding shed can go up to the boundary if it's at least 900 mm from a house wall or 450 mm from the eaves. Planning rules may still need 1 m, so check with the City."),
    ("How much is a shed permit in Melville?",
     "$166.65 for a shed under $20,000. Over that, 0.19% plus a 0.137% levy, and a $1,900 verge bond."),
    ("How big can a shed be in Melville without planning approval?",
     "Up to 60 m² or 10% of the site (whichever is less), with walls up to 2.4 m and ridge up to 4.2 m."),
]


def page(S):
    return {"path": "city-of-melville-shed-rules.html", "published": "2026-11-13", "type": "Council guide", "icon": "pin",
            "card": "When a shed in Melville needs a building permit or planning approval, plus fees.",
            "title": "City of Melville Shed Rules (2026)",
            "desc": "City of Melville shed rules: building permit over 10 m² or 2.4 m, planning limits of 60 m² and 4.2 m ridge, boundary rules, fees and timeframes.",
            "eyebrow": "Council guide", "h1": "City of Melville shed rules", "crumb": "Melville shed rules",
            "answer": "<p>In Melville, a freestanding shed needs a <strong>building permit</strong> if it's over <strong>10 m²</strong>, over <strong>2.4 m</strong> high, or in wind region C or D. Planning approval usually isn't needed if it's no more than <strong>60 m²</strong> (or 10% of the site), walls 2.4 m, ridge 4.2 m, and 1 m from side and rear boundaries.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/garden-shed-approval", "Garden shed approval"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?")],
            "sources": [("Building a shed or outbuilding, City of Melville", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding"),
                        ("Planning exemptions, City of Melville", "https://www.melvillecity.com.au/planning-and-building/planning-exemptions")]}
