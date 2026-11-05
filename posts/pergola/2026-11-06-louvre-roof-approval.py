BODY = """
<h2>Why louvres are tricky</h2>
<p>A pergola lets rain through. A patio has a roof that keeps rain out. An opening louvre roof does both, depending on whether the blades are open or closed. WA's rules don't name louvre roofs directly, so each council decides which group they fall into. That's why you'll hear different answers.</p>

<h2>How two Perth councils treat them</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>City of Joondalup</th><th>City of Belmont</th></tr></thead><tbody>
<tr><td>Treated like</td><td>A patio (for the building permit)</td><td>A pergola (its definition includes "operable louvered roofing")</td></tr>
<tr><td>No building permit if</td><td>Freestanding, <strong>10 m²</strong> or less, and <strong>2.4 m</strong> high or less</td><td>Less than <strong>20 m²</strong>, no more than <strong>2.4 m</strong> high, for a house</td></tr>
<tr><td>Planning approval</td><td>Typically not needed for houses (may be on some dual-density lots built at the higher code)</td><td>Needed in the front setback if it doesn't meet the R-Codes, in heritage areas, special precincts or near the Swan River</td></tr>
<tr><td>Setbacks</td><td>900 mm from the house if freestanding; 900 mm from side and rear boundaries if attached</td><td>Must still meet the building code, even when exempt</td></tr>
</tbody></table></div>
<p>So the same 15 m² freestanding louvre roof could need a permit in Joondalup but not in Belmont. Other councils may differ again.</p>

<h2>Bigger louvre roofs need a permit anyway</h2>
<p>Under either approach, a louvre roof over 20 m² or taller than 2.4 m needs a building permit. In Joondalup, any louvre roof attached to the house needs one too. Many louvre roofs over an alfresco are bigger than 20 m², so in practice a lot of them need a permit.</p>

<h2>What you lodge</h2>
<p>For an uncertified application (form BA2), Belmont expects:</p>
<ul>
<li>A site plan at 1:200 or better, showing setbacks, ground levels and easements</li>
<li>Elevations at 1:100 or better</li>
<li>Structural design certified by a practising structural engineer</li>
</ul>
<p>Louvre suppliers usually provide engineering for their system. Ask for it with your quote.</p>
<p>Check your own design with our <a href="/patio-approval-checker">patio approval checker</a>, or read <a href="/roof-on-pergola-approval">putting a roof on a pergola</a> and <a href="/pergola-vs-patio">pergola vs patio</a>.</p>
"""

FAQS = [
    ("Do louvre roofs need council approval in WA?",
     "Yes if over 20 m² or over 2.4 m high. Councils differ on small freestanding ones: Joondalup treats them like patios (permit-free only up to 10 m²), while Belmont treats them like pergolas (permit-free under 20 m²)."),
    ("Is a louvre roof a pergola or a patio?",
     "It depends on the council. Belmont's definition of a pergola includes operable louvred roofing. Joondalup groups louvred roofs with patios for building permits."),
    ("Do I need planning approval for a louvre roof?",
     "Often not for a house. Joondalup says planning approval is typically not needed, and Belmont only needs it in the front setback, heritage areas, special precincts or near the Swan River."),
    ("How close to the boundary can a louvre roof be?",
     "Joondalup asks for 900 mm from side and rear boundaries for attached structures, and 900 mm from the house for freestanding ones. Check your council's rules."),
    ("What do I need to apply for a louvre roof permit?",
     "Usually a site plan, elevations and structural engineering. Belmont lists a 1:200 site plan, 1:100 elevations and a structural engineer's certified design for BA2 applications."),
]


def page(S):
    return {"path": "louvre-roof-approval.html", "published": "2026-11-06", "type": "Question answer", "icon": "pergola",
            "card": "Pergola or patio? How Joondalup and Belmont treat opening roofs.",
            "title": "Do You Need Approval for a Louvre Roof in WA?",
            "desc": "Louvre roof council approval in WA: whether it counts as a pergola or patio, Joondalup vs Belmont rules, size limits, setbacks and what to lodge.",
            "eyebrow": "Question answer", "h1": "Do you need approval for a louvre or opening roof?", "crumb": "Louvre roof approval",
            "answer": "<p><strong>Often, yes.</strong> An opening louvre roof over 20 m² or over 2.4 m high needs a building permit. Councils vary on smaller ones. Joondalup treats them like patios (no permit only up to 10 m²). Belmont treats them like pergolas (no permit under 20 m²). Planning approval often isn't needed for a house.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/roof-on-pergola-approval", "Putting a roof on a pergola"), ("/pergola-vs-patio", "Pergola vs patio"), ("/patio-approval-checker", "Patio approval checker")],
            "sources": [("Patio, pergola or shade sails (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/patio,-pergola-or-shade-sails"),
                        ("Patio, pergola or shade sail (City of Belmont)", "https://www.belmont.wa.gov.au/build/demolishing-and-building/approval-for-buildings-and-structures/i-want-to-build/patio,-pergola-or-shade-sail")]}
