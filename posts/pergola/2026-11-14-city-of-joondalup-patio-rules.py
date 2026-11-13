BODY = """
<h2>Building permit rules</h2>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>No building permit if</th></tr></thead><tbody>
<tr><td>Patio or louvre roof</td><td>Standalone, 10 m² or less, 2.4 m or less</td></tr>
<tr><td>Pergola</td><td>20 m² or less and 2.4 m or less</td></tr>
<tr><td>Shade sail</td><td>Standalone, 20 m² or less, 2.4 m or less</td></tr>
<tr><td>Shade sail attached to a building</td><td>Always needs a permit</td></tr>
</tbody></table></div>
<p>For fire safety, a detached patio or louvre roof must be at least <strong>900 mm from the house</strong>, and an attached one at least <strong>900 mm from any boundary</strong> (except a boundary to a road or public space). Vergola rooflines should be 900 mm from side and rear boundaries.</p>
<p>Pergolas can go up to the boundary, but must not touch or be fixed to the dividing fence, and footings must stay on your land.</p>

<h2>Planning approval for patios</h2>
<p>On a house or grouped dwelling lot, a patio usually doesn't need planning approval if:</p>
<ul>
<li>It's open on two or more sides</li>
<li>It meets the street setback for your R-Code (see below)</li>
<li>It's at least <strong>450 mm</strong> from the boundary if no more than 2.7 m high and 10 m long; bigger patios need the full side setback</li>
<li>It suits the house if it can be seen from the street</li>
<li>You keep enough open space and outdoor living area</li>
</ul>
<p>Watch out for raised floors: if the patio's finished level is more than <strong>500 mm</strong> above natural ground, extra rules apply.</p>

<h2>Setbacks and open space by R-Code</h2>
<div class="table-wrap"><table>
<thead><tr><th>R-Code</th><th>Street setback</th><th>Open space</th><th>Outdoor living area</th></tr></thead><tbody>
<tr><td>R20</td><td>3 m (average 6 m); 1.5 m to a side street</td><td>50%</td><td>20 m²</td></tr>
<tr><td>R20/25</td><td>4 m; 2 m to a side street</td><td>50%</td><td>20 m²</td></tr>
<tr><td>R20/30</td><td>4 m; 2 m</td><td>45%</td><td>16 m²</td></tr>
<tr><td>R20/40</td><td>4 m; 2 m</td><td>45%</td><td>13.3 m²</td></tr>
<tr><td>R20/60</td><td>4 m; 2 m</td><td>40%</td><td>10.7 m²</td></tr>
</tbody></table></div>
<p>Pergolas, louvre roofs and shade sails usually don't need planning approval on house lots. Joondalup says you don't need your neighbour's approval to apply, but it may notify neighbours if a project could affect them.</p>
<p>Compare <a href="/city-of-melville-patio-rules">City of Melville patio rules</a>, or read <a href="/louvre-roof-approval">louvre roof approval</a> and <a href="/shade-sail-approval-wa">shade sail approval</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in Joondalup?",
     "Yes, unless it's standalone, 10 m² or less and 2.4 m or less high. Attached patios need a building permit."),
    ("Does a pergola need a permit in Joondalup?",
     "Not if it's 20 m² or less and 2.4 m or less high. It can go to the boundary but must not be fixed to the dividing fence."),
    ("How close to the boundary can a patio be in Joondalup?",
     "Without planning approval, at least 450 mm if it's no more than 2.7 m high and 10 m long. For fire safety, an attached patio must be 900 mm from the boundary."),
    ("Do I need my neighbour's approval for a patio in Joondalup?",
     "No. Joondalup says neighbour approval isn't needed to apply, but it may notify neighbours if the project could affect them."),
]


def page(S):
    return {"path": "city-of-joondalup-patio-rules.html", "published": "2026-11-14", "type": "Council guide", "icon": "pin",
            "card": "Joondalup's rules for patios, pergolas, louvre roofs and shade sails, with setbacks by R-Code.",
            "title": "City of Joondalup Patio, Pergola and Shade Sail Rules (2026)",
            "desc": "City of Joondalup patio rules: when patios, pergolas, louvre roofs and shade sails need a permit, boundary distances, and setbacks and open space by R-Code.",
            "eyebrow": "Council guide", "h1": "City of Joondalup patio rules", "crumb": "Joondalup patio rules",
            "answer": "<p>In Joondalup, a patio or louvre roof needs a building permit unless it's <strong>standalone, 10 m² or less and 2.4 m or less</strong>. Pergolas and standalone shade sails are exempt up to <strong>20 m²</strong> and 2.4 m. Patios usually skip planning approval if they're open on two sides and meet the setbacks.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/city-of-melville-patio-rules", "City of Melville patio rules"), ("/louvre-roof-approval", "Louvre roof approval"), ("/shade-sail-approval-wa", "Shade sail approval in WA")],
            "sources": [("Patio, pergola or shade sails, City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/patio,-pergola-or-shade-sails")]}
