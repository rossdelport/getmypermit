BODY = """
<h2>Why enclosing changes everything</h2>
<p>The R-Codes define a patio as "an unenclosed structure covered in a water impermeable material", attached to the house or not. All the patio rules, including the setbacks and the building permit exemptions, are written for that open structure.</p>
<p>Put walls, windows or doors around it and it is no longer a patio. It becomes part of the house (a sunroom, games room or extra living area) or an enclosed outbuilding, and it is assessed that way.</p>

<h2>What you'll need</h2>
<div class="table-wrap"><table>
<thead><tr><th>Approval</th><th>Needed when enclosing a patio?</th></tr></thead><tbody>
<tr><td>Building permit</td><td><strong>Yes</strong>, in almost every case. Any patio attached to the house already needs one, and new walls, windows and doors are building work.</td></tr>
<tr><td>Planning (development) approval</td><td><strong>Often.</strong> Needed if the enclosed room breaks the R-Codes standards, such as setbacks, open space or the outdoor living area, or the property is heritage-listed.</td></tr>
<tr><td>Building code (NCC) compliance</td><td><strong>Yes.</strong> A room you live in must meet the rules for habitable rooms, such as light, ventilation, ceiling height, energy efficiency and waterproofing where needed.</td></tr>
</tbody></table></div>

<h2>The planning rules that usually bite</h2>
<ul>
<li><strong>Setbacks.</strong> An open patio can often sit 1 m from the side fence, or even have its posts on the boundary in some cases. An enclosed room has to meet the setbacks for walls of the house, which can be larger, especially with windows facing the neighbour.</li>
<li><strong>Outdoor living area.</strong> The R-Codes require each house to keep a usable outdoor living area. If your patio <em>is</em> that area, enclosing it can leave you short.</li>
<li><strong>Open space.</strong> Every R-Code sets a minimum share of the lot to stay open. Turning the patio into a room adds to the built area and can push a small lot over the limit.</li>
<li><strong>Privacy.</strong> A raised floor (more than 0.5 m above the ground) with windows looking over a neighbour brings in privacy setbacks or screening.</li>
</ul>

<h2>What about blinds and screens?</h2>
<p>Outdoor blinds, café blinds and fly screens are a grey area. Councils don't all treat them the same way, and the answer can depend on whether they are fixed or roll away. Before you buy, ask your council whether your setup still counts as "unenclosed". Fixed walls, glass panels, windows or doors on all sides clearly enclose it.</p>

<h2>Already enclosed it?</h2>
<p>You're not alone, and it can usually be fixed. A registered building surveyor inspects the work and issues a certificate of building compliance, then your council issues a building approval certificate. If the room breaks a planning rule, retrospective planning approval comes first. We handle both.</p>

<h2>How we'd approach it</h2>
<ol>
<li>Check your lot's R-Code, open space and outdoor living area with the patio enclosed.</li>
<li>Check the setbacks for the new walls and windows.</li>
<li>Prepare drawings showing the enclosure, plus engineering for any new loads on the patio frame.</li>
<li>Lodge planning approval first if needed, then the building permit.</li>
</ol>
"""

FAQS = [
    ("Can I enclose my patio without council approval in WA?",
     "Almost never. Enclosing a patio is building work that needs a building permit, and it often needs planning approval too because an enclosed room has to meet different setback and open space rules."),
    ("Does an enclosed patio count as a room?",
     "Yes. Once it has walls, windows or doors, it is no longer a patio under the R-Codes. If you use it as living space, it must meet the building code's rules for habitable rooms."),
    ("Do I need approval for patio blinds?",
     "Councils treat blinds differently. Roll-down outdoor blinds may be fine, but fixed walls, glass or doors on all sides enclose the patio. Check with your council before installing."),
    ("Can my existing patio frame hold walls and windows?",
     "Not always. A patio frame is designed for a roof, not walls and glazing. The building permit will need an engineer to check the frame and footings."),
]


def page(S):
    return {"path": "enclose-a-patio-approval.html", "published": "2026-10-30", "type": "Question answer", "icon": "pergola",
            "card": "Why enclosing a patio needs a building permit, when it needs planning approval too, and what to know about blinds.",
            "title": "Can You Enclose a Patio Without Council Approval in WA?",
            "desc": "Enclosing a patio in WA almost always needs a building permit, and often planning approval. Why the rules change once it has walls, the R-Codes traps, and what about blinds.",
            "eyebrow": "Question answer", "h1": "Can you enclose a patio without council approval?", "crumb": "Enclosing a patio",
            "answer": "<p>Almost never. Under the R-Codes a patio is an <strong>unenclosed</strong> structure. Add walls, windows or doors and it becomes part of the house, so you need a <strong>building permit</strong>, and often <strong>planning approval</strong> too, because the setback, open space and outdoor living area rules change.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-building-permit", "Patio building permits"), ("/patio-approval-cost-perth", "Patio approval cost in Perth"), ("/do-i-need-council-approval-for-a-pergola", "Do I need approval for a pergola?")],
            "sources": [("Patios in residential areas (City of Vincent, May 2024)", "https://vincent.wa.gov.au/Profiles/vincent/Assets/ClientData/Planning_Information_Sheets/2024/Planning_Information_Sheet_Patios_May2024.pdf"),
                        ("Patios information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf")]}
