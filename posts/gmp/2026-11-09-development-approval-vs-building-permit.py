BODY = """
<h2>Two different approvals</h2>
<p>In WA, "council approval" can mean two separate things. Many projects need one, some need both, and some need neither.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Development (planning) approval</th><th>Building permit</th></tr></thead><tbody>
<tr><td>What it checks</td><td>Whether the design and location suit the zoning and planning rules: setbacks, height, size, looks, overlooking, heritage</td><td>Whether it's safe and meets the building code: structure, fire separation, wind, drainage</td></tr>
<tr><td>Main rules</td><td>The R-Codes, the council's planning scheme and local policies</td><td>The Building Act 2011 and the National Construction Code</td></tr>
<tr><td>When you need it</td><td>When your project doesn't meet the "deemed-to-comply" rules, or is in a heritage area or special zone</td><td>For most building work, except small exempt structures</td></tr>
<tr><td>Application</td><td>Council development application form, plans, a cover letter and the certificate of title</td><td>Form BA1 (certified by a private surveyor) or BA2 (checked by council)</td></tr>
<tr><td>Usual timeframe</td><td>60 days, or 90 days if neighbours or agencies are consulted</td><td>10 business days (BA1) or 25 business days (BA2)</td></tr>
<tr><td>Typical fee</td><td>$147 for work under $50,000 (as the City of Melville lists it)</td><td>0.19% (BA1) or 0.32% (BA2) of the value, at least $121, plus the Building Services Levy</td></tr>
</tbody></table></div>

<h2>Which comes first?</h2>
<p><strong>Planning approval comes first.</strong> The City of Belmont says a building permit can't be issued until any required development approval has been granted and its conditions resolved. Some councils, like Wanneroo, let you lodge an uncertified building application while the planning one is pending, but it's put on hold until planning approval is issued. A certified (BA1) application must include all prior approvals.</p>

<h2>Common examples</h2>
<div class="table-wrap"><table>
<thead><tr><th>Project</th><th>Planning approval</th><th>Building permit</th></tr></thead><tbody>
<tr><td>Garden shed, 10 m² or less, 2.4 m high, freestanding</td><td>Usually not, if it meets the R-Codes</td><td>No</td></tr>
<tr><td>Patio attached to the house that meets the setbacks</td><td>Usually not</td><td>Yes</td></tr>
<tr><td>Carport in the front setback that doesn't meet the R-Codes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Granny flat of 70 m² or less meeting all the rules</td><td>No</td><td>Yes</td></tr>
<tr><td>Anything in a heritage area</td><td>Usually yes</td><td>Depends on the work</td></tr>
</tbody></table></div>
<p>Councils vary, so check your council's rules.</p>

<h2>Exempt doesn't mean anything goes</h2>
<p>Being exempt from one approval doesn't exempt you from the other. Belmont puts it plainly: a structure may be exempt from a building permit but still need planning approval, or the other way around. And even exempt work must still meet the building standards.</p>
<p>Not sure what you need? Use our <a href="/do-i-need-approval">approval checker</a>, see <a href="/what-doesnt-need-a-building-permit">what doesn't need a building permit</a>, or read <a href="/ba1-vs-ba2">BA1 vs BA2</a>.</p>
"""

FAQS = [
    ("What is the difference between development approval and a building permit in WA?",
     "Development (planning) approval checks the design and location against zoning and planning rules. A building permit checks that the building is safe and meets the building code. They're separate approvals."),
    ("Do I need development approval before a building permit?",
     "Yes, if your project needs both. A building permit can't be issued until development approval is granted and its conditions are resolved."),
    ("Can I have a building permit without development approval?",
     "Yes, if your project meets the deemed-to-comply rules and doesn't need planning approval. Many patios, sheds and granny flats only need a building permit."),
    ("How long does development approval take in WA?",
     "Councils usually have 60 days, or 90 days if they need to consult neighbours or other agencies."),
    ("How much is development approval in WA?",
     "For work under $50,000 the fee is $147, as councils such as Melville list it. Bigger projects cost more."),
]


def page(S):
    return {"path": "development-approval-vs-building-permit.html", "published": "2026-11-09", "type": "Comparison", "icon": "doc",
            "card": "What each checks, which comes first, timeframes, fees and common examples.",
            "title": "Development Approval vs Building Permit in WA",
            "desc": "Development approval vs building permit in WA: what each checks, which comes first, timeframes, fees, and which projects need one, both or neither.",
            "eyebrow": "Comparison", "h1": "Development approval vs building permit", "crumb": "DA vs building permit",
            "answer": "<p><strong>They're two separate approvals.</strong> Development (planning) approval checks whether the design and location suit the planning rules. A building permit checks it's safe and meets the building code. If you need both, get planning approval first. Many small projects only need a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/do-i-need-approval", "Do I need approval?"), ("/what-doesnt-need-a-building-permit", "What doesn't need a building permit"), ("/ba1-vs-ba2", "BA1 vs BA2")],
            "sources": [("Patio, pergola or shade sail (City of Belmont)", "https://www.belmont.wa.gov.au/build/demolishing-and-building/approval-for-buildings-and-structures/i-want-to-build/patio,-pergola-or-shade-sail"),
                        ("Building a carport or garage (City of Melville)", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-carport-or-garage"),
                        ("Building approvals: forms, fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
