BODY = """
<h2>Step 1: Decide on wheels or fixed</h2>
<p>This changes which rules the builder has to follow. In WA, a tiny home on wheels is treated as a <strong>caravan</strong>. A tiny home on the ground is a <strong>building</strong> and needs a building permit and must meet the building code.</p>

<h2>Step 2: Questions for a tiny home on wheels</h2>
<ul>
<li><strong>Can it be licensed?</strong> Ask how the builder gets the trailer licensed with the Department of Transport. A trailer with a damaged or missing VIN can't be licensed.</li>
<li><strong>Is it road legal size?</strong> Over <strong>2.5 m wide</strong> or <strong>4.3 m high</strong> needs a Main Roads permit to move.</li>
<li><strong>Who delivers it?</strong> Ask who moves it and what's included.</li>
<li><strong>Where can you live in it?</strong> Most councils limit living in a caravan on private land, so check with yours first.</li>
</ul>

<h2>Step 3: Questions for a fixed tiny home</h2>
<ul>
<li><strong>Are they registered?</strong> Work on a home worth over <strong>$20,000</strong> that needs a permit must be done by a registered builder or an approved owner-builder. Be careful of "permit-free" or "DIY" claims; the state warns they can be misleading.</li>
<li><strong>Who gets the permit?</strong> Ask who handles the Certificate of Design Compliance and building permit.</li>
<li><strong>Is there home indemnity insurance?</strong> It's required for permit work over $20,000. You can check the policy on the insurer's register.</li>
</ul>

<h2>Step 4: Check the contract and payments</h2>
<ul>
<li>For home building work between <strong>$7,500 and $500,000</strong>, the contract must be in writing and signed.</li>
<li>The deposit can be no more than <strong>6.5%</strong>, and progress payments should only be for work done.</li>
<li>For modular homes, the state suggests a small deposit, payments tied to stages, asking for proof of progress, and visiting the site.</li>
</ul>

<h2>Step 5: Compare prices fairly</h2>
<p>Advertised Perth prices in 2026 range from about <strong>$26,500</strong> to over <strong>$190,000</strong>. Check what each price includes: delivery, connection to power and water, and permits are often extra.</p>
<p>See <a href="/tiny-home-prices-perth">tiny home prices in Perth</a>, <a href="/wheels-vs-fixed-tiny-home">wheels vs fixed</a>, or <a href="/buying-second-hand-tiny-home">buying a second-hand tiny home</a>.</p>
"""

FAQS = [
    ("Does a tiny home builder in WA need to be registered?",
     "For a fixed tiny home worth over $20,000 that needs a building permit, yes, unless you're an approved owner-builder. A tiny home on wheels is a caravan, so builder registration doesn't apply in the same way."),
    ("How much deposit should I pay a tiny home builder?",
     "For a home building contract, the deposit can be no more than 6.5%. Progress payments should only be for work done."),
    ("What should I ask a tiny home on wheels builder?",
     "Ask how it will be licensed, whether it's under 2.5 m wide and 4.3 m high, who delivers it, and what's included in the price."),
    ("Are permit-free tiny homes real?",
     "There are no special exemptions for prefab homes in WA. A fixed tiny home needs a building permit, and the state warns that permit-free claims can be misleading."),
]


def page(S):
    return {"path": "choosing-a-tiny-home-builder.html", "published": "2026-11-20", "type": "How-to guide", "icon": "plan",
            "card": "How to choose a tiny home builder in Perth: the questions to ask and the red flags.",
            "title": "How to Choose a Tiny Home Builder in Perth (2026)",
            "desc": "How to choose a tiny home builder in Perth: questions for wheels and fixed builds, registration, licensing, deposits, contracts and comparing prices.",
            "eyebrow": "How-to guide", "h1": "How to choose a tiny home builder in Perth", "crumb": "Choosing a tiny home builder",
            "answer": "<p>First decide on <strong>wheels or fixed</strong>. For wheels, ask how it'll be <strong>licensed</strong> and moved. For fixed, check the builder is <strong>registered</strong> and handles the <strong>building permit</strong>. Get a written contract, pay no more than a <strong>6.5% deposit</strong>, and be wary of \"permit-free\" claims.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-prices-perth", "Tiny home prices in Perth"), ("/wheels-vs-fixed-tiny-home", "Wheels vs fixed tiny home"), ("/buying-second-hand-tiny-home", "Buying a second-hand tiny home")],
            "sources": [("Building or renovating your home, Building and Energy", "https://www.wa.gov.au/organisation/building-and-energy/building-or-renovating-your-home"),
                        ("Tiny houses fact sheet, WAPC", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf"),
                        ("Licensing a caravan or camper trailer, Department of Transport", "https://transport.wa.gov.au/licensing/vehicle/license-vehicle/caravan-camper-trailer"),
                        ("Permit Order Scheme, Main Roads WA", "https://www.mainroads.wa.gov.au/heavy-vehicles/permit-order-scheme/")]}
