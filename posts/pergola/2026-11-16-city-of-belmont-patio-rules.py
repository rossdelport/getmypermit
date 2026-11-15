BODY = """
<h2>What Belmont calls each one</h2>
<ul>
<li><strong>Patio:</strong> an unenclosed structure with a waterproof roof, attached to the house or not.</li>
<li><strong>Pergola:</strong> an open frame covered in a material that lets water through, or an <strong>operable louvred roof</strong>.</li>
<li><strong>Shade sail:</strong> fabric that lets water through, fixed to posts or another structure. A shade sail with a waterproof roof counts as a <strong>patio</strong>.</li>
</ul>

<h2>Building permit</h2>
<p>The City of Belmont needs a building permit for <strong>all</strong> patios, pergolas and shade sails, except:</p>
<div class="table-wrap"><table>
<thead><tr><th>Structure</th><th>No permit if</th></tr></thead><tbody>
<tr><td>Patio</td><td>Freestanding, under 2.4 m high and under 10 m²</td></tr>
<tr><td>Pergola or shade sail with a house</td><td>Under 20 m² and no more than 2.4 m high</td></tr>
</tbody></table></div>
<p>So any <strong>attached</strong> patio needs a permit, whatever its size. Even without a permit, the structure must still meet the National Construction Code.</p>

<h2>Planning (development) approval</h2>
<p>Most backyard patios in Belmont don't need planning approval. You need it if the patio, pergola or shade sail:</p>
<ul>
<li>is in the <strong>front setback</strong> and doesn't meet the standard R-Codes rules, or</li>
<li>is in a <strong>heritage area</strong> under Local Planning Scheme No. 15, or</li>
<li>is on a lot in a <strong>Special Development Precinct</strong>, or</li>
<li>is within or next to the <strong>Swan River Trust Development Control Area</strong> (generally properties near the river).</li>
</ul>
<p>If you need both, the City won't issue the building permit until planning approval is granted and its conditions are dealt with.</p>

<h2>What to lodge</h2>
<p>For a building permit:</p>
<ul>
<li>A <strong>BA1</strong> (certified, decided in 10 business days, with a BA3 from a registered building surveyor) or <strong>BA2</strong> (uncertified, 25 business days).</li>
<li>For a BA2: a site plan (at least 1:200) with setbacks, ground levels and easements; elevations and a floor plan (at least 1:100); and structural design certified by a registered structural engineer.</li>
<li>The fees, and a Construction Training Fund receipt if the work is over $100,000.</li>
</ul>
<p>For planning approval: the Application for Approval to Commence Development, a Certificate of Title no more than 6 months old, plans and the fees.</p>
<p>You can lodge online through the City's Planning and Building portal, in person at 215 Wright Street, Cloverdale, or by mail. Questions: 9477 7222.</p>
<p>Check your own patio with the <a href="/patio-approval-checker">patio approval checker</a>, or read about <a href="/shade-sail-approval-wa">shade sail approval</a> and <a href="/louvre-roof-approval">louvre roof approval</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a patio in the City of Belmont?",
     "Yes, unless it's freestanding, under 2.4 m high and under 10 m². Attached patios always need a building permit."),
    ("Do I need approval for a pergola or shade sail in Belmont?",
     "Not if it goes with a house, is under 20 m² and no more than 2.4 m high. Larger ones need a building permit."),
    ("When does a Belmont patio need planning approval?",
     "If it's in the front setback and doesn't meet the R-Codes, in a heritage area, in a Special Development Precinct, or within or next to the Swan River Trust Development Control Area."),
    ("Is a louvred roof a patio or a pergola in Belmont?",
     "Belmont treats an operable louvred roof as a pergola."),
]


def page(S):
    return {"path": "city-of-belmont-patio-rules.html", "published": "2026-11-16", "type": "Council guide", "icon": "pin",
            "card": "When a patio, pergola or shade sail in Belmont needs a building permit or planning approval.",
            "title": "City of Belmont Patio, Pergola and Shade Sail Rules (2026)",
            "desc": "City of Belmont patio rules: when patios, pergolas and shade sails need a building permit, when planning approval applies, and what to lodge.",
            "eyebrow": "Council guide", "h1": "City of Belmont patio, pergola and shade sail rules", "crumb": "Belmont patio rules",
            "answer": "<p>In Belmont, every patio needs a <strong>building permit</strong> unless it's freestanding, under <strong>2.4 m</strong> high and under <strong>10 m²</strong>. A pergola or shade sail is exempt if under <strong>20 m²</strong> and 2.4 m. <strong>Planning approval</strong> is only needed in the front setback, heritage areas, special precincts or near the Swan River.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-checker", "Patio approval checker"), ("/shade-sail-approval-wa", "Shade sail approval in WA"), ("/louvre-roof-approval", "Louvre roof approval")],
            "sources": [("Patio, pergola or shade sail, City of Belmont", "https://www.belmont.wa.gov.au/Build/Demolishing-and-Building/Approval-for-buildings-and-structures/I-want-to-build/Patio,-pergola-or-shade-sail"),
                        ("Patios, pergolas and shade sails fact sheet (July 2025), City of Belmont", "https://www.belmont.wa.gov.au/docs/ecm/building-surveying-fact-sheet-patios,-pergolas-shade-sails.pdf")]}
