BODY = """
<h2>Side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Attached carport</th><th>Freestanding carport</th></tr></thead><tbody>
<tr><td>Building permit</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Can it skip a permit if small?</td><td>No</td><td>In practice no: even a minimum single carport (5.4 m x 2.4 m, about 13 m²) is bigger than the 10 m² freestanding exemption</td></tr>
<tr><td>What the plans must show</td><td>How it connects to the house roof frame and footings, with engineering</td><td>Its own posts, footings and engineering</td></tr>
<tr><td>Planning rules</td><td>The same street setback, side boundary, 60% frontage and open-view rules apply to both</td><td>Same</td></tr>
</tbody></table></div>

<h2>Both always need a building permit</h2>
<p>The Cities of Stirling and Wanneroo both say every carport needs a building permit. The state's 10 m² exemption is for freestanding patios, sheds and gazebos, and a carport big enough to park in is larger than that anyway.</p>

<h2>Attached carports</h2>
<p>An attached carport ties into the house, so the plans need connection details to the roof frame and footings, and structural engineering. At Wanneroo, for example, attached roofed structures like patios need these details on every application. The R-Codes definition of a carport allows it to be closed in only where it meets the house or a boundary on one side.</p>

<h2>Freestanding carports</h2>
<p>A freestanding carport stands on its own posts and footings. It still has to meet the boundary rules: at Stirling, posts at least 1 m from the side boundary to skip planning approval; at Wanneroo, 1 m (or 1.5 m if longer than 14 m), or on the boundary if no longer than 10 m and no higher than 2.7 m with the roof 500 mm back. Building code fire rules apply too: 900 mm from the boundary, or 500 mm if the carport is open.</p>

<h2>Which is easier to approve?</h2>
<p>Neither skips the permit. The planning rules are the same, so the choice usually comes down to your site, the look you want and the cost of the engineering. Use our <a href="/front-setback-carport-calculator">front setback calculator</a> if it's going in front of the house.</p>
"""

FAQS = [
    ("Does an attached carport need a permit in WA?",
     "Yes. Every carport needs a building permit, and an attached one needs connection details to the house and engineering."),
    ("Does a freestanding carport need a permit in WA?",
     "Yes. The 10 m² exemption is for freestanding patios, sheds and gazebos, and even a minimum single carport (5.4 m x 2.4 m) is about 13 m²."),
    ("Are the planning rules different for attached and freestanding carports?",
     "No. Both have to meet the same street setback, side boundary, 60% frontage and open-view rules."),
    ("How close to the boundary can a freestanding carport be?",
     "At Stirling, posts at least 1 m from the side boundary. Wanneroo allows posts on the boundary if the carport is no longer than 10 m and no higher than 2.7 m, with the roof 500 mm back."),
]


def page(S):
    return {"path": "attached-vs-freestanding-carport.html", "published": "2026-11-05", "type": "Comparison", "icon": "carport",
            "card": "Both need a permit, but the plans and boundary rules work differently. Here's the comparison.",
            "title": "Attached vs Freestanding Carport: Permit Rules (WA)",
            "desc": "Attached vs freestanding carports in WA: why both need a building permit, connection details and engineering, boundary and fire-separation rules, and which is easier to approve.",
            "eyebrow": "Comparison", "h1": "Attached vs freestanding carport", "crumb": "Attached vs freestanding",
            "answer": "<p><strong>Both need a building permit.</strong> An attached carport's plans must show how it connects to the house, with engineering. A freestanding one needs its own footings and must meet the boundary and fire-separation rules. The planning rules (setbacks, 60% frontage, open view) are the same for both.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-council-approval", "Carport council approval"), ("/front-setback-carport-calculator", "Front setback carport calculator"), ("/city-of-stirling-carport-rules", "City of Stirling carport rules")],
            "sources": [("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf"),
                        ("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf"),
                        ("Patios information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Do I need a permit? (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit")]}
