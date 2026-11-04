BODY = """
<h2>Seven checks before you sign</h2>
<ol>
<li><strong>Are they a registered builder?</strong> A granny flat is a home (Class 1a), so building work worth $20,000 or more that needs a permit must be done by a registered builder. The $50,000 exemption since July 2026 only covers sheds, garages, carports and patios. Check the builder with the state's Find a registered builder search.</li>
<li><strong>Is there a written contract?</strong> For home building contracts between $7,500 and $500,000, the Home Building Contracts Act applies. The contract must be in writing and signed by both of you, and the builder must give you the "Notice for the homeowner" first.</li>
<li><strong>Is the deposit 6.5% or less?</strong> That's the legal maximum before work starts on these contracts.</li>
<li><strong>Do progress payments match the work?</strong> You should only pay for work done or materials delivered. Upfront payments beyond the deposit aren't allowed and can affect your insurance claim.</li>
<li><strong>Have you seen the home indemnity insurance certificate?</strong> It's required for permit work over $20,000. Check it on QBE's online register, and don't pay anything until it's in place. It covers loss of deposit (up to $40,000) and incomplete or defective work (up to $200,000) if the builder dies, disappears or goes broke.</li>
<li><strong>Who handles the approvals?</strong> Ask if the quote includes the plans, energy efficiency report, engineering, building permit and, if needed, planning approval. A granny flat always needs a building permit.</li>
<li><strong>Will the design pass?</strong> Make sure it's no more than 70 m² and meets your council's rules. Some councils, like Joondalup, also want an extra parking bay and matching materials.</li>
</ol>

<h2>Watch out for "plans first" agreements</h2>
<p>A preparation of plans agreement (PPA), where you pay a builder to draw plans before the main contract, isn't part of the building contract, so it isn't covered by home indemnity insurance.</p>

<h2>After it's built</h2>
<p>In WA, builders must fix defective work for <strong>six years</strong> after practical completion. Complaints go to the Building Commissioner.</p>
"""

FAQS = [
    ("Does a granny flat builder need to be registered in WA?",
     "Yes, if the work needs a building permit and is worth $20,000 or more, which covers almost every granny flat. The $50,000 exemption only applies to sheds, garages, carports and patios."),
    ("What is the maximum deposit for a granny flat in WA?",
     "6.5% of the contract price, for home building contracts between $7,500 and $500,000."),
    ("Do I need home indemnity insurance for a granny flat?",
     "Yes, for permit work over $20,000. Your builder must give you the certificate, and you can check it on QBE's online register."),
    ("How long is a builder responsible for defects in WA?",
     "Six years from practical completion."),
]


def page(S):
    return {"path": "choosing-a-granny-flat-builder.html", "published": "2026-11-05", "type": "How-to guide", "icon": "granny",
            "card": "Registration, contract, deposit, insurance and approvals: seven checks before you sign.",
            "title": "How to Choose a Granny Flat Builder in Perth (7 Checks)",
            "desc": "How to choose a granny flat builder in Perth: check registration, the written contract, the 6.5% deposit limit, home indemnity insurance, approvals and the 6-year defect period.",
            "eyebrow": "How-to guide", "h1": "How to choose a granny flat builder in Perth", "crumb": "Choosing a builder",
            "answer": "<p>Check the builder is <strong>registered</strong>, get a <strong>written contract</strong>, keep the deposit to <strong>6.5% or less</strong>, and see the <strong>home indemnity insurance</strong> certificate before paying anything. Ask exactly which approvals the quote includes, as every granny flat needs a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-cost-perth", "Granny flat cost in Perth"), ("/granny-flat-approval-process", "Granny flat approval process"), ("/city-of-joondalup-granny-flat-rules", "Joondalup granny flat rules")],
            "sources": [("Building or renovating your home (Building and Energy, updated September 2026)", "https://www.wa.gov.au/organisation/building-and-energy/building-or-renovating-your-home"),
                        ("Find a registered builder (WA Government)", "https://www.wa.gov.au/service/community-services/find-registered-builder"),
                        ("Renovations in a strata titles scheme: building defects (Landgate)", "https://www.landgate.wa.gov.au/siteassets/documents/strata-and-community-titles/strata-titles/learn-about-strata/getting-things-done---fact-sheet.pdf"),
                        ("Granny flat or ancillary dwelling (City of Joondalup)", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/granny-flat-or-ancillary-dwelling")]}
