BODY = """
<h2>The key difference: wheels</h2>
<p>A <strong>tiny home on wheels</strong> that stays towable is treated as a <strong>caravan</strong> in WA. A <strong>transportable home</strong> is built off-site and then placed on footings or stumps on your land, so it's a <strong>building</strong>. That one difference changes almost every rule.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Tiny home on wheels</th><th>Transportable home</th></tr></thead><tbody>
<tr><td>What the law calls it</td><td>A caravan</td><td>A building (house or granny flat)</td></tr>
<tr><td>Building permit</td><td>Not needed</td><td>Needed</td></tr>
<tr><td>Building code (NCC)</td><td>Doesn't apply as a building</td><td>Must comply</td></tr>
<tr><td>How long you can live in it</td><td>5 nights in 28 days without approval; up to 24 months with council approval</td><td>Permanently, once approved</td></tr>
<tr><td>Registration</td><td>Licensed with the Department of Transport</td><td>Not registered as a vehicle</td></tr>
<tr><td>Who can install it</td><td>Not a building job</td><td>Registered builder or approved owner-builder, if a habitable building over $20,000</td></tr>
</tbody></table></div>

<h2>No shortcut for prefab</h2>
<p>WA's building regulator and Consumer Protection have warned that there are <strong>no special exemptions</strong> for prefabricated or modular buildings. Claims that a kit or transportable home is "permit-free" may be misleading. Electrical and plumbing work must be done by licensed trades.</p>

<h2>Buying tips from Consumer Protection</h2>
<ul>
<li>Pay a <strong>small deposit</strong>, with progress payments tied to manufacturing, delivery and installation</li>
<li>Ask for <strong>evidence</strong> of progress before each payment</li>
<li>Visit the factory or site if you can</li>
</ul>

<h2>Which suits you?</h2>
<ul>
<li><strong>Tiny home on wheels</strong> if you need to move it, or only want a temporary home while you build.</li>
<li><strong>Transportable home</strong> if you want a permanent home that you can live in for good once it's approved, often as a granny flat.</li>
</ul>
<p>Read <a href="/fixed-tiny-home-permit">fixed tiny home permits</a>, <a href="/tiny-home-vs-caravan">tiny home vs caravan</a> or <a href="/wheels-vs-fixed-tiny-home">wheels vs fixed tiny homes</a>.</p>
"""

FAQS = [
    ("Does a transportable home need a building permit in WA?",
     "Yes. Once it's on footings or stumps it's a building, and there are no special exemptions for prefabricated or modular buildings."),
    ("Is a tiny home on wheels a transportable home?",
     "No. A tiny home on wheels that stays towable is a caravan. A transportable home is placed on footings and becomes a building."),
    ("Can I live permanently in a transportable home?",
     "Yes, once it's approved as a house or granny flat. A tiny home on wheels can't be lived in permanently outside a caravan park under current rules."),
    ("Who can install a transportable home?",
     "If it's a habitable building over $20,000 that needs a permit, a registered builder or an approved owner-builder."),
]


def page(S):
    return {"path": "tiny-home-vs-transportable.html", "published": "2026-11-14", "type": "Comparison", "icon": "tiny",
            "card": "Why a tiny home on wheels is a caravan but a transportable home is a building, and what that means.",
            "title": "Tiny Home vs Transportable Home: Approvals Compared (WA)",
            "desc": "Tiny home vs transportable home in WA: a towable tiny home is a caravan, a transportable on footings is a building that needs a permit. Rules side by side.",
            "eyebrow": "Comparison", "h1": "Tiny home vs transportable home", "crumb": "Tiny home vs transportable",
            "answer": "<p>A <strong>tiny home on wheels</strong> is legally a caravan: no building permit, but you can only live in it for up to <strong>24 months</strong> at a time with council approval. A <strong>transportable home</strong> on footings is a <strong>building</strong>: it needs a building permit and must meet the building code, but once approved you can live in it permanently.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/fixed-tiny-home-permit", "Fixed tiny home permit"), ("/tiny-home-vs-caravan", "Tiny home vs caravan"), ("/wheels-vs-fixed-tiny-home", "Wheels vs fixed tiny home")],
            "sources": [("Tiny houses fact sheet, December 2024 (WAPC)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf"),
                        ("Building approvals (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
