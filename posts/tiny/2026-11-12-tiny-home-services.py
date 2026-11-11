BODY = """
<h2>Why services matter for approval</h2>
<p>If you want to live in a tiny home on wheels for more than <strong>5 nights in any 28 days</strong>, you need council approval. Under the Caravan Parks and Camping Grounds Regulations, the council can approve up to 24 months, and can set conditions so the land is <strong>safe</strong> and has <strong>access to services</strong>. So your plan for power, water and waste is a big part of the application.</p>

<h2>What one council asks for</h2>
<p>The City of Swan's temporary accommodation form shows the kind of detail councils want:</p>
<div class="table-wrap"><table>
<thead><tr><th>Service</th><th>What you tell the council</th></tr></thead><tbody>
<tr><td>Wastewater</td><td>Sewer, an existing system, or a new onsite system</td></tr>
<tr><td>Water</td><td>Scheme water or a tank</td></tr>
<tr><td>Power</td><td>How it's supplied</td></tr>
<tr><td>Ablutions</td><td>Toilet, shower, wash trough and kitchen sink</td></tr>
</tbody></table></div>
<p>Swan also asks for a layout plan, a site plan showing how close it is to buildings and neighbours' houses, a copy of the registration, and a bushfire plan if the land is bushfire prone. Councils vary, so check your council's form.</p>

<h2>Keep it movable</h2>
<p>A tiny home on wheels is treated as a caravan. Regulation 15 says it must keep its wheels and be able to be moved within <strong>24 hours</strong> of disconnecting its services. The fine is up to <strong>$5,000</strong>. So use connections that can be undone, not ones that fix it to the ground.</p>

<h2>Step by step</h2>
<ol>
<li><strong>Ask your council</strong> what it accepts for wastewater, water and power on your lot.</li>
<li><strong>Plan each service</strong> and who will connect it. Electrical and plumbing work must be done by licensed trades.</li>
<li><strong>Draw a site plan</strong> showing the tiny home, the connections, and distances to buildings and boundaries.</li>
<li><strong>Apply to the council</strong> with the form, plans and registration.</li>
</ol>

<h2>If it's a fixed tiny home</h2>
<p>Once a tiny home is fixed to the ground, it's a building, not a caravan. It needs a building permit, and its plumbing, power and wastewater are checked like a house or granny flat.</p>
<p>Read <a href="/live-in-caravan-on-own-land-wa">living in a caravan on your own land</a>, <a href="/city-of-swan-tiny-homes">City of Swan tiny homes</a>, or try the <a href="/tiny-home-stay-calculator">tiny home stay calculator</a>.</p>
"""

FAQS = [
    ("Do I need to connect a tiny home on wheels to sewer?",
     "Your council decides what it accepts. The City of Swan asks whether wastewater goes to sewer, an existing system or a new onsite system."),
    ("Can a tiny home on wheels use tank water?",
     "The City of Swan's form lists scheme water or a tank as options. Check what your council accepts."),
    ("Can I hard-wire a tiny home on wheels?",
     "It must be able to be moved within 24 hours of disconnecting its services, so connections should be ones that can be undone. Electrical work must be done by a licensed electrician."),
    ("What does the council need to see about services?",
     "Councils such as Swan ask about wastewater, water, power and ablutions (toilet, shower, wash trough and kitchen sink), plus a site plan."),
]


def page(S):
    return {"path": "tiny-home-services.html", "published": "2026-11-12", "type": "How-to guide", "icon": "tiny",
            "card": "What councils want to know about power, water and waste before approving a tiny home on wheels.",
            "title": "How to Set Up Power, Water and Waste for a Tiny Home (WA)",
            "desc": "How to set up power, water and wastewater for a tiny home on wheels in WA, what councils like Swan ask for, and the 24-hour movability rule.",
            "eyebrow": "How-to guide", "h1": "How to set up power, water and waste for a tiny home",
            "crumb": "Tiny home services",
            "answer": "<p>To live in a tiny home on wheels for more than 5 nights in 28 days, you need council approval, and the council must be satisfied the land has <strong>access to services</strong>. Councils such as Swan ask how you'll handle <strong>wastewater, water, power</strong> and <strong>toilet and shower</strong>. Keep connections removable: it must be movable within <strong>24 hours</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/live-in-caravan-on-own-land-wa", "Living in a caravan on your own land"), ("/city-of-swan-tiny-homes", "City of Swan tiny homes"), ("/tiny-home-stay-calculator", "Tiny home stay calculator")],
            "sources": [("Caravan Parks and Camping Grounds Regulations 1997 (WA legislation)", "https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_s1418.html"),
                        ("Temporary accommodation and camping outside of caravan parks (WA Government)", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks"),
                        ("Tiny houses fact sheet, December 2024 (WAPC)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf")]}
