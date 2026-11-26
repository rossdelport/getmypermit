BODY = """
<h2>Building permit</h2>
<p>A patio needs a building permit unless it's <strong>freestanding</strong>, <strong>10 m² or less</strong> and <strong>2.4 m or lower</strong>. A patio attached to the house always needs one. Exempt patios still have to meet the building code, including fire separation. See the <a href="/patio-approval-checker">patio approval checker</a>.</p>

<h2>Planning approval</h2>
<p>The City of Vincent says a patio <strong>doesn't</strong> need planning approval if it's on a lot with a house or grouped dwelling, isn't in a heritage-protected place, and either fully meets the R-Codes and the City's Built Form Policy, or meets the City's planning exemptions:</p>
<ul>
<li>not in the front or secondary street setback,</li>
<li>no more than <strong>30 m²</strong>,</li>
<li>no more than <strong>3.5 m</strong> high,</li>
<li>floor no more than 0.5 m above ground, and</li>
<li>doesn't break the R-Codes rules for outdoor living area, open space and boundary walls.</li>
</ul>
<p>Patios with apartments or shops on the lot, or that don't meet the R-Codes, need planning approval. The City has 60 days to decide (90 with consultation), and approval lasts 2 years.</p>

<h2>Setbacks</h2>
<div class="table-wrap"><table>
<thead><tr><th>Patio</th><th>Usual setback</th></tr></thead><tbody>
<tr><td>Up to 10 m long and 3.5 m high</td><td>1 m from the boundary</td></tr>
<tr><td>Over 14 m long, up to 3.5 m high</td><td>1.5 m</td></tr>
<tr><td>Up to 10 m long and 2.7 m high, behind the front setback</td><td>Can be nil (on the boundary), with eaves and gutters 450 mm back</td></tr>
</tbody></table></div>
<p>Setbacks are measured to the posts, as long as eaves are no deeper than 0.75 m. Newer R-Codes Part C lots have similar rules. See <a href="/patio-on-boundary-wa">patios on the boundary</a>.</p>

<h2>Raised patios and privacy</h2>
<p>If the floor is more than <strong>0.5 m</strong> above the ground, privacy rules apply. Usually the raised area must be 7.5 m from the boundary (R50 or lower) or have fixed screening at least 1.6 m high. See <a href="/deck-height-rules">deck height rules</a>.</p>
<p>Call the City on 9273 6000.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in the City of Vincent?",
     "A building permit is needed unless it's freestanding, 10 m² or less and no more than 2.4 m high. An attached patio always needs one."),
    ("Does a patio need planning approval in Vincent?",
     "Not if it meets the R-Codes and Built Form Policy, or the City's exemptions (up to 30 m², 3.5 m high, not in a street setback, not heritage)."),
    ("Can a patio go on the boundary in Vincent?",
     "Often yes, if it's no more than 10 m long and 2.7 m high, behind the front setback, with eaves and gutters at least 450 mm from the boundary."),
    ("Does a raised patio need screening in Vincent?",
     "If the floor is more than 0.5 m above ground, it usually needs a 7.5 m setback (R50 or lower) or fixed screening at least 1.6 m high."),
]


def page(S):
    return {"path": "city-of-vincent-patio-rules.html", "published": "2026-11-27", "type": "Council guide", "icon": "pin",
            "card": "City of Vincent patio rules: building permits, the 30 m² planning exemption, setbacks and privacy.",
            "title": "City of Vincent Patio Rules (2026)",
            "desc": "City of Vincent patio rules: when you need a building permit, the planning exemption for patios up to 30 m² and 3.5 m, boundary setbacks, nil setbacks and privacy rules for raised patios.",
            "eyebrow": "Council guide", "h1": "City of Vincent patio rules", "crumb": "Vincent patio rules",
            "answer": "<p>In the City of Vincent, a patio needs a <strong>building permit</strong> unless it's freestanding, 10 m² or less and 2.4 m or lower. Planning approval usually isn't needed if it's <strong>30 m²</strong> or less, <strong>3.5 m</strong> or lower, out of the street setback and not heritage, or it fully meets the R-Codes.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-checker", "Patio approval checker"), ("/patio-on-boundary-wa", "Patio on the boundary"), ("/deck-height-rules", "Deck height rules")],
            "sources": [("Planning information sheet: patios in residential areas (May 2024), City of Vincent", "https://www.vincent.wa.gov.au/Profiles/vincent/Assets/ClientData/Planning_Information_Sheets/2024/Planning_Information_Sheet_Patios_May2024.pdf")]}
