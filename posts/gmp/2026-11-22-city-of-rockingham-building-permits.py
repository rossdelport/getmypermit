BODY = """
<h2>BA1 or BA2?</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>BA1 (certified)</th><th>BA2 (uncertified)</th></tr></thead><tbody>
<tr><td>Who checks the plans</td><td>A private building surveyor, who signs a Certificate of Design Compliance (BA3) first</td><td>The City's building surveyors, who issue the BA3 with the permit</td></tr>
<tr><td>What you lodge</td><td>BA1, BA3 and the drawings listed on the BA3</td><td>BA2, site plan, floor plans, elevations, sections, construction details and engineering</td></tr>
<tr><td>City's decision time</td><td>10 business days</td><td>25 business days</td></tr>
</tbody></table></div>
<p>All commercial building permits in Rockingham must be certified (BA1).</p>

<h2>What needs a permit</h2>
<p>The City lists fences, pools, spas and barriers, garden sheds, verandahs, gazebos, garages, workshops, pergolas, houses, retaining walls and changes to ground levels (cut and fill). Some small work is exempt under the state Building Regulations 2012, such as a freestanding shed of 10 m² or less and 2.4 m or less high.</p>
<p>If the work is worth more than <strong>$20,000</strong>, the permit is issued to a registered builder or an approved owner-builder. Since 1 July 2026, the limit for a shed, garage or carport is <strong>$50,000</strong>.</p>

<h2>What goes in a BA2</h2>
<ul>
<li>A site plan at 1:200 or larger, with spot levels, all existing buildings, boundary setbacks, any septic system and a north point.</li>
<li>Floor plans, elevations and sections at 1:100, with all dimensions.</li>
<li>Construction details showing all materials and sizes.</li>
<li>Structural details designed and certified by a practising structural engineer.</li>
</ul>
<p>Fees are paid when you lodge. You can lodge online through the City's <strong>Rock Port</strong> portal, in person at the Civic Boulevard office, or by post.</p>

<h2>Planning approval first?</h2>
<p>Most houses and home projects on residential lots only need a building permit if they meet the R-Codes. But any development on <strong>Special Residential</strong> or <strong>Special Rural</strong> land needs Town Planning consent first, including changes to a building envelope. Commercial, industrial and three or more grouped dwellings also need a development application.</p>

<h2>Time limits and after you build</h2>
<ul>
<li>A permit usually lasts <strong>2 years</strong>. Rockingham's page says it's void if work hasn't started within 12 months.</li>
<li>The builder must lodge a <strong>BA7 notice of completion</strong> within <strong>7 days</strong> of finishing.</li>
<li>Copies of old building plans cost $60 for a residential set or $25 per plan, and can take up to 10 working days.</li>
</ul>

<h2>Already built without a permit?</h2>
<p>Building without a permit can bring a penalty of up to $50,000 for a first offence. To fix it, you lodge a <strong>BA13</strong> building approval certificate application with a <strong>BA18</strong> certificate of building compliance from a registered building surveyor. On rural and special zones you need retrospective planning approval first.</p>
<p>See <a href="/which-ba-form">which BA form you need</a>, <a href="/check-if-building-is-approved">how to check if a building is approved</a>, or <a href="/retrospective-approval">retrospective approval</a>. Call the City on 9528 0333.</p>
"""

FAQS = [
    ("How long does a building permit take in Rockingham?",
     "10 business days for a certified BA1 and 25 business days for an uncertified BA2, once the City has everything it needs."),
    ("Can I lodge a building permit online in Rockingham?",
     "Yes, through the City's Rock Port portal. You can also lodge in person or by post."),
    ("How long is a Rockingham building permit valid?",
     "Usually 2 years from the date it's issued, unless it says otherwise."),
    ("Do I need planning approval in Rockingham?",
     "On Special Residential and Special Rural land, yes, for any development. On normal residential lots, usually not if you meet the R-Codes."),
]


def page(S):
    return {"path": "city-of-rockingham-building-permits.html", "published": "2026-11-22", "type": "Council guide", "icon": "pin",
            "card": "City of Rockingham building permits: BA1 vs BA2, what to lodge, Rock Port and special rural zones.",
            "title": "City of Rockingham Building Permits (2026)",
            "desc": "City of Rockingham building permits: BA1 (10 days) vs BA2 (25 days), what to lodge, online lodgement on Rock Port, special rural zones, the BA7 and unauthorised work.",
            "eyebrow": "Council guide", "h1": "City of Rockingham building permits", "crumb": "City of Rockingham building permits",
            "answer": "<p>The City of Rockingham decides a certified <strong>BA1</strong> in <strong>10 business days</strong> and an uncertified <strong>BA2</strong> in <strong>25 business days</strong>. You can lodge online through <strong>Rock Port</strong>. On Special Residential or Special Rural land, you need planning consent first.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/which-ba-form", "Which BA form do I need?"), ("/check-if-building-is-approved", "Check if a building is approved"), ("/retrospective-approval", "Retrospective approval")],
            "sources": [("Building applications and permits, City of Rockingham", "https://rockingham.wa.gov.au/planning-and-building/lodge-an-application/building-applications-and-permits"),
                        ("How do I obtain a building permit?, City of Rockingham", "https://rockingham.wa.gov.au/getContentAsset/3766d1d9-8266-4054-bccf-82a3d53c4d56/3ca954ad-3848-47c6-8f97-68cebe0b47a2/How-do-I-obtain-a-Building-Permit.pdf?language=en"),
                        ("Unauthorised building work, City of Rockingham", "https://rockingham.wa.gov.au/getContentAsset/11d17f25-4ae3-49ca-a22d-abeb6a8a0435/3ca954ad-3848-47c6-8f97-68cebe0b47a2/Unauthorised-Building-Work.pdf?language=en")]}
