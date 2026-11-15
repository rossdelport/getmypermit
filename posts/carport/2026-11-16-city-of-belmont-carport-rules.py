BODY = """
<h2>What counts as a carport</h2>
<p>The City of Belmont defines a carport as a roofed structure for one or more cars that is <strong>open-sided</strong> (except where it meets the house or a boundary) and has <strong>no door</strong>, unless the door is visually permeable. Add a solid door and it's no longer a carport.</p>

<h2>Building permit</h2>
<p>Belmont needs a building permit for <strong>all carports</strong>, except one that is freestanding, under 2.4 m high and under 10 m². Since nearly every carport is bigger than 10 m², you should expect to need one.</p>

<h2>Planning (development) approval</h2>
<p>You need planning approval if the carport:</p>
<ul>
<li>doesn't meet the standard R-Codes rules, or</li>
<li>doesn't meet the City's Local Planning Scheme No. 15, or</li>
<li>is in a heritage area, a Special Precinct Development lot, or within or next to the Swan Canning Development Control Area (generally properties near the river).</li>
</ul>
<p>A carport in the <strong>front (primary street) setback</strong> also needs planning approval <strong>unless all four</strong> of these are true:</p>
<div class="table-wrap"><table>
<thead><tr><th>Requirement</th><th>What it means</th></tr></thead><tbody>
<tr><td>Open-sided</td><td>Only closed where it meets the house and one side boundary</td></tr>
<tr><td>See-through door</td><td>Any door lets you see through to the house</td></tr>
<tr><td>Matching roof</td><td>Roof pitch and colour match the house</td></tr>
<tr><td>More than 2.0 m back</td><td>Set more than 2 m from the front boundary</td></tr>
</tbody></table></div>
<p>If you need both approvals, the City won't issue the building permit until planning approval is granted and its conditions are dealt with.</p>

<h2>What to lodge</h2>
<ul>
<li>A <strong>BA1</strong> form with a BA3 certificate from a registered building surveyor, or a <strong>BA2</strong> form.</li>
<li>For a BA2: a site plan (at least 1:200) with setbacks, levels and easements; elevations and a floor plan (at least 1:100); and structural design certified by a registered structural engineer.</li>
<li>The fees, and a CTF receipt if the work is over $100,000.</li>
</ul>
<p>Lodge online through the City's Planning and Building portal, in person at 215 Wright Street, Cloverdale, or by mail.</p>
<p>Work out your street setback with the <a href="/front-setback-carport-calculator">front setback calculator</a>, see if a door changes things with the <a href="/carport-to-garage-checker">carport to garage checker</a>, or compare <a href="/carport-vs-garage">carport vs garage</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a carport in the City of Belmont?",
     "Yes. Belmont needs a building permit for all carports except freestanding ones under 2.4 m high and under 10 m²."),
    ("How close to the front boundary can a carport be in Belmont?",
     "Without planning approval, more than 2.0 m from the front boundary, if it's also open-sided, has a see-through door (if any) and a roof matching the house."),
    ("Can a Belmont carport have a door?",
     "Only a visually permeable one. A solid door means it's not a carport under Belmont's definition."),
    ("How do I lodge a carport application in Belmont?",
     "Online through the City's Planning and Building portal, in person at 215 Wright Street, Cloverdale, or by mail."),
]


def page(S):
    return {"path": "city-of-belmont-carport-rules.html", "published": "2026-11-16", "type": "Council guide", "icon": "pin",
            "card": "When a carport in Belmont needs a building permit or planning approval, including the 2 m front rule.",
            "title": "City of Belmont Carport Rules (2026)",
            "desc": "City of Belmont carport rules: building permit for almost all carports, the four tests for a front setback carport (incl. 2 m from the boundary), and what to lodge.",
            "eyebrow": "Council guide", "h1": "City of Belmont carport rules", "crumb": "Belmont carport rules",
            "answer": "<p>In Belmont, almost every carport needs a <strong>building permit</strong>. A carport in the front setback can skip <strong>planning approval</strong> only if it's open-sided, any door is see-through, the roof matches the house, and it's more than <strong>2.0 m</strong> from the front boundary.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/front-setback-carport-calculator", "Front setback calculator"), ("/carport-to-garage-checker", "Carport to garage checker"), ("/carport-vs-garage", "Carport vs garage")],
            "sources": [("Carport, City of Belmont", "https://www.belmont.wa.gov.au/Build/Demolishing-and-Building/Approval-for-buildings-and-structures/I-want-to-build/Carport")]}
