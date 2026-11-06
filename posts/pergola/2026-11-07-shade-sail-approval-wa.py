BODY = """
<h2>The basic WA rule</h2>
<p>WA's building rules let you put up a shade sail without a building permit if it's for a house, covers no more than <strong>20 m²</strong>, and is no more than <strong>2.4 m</strong> high. Most shade sails over an outdoor area are higher than 2.4 m, so in practice many do need a permit.</p>
<p>Even when no permit is needed, the sail must still be built to the building code. Strong winds put big loads on posts and fixings.</p>

<h2>How two Perth councils apply it</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>City of Joondalup</th><th>City of Belmont</th></tr></thead><tbody>
<tr><td>No building permit if</td><td>Standalone, <strong>20 m²</strong> or less, and <strong>2.4 m</strong> high or less</td><td>For a house, less than <strong>20 m²</strong>, and no more than <strong>2.4 m</strong> high</td></tr>
<tr><td>Sail fixed to the house or another building</td><td>Always needs a building permit, whatever the size</td><td>Same size and height test applies</td></tr>
<tr><td>Sail with a waterproof cover</td><td>Not covered separately</td><td>Treated as a patio (stricter: only exempt if freestanding and under 10 m²)</td></tr>
<tr><td>Planning approval</td><td>Typically not needed for houses</td><td>Needed in the front setback if it doesn't meet the R-Codes, in heritage areas, special precincts or near the Swan River</td></tr>
</tbody></table></div>
<p>Other councils may differ, so check yours.</p>

<h2>Common traps</h2>
<ul>
<li><strong>Fixing to the house.</strong> In Joondalup this alone means you need a permit.</li>
<li><strong>Fixing to the fence.</strong> Joondalup says no part of a pergola or attached shade sail can be fixed to a dividing fence or hang over the neighbour's land.</li>
<li><strong>Waterproof fabric.</strong> A sail that keeps rain out can count as a patio, which has tighter limits.</li>
<li><strong>Height.</strong> The 2.4 m limit is easy to go over once you allow for head room and a sloped sail.</li>
</ul>

<h2>What you lodge if you need a permit</h2>
<p>For an uncertified application (form BA2), councils usually want:</p>
<ul>
<li>A site plan (at least 1:200) showing setbacks and easements</li>
<li>Elevations (at least 1:100)</li>
<li>Structural design certified by a structural engineer, covering the posts, footings and fixings</li>
</ul>
<p>Joondalup has a specific checklist for pergolas and shade sails. Many shade sail installers include engineering in their quote, so ask.</p>
<p>Not sure if yours is a pergola, patio or sail? Read <a href="/pergola-vs-patio">pergola vs patio</a>, try the <a href="/patio-approval-checker">patio approval checker</a>, or see <a href="/do-i-need-council-approval-for-a-pergola">do I need council approval for a pergola?</a></p>
"""

FAQS = [
    ("Do I need council approval for a shade sail in WA?",
     "You need a building permit unless the sail is for a house, 20 m² or less and no more than 2.4 m high. Some councils, like Joondalup, require a permit for any sail fixed to a building."),
    ("Can I attach a shade sail to my house without a permit?",
     "It depends on the council. In Joondalup, any shade sail attached to another building needs a building permit regardless of size. Check with your council."),
    ("Can I attach a shade sail to my fence?",
     "Usually not. Joondalup says no part of a pergola or attached shade sail can be fixed to a dividing fence or encroach on neighbouring land."),
    ("Is a waterproof shade sail a patio?",
     "In Belmont, yes. A shade sail with a non-permeable cover is treated as a patio, which is only exempt if freestanding and under 10 m²."),
    ("Do shade sails need planning approval?",
     "Usually not for a house. Belmont needs it in the front setback if the R-Codes aren't met, in heritage areas, special precincts or near the Swan River."),
]


def page(S):
    return {"path": "shade-sail-approval-wa.html", "published": "2026-11-07", "type": "Question answer", "icon": "pergola",
            "card": "The 20 m² and 2.4 m rule, plus the traps: fixing to the house, the fence, and waterproof sails.",
            "title": "Do You Need Council Approval for a Shade Sail in WA?",
            "desc": "Shade sail approval in WA: the 20 m² and 2.4 m exemption, Joondalup vs Belmont rules, fixing to the house or fence, and what to lodge.",
            "eyebrow": "Question answer", "h1": "Do you need council approval for a shade sail?", "crumb": "Shade sail approval",
            "answer": "<p><strong>Often, yes.</strong> A shade sail for a house needs no building permit only if it's <strong>20 m² or less</strong> and <strong>2.4 m high or less</strong>. Councils vary on the details. Joondalup needs a permit for any sail fixed to a building, and Belmont treats a waterproof sail as a patio. Planning approval usually isn't needed for a house.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/pergola-vs-patio", "Pergola vs patio"), ("/patio-approval-checker", "Patio approval checker"), ("/do-i-need-council-approval-for-a-pergola", "Do I need council approval for a pergola?")],
            "sources": [("Patio, pergola or shade sails (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/patio,-pergola-or-shade-sails"),
                        ("Patio, pergola or shade sail (City of Belmont)", "https://www.belmont.wa.gov.au/build/demolishing-and-building/approval-for-buildings-and-structures/i-want-to-build/patio,-pergola-or-shade-sail")]}
