BODY = """
<h2>Before you start</h2>
<p>Every council in WA uses the same state forms, but each council has its own online portal. Have these ready before you log in:</p>
<ul>
<li><strong>The right form</strong> from the Building and Energy website: a <strong>BA1</strong> (certified, with a BA3 certificate from a building surveyor) or a <strong>BA2</strong> (uncertified, for houses and Class 10 work like sheds, patios and carports only). Not sure? Use the <a href="/which-ba-form">which BA form checker</a>.</li>
<li><strong>Plans as PDFs:</strong> usually a site plan (at least 1:200), elevations and a floor plan (at least 1:100), and structural engineering where needed.</li>
<li><strong>The estimated cost</strong> of the work, because fees are worked out from it.</li>
<li><strong>A Construction Training Fund receipt</strong> if the work is over $100,000.</li>
</ul>

<h2>Step by step</h2>
<ol>
<li><strong>Find your council's portal</strong> (see the table below).</li>
<li><strong>Create an account.</strong> First-time users need to register; most portals let you track the application afterwards.</li>
<li><strong>Choose "building permit"</strong> and the right application type (BA1 or BA2).</li>
<li><strong>Upload the signed form and your documents.</strong> Make sure every section is signed. Incomplete applications can be refused.</li>
<li><strong>Pay the fees.</strong> Some councils take payment in the portal; others email you a tax invoice.</li>
<li><strong>Answer any requests</strong> for more information quickly, as the clock can stop while council waits.</li>
<li><strong>Wait for the decision:</strong> up to <strong>10 business days</strong> for a BA1 and <strong>25 business days</strong> for a BA2.</li>
</ol>

<h2>What some Perth councils use</h2>
<div class="table-wrap"><table>
<thead><tr><th>Council</th><th>How to lodge</th></tr></thead><tbody>
<tr><td>City of Rockingham</td><td>Rock Port online portal (create an account first)</td></tr>
<tr><td>City of Belmont</td><td>Planning and Building Online Application portal, or in person or by mail</td></tr>
<tr><td>City of Gosnells</td><td>Online through the City's portal (required for unauthorised-work applications); a tax invoice is emailed for the fees</td></tr>
<tr><td>City of Stirling</td><td>Online lodgement service</td></tr>
</tbody></table></div>
<p>Councils vary, so check your council's building page for the current link and any checklist it wants with your application.</p>

<h2>Common reasons for delays</h2>
<ul>
<li>Unsigned forms or missing owner signatures.</li>
<li>No site plan, or one that doesn't show setbacks and levels.</li>
<li>No engineering for a structure that needs it.</li>
<li>Planning approval needed first: a building permit can't be issued until it's granted.</li>
</ul>
<p>See what you'll pay with the <a href="/building-permit-fee-calculator">building permit fee calculator</a>, or compare <a href="/ba1-vs-ba2">BA1 vs BA2</a>.</p>
"""

FAQS = [
    ("Can I apply for a building permit online in WA?",
     "Yes. Most councils take applications through their own online portal, using the state's BA1 or BA2 forms from the Building and Energy website."),
    ("What do I need to lodge a building permit online?",
     "The signed BA1 or BA2 form, plans as PDFs (site plan, elevations, floor plan), engineering where needed, the estimated cost, and a CTF receipt if the work is over $100,000."),
    ("How long does an online building permit take?",
     "Up to 10 business days for a certified BA1 and 25 business days for an uncertified BA2, once the application is complete."),
    ("Can I still lodge a building permit in person?",
     "Some councils allow it. The City of Belmont, for example, accepts applications in person or by mail as well as online."),
]


def page(S):
    return {"path": "how-to-lodge-a-building-permit-online.html", "published": "2026-11-16", "type": "How-to guide", "icon": "doc",
            "card": "What to have ready, the steps, and which portal some Perth councils use.",
            "title": "How to Lodge a Building Permit Online in WA (2026)",
            "desc": "How to lodge a building permit online in WA: the forms and plans you need, step-by-step lodging, council portals in Perth, timeframes and common delays.",
            "eyebrow": "How-to guide", "h1": "How to lodge a building permit online in WA", "crumb": "Lodge a permit online",
            "answer": "<p>Download a <strong>BA1 or BA2</strong> form from the Building and Energy website, then lodge it with your plans through your <strong>council's online portal</strong> and pay the fees. Council decides within <strong>10 business days</strong> (BA1) or <strong>25 business days</strong> (BA2).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/which-ba-form", "Which BA form do I need?"), ("/building-permit-fee-calculator", "Building permit fee calculator"), ("/ba1-vs-ba2", "BA1 vs BA2")],
            "sources": [("Building applications and permits, City of Rockingham", "https://rockingham.wa.gov.au/planning-and-building/lodge-an-application/building-applications-and-permits"),
                        ("Carport, City of Belmont", "https://www.belmont.wa.gov.au/Build/Demolishing-and-Building/Approval-for-buildings-and-structures/I-want-to-build/Carport"),
                        ("Unauthorised work, City of Gosnells", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Building-regulations-and-requirements/Unauthorised-work"),
                        ("Building approval forms, Building and Energy", "https://www.commerce.wa.gov.au/building-and-energy/building-approval-forms-0")]}
