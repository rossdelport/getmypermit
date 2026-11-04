BODY = """
<h2>Tiny homes on wheels</h2>
<p>The Shire treats a tiny home on wheels that can be towed as a <strong>caravan</strong> (or a park home). On private land:</p>
<ul>
<li>Using it for <strong>more than 5 days in any 28-day period</strong> needs <strong>development approval</strong> as a temporary land use under the Shire's Local Planning Scheme No. 3.</li>
<li>Council can approve it for up to <strong>24 months</strong> in a row under the state's caravan regulations.</li>
<li>If you're waiting to build a house on the lot, the Shire's <strong>Local Planning Policy 4.5</strong> (Short Term and Temporary Accommodation) may support a tiny home on wheels in the meantime.</li>
</ul>
<p>Approvals come with conditions: the tiny home must be kept safe and healthy, and the land must be suitable, including access to services.</p>

<h2>Tiny homes not on wheels</h2>
<p>A fixed tiny home is assessed as a <strong>single house</strong> (if it's the only home on the lot) or an <strong>ancillary dwelling</strong> (if there's already a house). The Shire's scheme allows up to <strong>100 m²</strong>, more than the 70 m² in the standard R-Codes. Only <strong>one</strong> fixed tiny home can be approved per lot.</p>
<p>It must meet the building code and the Shire's health local laws, including:</p>
<ul>
<li>a kitchen, bathroom and laundry</li>
<li>ceilings at least <strong>2.4 m</strong> in living spaces and <strong>2.1 m</strong> in other spaces</li>
<li>structural certification from an engineer</li>
<li>connection to sewer, drinking water and electricity (including hot water), plus energy efficiency and sanitation standards</li>
<li>a BAL report and Bushfire Management Statement if the lot is bushfire-prone</li>
</ul>
<p>The Shire recommends using a private building surveyor to certify the building permit application.</p>

<h2>Contact</h2>
<p>Shire of Serpentine-Jarrahdale, <strong>(08) 9526 1111</strong>, info@sjshire.wa.gov.au.</p>
"""

FAQS = [
    ("Can I live in a tiny home on wheels in Serpentine-Jarrahdale?",
     "Yes, with approval. More than 5 days in any 28-day period needs development approval, and the Shire can approve it for up to 24 months in a row."),
    ("How big can a fixed tiny home be in Serpentine-Jarrahdale?",
     "Up to 100 m² under the Shire's Local Planning Scheme No. 3. Only one can be approved per lot."),
    ("Can I live in a tiny home while building my house in Serpentine-Jarrahdale?",
     "The Shire's Local Planning Policy 4.5 may support a tiny home on wheels while you wait to build a house on the lot."),
    ("What does a fixed tiny home need in Serpentine-Jarrahdale?",
     "A kitchen, bathroom and laundry, 2.4 m ceilings in living spaces, engineer's certification, connection to sewer, water and power, and a BAL report if bushfire-prone."),
]


def page(S):
    return {"path": "shire-of-serpentine-jarrahdale-tiny-homes.html", "published": "2026-11-05", "type": "Council guide", "icon": "tiny",
            "card": "The 5-in-28-day rule, 24-month approvals and the 100 m² limit for fixed tiny homes.",
            "title": "Shire of Serpentine-Jarrahdale Tiny Home Rules (2026)",
            "desc": "Serpentine-Jarrahdale tiny home rules: development approval after 5 days in 28, 24-month approvals for homes on wheels, and the 100 m² limit and building rules for fixed tiny homes.",
            "eyebrow": "Council guide", "h1": "Shire of Serpentine-Jarrahdale tiny home rules", "crumb": "Serpentine-Jarrahdale tiny homes",
            "answer": "<p>In Serpentine-Jarrahdale, a tiny home on wheels used for <strong>more than 5 days in any 28</strong> needs development approval, and can be approved for up to <strong>24 months</strong>. A fixed tiny home can be up to <strong>100 m²</strong> as a house or granny flat, one per lot, with a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shire-of-mundaring-tiny-homes", "Shire of Mundaring tiny homes"), ("/live-in-caravan-on-own-land-wa", "Living in a caravan on your own land"), ("/fixed-tiny-home-permit", "Fixed tiny home permits")],
            "sources": [("Tiny Home information note (Shire of Serpentine-Jarrahdale)", "https://www.sjshire.wa.gov.au/Profiles/sj/Assets/ClientData/Final_Tiny_Homes_on_Wheels_.pdf"),
                        ("Tiny homes information (Shire of Serpentine-Jarrahdale)", "https://www.sjshire.wa.gov.au/planning-building-and-roads/planning/planning-advice/tiny-homes-information.aspx")]}
