BODY = """
<h2>Why registration matters</h2>
<p>In WA, a tiny home on wheels is treated as a <strong>caravan</strong> only if it's a genuine vehicle, built to be moved, not just able to be moved. Licensing (registering) it with the Department of Transport and Major Infrastructure helps show it's a vehicle. Some councils ask for it: the City of Swan's temporary accommodation form accepts <strong>licensed vehicles only</strong>, with conditional approval if the registration is still pending.</p>
<p>A home on wheels that's too big to be towed on the road may instead be a <strong>park home</strong>. Park homes don't need a vehicle licence, but they can only be lived in inside a licensed caravan park.</p>

<h2>How to license a tiny home as a caravan</h2>
<ol>
<li><strong>Get it inspected.</strong> Take it to an Authorised Inspection Station for a roadworthiness inspection. The department can't license a vehicle whose VIN has been removed or defaced.</li>
<li><strong>Fill in form VL17</strong>, Application to license a vehicle.</li>
<li><strong>Bring ID</strong>: one primary and one secondary document. First-timers without a WA driver's licence also fill in form VL186.</li>
<li><strong>Lodge in person</strong> at a service centre or regional agent, with the inspection certificate and proof of ownership (such as a receipt or contract of sale showing the VIN).</li>
</ol>
<p>If the weight can't be confirmed from the maker's specifications or records, you'll also need a <strong>weighbridge certificate</strong>.</p>

<h2>What it costs</h2>
<div class="table-wrap"><table>
<thead><tr><th>Fee (2026/27)</th><th>Amount</th></tr></thead><tbody>
<tr><td>Caravan (trailer type) licence</td><td><strong>$7.44 per 100 kg</strong></td></tr>
<tr><td>Recording fee (3, 6 or 12-month renewals, not direct debit)</td><td>$9.70</td></tr>
<tr><td>Motor injury insurance</td><td>Extra, set separately</td></tr>
<tr><td>Vehicle licence duty</td><td>Not payable for caravans permanently fitted for living in and used mainly for journeys</td></tr>
</tbody></table></div>
<p>Example: a 4,000 kg tiny home at $7.44 per 100 kg is about <strong>$298</strong> a year in licence fees, before the flat fee, recording fee and insurance.</p>

<h2>Registration doesn't replace council approval</h2>
<p>Licensing makes it a road vehicle. It doesn't give you the right to live in it anywhere. You can still only stay <strong>5 nights in any 28 days</strong> without approval, or up to <strong>24 months</strong> at a time with council approval. The wheels must stay on, and it must be able to be moved within 24 hours of the services being disconnected.</p>
<p>Work out your limit with the <a href="/tiny-home-stay-calculator">tiny home stay calculator</a>, check whether yours is a caravan with the <a href="/caravan-or-building-checker">caravan or building checker</a>, or read about <a href="/moving-a-tiny-home">moving a tiny home</a>.</p>
"""

FAQS = [
    ("Does a tiny home on wheels need to be registered in WA?",
     "To tow it on public roads and be treated as a caravan, it should be licensed with the Department of Transport and Major Infrastructure. Some councils, such as Swan, only approve licensed vehicles for temporary accommodation."),
    ("How much does it cost to register a tiny home on wheels in WA?",
     "A trailer-type caravan is $7.44 per 100 kg for 2026/27, plus a flat fee, recording fee and motor injury insurance. A 4,000 kg home is about $298 in licence fees."),
    ("How do I register a tiny home on wheels?",
     "Get a roadworthiness inspection at an Authorised Inspection Station, fill in form VL17, and lodge it in person with ID, the inspection certificate and proof of ownership."),
    ("Does registration mean I can live in my tiny home anywhere?",
     "No. It's still a caravan under the camping rules: 5 nights in any 28 days without approval, or up to 24 months with council approval."),
]


def page(S):
    return {"path": "tiny-home-registration-wa.html", "published": "2026-11-11", "type": "Question answer", "icon": "car",
            "card": "Why licensing matters for council approval, how to do it and what it costs.",
            "title": "Does a Tiny Home on Wheels Need Registering in WA?",
            "desc": "Registering a tiny home on wheels in WA: why councils care, the inspection and VL17 steps, the $7.44 per 100 kg caravan fee, and what registration doesn't do.",
            "eyebrow": "Question answer", "h1": "Does a tiny home on wheels need to be registered in WA?", "crumb": "Registering a tiny home",
            "answer": "<p>To be towed on the road and treated as a caravan, <strong>yes</strong>: license it with the Department of Transport and Major Infrastructure. You need a roadworthiness inspection, form VL17 and ID, lodged in person. Fees are <strong>$7.44 per 100 kg</strong>. Some councils, such as Swan, only approve licensed vehicles for living in.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-stay-calculator", "Tiny home stay calculator"), ("/caravan-or-building-checker", "Caravan or building checker"), ("/moving-a-tiny-home", "Moving a tiny home")],
            "sources": [("License a caravan or camper trailer (Department of Transport and Major Infrastructure)", "https://transport.wa.gov.au/licensing/vehicle/license-vehicle/caravan-camper-trailer"),
                        ("Tiny houses fact sheet, December 2024 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf"),
                        ("Temporary accommodation application form (City of Swan)", "https://www.swan.wa.gov.au/awcontent/Web/Documents/Services%20and%20Community/Public%20health/W-AP-Temporary-Accommodation-Application-Form.pdf"),
                        ("Caravan Parks and Camping Grounds Regulations 1997 (WA legislation)", "https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_s1418.html")]}
