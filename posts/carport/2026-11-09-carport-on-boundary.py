BODY = """
<h2>What the R-Codes allow</h2>
<p>The R-Codes treat carports, patios and verandahs the same way for boundary setbacks. Which rule applies depends on your lot's density code.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Most single houses (R40 and below)</th><th>Higher density (single houses R50+, grouped dwellings R30+)</th></tr></thead><tbody>
<tr><td>Posts on the boundary allowed if</td><td>No more than <strong>10 m long</strong> and <strong>2.7 m high</strong>, behind the primary street setback</td><td>Less than <strong>10 m long</strong>, no more than <strong>3 m</strong> equivalent wall height, and a ridge no higher than <strong>4.2 m</strong></td></tr>
<tr><td>Roof and gutters</td><td>At least <strong>450 mm</strong> from the boundary</td><td>Can be built up to the boundary</td></tr>
<tr><td>Post size</td><td colspan="2">Posts 450 mm by 450 mm or smaller don't count as a boundary wall</td></tr>
</tbody></table></div>
<p>If your carport meets these, it doesn't need planning approval for its boundary setback. It still has to meet the other rules, like the street setback and width.</p>

<h2>Some councils are stricter</h2>
<p>Local policies can change the numbers. The City of Stirling's carport information sheet says planning approval isn't needed if, among other things, the carport posts are <strong>at least 1 m</strong> from the side boundary. Check your council's own sheet before you design.</p>

<h2>The building code still applies</h2>
<p>The R-Codes note that carports on or near the boundary must also meet the National Construction Code, including fire separation and non-combustible materials. This is part of the building permit. Your designer or building surveyor will check it.</p>

<h2>Boundary walls are different</h2>
<p>A solid wall on the boundary is a "boundary wall", not just posts. The City of Stirling says garage boundary walls can be built on lots coded R20 and above, but need planning approval at R12.5 and below. They must sit behind the street setback, for example 6 m at R20/R25 and 4 m at R30/R40. If your carport will have a solid wall on the boundary, ask your council how it will be assessed.</p>

<h2>Neighbours</h2>
<ul>
<li>You don't need your neighbour's approval to apply for planning approval. Stirling says the council may advertise the plans to neighbours if it thinks they'll be affected.</li>
<li>Keep everything on your side. If any part, like footings or gutters, would go over the boundary, you need the neighbour's written consent (form BA20).</li>
<li>Councils such as Joondalup say structures shouldn't be fixed to a dividing fence.</li>
</ul>
<p>See also <a href="/carport-council-approval">carport council approval</a>, <a href="/city-of-stirling-carport-rules">City of Stirling carport rules</a> and <a href="/attached-vs-freestanding-carport">attached vs freestanding carports</a>.</p>
"""

FAQS = [
    ("Can a carport be built on the boundary in WA?",
     "Often, yes. Under the R-Codes, carports up to 10 m long and 2.7 m high on most house lots can have posts on the boundary, behind the street setback, with the roof 450 mm back. Some councils, like Stirling, ask for posts 1 m from the side boundary."),
    ("How close to the boundary can a carport roof be?",
     "On most single house lots (R40 and below), the eaves, gutters and roof must be at least 450 mm from the boundary under the R-Codes. Building code fire rules also apply."),
    ("Do I need my neighbour's permission for a carport on the boundary?",
     "Not to apply for planning approval, though the council may ask for their comments. If any part goes over the boundary, you need their written consent (form BA20)."),
    ("Can a carport have a wall on the boundary?",
     "A solid wall on the boundary is a boundary wall and has its own rules. In Stirling, boundary walls are allowed on R20 and above lots behind the street setback; at R12.5 and below they need planning approval."),
    ("Does a carport on the boundary need a building permit?",
     "Yes. Carports need a building permit, which checks fire separation and the structure."),
]


def page(S):
    return {"path": "carport-on-boundary.html", "published": "2026-11-09", "type": "Question answer", "icon": "carport",
            "card": "The R-Code post and roof rules, stricter councils, boundary walls and neighbours.",
            "title": "Can a Carport Go on the Boundary in WA?",
            "desc": "Building a carport on the boundary in WA: the R-Codes rules for posts and roof, stricter council rules, boundary walls, fire separation and neighbours.",
            "eyebrow": "Question answer", "h1": "Can a carport go on the boundary?", "crumb": "Carport on the boundary",
            "answer": "<p><strong>Often, yes.</strong> On most house lots the R-Codes let carport posts sit on the boundary if the carport is no more than <strong>10 m long</strong> and <strong>2.7 m high</strong>, behind the street setback, with the roof at least <strong>450 mm</strong> back. Councils vary: Stirling asks for posts 1 m from the side boundary. You'll still need a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-council-approval", "Carport council approval"), ("/city-of-stirling-carport-rules", "City of Stirling carport rules"), ("/attached-vs-freestanding-carport", "Attached vs freestanding carports")],
            "sources": [("Residential Design Codes Volume 1, April 2026 (WA Planning)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Carports and garages information sheet (City of Stirling)", "https://www.stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf")]}
