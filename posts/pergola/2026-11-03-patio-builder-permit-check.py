BODY = """
<h2>Why it's on you</h2>
<p>Building and Energy, the state regulator, says <strong>owners must make sure a building permit is obtained</strong> from council before work starts, and penalties apply if it isn't. So even when a builder says "we look after the permit", it pays to check.</p>
<p>Patios (roofed outdoor areas) are Class 10a buildings. Most need a building permit, unless they're freestanding, 10 m² or less and 2.4 m or lower.</p>

<h2>Six checks before you sign</h2>
<ol>
<li><strong>Is the permit in the quote?</strong> Look for a line that says the builder prepares the drawings, engineering and building permit application, and pays the council fees. If it isn't written down, assume it isn't included.</li>
<li><strong>Who is the applicant?</strong> Ask whose name goes on the application. Every owner on the title still has to sign the BA2 form.</li>
<li><strong>Is planning approval covered?</strong> If your patio is in the front yard, on a heritage property or doesn't meet the setbacks, it may need planning approval first. Ask if the builder handles that too.</li>
<li><strong>Is there a written contract?</strong> For home building work between $7,500 and $500,000, the Home Building Contracts Act applies whether or not the builder is registered. Contracts must be in writing and signed by both of you, and the builder must give you the "Notice for the homeowner".</li>
<li><strong>Is the deposit 6.5% or less?</strong> That's the most a builder can ask for before work starts on these contracts. Progress payments should only cover work done or materials delivered.</li>
<li><strong>Over $20,000?</strong> Home indemnity insurance is required for work that needs a building permit and is worth more than $20,000. Ask for the certificate and check it on QBE's online register before you pay anything.</li>
</ol>

<h2>Do they need to be a registered builder?</h2>
<p>Since <strong>1 July 2026</strong>, a patio worth <strong>less than $50,000</strong> doesn't have to be built by a registered builder. Patios worth more do. You can check a builder's registration with the state's Find a registered builder search.</p>

<h2>Before work starts</h2>
<ul>
<li>Ask for a <strong>copy of the building permit</strong>. Don't let work start without it.</li>
<li>Check the plans on the permit match what you're getting (size, height and position).</li>
<li>Within 7 days of finishing, a notice of completion (BA7) goes to council. Ask who lodges it.</li>
</ul>
"""

FAQS = [
    ("Who is responsible for getting the building permit for a patio?",
     "Building and Energy says owners must make sure a building permit is obtained before work starts. A builder can prepare and lodge it, but check it's included in your quote and ask for a copy before work begins."),
    ("Does my patio builder need to be registered in WA?",
     "Only if the patio is worth $50,000 or more. Since 1 July 2026, Class 10a buildings like patios under $50,000 don't need a registered builder."),
    ("What is the maximum deposit for a patio in WA?",
     "6.5% of the contract price for home building contracts between $7,500 and $500,000."),
    ("Do I need home indemnity insurance for a patio?",
     "Yes, if the work needs a building permit and is worth more than $20,000. Your builder must give you a copy of the certificate."),
]


def page(S):
    return {"path": "patio-builder-permit-check.html", "published": "2026-11-03", "type": "How-to guide", "icon": "pergola",
            "card": "Six checks before you sign, so the permit, deposit and insurance are all in order.",
            "title": "How to Check Your Patio Builder Is Handling the Permit (WA)",
            "desc": "Six checks before you sign with a patio builder in WA: permit in the quote, planning approval, written contract, 6.5% deposit limit, home indemnity insurance and registration.",
            "eyebrow": "How-to guide", "h1": "How to check your patio builder is handling the permit", "crumb": "Patio builder permit check",
            "answer": "<p>In WA, the <strong>owner</strong> has to make sure a building permit is issued before work starts. Check the permit is written into the quote, ask for a <strong>copy of the permit</strong> before building, keep the deposit to <strong>6.5% or less</strong>, and get home indemnity insurance for jobs over $20,000.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-building-permit", "Patio building permits"), ("/patio-approval-checker", "Patio approval checker"), ("/patio-approval-cost-perth", "Patio approval cost in Perth")],
            "sources": [("Building or renovating your home (Building and Energy, updated September 2026)", "https://www.wa.gov.au/organisation/building-and-energy/building-or-renovating-your-home"),
                        ("Do I need a permit? (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit"),
                        ("Find a registered builder (WA Government)", "https://www.wa.gov.au/service/community-services/find-registered-builder")]}
