BODY = """
<h2>The four drawings councils ask for</h2>
<p>If you apply yourself with an uncertified application (form BA2), the council checks your drawings. Wanneroo and Belmont both ask for the same core set:</p>
<div class="table-wrap"><table>
<thead><tr><th>Drawing</th><th>Scale</th><th>What it shows</th></tr></thead><tbody>
<tr><td>Site plan</td><td>1:200 or larger</td><td>Whole block, boundaries, house, patio and the distances between them</td></tr>
<tr><td>Elevations (and sections)</td><td>1:100</td><td>Side views of the patio with heights and roof pitch</td></tr>
<tr><td>Construction details</td><td>To suit</td><td>Post, beam and roof sizes, footings, and how it connects to the house</td></tr>
<tr><td>Engineer's design</td><td>To suit</td><td>A structural engineer's certification of the patio</td></tr>
</tbody></table></div>

<h2>Step 1: the site plan</h2>
<p>Start with a copy of your lot plan or survey. Then draw on it:</p>
<ul>
<li>All boundaries, with their lengths</li>
<li>The house and any other buildings, sheds or retaining walls</li>
<li>The patio, with its size and its distance to each nearby boundary and building</li>
<li>Ground levels (spot levels) and the finished floor level, as Wanneroo asks</li>
<li>Any easements and septic system</li>
<li>A north point</li>
</ul>
<p>Measure setbacks to the <strong>posts</strong> and to the <strong>roof edge</strong>. Councils check both. In Wanneroo, for example, posts can sit on the boundary only if the patio is no more than 10 m long and 2.7 m high, with the roof at least 500 mm back.</p>

<h2>Step 2: elevations</h2>
<p>Draw the patio from the front and side at 1:100. Show the height at the gutter, the highest point of the roof, the roof pitch and the ground line. If the patio attaches to the house, show where and how.</p>

<h2>Step 3: construction details and engineering</h2>
<p>Ask your patio supplier or builder for engineering that suits your wind rating. It should cover post sizes, beam spans, footing sizes and tie-downs. If the patio is attached to the house, Wanneroo also asks for connection details.</p>

<h2>Step 4: check before you lodge</h2>
<ul>
<li>Every drawing has the address, a scale and a date</li>
<li>Dimensions match across all drawings</li>
<li>Setbacks meet your council's rules, or you've applied for planning approval</li>
<li>Your council's extra forms are included. Wanneroo needs a Street and Verge Bond Permit application with every building permit.</li>
</ul>
<p>Councils vary, so check your council's checklist. If you use a private building surveyor (form BA1), they check the drawings first.</p>
<p>Check whether you need a permit at all on <a href="/patio-building-permit">patio building permit</a>, read about <a href="/patio-on-boundary-wa">building a patio on the boundary</a>, or see <a href="/patio-approval-cost-perth">what patio approval costs</a>.</p>
"""

FAQS = [
    ("What plans do I need for a patio permit in WA?",
     "Usually a site plan at 1:200, elevations at 1:100, construction details and a structural engineer's design. Councils such as Wanneroo and Belmont ask for this set with an uncertified (BA2) application."),
    ("Can I draw my own patio plans?",
     "Usually yes. Councils ask for clear, scaled, dimensioned drawings. The engineering must come from a structural engineer, which some patio suppliers provide."),
    ("What scale should a patio site plan be?",
     "At least 1:200 for the site plan and 1:100 for elevations, in Wanneroo and Belmont."),
    ("What should a patio site plan show?",
     "Boundaries, existing buildings, the patio with its size and setbacks to posts and roof, ground levels, easements, any septic system and a north point. Councils vary, so check your council's checklist."),
]


def page(S):
    return {"path": "patio-plans-for-council.html", "published": "2026-11-10", "type": "How-to guide", "icon": "plan",
            "card": "The four drawings councils ask for, step by step, with a checklist before you lodge.",
            "title": "How to Draw Patio Plans for Council (WA Guide)",
            "desc": "How to draw patio plans for a WA council: site plan at 1:200, elevations at 1:100, construction details and engineering, with a checklist before you lodge.",
            "eyebrow": "How-to guide", "h1": "How to draw patio plans for council", "crumb": "Patio plans for council",
            "answer": "<p>Councils usually want four things: a <strong>site plan</strong> at 1:200 showing setbacks, <strong>elevations</strong> at 1:100 showing heights, <strong>construction details</strong>, and a <strong>structural engineer's design</strong>. Wanneroo and Belmont both ask for this set with a BA2 application. Councils vary, so check yours.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-building-permit", "Patio building permit"), ("/patio-on-boundary-wa", "Patio on the boundary"), ("/patio-approval-cost-perth", "Patio approval cost")],
            "sources": [("Patios information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Patio, pergola or shade sail (City of Belmont)", "https://www.belmont.wa.gov.au/build/demolishing-and-building/approval-for-buildings-and-structures/i-want-to-build/patio,-pergola-or-shade-sail")]}
