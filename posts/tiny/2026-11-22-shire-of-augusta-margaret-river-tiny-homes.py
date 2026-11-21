BODY = """
<h2>What the Shire allows</h2>
<p>Since the state's caravan and camping rules changed on <strong>1 September 2024</strong>, the Shire of Augusta Margaret River can approve:</p>
<ul>
<li><strong>Living in a tiny home on wheels</strong> on private land, for up to 24 months at a time.</li>
<li><strong>Camping in one caravan while you build a house</strong>, once the house has a building permit, on R5 or lower residential lots and rural-type zones.</li>
</ul>

<h2>What counts as a tiny home on wheels</h2>
<p>For the Shire, a tiny home on wheels is up to <strong>50 m²</strong>, built on a trailer, looks and works like a house, and is lived in <strong>permanently</strong>. It is not a short-term rental, and not a bus, van, tent or yurt.</p>

<h2>Where it can go</h2>
<ul>
<li>On a lot that <strong>already has a house</strong>, where a granny flat could otherwise be approved under the R-Codes or the zone rules.</li>
<li>In a bushfire-prone area, only where the spot is rated <strong>BAL-29 or lower</strong>.</li>
<li>Inside any approved building envelope, and grouped with the existing buildings, sharing the driveway, water and waste systems where possible.</li>
</ul>

<h2>What to send</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Details</th></tr></thead><tbody>
<tr><td>Application form</td><td>Signed by you and the landowner, with the fee</td></tr>
<tr><td>Site plan to scale</td><td>Boundaries, north point, where it's parked, setbacks, water supply, wastewater, power and other buildings</td></tr>
<tr><td>Floor plan and elevations</td><td>Floor area, toilet and laundry, heights and external colours and materials</td></tr>
<tr><td>Planning check</td><td>Confirmation from the Shire's planners that it meets the granny flat exemption for your zone</td></tr>
<tr><td>BAL assessment</td><td>If you're in a bushfire-prone area</td></tr>
</tbody></table></div>
<p>A toilet, shower and laundry must be available that meet the building code and health rules. An on-site wastewater system needs a Shire "permit to use".</p>

<h2>After you apply</h2>
<p>If the Shire hasn't approved it within <strong>63 days</strong>, it's taken as refused. If it refuses, you can apply to the Minister for Local Government. You also need the Minister's approval for more than one caravan on a lot. The Shire can add conditions and can cancel an approval if they're broken. Call the Shire on (08) 9780 5255.</p>
<p>Read <a href="/tiny-home-council-application">how to apply to your council</a>, <a href="/tiny-home-services">connecting services to a tiny home</a>, or <a href="/wheels-vs-fixed-tiny-home">wheels vs fixed</a>.</p>
"""

FAQS = [
    ("Can I live in a tiny home in Margaret River?",
     "Yes, with Shire approval, on a lot that already has a house, for up to 24 months at a time. It must be up to 50 m² and lived in permanently."),
    ("Can I Airbnb a tiny home on wheels in Augusta Margaret River?",
     "Not under this approval. The Shire's tiny home rules are for permanent living, not short-term rental."),
    ("Can I live in a caravan while I build in Margaret River?",
     "Yes, in one caravan, once your house has a building permit, on R5 or lower residential lots and rural-type zones."),
    ("How long does the Shire take to decide?",
     "If it hasn't approved your application within 63 days, it's taken as refused, and you can apply to the Minister."),
]


def page(S):
    return {"path": "shire-of-augusta-margaret-river-tiny-homes.html", "published": "2026-11-22", "type": "Council guide", "icon": "pin",
            "card": "Shire of Augusta Margaret River tiny homes: the 50 m² limit, where they can go and what to send.",
            "title": "Shire of Augusta Margaret River Tiny Home Rules (2026)",
            "desc": "Tiny homes on wheels in the Shire of Augusta Margaret River: the 50 m² limit, lots that already have a house, BAL-29, what to send with your application and the 63-day rule.",
            "eyebrow": "Council guide", "h1": "Shire of Augusta Margaret River tiny home rules", "crumb": "Augusta Margaret River tiny homes",
            "answer": "<p>The Shire of Augusta Margaret River can approve living in a <strong>tiny home on wheels</strong> for up to <strong>24 months</strong>, on a lot that already has a house. It must be up to <strong>50 m²</strong>, lived in permanently (not a short-term rental), and at <strong>BAL-29 or lower</strong> in bushfire areas.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-council-application", "Applying to your council"), ("/tiny-home-services", "Tiny home services"), ("/wheels-vs-fixed-tiny-home", "Wheels vs fixed tiny home")],
            "sources": [("Camping on private property and tiny homes on wheels, Shire of Augusta Margaret River", "https://www.amrshire.wa.gov.au/planning-and-building/health-and-safety-(buildings-and-property)/camping-on-private-property-and-tiny-homes-on-wheels"),
                        ("Information sheet: camping on private property and tiny homes on wheels, Shire of Augusta Margaret River", "https://www.amrshire.wa.gov.au/getattachment/cca28a87-0ad4-441b-89fa-007b7996a2df/Information-Sheet.pdf"),
                        ("Application form and checklist for living in a tiny house on wheels, Shire of Augusta Margaret River", "https://www.amrshire.wa.gov.au/getattachment/32ef6f75-22c5-4cd9-9ce7-fada488fda71/Application-form-and-Checklist-for-THOW.pdf")]}
