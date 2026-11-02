BODY = """
<h2>Why you can't just split it off</h2>
<p>Under the R-Codes, a granny flat (an "ancillary dwelling") has to be on the <strong>same lot</strong> as the main house. The state's R-Codes guidance says subdivision into strata, built-strata or green-title lots to put the granny flat on its own lot <strong>isn't permitted</strong>. The house and granny flat are treated as two dwellings on one lot.</p>

<h2>The only way to subdivide</h2>
<p>You can only subdivide if the lot meets the <strong>minimum site area</strong> for its R-Code, and the result meets all the other R-Codes rules. The two homes are then no longer a house and a granny flat. They become <strong>two grouped dwellings</strong> or <strong>two single houses</strong>.</p>
<p>That usually means more than just a title change. Each home has to meet the rules for a full dwelling, which can include things like open space, outdoor living areas and parking.</p>

<h2>What this means when you build</h2>
<ul>
<li>A granny flat is limited to <strong>70 m²</strong> and doesn't need a minimum lot size, which makes it easy to approve, but it stays tied to the house.</li>
<li>If you think you'll want to sell the second home separately one day, check your lot's R-Code and minimum site area first. Building to grouped dwelling rules from the start may make more sense.</li>
<li>Anyone can live in a granny flat now, including tenants, so renting it out doesn't need subdivision.</li>
</ul>
"""

FAQS = [
    ("Can I subdivide my granny flat in WA?",
     "Not as a granny flat. The R-Codes don't allow a granny flat to be put on its own lot. You can only subdivide if the lot meets the minimum site area for its R-Code, and the two homes then become grouped dwellings or single houses."),
    ("Can I sell my granny flat separately?",
     "Not while it's a granny flat, because it must stay on the same lot as the main house. Selling separately needs a subdivision that meets the R-Codes rules for two full dwellings."),
    ("Can I strata title a granny flat?",
     "No. The R-Codes guidance says strata, built-strata and green-title subdivision of a granny flat isn't permitted, unless the site meets the requirements for two grouped dwellings or single houses."),
    ("Can I rent out my granny flat without subdividing?",
     "Yes. There's no longer a rule that only family can live in a granny flat, so you can rent it out on the same lot."),
]


def page(S):
    return {"path": "subdivide-granny-flat.html", "published": "2026-11-03", "type": "Question answer", "icon": "granny",
            "card": "Why a granny flat can't go on its own title, and the only way to split it off.",
            "title": "Can I Subdivide My Granny Flat Later? (WA Rules)",
            "desc": "Can you subdivide or strata title a granny flat in WA? Why the R-Codes don't allow it, the only way to split it off, and what to think about before you build.",
            "eyebrow": "Question answer", "h1": "Can I subdivide my granny flat later?", "crumb": "Subdivide a granny flat",
            "answer": "<p><strong>Not as a granny flat.</strong> The R-Codes say a granny flat must stay on the same lot as the house, so strata or green-title subdivision isn't allowed. You can only subdivide if the lot meets the <strong>minimum site area</strong> for its R-Code, and the two homes become grouped dwellings or single houses.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-minimum-lot-size", "Granny flat minimum lot size"), ("/granny-flat-size-calculator", "Granny flat 70 m² calculator")],
            "sources": [("R-Codes Volume 1 Explanatory Guidelines, 2024 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-04/r-codes-vol-1-explanatory-guideline_2024-mar2024.pdf"),
                        ("Granny flats information sheet (Department of Planning, Lands and Heritage)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf")]}
