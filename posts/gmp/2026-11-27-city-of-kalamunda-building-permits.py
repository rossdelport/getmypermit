BODY = """
<h2>What needs a building permit in Kalamunda</h2>
<p>The City of Kalamunda's building information sheet (updated July 2026) says you need a building permit from the City for:</p>
<div class="table-wrap"><table>
<thead><tr><th>Work</th><th>Permit needed?</th></tr></thead><tbody>
<tr><td>Houses, including granny flats and tiny houses</td><td>Yes</td></tr>
<tr><td>Additions or alterations to a house or outbuilding</td><td>Yes</td></tr>
<tr><td>Turning a space into a habitable room</td><td>Yes</td></tr>
<tr><td>Carports and garages</td><td>Yes</td></tr>
<tr><td>Earthworks</td><td>Yes</td></tr>
<tr><td>Demolishing or removing a building</td><td>Yes</td></tr>
<tr><td>Swimming pools and spas</td><td>Yes</td></tr>
<tr><td>Patios, pergolas, vergolas and shade sails</td><td>Yes, some exemptions apply</td></tr>
<tr><td>Sheds</td><td>Yes, some exemptions apply</td></tr>
<tr><td>Retaining walls</td><td>500 mm high or more</td></tr>
<tr><td>Fences, non-masonry</td><td>Over 1.8 m high</td></tr>
<tr><td>Fences, masonry</td><td>Over 750 mm high</td></tr>
<tr><td>Water tanks</td><td>Over 5,000 litres</td></tr>
</tbody></table></div>
<p>Repairs and maintenance listed in Schedule 4 of the Building Regulations 2012 usually don't need a permit, but the owner still has to make sure the work meets the building standards. See <a href="/what-doesnt-need-a-building-permit">what doesn't need a building permit</a>.</p>

<h2>Other approvals you might need first</h2>
<ul>
<li><strong>Planning (development) approval</strong> from the City's planners.</li>
<li><strong>Health approval</strong> for an effluent (septic) system on unsewered land, common in the hills.</li>
</ul>
<p>It's up to you to get these before you lodge the building application, and your building plans must match them.</p>

<h2>Turning a room into living space</h2>
<p>Kalamunda has a checklist for converting a patio, shed, carport or garage into a habitable room. It includes a 2.4 m lined ceiling, a damp-proof floor, windows of at least a tenth of the floor area, ventilation and energy efficiency.</p>

<h2>How to apply</h2>
<p>Lodge a BA1 (certified by a private building surveyor) or BA2 (checked by the City) with the documents on the City's building checklist. Building Services is on 08 9257 9999. See <a href="/which-ba-form">which BA form you need</a> and <a href="/demolition-permit-wa">demolition permits</a>.</p>
"""

FAQS = [
    ("Do I need a building permit for a tiny house in Kalamunda?",
     "Yes. The City of Kalamunda lists dwellings, including granny flats and tiny houses, as needing a building permit."),
    ("What fence height needs a permit in Kalamunda?",
     "Non-masonry fences over 1.8 m and masonry fences over 750 mm need a building permit."),
    ("Do retaining walls need a permit in Kalamunda?",
     "Yes, if they are 500 mm high or more."),
    ("Does a water tank need a permit in Kalamunda?",
     "Only if it holds more than 5,000 litres."),
]


def page(S):
    return {"path": "city-of-kalamunda-building-permits.html", "published": "2026-11-27", "type": "Council guide", "icon": "pin",
            "card": "City of Kalamunda building permits: what needs one, fence and wall heights, and approvals you need first.",
            "title": "City of Kalamunda Building Permits (2026 Guide)",
            "desc": "City of Kalamunda building permits: which projects need a permit (including tiny houses, carports and earthworks), fence, retaining wall and water tank limits, planning and health approvals, and how to apply.",
            "eyebrow": "Council guide", "h1": "City of Kalamunda building permits", "crumb": "City of Kalamunda",
            "answer": "<p>In the City of Kalamunda, you need a building permit for houses (including <strong>granny flats and tiny houses</strong>), carports, garages, pools, earthworks and demolition. Retaining walls need one from <strong>500 mm</strong>, masonry fences over <strong>750 mm</strong> and other fences over <strong>1.8 m</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/what-doesnt-need-a-building-permit", "What doesn't need a building permit?"), ("/which-ba-form", "Which BA form do I need?"), ("/demolition-permit-wa", "Demolition permits in WA")],
            "sources": [("Information sheet 1: building applications (July 2026), City of Kalamunda", "https://www.kalamunda.wa.gov.au/docs/default-source/building/information-sheets/1bldinfosheet-faq.pdf?sfvrsn=97937ff3_24"),
                        ("Information sheet 3: converting into a habitable room, City of Kalamunda", "https://www.kalamunda.wa.gov.au/docs/default-source/building/information-sheets/3bldinfosheet.pdf?sfvrsn=f0dad063_28")]}
