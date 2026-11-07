BODY = """
<h2>Two separate tests</h2>
<p>Building a patio close to the fence has to pass two different sets of rules:</p>
<ol>
<li><strong>Planning rules (the R-Codes and council policies)</strong> decide how close the posts and roof can be before you need planning approval.</li>
<li><strong>The building code (fire separation)</strong> decides how close the roof can be to the boundary for the building permit.</li>
</ol>
<p>A patio can pass one and fail the other, so check both.</p>

<h2>What Perth councils say</h2>
<div class="table-wrap"><table>
<thead><tr><th>Council</th><th>Planning (no approval needed if...)</th><th>Building code note</th></tr></thead><tbody>
<tr><td>City of Wanneroo</td><td>Posts can be <strong>on the boundary</strong> with eaves, gutters and roof at least <strong>500 mm</strong> back, if the patio is no more than 10 m long, 2.7 m high, and behind the street setback. Otherwise 1 m from the side boundary (1.5 m if over 14 m long).</td><td>900 mm from the patio roof to a side or rear boundary for fire separation</td></tr>
<tr><td>City of Joondalup</td><td>At least <strong>450 mm</strong> from the boundary if no more than 2.7 m high and 10 m long. Bigger patios follow the R-Code setbacks (usually 1 m, or 1.5 m over 14 m long at R20).</td><td>Patios attached to the house must be <strong>900 mm</strong> from any boundary (not counting a road or public space)</td></tr>
<tr><td>City of Cockburn</td><td>Check the City's rules</td><td>A patio attached to a house must be <strong>900 mm</strong> from a boundary, other than a road or public space</td></tr>
</tbody></table></div>
<p>Councils vary, and your R-Code and any local development plan can change the numbers.</p>

<h2>Why 900 mm keeps coming up</h2>
<p>The 900 mm rule is about fire. It stops a fire spreading from your patio and house to the neighbour's place. Where the patio is too close, the building code usually needs extra fire protection, which a building surveyor or engineer would design. Ask before you assume a boundary patio is impossible.</p>

<h2>Don't fix it to the fence</h2>
<p>Whatever the setback, the patio should stand on its own posts and footings on your land. Councils such as Joondalup say structures shouldn't be fixed to a dividing fence or hang over the neighbour's property. If any part would go over the boundary, you need the neighbour's written consent (form BA20) before a permit can be issued.</p>

<h2>Planning approval if you don't meet the rules</h2>
<p>If your patio is closer than the standard setback, longer, or taller, you can still apply for planning approval. The council may ask your neighbours for comment.</p>
<p>See if your design is permit-free with the <a href="/patio-approval-checker">patio approval checker</a>, and read <a href="/patio-building-permit">patio building permits</a> and <a href="/city-of-wanneroo-patio-rules">City of Wanneroo patio rules</a>.</p>
"""

FAQS = [
    ("Can a patio be built on the boundary in WA?",
     "Sometimes. Wanneroo allows posts on the boundary with the roof 500 mm back for patios up to 10 m long and 2.7 m high behind the street setback. But the building code usually wants the roof 900 mm from the boundary for fire separation. Councils vary."),
    ("How close to the fence can I build a patio in Perth?",
     "Joondalup allows 450 mm for patios up to 2.7 m high and 10 m long, with 900 mm for attached patios under the building code. Wanneroo allows posts on the boundary in some cases. Check your council."),
    ("Why do patios need to be 900 mm from the boundary?",
     "For fire separation under the building code. It reduces the risk of fire spreading between properties. Closer patios usually need extra fire protection."),
    ("Can I attach my patio to the dividing fence?",
     "No. Patios should stand on their own posts on your land. Councils like Joondalup say structures shouldn't be fixed to dividing fences."),
    ("Do I need my neighbour's permission for a patio on the boundary?",
     "Not if it's fully on your land and meets the rules. If any part goes over the boundary, you need their written consent (form BA20). The council may also ask neighbours for comment on a planning application."),
]


def page(S):
    return {"path": "patio-on-boundary-wa.html", "published": "2026-11-08", "type": "Question answer", "icon": "pergola",
            "card": "Planning setbacks vs the 900 mm fire rule, with Wanneroo, Joondalup and Cockburn compared.",
            "title": "Can a Patio Be Built on the Boundary in WA?",
            "desc": "Building a patio on or near the boundary in WA: planning setbacks vs the 900 mm fire separation rule, Wanneroo, Joondalup and Cockburn compared.",
            "eyebrow": "Question answer", "h1": "Can a patio be built on the boundary?", "crumb": "Patio on the boundary",
            "answer": "<p><strong>Sometimes, but it's tricky.</strong> Some councils let the posts go on the boundary for small patios (Wanneroo: up to 10 m long and 2.7 m high, roof 500 mm back). But the building code usually needs the roof <strong>900 mm</strong> from the boundary for fire safety, unless extra fire protection is designed in. Councils vary.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-checker", "Patio approval checker"), ("/patio-building-permit", "Patio building permits"), ("/city-of-wanneroo-patio-rules", "City of Wanneroo patio rules")],
            "sources": [("Patios information sheet (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Patio, pergola or shade sails (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/patio,-pergola-or-shade-sails"),
                        ("Pergolas, sheds, shade sails and water tanks (City of Cockburn)", "https://www.cockburn.wa.gov.au/Building-Planning-and-Roads/Applications-and-Permits/Pergolas-Sheds-Shade-Sails-and-Water-Tanks")]}
