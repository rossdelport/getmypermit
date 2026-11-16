BODY = """
<h2>Two different approvals</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Planning (development) approval</th><th>Building permit</th></tr></thead><tbody>
<tr><td>What it checks</td><td>Where the shed goes and how big it is: setbacks, size, height, street look</td><td>How it's built: structure, wind, footings, fire separation</td></tr>
<tr><td>Rules it uses</td><td>The R-Codes, your council's planning scheme and policies</td><td>The Building Act and the National Construction Code</td></tr>
<tr><td>Needed for a shed?</td><td>Only if it doesn't meet the standard rules</td><td>Yes, unless it's small (see below)</td></tr>
<tr><td>Form</td><td>Application for Development Approval</td><td>BA1 (certified) or BA2 (uncertified)</td></tr>
<tr><td>Usual timeframe</td><td>Up to 60 days (90 if neighbours are asked)</td><td>10 business days (BA1) or 25 (BA2)</td></tr>
</tbody></table></div>

<h2>When a shed needs a building permit</h2>
<p>Most do. Perth councils usually exempt a shed that is <strong>freestanding, no bigger than 10 m² and no taller than 2.4 m</strong>. Anything bigger needs a building permit. A small exempt shed must still be built properly.</p>

<h2>When a shed also needs planning approval</h2>
<p>Under the standard R-Codes rules for outbuildings, a backyard shed on a house lot usually doesn't need planning approval if it:</p>
<ul>
<li>is no bigger than <strong>60 m²</strong> or 10% of the lot (whichever is less), counting all your outbuildings together,</li>
<li>has walls no higher than <strong>2.4 m</strong> and a ridge no higher than <strong>4.2 m</strong>,</li>
<li>isn't in the front setback, and</li>
<li>meets the side and rear setbacks and leaves enough open space.</li>
</ul>
<p>Go over any of those and you'll usually need planning approval <strong>first</strong>, then the building permit. Councils vary. For example, the City of Bayswater's Residential Development Policy (September 2026) allows outbuilding walls up to <strong>3.0 m</strong>. Heritage areas, rural zones and special estates can have their own rules too.</p>

<h2>Which comes first?</h2>
<p>If you need both, get planning approval first. The building permit has to match what was approved, and councils won't usually issue it until planning conditions are met.</p>
<p>Check your shed with the <a href="/shed-size-checker">shed size checker</a>, read <a href="/how-to-get-a-shed-permit">how to get a shed permit</a>, or see <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a>.</p>
"""

FAQS = [
    ("Do I need planning approval for a shed in WA?",
     "Usually not, if it's no bigger than 60 m² (or 10% of the lot), walls no higher than 2.4 m, ridge no higher than 4.2 m, not in the front setback and meets setbacks. Councils vary."),
    ("Do I need a building permit for a shed in WA?",
     "Yes, unless it's freestanding, no bigger than 10 m² and no taller than 2.4 m."),
    ("What's the difference between planning approval and a building permit?",
     "Planning approval checks where the shed goes and how big it is. A building permit checks that it's built safely to the building code."),
    ("Which do I get first?",
     "Planning approval, if you need it. The building permit follows and must match the approved plans."),
]


def page(S):
    return {"path": "shed-planning-vs-building-permit.html", "published": "2026-11-17", "type": "Comparison", "icon": "shed",
            "card": "The difference between planning approval and a building permit for a shed, and when you need each.",
            "title": "Shed Planning Approval vs Building Permit (WA)",
            "desc": "Planning approval vs building permit for a shed in WA: what each checks, the 10 m² and 60 m² limits, wall and ridge heights, and which comes first.",
            "eyebrow": "Comparison", "h1": "Planning approval vs building permit for sheds", "crumb": "Planning vs building permit",
            "answer": "<p>A <strong>building permit</strong> checks the shed is built safely, and most sheds over <strong>10 m²</strong> or <strong>2.4 m</strong> high need one. <strong>Planning approval</strong> checks where it goes and how big it is, and is usually only needed if the shed is over <strong>60 m²</strong> (or 10% of the lot), has walls over 2.4 m or a ridge over 4.2 m, or sits in the front setback.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/how-to-get-a-shed-permit", "How to get a shed permit"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?")],
            "sources": [("Building approvals, WA Government (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Outbuildings information sheet, City of Joondalup", "https://api.joondalup.wa.gov.au/files/Outbuildings.pdf"),
                        ("Building a shed or outbuilding, City of Melville", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding"),
                        ("Residential Development Policy (September 2026), City of Bayswater", "https://www.bayswater.wa.gov.au/online-services/forms-and-publications/policies/2026/residential-development-policy")]}
