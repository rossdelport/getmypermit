BODY = """
<p>WA's Building Regulations 2012 (Schedule 4) list the small jobs that don't need a building permit. Councils apply the same state list, so the limits below are the same across Perth. Here they are in plain English, using the City of Gosnells' summary of the list.</p>

<h2>The exemption list</h2>
<div class="table-wrap"><table>
<thead><tr><th>Work</th><th>No building permit needed if</th></tr></thead><tbody>
<tr><td>Shed, patio or gazebo</td><td>Freestanding, <strong>10 m&sup2; or less</strong> and <strong>2.4 m tall or less</strong></td></tr>
<tr><td>Shade sail or pergola (open, no solid roof) next to a house</td><td><strong>20 m&sup2; or less</strong> and 2.4 m tall or less</td></tr>
<tr><td>Colorbond or fibre cement dividing fence</td><td><strong>2 m high or less</strong> and not forward of the house</td></tr>
<tr><td>Rainwater tank</td><td><strong>5,000 litres or less</strong></td></tr>
<tr><td>Solar panels or hot water system on a house or its outbuilding</td><td>Always exempt, unless the roof needs structural changes or a stand to hold them</td></tr>
<tr><td>Freestanding mast, antenna or flagpole</td><td><strong>3 m tall or less</strong> (2 m above the roof if attached to a building)</td></tr>
<tr><td>Cosmetic renovations</td><td>Cabinetry, new benchtops, painting and non-structural repairs</td></tr>
<tr><td>Roof-mounted evaporative air conditioner in a bushfire-prone area</td><td>BAL-Low, or BAL-12.5 to BAL-29 with a unit that meets the bushfire standard</td></tr>
<tr><td>Demolishing a patio, shed, pool or similar</td><td><strong>40 m&sup2; or less</strong>, no asbestos risk and not heritage-protected (no demolition permit)</td></tr>
</tbody></table></div>

<h2>Things that always need a permit</h2>
<ul>
<li><strong>Any swimming pool or spa</strong> that can hold 30 cm of water or more, including portable and inflatable pools.</li>
<li><strong>Any pool safety fence</strong>, whatever its height or material.</li>
<li><strong>Anything attached to the house</strong>, such as a patio, carport or verandah, at any size.</li>
<li><strong>Garages, carports and granny flats.</strong></li>
<li><strong>Structural changes</strong>, such as removing a load-bearing wall or adding a room.</li>
</ul>

<h2>"Exempt" doesn't mean "no rules"</h2>
<p>This catches a lot of people. An exemption only means you don't need a <em>building permit</em>. As the City of Gosnells puts it, exemption "does not negate the need for other required approvals, such as Development Approval and Health Approval, or the need to comply with statutory requirements, such as the National Construction Code and the Residential Design Codes".</p>
<p>So a small exempt shed still has to sit the right distance from your fence, stay out of the front yard and be built properly. If it breaks a planning rule, it needs planning approval even though it needs no building permit. Nobody signs off exempt work, so getting it right is up to you.</p>

<h2>Is there a 7-year rule?</h2>
<p>No. WA has no rule that makes unapproved work legal after 7 years (or any number of years). Work done without a required permit stays unauthorised until it is approved. The fix is a <a href="/retrospective-approval">building approval certificate</a>, which a registered building surveyor inspects and certifies.</p>

<h2>Not sure?</h2>
<p>Use our <a href="/do-i-need-approval">20-second approval checker</a>, or the <a href="/which-ba-form">form finder</a> if you already know you need a permit.</p>
"""

FAQS = [
    ("What's the biggest shed I can build without a permit in WA?",
     "A freestanding shed with a floor area of 10 m&sup2; or less and no taller than 2.4 m. That is about 3 m x 3.3 m. Anything bigger, taller or attached needs a building permit."),
    ("Do I need a permit for a pergola in WA?",
     "Not for an open pergola (no solid roof, or only shade cloth) next to a house if it is 20 m&sup2; or less and 2.4 m tall or less. A pergola or patio with a solid roof follows the 10 m&sup2; rule instead."),
    ("Do I need a permit for a Colorbond fence?",
     "Usually not for a dividing fence up to 2 m high that doesn't come forward of the house. Front fences, fences over 2 m, retaining under a fence and any pool fence can need one."),
    ("Do I need a permit to put solar panels on my roof?",
     "No building permit for panels on a house or its outbuilding, as long as the roof doesn't need structural changes and the panels don't need a stand or frame that changes the structure."),
]


def page(S):
    return {"path": "what-doesnt-need-a-building-permit.html", "published": "2026-10-30", "type": "Question answer", "icon": "check",
            "card": "The full list of small jobs that don't need a building permit in WA, with the size limits, and what still needs approval.",
            "title": "What Doesn't Need a Building Permit in WA? The Exemption List (2026)",
            "desc": "Sheds and patios up to 10 m² and 2.4 m, open pergolas up to 20 m², dividing fences up to 2 m, tanks up to 5,000 L: the full WA building permit exemption list in plain English.",
            "eyebrow": "Question answer", "h1": "What doesn't need a building permit in WA?", "crumb": "What doesn't need a building permit?",
            "answer": "<p>In WA you don't need a building permit for a <strong>freestanding shed, patio or gazebo up to 10 m&sup2; and 2.4 m tall</strong>, an <strong>open pergola or shade sail up to 20 m&sup2;</strong>, a <strong>dividing fence up to 2 m</strong>, a <strong>rainwater tank up to 5,000 L</strong>, solar panels and cosmetic renovations. Pools, pool fences and anything attached to the house always need one. Planning rules still apply to exempt work.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/do-i-need-approval", "Do I need council approval? (checker)"), ("/which-ba-form", "Which BA form do I need?"), ("/retrospective-approval", "Retrospective approval")],
            "sources": [("Do I need a permit? (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit"),
                        ("Patios in residential areas, quoting Schedule 4 of the Building Regulations 2012 (City of Vincent)", "https://vincent.wa.gov.au/Profiles/vincent/Assets/ClientData/Planning_Information_Sheets/2024/Planning_Information_Sheet_Patios_May2024.pdf"),
                        ("Building approvals (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
