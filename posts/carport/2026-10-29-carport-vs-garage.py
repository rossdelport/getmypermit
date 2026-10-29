BODY = """
<h2>Side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Carport</th><th>Garage</th></tr></thead><tbody>
<tr><td>What it is (R-Codes)</td><td>A roof for cars, open except where it meets the house or one boundary, with no door unless the door is see-through</td><td>Any other roofed structure for cars that is attached to the house</td></tr>
<tr><td>Building permit</td><td>Always</td><td>Always</td></tr>
<tr><td>Distance from the street</td><td>Can usually be about half the normal setback (e.g. 3 m on an R20 lot instead of 6 m)</td><td>Usually 4.5 m, or closer if at least 0.5 m behind the front of the house</td></tr>
<tr><td>Width across the front</td><td>Up to 60% of the lot frontage</td><td>Garage doors are limited too, often to around half the frontage</td></tr>
<tr><td>Next to a side boundary</td><td>Posts usually 1 m from the boundary; some councils allow posts on the boundary for short carports</td><td>Can be a boundary wall on many lots (R20 and above), within length and height limits</td></tr>
<tr><td>Fire rules near the boundary</td><td>Can be as close as 500 mm if it is open enough and non-combustible</td><td>Fire-rated wall needed when close to the boundary</td></tr>
<tr><td>Door</td><td>Only a see-through door</td><td>Any door</td></tr>
<tr><td>Cost to build</td><td>Usually much less</td><td>More: slab, walls, door and often fire-rated wall</td></tr>
</tbody></table></div>

<h2>The big difference: how close to the street</h2>
<p>Planning rules keep the front of the house open so the street looks good and is safe. Because a carport is open and you can see through it, it is allowed much closer to the street than a garage.</p>
<p>The City of Wanneroo's carport rules spell it out: on an R20 lot the normal street setback is 6 m (4 m on R30 or R40), and a carport can go at half that, as long as it is <strong>no wider than 60% of the frontage</strong>, you can <strong>see between the house and the street</strong>, and the materials suit the house. A garage, by contrast, usually has to sit 4.5 m back, or at least 0.5 m behind the front wall of the house (City of Stirling).</p>
<p>That is why so many Perth homes add a carport in front of the house rather than a garage. If you need to park in front of the house, a carport is often the only way to do it without planning approval.</p>

<h2>Both need a building permit</h2>
<p>Whichever you choose, you need a building permit before work starts. Wanneroo says a building permit is "always required for carports", and Stirling says the same for carports and garages. Planning approval is needed on top when the design breaks the standard rules, or the property is in a heritage area.</p>

<h2>Turning a carport into a garage</h2>
<p>Adding a solid roller door or enclosing the sides turns a carport into a garage under the planning rules. A carport built close to the street could then break the garage setback, and the change needs approval. If you want security, a see-through door (such as an open slat or mesh tilt door) keeps it a carport.</p>

<h2>Minimum sizes</h2>
<p>The City of Stirling's sheet gives the sizes it checks: a single carport or garage at least <strong>5.4 m long and 2.4 m wide</strong> (3 m if next to a wall or post), and a double at least <strong>5.4 m by 4.8 m</strong> (5.4 m wide next to a wall). Design to these and you avoid a common reason for planning questions.</p>

<h2>Which should you choose?</h2>
<ul>
<li><strong>Choose a carport</strong> if you need to park in front of the house, want the lower cost, or have a narrow side setback.</li>
<li><strong>Choose a garage</strong> if you need security and storage and have room behind the front of the house.</li>
<li><strong>Not sure?</strong> Tell us your address and we'll tell you what your council allows on your lot before you buy anything.</li>
</ul>
"""

FAQS = [
    ("Is a carport cheaper to approve than a garage?",
     "The council fees work the same way for both: 0.32% of the value for an uncertified application, at least $121, plus the Building Services Levy. Because a carport usually costs less to build, its fees are often at the minimum. A garage is more likely to need planning approval because of street setbacks."),
    ("Can I put a roller door on my carport in WA?",
     "Only a see-through (visually permeable) door keeps it a carport. A solid door makes it a garage under the planning rules, which may then need planning approval."),
    ("Does a carport need planning approval?",
     "Not if it meets the standard rules for setbacks, width, open space and views, and isn't on a heritage property. Otherwise, yes, before the building permit."),
    ("Is a detached garage a garage or a shed?",
     "Under the R-Codes, a garage is attached to the house. A freestanding garage is usually assessed as an outbuilding, with the outbuilding size and height limits."),
]


def page(S):
    return {"path": "carport-vs-garage.html", "published": "2026-10-29", "type": "Comparison", "icon": "car",
            "card": "How carports and garages differ on approval, street setbacks, boundaries, doors and cost in Perth.",
            "title": "Carport vs Garage in WA: Approval, Setbacks and Cost Compared",
            "desc": "Carport or garage? Both need a building permit in WA, but carports can usually sit much closer to the street. Setbacks, boundaries, doors and cost compared.",
            "eyebrow": "Comparison", "h1": "Carport vs garage", "crumb": "Carport vs garage",
            "answer": "<p>Both need a <strong>building permit</strong> in WA. The big difference is planning: an open carport can usually be built at <strong>half the normal street setback</strong> if it is no wider than 60% of the frontage, while a garage usually has to be <strong>4.5 m back</strong> or behind the front of the house. Add a solid door and a carport becomes a garage.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-in-front-setback", "Carports in the front setback"), ("/carport-council-approval", "Carport council approval"), ("https://shedbuildingpermit.com.au/garage-building-permit", "Garage building permits")],
            "sources": [("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf"),
                        ("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf")]}
