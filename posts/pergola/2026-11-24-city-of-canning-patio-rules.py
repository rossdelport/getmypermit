BODY = """
<h2>Patio or pergola?</h2>
<p>The City of Canning calls a structure with a <strong>solid roof</strong> a patio or verandah. A <strong>pergola</strong> has an open or open-weave roof, like shade cloth. The rules differ.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>No building permit if</th></tr></thead><tbody>
<tr><td>Patio or verandah</td><td>Freestanding, 10 m² or less and 2.4 m high or less (all three)</td></tr>
<tr><td>Pergola</td><td>20 m² or less and 2.4 m high or less</td></tr>
</tbody></table></div>
<p>So any attached patio needs a permit. Exempt structures must still meet the building rules, local laws and planning policies.</p>

<h2>Setbacks and height</h2>
<ul>
<li><strong>Front:</strong> no closer to the street than the R-Codes front setback for your density.</li>
<li><strong>Corner lots:</strong> at least <strong>1.5 m</strong> from the secondary street.</li>
<li><strong>Side and rear:</strong> at least <strong>900 mm</strong>. Or the roof can be <strong>500 mm</strong> away with posts on the boundary, if you send a fire performance solution with the application.</li>
<li><strong>Height:</strong> posts up to <strong>2.7 m</strong>.</li>
</ul>

<h2>Open space</h2>
<p>You must keep the R-Codes minimum open space. A patio that's open on two sides counts as open space, up to 10% of the site area or 50 m² of roof, whichever is less. Check yours with the <a href="/patio-open-space-checker">open space checker</a>.</p>

<h2>What to send</h2>
<ul>
<li><strong>BA1:</strong> a Certificate of Design Compliance from a registered building surveyor and the plans it lists. Decided within <strong>10 working days</strong>.</li>
<li><strong>BA2:</strong> a 1:200 site plan with boundaries, other buildings and floor level against the house, plus 1:100 floor plans and elevations with structural details. Decided within <strong>25 working days</strong>.</li>
</ul>
<p>You may need a structural engineer to sign off the design. Owner-builders can build a patio. Check drainage easements with the City's Engineering Services first. Building Services is on 1300 422 664.</p>
<p>See <a href="/patio-on-boundary-wa">patios on the boundary</a> and <a href="/patio-engineering-wa">patio engineering</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in the City of Canning?",
     "Yes, unless it's freestanding, 10 m² or less and no more than 2.4 m high. Every attached patio needs a permit."),
    ("How close to the boundary can a patio be in Canning?",
     "At least 900 mm from side and rear boundaries, or 500 mm for the roof with posts on the boundary if you include a fire performance solution."),
    ("How high can a patio be in Canning?",
     "Patio posts can be up to 2.7 m high."),
    ("Does a pergola need a permit in Canning?",
     "Not if it's 20 m² or less and no more than 2.4 m high."),
]


def page(S):
    return {"path": "city-of-canning-patio-rules.html", "published": "2026-11-24", "type": "Council guide", "icon": "pin",
            "card": "City of Canning patio rules: permits, 900 mm setbacks, the 2.7 m post height and open space.",
            "title": "City of Canning Patio and Pergola Rules (2026)",
            "desc": "City of Canning patio and pergola rules: when you need a building permit, front, side and corner setbacks, boundary posts, the 2.7 m post height, open space and what to send.",
            "eyebrow": "Council guide", "h1": "City of Canning patio and pergola rules", "crumb": "Canning patio rules",
            "answer": "<p>In the City of Canning, a patio needs a <strong>building permit</strong> unless it's freestanding, 10 m² or less and 2.4 m or lower. Patios usually sit at least <strong>900 mm</strong> from side and rear boundaries, with posts up to <strong>2.7 m</strong> high. Pergolas up to 20 m² and 2.4 m high don't need a permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-on-boundary-wa", "Patio on the boundary"), ("/patio-open-space-checker", "Patio open space checker"), ("/patio-engineering-wa", "Patio engineering")],
            "sources": [("Building information sheet: patios (BIS-05), City of Canning", "https://cdn.canning.wa.gov.au/media/ifhnevrc/bis-05-information-sheet-patios-update.pdf"),
                        ("Building information sheet: work where a building permit is not required (BIS-03), City of Canning", "https://cdn.canning.wa.gov.au/media/2ghei4nv/bis-03-information-sheet-work-where-a-building-permit-is-not-required.pdf")]}
