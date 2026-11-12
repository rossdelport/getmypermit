BODY = """
<h2>Building permit rules</h2>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>Needs a building permit if</th></tr></thead><tbody>
<tr><td>Patio</td><td>Attached to the house (any size), or freestanding and over 10 m², over 2.4 m high, or in wind region C or D</td></tr>
<tr><td>Pergola</td><td>Over 2.4 m high, over 20 m², or in wind region C or D</td></tr>
<tr><td>Shade sail</td><td>Attached to the house (any size), or freestanding and over 10 m², over 2.4 m high, or in wind region C or D</td></tr>
<tr><td>Vergola (louvre roof)</td><td>Treated as a patio</td></tr>
</tbody></table></div>
<p>The City says a freestanding patio should be at least <strong>900 mm</strong> from the house and <strong>900 mm</strong> from the boundary, to meet the building code's fire rules.</p>

<h2>Planning approval</h2>
<p>In a residential zone, a patio usually doesn't need planning approval if:</p>
<ul>
<li>It's set back <strong>3 m</strong> from the front street and <strong>1.5 m</strong> from a side street</li>
<li>The eaves are no higher than <strong>3 m</strong> and the ridge no higher than <strong>3.5 m</strong></li>
<li>It's open on at least <strong>two sides</strong>, and open where it's next to a boundary</li>
<li>It covers no more than <strong>two-thirds</strong> of the main outdoor living area</li>
<li>Posts within 1 m of a side boundary are OK if all structures on that boundary total less than <strong>9 m</strong></li>
</ul>
<p><strong>Pergolas and shade sails</strong> don't need planning approval unless the property is heritage listed. In other zones, planning approval is always needed.</p>

<h2>Fees and timeframes</h2>
<ul>
<li>Building permit under $20,000: <strong>$166.65</strong>. Over $20,000: 0.19% plus a 0.137% levy.</li>
<li>Verge bond for work over $20,000: <strong>$1,900</strong> plus a $100 inspection fee.</li>
<li>Planning approval under $50,000: <strong>$147</strong>.</li>
<li>Decisions: BA1 in 10 working days, BA2 in 25. Planning in 60 days, or 90 with consultation.</li>
</ul>
<p>Read <a href="/city-of-wanneroo-patio-rules">City of Wanneroo patio rules</a>, <a href="/shade-sail-approval-wa">shade sail approval</a> or <a href="/louvre-roof-approval">louvre roof approval</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in Melville?",
     "Yes if it's attached to the house. A freestanding patio needs one if it's over 10 m², over 2.4 m high, or in wind region C or D."),
    ("Does a pergola need approval in Melville?",
     "Only a building permit if it's over 2.4 m high, over 20 m², or in wind region C or D. No planning approval unless the property is heritage listed."),
    ("How close to the front can a patio be in Melville?",
     "3 m from the front street and 1.5 m from a side street without planning approval. Closer may be possible, so ask the City."),
    ("How much is a patio permit in Melville?",
     "$166.65 for work under $20,000. Over that, 0.19% plus a 0.137% levy, and a $1,900 verge bond."),
]


def page(S):
    return {"path": "city-of-melville-patio-rules.html", "published": "2026-11-13", "type": "Council guide", "icon": "pin",
            "card": "When patios, pergolas, vergolas and shade sails in Melville need approval, plus fees.",
            "title": "City of Melville Patio, Pergola and Shade Sail Rules (2026)",
            "desc": "City of Melville patio rules: when patios, pergolas, vergolas and shade sails need a building permit or planning approval, setbacks, fees and timeframes.",
            "eyebrow": "Council guide", "h1": "City of Melville patio rules", "crumb": "Melville patio rules",
            "answer": "<p>In Melville, every <strong>attached patio</strong> needs a building permit. A freestanding patio or shade sail needs one if it's over <strong>10 m²</strong> or <strong>2.4 m</strong> high; a pergola if it's over <strong>20 m²</strong> or 2.4 m. Planning approval usually isn't needed if the patio is <strong>3 m</strong> from the front street and open on two sides.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/city-of-wanneroo-patio-rules", "City of Wanneroo patio rules"), ("/shade-sail-approval-wa", "Shade sail approval in WA"), ("/louvre-roof-approval", "Louvre roof approval")],
            "sources": [("Building a patio, pergola, vergola or shade sail, City of Melville", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-patio,-pergola-or-shade-sail"),
                        ("Planning exemptions, City of Melville", "https://www.melvillecity.com.au/planning-and-building/planning-exemptions")]}
