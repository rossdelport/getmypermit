BODY = """
<h2>Step 1: Check if you need a permit at all</h2>
<p>A freestanding shed of <strong>10 m² or less and no higher than 2.4 m</strong> doesn't need a building permit under the state's Building Regulations. It may still need planning approval if it breaks your council's rules, for example by sitting in the front setback. Anything bigger needs a building permit.</p>

<h2>Step 2: Check the planning rules</h2>
<p>Most councils let a shed skip planning approval if it meets the standard outbuilding rules. At the City of Wanneroo and the City of Melville, for example, that means:</p>
<ul>
<li>no more than <strong>60 m²</strong> or 10% of the lot (whichever is less)</li>
<li>walls no higher than <strong>2.4 m</strong> and a ridge no higher than <strong>4.2 m</strong></li>
<li>at least <strong>1 m</strong> from side and rear boundaries (Wanneroo asks for 1.5 m once a wall is longer than 14 m)</li>
<li>not used as a place to live, and not in the front setback</li>
</ul>
<p>If your shed doesn't fit, you'll need a development application first. At most councils the fee is $147 for work up to $50,000. Use our <a href="/shed-size-checker">shed size checker</a> to test your numbers.</p>

<h2>Step 3: Get drawings and engineering</h2>
<p>Most shed kit suppliers provide plans and engineering certificates for your wind region. You'll also need a <strong>site plan</strong> (usually at least 1:200) showing the distances to every boundary and building, and elevations (usually at least 1:100).</p>

<h2>Step 4: Lodge the application</h2>
<p>Homeowners usually lodge a <strong>BA2</strong> (uncertified) building permit application with their council. It costs 0.32% of the value of the work (at least $121), plus the $61.65 Building Services Levy for work up to $45,000. Some councils, like Wanneroo, also need a Street and Verge Bond application with every building permit. See <a href="https://getmypermit.com.au/how-to-fill-in-a-ba2-form">how to fill in a BA2</a>.</p>

<h2>Step 5: Wait for the permit</h2>
<p>Council has up to <strong>25 business days</strong> to decide a BA2. If they ask for more information, the clock stops until you reply. Don't start building until the permit is issued.</p>

<h2>Step 6: Build and finish</h2>
<p>Build to the approved plans. Within <strong>7 days</strong> of finishing, lodge a notice of completion (form BA7) with your council.</p>
"""

FAQS = [
    ("Do I need a permit for a shed in WA?",
     "Yes, unless it's freestanding, 10 m² or less and no higher than 2.4 m. Bigger sheds need a building permit, and some also need planning approval."),
    ("How long does a shed permit take in WA?",
     "For a BA2 application, council has up to 25 business days. If it also needs planning approval, add that time first."),
    ("How much does a shed permit cost?",
     "The council fee for a BA2 is 0.32% of the value, at least $121, plus the $61.65 Building Services Levy for work up to $45,000. Planning approval, if needed, is usually $147 for work up to $50,000."),
    ("Can I lodge a shed permit myself?",
     "Yes. Homeowners can lodge a BA2 themselves with the plans and engineering from the shed supplier."),
]


def page(S):
    return {"path": "how-to-get-a-shed-permit.html", "published": "2026-11-02", "type": "How-to guide", "icon": "shed",
            "card": "Six steps from checking if you need one to finishing the build, with WA fees and timeframes.",
            "title": "How to Get a Shed Permit in WA: Step by Step",
            "desc": "How to get a shed building permit in WA in six steps: exemptions, planning rules, drawings, the BA2 form, fees, the 25 business day wait and the BA7 notice.",
            "eyebrow": "How-to guide", "h1": "How to get a shed permit in WA", "crumb": "How to get a shed permit",
            "answer": "<p>Check if your shed is exempt (<strong>10 m² or less and 2.4 m or lower</strong>), check your council's outbuilding rules, get plans and engineering, then lodge a <strong>BA2</strong> with your council. It costs 0.32% of the value (at least $121) plus the levy, and council has up to <strong>25 business days</strong> to decide.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("/shed-size-checker", "Shed size checker"), ("/city-of-wanneroo-shed-rules", "City of Wanneroo shed rules")],
            "sources": [("Do I need a permit? (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit"),
                        ("Outbuildings information sheet (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/360/outbuildings_-_information_sheet.pdf"),
                        ("Building a shed or outbuilding (City of Melville)", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding"),
                        ("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                        ("Building approvals and the Building Services Levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
