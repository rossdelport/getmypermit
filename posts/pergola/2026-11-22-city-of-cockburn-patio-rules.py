BODY = """
<h2>Patio or pergola? It changes the rules</h2>
<p>The City of Cockburn treats a structure with a solid roof (Colorbond or polycarbonate) as a <strong>patio</strong>. An open roof or shade cloth makes it a <strong>pergola</strong>.</p>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>Building permit needed if</th></tr></thead><tbody>
<tr><td>Patio attached to the house, garage or another building</td><td>Always</td></tr>
<tr><td>Freestanding patio</td><td>Over 10 m², or over 2.4 m high</td></tr>
<tr><td>Pergola (open or shade cloth roof)</td><td>Over 20 m², or over 2.4 m high</td></tr>
<tr><td>Shade sail</td><td>Always, with a structural engineer's design for the posts, footings and fixings</td></tr>
</tbody></table></div>
<p>A shade sail made of waterproof fabric counts as a patio.</p>

<h2>Distances Cockburn asks for</h2>
<ul>
<li>A <strong>freestanding</strong> patio must be at least <strong>900 mm</strong> from the house.</li>
<li>A patio <strong>attached</strong> to the house must be at least <strong>900 mm</strong> from a side or rear boundary, for fire safety.</li>
<li>To build closer, you need a fire engineer's certified performance solution, or a fire-rated wall (FRL 60/60/60).</li>
</ul>
<p>These are building code rules. The R-Codes (planning rules) are separate, and a patio that breaks them, for example by eating into the open space your lot needs, may need planning approval too.</p>

<h2>What to lodge</h2>
<ul>
<li>A BA1 or BA2 form signed by <strong>all owners</strong> and the builder.</li>
<li>Two copies of a site plan at 1:200 or larger, showing the house, other buildings, setbacks to boundaries and the patio's size.</li>
<li>Two copies of elevations and a cross-section at 1:100, showing roof pitch, footing size, how it attaches to the house, the roof sheeting and the height.</li>
<li>A floor plan at 1:100 if needed, plus the fee and state levies.</li>
</ul>
<p>If you need planning approval, get it before you lodge the building permit. Even a patio that doesn't need a building permit can still need planning approval. The City decides a BA1 in 10 business days and a BA2 in 25, and offers free pre-lodgement meetings (9411 3608).</p>
<p>Read <a href="/attached-vs-freestanding-patio">attached vs freestanding patios</a>, <a href="/patio-on-boundary-wa">putting a patio on the boundary</a>, or <a href="/shade-sail-approval-wa">shade sail approval</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in Cockburn?",
     "Yes if it's attached to the house. A freestanding patio needs one if it's over 10 m² or over 2.4 m high."),
    ("Do I need a permit for a pergola in Cockburn?",
     "Only if it's over 20 m² or over 2.4 m high, and only if it has an open or shade cloth roof. A solid roof makes it a patio."),
    ("How close to the boundary can an attached patio be in Cockburn?",
     "900 mm, unless a fire engineer certifies a closer design or you build a fire-rated wall."),
    ("Does a shade sail need a permit in Cockburn?",
     "Yes. The City needs plans and a structural engineer's certification for the posts, footings and fixings."),
]


def page(S):
    return {"path": "city-of-cockburn-patio-rules.html", "published": "2026-11-22", "type": "Council guide", "icon": "pin",
            "card": "City of Cockburn patio rules: patio vs pergola, the 900 mm rule, shade sails and what to lodge.",
            "title": "City of Cockburn Patio and Pergola Rules (2026)",
            "desc": "City of Cockburn patio and pergola rules: when you need a building permit, the 900 mm boundary rule for attached patios, shade sails, and the plans to lodge.",
            "eyebrow": "Council guide", "h1": "City of Cockburn patio rules", "crumb": "City of Cockburn patio rules",
            "answer": "<p>In Cockburn, every <strong>attached</strong> patio needs a building permit, and a freestanding one does if it's over <strong>10 m²</strong> or <strong>2.4 m</strong> high. Open pergolas get more room: <strong>20 m²</strong>. An attached patio must usually be <strong>900 mm</strong> from the boundary, and shade sails always need a permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/attached-vs-freestanding-patio", "Attached vs freestanding patio"), ("/patio-on-boundary-wa", "Patio on the boundary"), ("/shade-sail-approval-wa", "Shade sail approval")],
            "sources": [("Pergolas, sheds, shade sails and water tanks, City of Cockburn", "https://www.cockburn.wa.gov.au/Building-Planning-and-Roads/Applications-and-Permits/Pergolas-Sheds-Shade-Sails-and-Water-Tanks"),
                        ("Pergolas, shade sails, sheds and water tanks application checklist, City of Cockburn", "https://www.cockburn.wa.gov.au/getattachment/8e71ab87-84ad-4232-a68f-1b23595c05da/ECM_5901276_v1_Pergolas,-Sheds,-Shade-Sails-and-Water-Tanks-Application-Checklist-docx.aspx"),
                        ("Building Permit Application, City of Cockburn", "https://www.cockburn.wa.gov.au/Building-Planning-and-Roads/Applications-and-Permits/Building-permit")]}
