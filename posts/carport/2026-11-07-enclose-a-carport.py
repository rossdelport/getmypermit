BODY = """
<h2>A solid door turns a carport into a garage</h2>
<p>Councils use the R-Codes definitions. A <strong>carport</strong> must stay unenclosed, but it can have a see-through (visually permeable) door, like an open-mesh or slatted gate. Add a <strong>solid door</strong> and it's classed as a <strong>garage</strong>. Both the City of Joondalup and the City of Melville say this on their websites.</p>
<p>That matters because garages have stricter rules, especially on how far back from the street they must be.</p>

<h2>Carport vs garage setbacks</h2>
<p>Typical front setbacks before planning approval is needed:</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Carport</th><th>Garage</th></tr></thead><tbody>
<tr><td>Joondalup (R20)</td><td>3 m from the street the house faces</td><td>4.5 m, and 0.5 m behind the front of the house</td></tr>
<tr><td>Melville</td><td>3 m from the primary street</td><td>4.5 m from the primary street (3 m if the door is side-on and the street wall has windows)</td></tr>
</tbody></table></div>
<p>So a carport sitting 3 m from the street is fine as a carport. Put a solid roller door on it and it may no longer meet the garage setback. That usually means you need planning approval, and it may not be granted.</p>
<p>Councils also limit how much of the frontage a garage can take up, usually 50% for single-storey homes.</p>

<h2>Building permit</h2>
<p>Expect to need one. Joondalup says a building permit <strong>is</strong> required for building or converting a garage or carport. Adding walls and a door changes how the structure handles wind, so engineering may be needed too.</p>

<h2>Turning it into a room</h2>
<p>Converting a carport into a bedroom, office or living space is a bigger job. In Joondalup, planning approval is needed if:</p>
<ul>
<li>It's visible from the street and the materials don't match the house</li>
<li>A window or door to the new room is less than 1.5 m from a side or rear boundary</li>
<li>You'll no longer have the car parking the R-Codes need (usually two bays)</li>
</ul>
<p>The building permit for a room has extra rules, including a 2.4 m minimum ceiling height, stopping moisture and termites coming through the old carport floor, hardwired smoke alarms for all bedrooms, and moving any meter box to an outside wall.</p>

<h2>What to do</h2>
<ol>
<li>Decide whether you want a see-through door (stays a carport) or a solid one (becomes a garage).</li>
<li>Measure the setback from the street and compare it with your council's garage rule.</li>
<li>If it doesn't meet the rule, talk to your council about planning approval before buying a door.</li>
<li>Apply for the building permit.</li>
</ol>
<p>Learn more in <a href="/carport-vs-garage">carport vs garage</a>, check your setback with the <a href="/front-setback-carport-calculator">front setback carport calculator</a>, or see <a href="/carport-council-approval">carport council approval</a>.</p>
"""

FAQS = [
    ("Can I put a roller door on my carport in WA?",
     "You can, but a solid door makes it a garage under the R-Codes. Garages need a bigger street setback, usually 4.5 m, so you may need planning approval. A see-through door keeps it a carport."),
    ("Do I need approval to enclose a carport?",
     "Usually, yes. Expect a building permit, and planning approval if the enclosed structure doesn't meet the garage rules, such as the street setback."),
    ("What's the difference between a carport and a garage in WA?",
     "A carport is unenclosed, though it can have a see-through door. A garage is enclosed or has a solid door. Garages have stricter setback rules."),
    ("Can I convert my carport into a room?",
     "Yes, with approvals. You'll need a building permit, and planning approval if it affects street appearance, boundary setbacks or required car parking. The room needs a 2.4 m ceiling and moisture protection."),
]


def page(S):
    return {"path": "enclose-a-carport.html", "published": "2026-11-07", "type": "Question answer", "icon": "carport",
            "card": "Why a solid door makes it a garage, the setback trap, and converting to a room.",
            "title": "Can You Enclose a Carport in WA? Approval Rules",
            "desc": "Enclosing a carport in Perth: why a solid door makes it a garage, garage setbacks in Joondalup and Melville, permits, and converting a carport to a room.",
            "eyebrow": "Question answer", "h1": "Can you enclose a carport?", "crumb": "Enclosing a carport",
            "answer": "<p><strong>Yes, but it usually becomes a garage.</strong> A carport can have a see-through door, but a solid door makes it a garage under the R-Codes. Garages usually need to be <strong>4.5 m</strong> from the street instead of 3 m, so you may need planning approval. Expect a building permit either way.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-vs-garage", "Carport vs garage"), ("/front-setback-carport-calculator", "Front setback carport calculator"), ("/carport-council-approval", "Carport council approval")],
            "sources": [("Carport or garage and converting a garage to a habitable room (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/carport-or-garage-and-converting-a-garage-to-a-habitable-room"),
                        ("Building a carport or garage (City of Melville)", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-carport-or-garage")]}
