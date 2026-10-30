BODY = """
<h2>Step 1: Check what approvals you need</h2>
<p>The City of Stirling asks you to start with its project information sheet and its online <strong>planning wizard</strong>. Put in your address and project, and it lists the approvals and documents you'll need. Many jobs need only a building permit. Some also need <strong>development (planning) approval</strong> first, for example a carport in the front setback, or any carport on a heritage-listed property or in a heritage area such as Mount Lawley, Menora and Inglewood.</p>
<p>Some small structures need no building permit at all, such as a freestanding shed or patio of 10 m&sup2; or less and no taller than 2.4 m. <a href="/what-doesnt-need-a-building-permit">See what doesn't need a building permit</a>.</p>

<h2>Step 2: Choose BA1 or BA2</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>BA2 (uncertified)</th><th>BA1 (certified)</th></tr></thead><tbody>
<tr><td>Who checks the plans</td><td>The City's building surveyors</td><td>A private building surveyor first, who signs a BA3 certificate</td></tr>
<tr><td>Time for the City to decide</td><td>25 business days</td><td>10 business days</td></tr>
<tr><td>Permit fee (house or outbuilding)</td><td>0.32% of the value, at least $121</td><td>0.19% of the value, at least $121, plus the surveyor's fee</td></tr>
</tbody></table></div>
<p>Those times only start once the City has everything it needs. If it asks for more information, the clock stops until you reply.</p>

<h2>Step 3: Get the documents together</h2>
<p>For a building permit, the City says you'll need at least:</p>
<ul>
<li>A set of architectural plans (site plan, floor plan and elevations)</li>
<li>Structural engineering details from a structural engineer</li>
<li>An energy efficiency compliance report, where the building needs one (such as a house, extension or granny flat)</li>
<li>Specifications for the building materials, if asked</li>
</ul>
<p>The City publishes a checklist for each application type, including a BA2 checklist for houses and Class 10 structures like sheds, patios and carports.</p>

<h2>Step 4: Lodge online and pay</h2>
<p>Stirling has an <strong>online lodgement service</strong> for building permits and development applications, where you can also track your application. On top of the permit fee, the state's Building Services Levy is $61.65 for work up to $45,000.</p>
<p>From 1 July 2026, the City no longer collects the Construction Training Fund levy. For work over $100,000 you pay it directly to the Construction Training Fund and include the receipt with your application.</p>

<h2>Other Stirling forms you may need</h2>
<ul>
<li><strong>Verge permit</strong>, if you'll use or affect the verge during building.</li>
<li><strong>Crossover application</strong>, for a new or changed driveway crossover.</li>
<li><strong>Deemed-to-comply check</strong>, a City form for checking whether a single house design meets the standard planning rules.</li>
<li><strong>BA19</strong> to change the builder or other permit details. From 8 July 2026 the City charges $110 for this.</li>
</ul>

<h2>Contact the City</h2>
<p>City of Stirling Administration Centre, 25 Cedric Street, Stirling WA 6021. Phone (08) 9205 8555.</p>
"""

FAQS = [
    ("How long does a building permit take at the City of Stirling?",
     "10 business days for a certified (BA1) application and 25 business days for an uncertified (BA2) application, once the City has everything it needs."),
    ("How much is a building permit at the City of Stirling?",
     "The fee is set by the state: 0.32% of the value for an uncertified BA2, or 0.19% for a certified BA1, with a $121 minimum. Add the $61.65 Building Services Levy for work up to $45,000."),
    ("Can I lodge a building permit online in Stirling?",
     "Yes. The City has an online lodgement service for building permits and development applications, and you can track your application there."),
    ("Does the City of Stirling still collect the CTF levy?",
     "No. From 1 July 2026 you pay the Construction Training Fund levy directly to the fund, and only for work over $100,000. Include the receipt with your application."),
]


def page(S):
    return {"path": "city-of-stirling-building-permits.html", "published": "2026-10-31", "type": "Council guide", "icon": "pin",
            "card": "How to get a building permit from the City of Stirling: approvals check, BA1 or BA2, documents, online lodging and fees.",
            "title": "City of Stirling Building Permits: How to Apply (2026 Guide)",
            "desc": "How to get a building permit from the City of Stirling in 2026: the planning wizard, BA1 vs BA2, the documents you need, online lodging, timeframes and fees.",
            "eyebrow": "Council guide", "h1": "City of Stirling building permits", "crumb": "City of Stirling",
            "answer": "<p>Check your project with the City's <strong>planning wizard</strong>, then lodge a <strong>BA2</strong> (the City checks your plans, 25 business days) or a <strong>BA1</strong> with a private surveyor's certificate (10 business days) through the City's <strong>online lodgement service</strong>. The fee is 0.32% (BA2) or 0.19% (BA1) of the value, at least $121, plus the $61.65 levy.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/which-ba-form", "Which BA form do I need?"), ("/what-doesnt-need-a-building-permit", "What doesn't need a building permit"), ("/do-i-need-approval", "Do I need council approval?")],
            "sources": [("Lodging an application (City of Stirling)", "https://www.stirling.wa.gov.au/developing-property/planning-advice/develop-your-property/lodging-an-application"),
                        ("Lodging and tracking applications (City of Stirling)", "https://www.stirling.wa.gov.au/developing-property/planning-advice/lodge-an-application"),
                        ("Building documents, forms and checklists (City of Stirling)", "https://www.stirling.wa.gov.au/developing-property/building-advice/building-documents"),
                        ("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf"),
                        ("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                        ("Building approvals and the Building Services Levy (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
