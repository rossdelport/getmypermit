BODY = """
<h2>In the eyes of the law, they're the same</h2>
<p>The WA planning commission's tiny houses fact sheet says a tiny home on wheels that's fitted for living in is a <strong>caravan</strong>. A 2018 tribunal case (Henville v City of Armadale) found that something is either a vehicle or a building, not both. So a tiny home on wheels follows the caravan rules.</p>

<h2>The rules that apply to both</h2>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Caravan or tiny home on wheels</th></tr></thead><tbody>
<tr><td>Building permit</td><td>Not needed</td></tr>
<tr><td>Short stays on your own land</td><td>Up to 5 nights in any 28 days, no approval</td></tr>
<tr><td>Longer stays</td><td>Council approval, up to 24 consecutive months</td></tr>
<tr><td>How many on a lot</td><td>One lived in at a time, unless approved</td></tr>
<tr><td>Wheels</td><td>Must stay on; movable within 24 hours of disconnecting services</td></tr>
<tr><td>Living there permanently</td><td>Not allowed outside a caravan park under the current rules</td></tr>
<tr><td>Registration</td><td>Licensed with the Department of Transport</td></tr>
</tbody></table></div>

<h2>Where they differ</h2>
<p>The differences are practical, not legal. Tiny homes are usually built to look and feel like a small house. Weight matters, because caravan licence fees are worked out by weight ($7.44 per 100 kg in 2026/27). Check the tare weight before you buy.</p>
<p>If you take the wheels off and fix it to the ground, a tiny home stops being a caravan. It becomes a <strong>building</strong>, needs a building permit and must meet the building code.</p>

<h2>What this means for you</h2>
<ul>
<li>For a <strong>short or temporary</strong> stay, a tiny home on wheels and a caravan have the same options.</li>
<li>For a <strong>permanent home</strong>, a fixed tiny home approved as a house or granny flat is the main way under current rules.</li>
</ul>
<p>Not sure which yours is? Try the <a href="/caravan-or-building-checker">caravan or building checker</a>, or read <a href="/tiny-home-registration-wa">tiny home registration</a> and <a href="/live-in-caravan-on-own-land-wa">living in a caravan on your own land</a>.</p>
"""

FAQS = [
    ("Is a tiny home on wheels a caravan in WA?",
     "Yes. The WAPC's tiny houses fact sheet says a wheeled tiny home fitted for living in is treated as a caravan."),
    ("Does a tiny home on wheels need a building permit?",
     "No, because it's a caravan, not a building. A fixed tiny home does need one."),
    ("Can I live permanently in a tiny home on wheels in WA?",
     "Not under the current rules, outside a caravan park. Councils can approve up to 24 consecutive months at a time."),
    ("Do tiny homes need to be registered like caravans?",
     "Yes. A tiny home on wheels is licensed with the Department of Transport, with fees based on weight."),
]


def page(S):
    return {"path": "tiny-home-vs-caravan.html", "published": "2026-11-13", "type": "Comparison", "icon": "tiny",
            "card": "Why WA law treats a tiny home on wheels like a caravan, and where they really differ.",
            "title": "Tiny Home vs Caravan: What's the Difference in WA?",
            "desc": "Tiny home vs caravan in WA: the law treats a tiny home on wheels as a caravan. Stay limits, approvals, registration, and when it becomes a building.",
            "eyebrow": "Comparison", "h1": "Tiny home vs caravan", "crumb": "Tiny home vs caravan",
            "answer": "<p>In WA, a tiny home on wheels fitted for living in is legally a <strong>caravan</strong>. Both follow the same rules: no building permit, <strong>5 nights in 28 days</strong> without approval, up to <strong>24 months</strong> with council approval, and wheels must stay on. Take the wheels off and it becomes a building.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/caravan-or-building-checker", "Caravan or building checker"), ("/tiny-home-registration-wa", "Tiny home registration"), ("/live-in-caravan-on-own-land-wa", "Living in a caravan on your own land")],
            "sources": [("Tiny houses fact sheet, December 2024 (WAPC)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf"),
                        ("Caravan Parks and Camping Grounds Regulations 1997 (WA legislation)", "https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_s1418.html"),
                        ("Licensing a caravan or camper trailer (Department of Transport)", "https://transport.wa.gov.au/licensing/vehicle/license-vehicle/caravan-camper-trailer")]}
