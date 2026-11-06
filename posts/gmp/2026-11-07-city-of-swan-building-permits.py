BODY = """
<h2>Do you need a building permit in the City of Swan?</h2>
<p>The City of Swan follows the same state rules as every WA council. Most new buildings and many additions need a building permit before work starts. Some small structures are exempt, such as a freestanding garden shed of 10 m² or less and no more than 2.4 m high. Check first with our <a href="/what-doesnt-need-a-building-permit">list of what doesn't need a permit</a>.</p>
<p>A building permit is separate from planning approval. If your project also needs planning approval, get that first.</p>

<h2>Which form to use</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>BA1 (certified)</th><th>BA2 (uncertified)</th></tr></thead><tbody>
<tr><td>Who checks the plans</td><td>A private registered building surveyor, before you lodge (they issue a BA3 certificate)</td><td>The City of Swan's building surveyors</td></tr>
<tr><td>What it can be used for</td><td>Any building</td><td>Houses (Class 1a), sheds, garages, carports, patios, pools and other Class 10 structures only</td></tr>
<tr><td>Time the City has to decide</td><td><strong>10 business days</strong></td><td><strong>25 business days</strong></td></tr>
</tbody></table></div>
<p>The clock starts at midnight the day after the City receives a <strong>complete</strong> application. Not sure which suits you? Read <a href="/ba1-vs-ba2">BA1 vs BA2</a>.</p>

<h2>How to lodge</h2>
<ul>
<li><strong>Online</strong> through the City's ePathway portal. The City says online is its preferred way.</li>
<li>By email to the City's lodgement address, in person at 2 Midland Square, Midland, or by post.</li>
</ul>
<p>You can track your application online. The tracker shows key milestones, not every step.</p>

<h2>If the City asks for more information</h2>
<p>You must send it within <strong>21 days</strong>, or the application may be refused. An incomplete application may also be refused, and the City says fees are unlikely to be refunded. So it pays to get the paperwork right the first time.</p>

<h2>Government fees</h2>
<p>These are set by the state and are usually the same at every council:</p>
<div class="table-wrap"><table>
<thead><tr><th>Fee</th><th>Amount</th></tr></thead><tbody>
<tr><td>BA1 permit (house or Class 10)</td><td>0.19% of the value, at least $121</td></tr>
<tr><td>BA2 permit</td><td>0.32% of the value, at least $121</td></tr>
<tr><td>Building Services Levy</td><td>$61.65 for work up to $45,000; 0.137% above that</td></tr>
</tbody></table></div>
<p>Work out yours with the <a href="/building-permit-fee-calculator">building permit fee calculator</a>. The City's own schedule of fees covers other charges, like copies of old plans.</p>

<h2>After the permit</h2>
<p>Build to the approved plans, and lodge a notice of completion (form BA7) within <strong>7 days</strong> of finishing. If the City refuses your application, you can appeal to the State Administrative Tribunal.</p>
"""

FAQS = [
    ("How long does a City of Swan building permit take?",
     "The City has 10 business days to decide a certified (BA1) application and 25 business days for an uncertified (BA2) one. The clock starts the day after a complete application is received."),
    ("How do I apply for a building permit in the City of Swan?",
     "Online through the City's ePathway portal (its preferred way), or by email, in person at 2 Midland Square, Midland, or by post."),
    ("How much is a building permit in the City of Swan?",
     "State fees apply: 0.19% of the value for a BA1 or 0.32% for a BA2, at least $121, plus the Building Services Levy of $61.65 for work up to $45,000."),
    ("What happens if my City of Swan application is missing information?",
     "You have 21 days to provide it, or the application may be refused. The City says fees are unlikely to be refunded for refused incomplete applications."),
    ("Can I appeal a City of Swan building permit refusal?",
     "Yes. You can lodge an appeal with the State Administrative Tribunal."),
]


def page(S):
    return {"path": "city-of-swan-building-permits.html", "published": "2026-11-07", "type": "Council guide", "icon": "pin",
            "card": "Forms, timeframes, how to lodge and the fees for City of Swan building permits.",
            "title": "City of Swan Building Permits: How to Apply (2026)",
            "desc": "How to get a building permit in the City of Swan: BA1 vs BA2, the 10 and 25 business day timeframes, lodging online, the 21-day rule, and fees.",
            "eyebrow": "Council guide", "h1": "City of Swan building permits: how to apply", "crumb": "City of Swan building permits",
            "answer": "<p>Lodge a <strong>BA1</strong> (certified by a private building surveyor) or a <strong>BA2</strong> (checked by the City), preferably online. The City has <strong>10 business days</strong> to decide a BA1 and <strong>25 business days</strong> for a BA2, counted from when your application is complete. If they ask for more information, you have <strong>21 days</strong> to provide it.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/ba1-vs-ba2", "BA1 vs BA2"), ("/building-permit-fee-calculator", "Building permit fee calculator"), ("/what-doesnt-need-a-building-permit", "What doesn't need a building permit")],
            "sources": [("Building (City of Swan)", "https://www.swan.wa.gov.au/plan-and-build/building"),
                        ("Building approvals: forms, fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
