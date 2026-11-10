BODY = """
<h2>What a carport site plan must show</h2>
<p>The site plan is a bird's-eye drawing of your whole block. It's how the council checks your setbacks. For an uncertified (BA2) application, the City of Wanneroo asks for a site plan at a minimum scale of <strong>1:200</strong> showing:</p>
<ul>
<li>Contour survey or spot levels, and the proposed finished floor level</li>
<li>How far the carport is from every lot boundary</li>
<li>How far it is from other buildings on the lot, including retaining walls</li>
<li>Any septic system</li>
<li>A north point</li>
</ul>
<p>The City of Stirling's planning site plan also asks for a <strong>north point, the crossover and levels</strong>. Councils vary, so check your council's checklist.</p>

<h2>Step by step</h2>
<ol>
<li><strong>Get your lot plan.</strong> Start with your Certificate of Title diagram, survey or the plans from when the house was built. Councils such as Stirling let owners request copies of approved plans.</li>
<li><strong>Draw the boundaries to scale.</strong> At 1:200, 1 cm on paper is 2 m on the ground. Label each boundary's length.</li>
<li><strong>Add what's already there.</strong> The house, sheds, pool, retaining walls, driveway and crossover.</li>
<li><strong>Draw the carport.</strong> Show its full outline and size. Mark the <strong>posts</strong> and the <strong>roof edge</strong>, because councils check setbacks to both.</li>
<li><strong>Dimension the setbacks.</strong> Measure from the posts and the roof edge to the street boundary, each side boundary, and the house.</li>
<li><strong>Add levels, north point, scale and address.</strong> Then date it.</li>
</ol>

<h2>The numbers councils check</h2>
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Example rule</th></tr></thead><tbody>
<tr><td>Front setback</td><td>Wanneroo's sheet: 6 m on R20 (4 m on R30 or R40), halved if the carport is no wider than 60% of the frontage</td></tr>
<tr><td>Width of frontage</td><td>Stirling: no more than 60% of the frontage</td></tr>
<tr><td>Side boundary</td><td>Wanneroo: posts 1 m back, or on the boundary if the carport is no more than 10 m long and 2.7 m high, with the roof 500 mm back</td></tr>
<tr><td>Building code</td><td>900 mm from a side boundary or another building, or 500 mm if the carport is open enough and has a suitable roof</td></tr>
<tr><td>Minimum size</td><td>Stirling: 5.4 x 2.4 m for a single bay, 5.4 x 4.8 m for a double</td></tr>
</tbody></table></div>

<h2>What else to lodge</h2>
<p>The site plan isn't enough on its own. Wanneroo also asks for floor plan, elevations and sections at 1:100, construction details and a structural engineer's details. Other councils usually ask for something similar.</p>
<p>Check your front setback with the <a href="/front-setback-carport-calculator">front setback carport calculator</a>, read <a href="/city-of-wanneroo-carport-rules">City of Wanneroo carport rules</a>, or see <a href="/carport-on-boundary">building a carport on the boundary</a>.</p>
"""

FAQS = [
    ("What scale should a carport site plan be?",
     "At least 1:200. Wanneroo asks for a minimum of 1:200 for the site plan and 1:100 for elevations."),
    ("What does a carport site plan need to show?",
     "Boundaries, existing buildings and retaining walls, the carport and its setbacks to boundaries and buildings, levels, any septic system and a north point. Stirling also asks for the crossover."),
    ("Can I draw my own carport site plan?",
     "Usually yes, if it's to scale, dimensioned and shows everything on the council's checklist. Engineering must still come from a structural engineer."),
    ("Where do I get my lot dimensions?",
     "From your Certificate of Title diagram, a survey, or the plans from when the house was built. Councils such as Stirling let owners request copies of approved plans."),
]


def page(S):
    return {"path": "carport-site-plan.html", "published": "2026-11-11", "type": "How-to guide", "icon": "plan",
            "card": "What councils want on the site plan, step by step, and the setbacks they check.",
            "title": "How to Draw a Carport Site Plan for Council (WA)",
            "desc": "How to draw a carport site plan for a WA council: 1:200 scale, boundaries, setbacks to posts and roof, levels and north point, plus the numbers councils check.",
            "eyebrow": "How-to guide", "h1": "How to draw a carport site plan", "crumb": "Carport site plan",
            "answer": "<p>A carport site plan is a scaled drawing of your block, usually at <strong>1:200</strong>. It shows the boundaries, the house and other buildings, the carport, and the distance from its <strong>posts and roof</strong> to each boundary. Councils such as Wanneroo also want levels, any septic system and a north point.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/front-setback-carport-calculator", "Front setback carport calculator"), ("/city-of-wanneroo-carport-rules", "City of Wanneroo carport rules"), ("/carport-on-boundary", "Carport on the boundary")],
            "sources": [("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf"),
                        ("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf")]}
