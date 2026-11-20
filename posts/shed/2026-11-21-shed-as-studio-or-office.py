BODY = """
<h2>Why a studio isn't "just a shed"</h2>
<p>The R-Codes use the building code's meaning of a <strong>habitable room</strong>: a room for normal domestic activities. The list includes a <strong>study</strong>, <strong>music room</strong>, <strong>gymnasium</strong>, sewing room, playroom, living room and bedroom.</p>
<p>A shed is a Class 10a building, which is <strong>non-habitable</strong>. So if you fit it out and use it as a studio, office or gym, it's being used as a habitable room, and the shed rules no longer fit.</p>

<h2>What that means for approvals</h2>
<div class="table-wrap"><table>
<thead><tr><th>Approval</th><th>What usually applies</th></tr></thead><tbody>
<tr><td>Building permit</td><td>Needed for a change of use, for example "shed or garage to habitable building or habitable room" (Town of Cottesloe list)</td></tr>
<tr><td>Building standards</td><td>The building must meet the rules for its new use, not shed rules</td></tr>
<tr><td>Planning approval</td><td>Under the R-Codes an outbuilding is non-habitable, so the shed exemptions may not apply. Councils vary, so ask yours</td></tr>
</tbody></table></div>

<h2>What usually has to be upgraded</h2>
<p>The City of Albany's guide to turning a shed into a habitable building lists what it checks. Other councils are similar:</p>
<ul>
<li>A structural engineer's check of the slab (including a waterproof membrane underneath) and that the frame can carry wall and ceiling linings.</li>
<li>Ceilings at least <strong>2.4 m</strong> high.</li>
<li>Windows at least <strong>10%</strong> of the floor area for light, and openings at least <strong>5%</strong> for fresh air.</li>
<li>Hardwired smoke alarms, insulation, energy-efficiency measures and safety glass where needed.</li>
<li>Wiring to residential standards, and a termite certificate for timber.</li>
</ul>
<p>Adding a kitchen, bathroom and bed turns it into a dwelling, which is a bigger step again.</p>

<h2>What about running a business from it?</h2>
<p>That's a separate planning question. The City of Stirling, for example, says a home office or home occupation doesn't need planning approval, but a home business does. The building rules above still apply to the shed itself.</p>
<p>Read <a href="/what-is-a-class-10a-building">what Class 10a means</a>, <a href="/toilet-or-shower-in-a-shed">adding a toilet or shower to a shed</a>, or <a href="/how-to-get-a-shed-permit">how to get a shed permit</a>.</p>
"""

FAQS = [
    ("Can I use my shed as a home office in WA?",
     "Not as a plain shed. A study or office is a habitable room, and a shed is non-habitable, so it usually needs a building permit and upgrades to meet the rules for habitable rooms."),
    ("Is a home gym in a shed allowed?",
     "The R-Codes list a gymnasium as a habitable room, so the same rules apply as for a studio or office."),
    ("What ceiling height does a habitable room need?",
     "Usually at least 2.4 m. That's a common problem with sheds."),
    ("Can I just store things and do hobbies in my shed?",
     "Using a shed for storage is what it's approved for. If you fit it out and use it like a room of the house, ask your council first."),
]


def page(S):
    return {"path": "shed-as-studio-or-office.html", "published": "2026-11-21", "type": "Question answer", "icon": "shed",
            "card": "Can you use a shed as a studio, home office or gym in WA? What the rules say.",
            "title": "Can I Use My Shed as a Studio or Home Office? (WA)",
            "desc": "Using a shed as a studio, home office or gym in WA: why it counts as a habitable room, the building permit you usually need, and what has to be upgraded.",
            "eyebrow": "Question answer", "h1": "Can I use my shed as a studio or home office?", "crumb": "Shed as a studio or office",
            "answer": "<p><strong>Not as a plain shed.</strong> A study, studio or gym is a <strong>habitable room</strong>, and a shed is approved as <strong>non-habitable</strong>. To use it that way you usually need a building permit for the change of use, and upgrades such as a <strong>2.4 m</strong> ceiling, light, ventilation, insulation and smoke alarms.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/what-is-a-class-10a-building", "What is a Class 10a building?"), ("/toilet-or-shower-in-a-shed", "Toilet or shower in a shed"), ("/how-to-get-a-shed-permit", "How to get a shed permit")],
            "sources": [("Residential Design Codes Volume 1 (definitions), WAPC", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Change of classification: habitable sheds, City of Albany", "https://www.albany.wa.gov.au/documents/13708/change-of-classification-class10a-to-class-1a-(habitable-sheds)"),
                        ("Do I need a building permit?, Town of Cottesloe", "https://www.cottesloe.wa.gov.au/Profiles/cottesloe/Assets/ClientData/Do-I-need-a-Building-Permit.pdf"),
                        ("Where do I start?, City of Stirling", "https://www.stirling.wa.gov.au/developing-property/planning-advice/develop-your-property/where-do-i-start")]}
