BODY = """
<h2>It depends which kind of tiny home</h2>
<p>In WA, a tiny home on wheels fitted out to live in is treated like a caravan. A tiny home without wheels is a building. The approvals, and so the fees, are completely different. Not sure which you have? Use the <a href="/caravan-or-building-checker">caravan or building checker</a>.</p>

<h2>Tiny home on wheels: council approval to stay</h2>
<p>Under the Caravan Parks and Camping Grounds Regulations, you can stay on land you own or have the right to use for up to <strong>5 nights in any 28 days</strong>. For longer, you apply to your council, which can approve up to <strong>24 consecutive months</strong>.</p>
<ul>
<li>The regulations don't set a state fee for this approval. Each council sets its own.</li>
<li>Some councils charge a licence fee. The City of Swan, for example, says a fee for a temporary licence must be paid before it processes your application.</li>
<li>Some councils charge for advice first. The Shire of Mundaring lists a <strong>$73</strong> preliminary check.</li>
<li>If the council doesn't approve your application within <strong>63 days</strong>, it's taken to be refused.</li>
</ul>
<p>Some councils treat a long stay as a planning matter too, which can add a development application fee. The state planning fee for work valued under $50,000 is $147, as the City of Melville lists it.</p>

<h2>Other costs for a tiny home on wheels</h2>
<ul>
<li><strong>Services.</strong> Councils can make approval depend on access to power, water and sewage. The City of Swan's form asks how wastewater will be handled: sewer, an existing septic system or a new one. A new septic system needs its own health approval and fee.</li>
<li><strong>Registration.</strong> The City of Swan only approves registered (licensed) vehicles, so keep the trailer's registration current.</li>
<li><strong>Bushfire plan.</strong> Needed on bushfire-prone land in councils like Swan.</li>
</ul>

<h2>Fixed tiny home: building permit fees</h2>
<p>A tiny home on footings needs a building permit, like any house. The state fees are:</p>
<div class="table-wrap"><table>
<thead><tr><th>Fee</th><th>Amount</th><th>Example: $80,000 tiny home</th></tr></thead><tbody>
<tr><td>BA1 permit (certified)</td><td>0.19% of the value, at least $121</td><td>$152</td></tr>
<tr><td>BA2 permit (uncertified)</td><td>0.32% of the value, at least $121</td><td>$256</td></tr>
<tr><td>Building Services Levy</td><td>$61.65 up to $45,000; 0.137% of the value above that</td><td>$109.60</td></tr>
</tbody></table></div>
<p>With a BA1, you also pay a private building surveyor for the Certificate of Design Compliance. Planning approval may be needed too, depending on your lot and council. A fixed tiny home is usually assessed as a single house or a granny flat.</p>

<h2>Keep in mind</h2>
<p>The government fees are usually the small part. Plans, engineering, site works and connecting services cost more. Councils vary, so ask yours for its fee schedule before you start. Read more in <a href="/tiny-home-council-application">the tiny home council application</a> and <a href="/fixed-tiny-home-permit">fixed tiny home permits</a>.</p>
"""

FAQS = [
    ("How much does council approval for a tiny home cost in WA?",
     "It depends on the council and the type. For a tiny home on wheels, councils set their own fees for long-stay approval. For a fixed tiny home, state building permit fees apply: 0.19% (BA1) or 0.32% (BA2) of the value, at least $121, plus the Building Services Levy."),
    ("Is there a state fee to live in a tiny home on wheels on private land?",
     "The Caravan Parks and Camping Grounds Regulations don't set a fee for council approval to camp on private land. Councils set their own, and some charge a licence fee."),
    ("How long can I live in a tiny home on wheels without approval in WA?",
     "Up to 5 nights in any 28 days on land you own or have the right to use. Longer stays need council approval, for up to 24 consecutive months."),
    ("How long does a council have to approve a tiny home on wheels?",
     "If the council doesn't give approval within 63 days, the application is taken to be refused."),
    ("What does a building permit cost for a fixed tiny home?",
     "For an $80,000 tiny home, about $152 for a BA1 or $256 for a BA2, plus a $109.60 Building Services Levy. A BA1 also needs a private building surveyor's certificate."),
]


def page(S):
    return {"path": "tiny-home-approval-cost.html", "published": "2026-11-08", "type": "Cost guide", "icon": "price",
            "card": "Council fees for wheels vs building permit fees for fixed tiny homes, with examples.",
            "title": "Tiny Home Approval Cost in WA (2026)",
            "desc": "What tiny home approval costs in WA: council fees for tiny homes on wheels, the 5-night and 24-month rules, and building permit fees for fixed tiny homes.",
            "eyebrow": "Cost guide", "h1": "How much does tiny home approval cost in WA?", "crumb": "Tiny home approval cost",
            "answer": "<p>For a tiny home <strong>on wheels</strong>, there's no state fee: each council sets its own for long-stay approval, and some charge a licence fee. For a <strong>fixed</strong> tiny home, state building permit fees apply: 0.19% (BA1) or 0.32% (BA2) of the value, at least <strong>$121</strong>, plus the Building Services Levy. An $80,000 fixed tiny home is about $262 to $366 in government fees.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/caravan-or-building-checker", "Caravan or building checker"), ("/tiny-home-council-application", "Tiny home council application"), ("/fixed-tiny-home-permit", "Fixed tiny home permits")],
            "sources": [("Caravan Parks and Camping Grounds Regulations 1997 (WA legislation)", "https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_47625.pdf"),
                        ("Building approvals: forms, fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Application to reside in temporary accommodation (City of Swan)", "https://www.swan.wa.gov.au/awcontent/Web/Documents/Services%20and%20Community/Public%20health/W-AP-Temporary-Accommodation-Application-Form.pdf")]}
