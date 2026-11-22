BODY = """
<h2>Two approvals to think about</h2>
<p>A shed on a rural or rural residential lot can need two things:</p>
<ul>
<li><strong>Planning approval</strong> (development approval). Many shires let you skip this if the shed meets their outbuilding policy. If it doesn't, you apply and explain why.</li>
<li><strong>A building permit.</strong> Most sheds over 10 m² or 2.4 m high need one, rural or not. Genuine farm buildings are treated as a separate building type, but you usually still need a permit. Ask your shire.</li>
</ul>

<h2>What rural shed policies usually cover</h2>
<p>Each shire writes its own rules, so councils vary. The Shire of Northam's policy for its Rural Residential, Rural Smallholding and Rural zones is a good example of what to expect.</p>
<div class="table-wrap"><table>
<thead><tr><th>Lot size</th><th>Biggest single shed</th><th>All sheds combined</th></tr></thead><tbody>
<tr><td>Under 2 ha</td><td>200 m²</td><td>200 m²</td></tr>
<tr><td>2 to 5 ha</td><td>250 m²</td><td>250 m²</td></tr>
<tr><td>5 to 15 ha</td><td>300 m²</td><td>500 m²</td></tr>
<tr><td>15 to 40 ha</td><td>400 m²</td><td>750 m²</td></tr>
<tr><td>Over 40 ha</td><td>1,000 m²</td><td>Case by case</td></tr>
</tbody></table></div>
<p>Northam also sets wall heights from 4 m (within 20 m of a boundary) up to 5 m (50 m or more away). Sheds must sit inside any building envelope and not between the house and the road on Rural Residential lots.</p>

<h2>Common rural rules to check</h2>
<ul>
<li><strong>Shed before a house.</strong> Many shires won't approve a shed on a vacant rural residential lot unless the house is approved first or at the same time. Northam also asks for a $20,000 bank guarantee.</li>
<li><strong>Toilets and showers.</strong> Often only allowed if there's already a house on the lot.</li>
<li><strong>Living in it.</strong> Not allowed. A shed is not a house.</li>
<li><strong>Second-hand materials and colours.</strong> Northam needs planning approval for second-hand materials and asks for pre-painted wall sheeting in its rural residential zones.</li>
<li><strong>Farm sheds.</strong> On Rural-zoned land, Northam doesn't apply the size limits to sheds the Shire agrees are needed for farming.</li>
<li><strong>Bushfire.</strong> Rural lots are often bushfire prone. Put the shed in a cleared area and build to the bushfire standard where needed.</li>
</ul>

<h2>Steps</h2>
<ol>
<li>Find your lot's zone and any building envelope on your shire's map.</li>
<li>Read your shire's outbuilding policy for that zone.</li>
<li>If the shed meets it, apply for the building permit. If not, apply for planning approval first.</li>
<li>Lodge the permit with a site plan, shed plans and engineering.</li>
</ol>
<p>See the <a href="/shed-size-checker">shed size checker</a>, <a href="/shed-bushfire-area">sheds in bushfire areas</a> and <a href="/shed-planning-vs-building-permit">planning vs building permit</a>.</p>
"""

FAQS = [
    ("Do I need council approval for a shed on a farm in WA?",
     "Usually you need a building permit. Many shires don't ask for planning approval for sheds needed for farming on Rural-zoned land, but rules vary, so check with your shire first."),
    ("Can I build a shed on vacant rural land before the house?",
     "Often not on rural residential lots. Many shires, like Northam, need the house approved first or at the same time, and some ask for a bond."),
    ("How big can a shed be on a rural block?",
     "It depends on the shire and lot size. In the Shire of Northam it ranges from 200 m² on lots under 2 ha to 1,000 m² on lots over 40 ha."),
    ("Can I put a toilet in my rural shed?",
     "Usually only if there's already a house on the lot or the shed is for an approved use. You'll also need health approval for the wastewater system."),
]


def page(S):
    return {"path": "rural-shed-approval.html", "published": "2026-11-23", "type": "How-to guide", "icon": "shed",
            "card": "How to get a farm or rural shed approved in WA: size limits, sheds before a house, toilets and farm sheds.",
            "title": "How to Get a Rural or Farm Shed Approved in WA (2026)",
            "desc": "Rural and farm shed approval in WA: planning vs building permit, typical size limits by lot size, sheds on vacant land, toilets, farm sheds and bushfire rules, with Shire of Northam examples.",
            "eyebrow": "How-to guide", "h1": "How to get a rural or farm shed approved", "crumb": "Rural shed approval",
            "answer": "<p>Most rural sheds in WA still need a <strong>building permit</strong>. Planning approval is usually only needed if the shed breaks your shire's outbuilding policy, such as size, height, location or building before a house. Size limits grow with lot size. In the Shire of Northam they run from <strong>200 m²</strong> to <strong>1,000 m²</strong>. Councils vary, so check yours.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/shed-bushfire-area", "Sheds in bushfire areas"), ("/shed-planning-vs-building-permit", "Planning vs building permit")],
            "sources": [("Local Planning Policy 24: Outbuildings in the Rural Residential, Rural Smallholding and Rural zones, Shire of Northam", "https://www.northam.wa.gov.au/publicnotices/notice-of-adoption-of-amended-local-planning-policy-no-24-outbuildings-in-the-rural-residential-rural-smallholding-and-rural-zones/646/documents/lpp24-outbuildings-in-the-rr-rsh-and-rural-zones_v2.pdf")]}
