BODY = """
<h2>What changed recently</h2>
<div class="table-wrap"><table>
<thead><tr><th>When</th><th>What</th><th>What it means for tiny homes</th></tr></thead><tbody>
<tr><td>April 2024</td><td>New R-Codes Volume 1 took effect</td><td>Granny flats no longer need a 350 m² lot, so a fixed tiny home can be a granny flat on smaller and strata lots</td></tr>
<tr><td>August 2024</td><td>State fact sheet on temporary accommodation published (last updated June 2026)</td><td>Sets out the 5 night and 24 month rules for living in a tiny home on wheels on private land</td></tr>
<tr><td>December 2024</td><td>State fact sheet on tiny houses published</td><td>Explains when a tiny home is a caravan and when it's a building</td></tr>
</tbody></table></div>

<h2>Tiny homes on wheels</h2>
<p>If your tiny home is a genuine vehicle (built to be towed, not just able to be moved), the law treats it as a <strong>caravan</strong>. It doesn't need a building permit, and usually doesn't need planning approval. But where you can live in it is limited:</p>
<ul>
<li><strong>Up to 5 nights</strong> with the property owner's approval</li>
<li><strong>Up to 24 months</strong> with approval from the owner <strong>and</strong> your council</li>
<li>After 24 months, you have to apply again</li>
</ul>
<p>Council can set conditions, such as having power, water, sewage and cooking facilities. If council says no, or cancels an approval, you can ask the <strong>Minister for Local Government</strong>, and council can't revoke a Minister's approval.</p>
<p>Living in a caravan <strong>permanently</strong> outside a caravan park still isn't allowed.</p>

<h2>Fixed tiny homes</h2>
<p>Take the wheels off and it's a <strong>building</strong>. A tiny home can't be both. As a building it needs a building permit and has to meet the National Construction Code. On a residential lot it's usually treated as a single house or a granny flat (up to 70 m²). It can skip planning approval if it meets all the standard R-Codes rules.</p>
<p>The state says the building code has <strong>no minimum room sizes</strong>, and a home as small as about 20 m² could comply if it's carefully designed. A registered building surveyor has to sign off that the design complies before a permit is issued.</p>

<h2>What hasn't changed</h2>
<p>The state's fact sheet notes people have asked for tiny homes on wheels to be approved for permanent living outside caravan parks, and for some building code rules (like loft bedrooms and ladders) to be relaxed. It says the current rules <strong>can't accommodate</strong> those requests. We'll update this page if that changes.</p>
"""

FAQS = [
    ("Are there new tiny home laws in WA?",
     "The main recent changes are the 2024 R-Codes (granny flats no longer need a 350 m² lot) and two state fact sheets from 2024 that explain the rules for tiny homes on wheels and fixed tiny homes. Living permanently in a tiny home on wheels outside a caravan park still isn't allowed."),
    ("How long can I live in a tiny home on wheels in WA?",
     "Up to 5 nights with the property owner's approval, or up to 24 months with approval from both the owner and the council. You can apply again after 24 months."),
    ("Does a tiny home on wheels need a building permit in WA?",
     "No, if it's a genuine vehicle it's treated as a caravan. A tiny home without wheels is a building and needs a building permit."),
    ("Is there a minimum size for a tiny home in WA?",
     "The building code doesn't set minimum room sizes. The state says a home of about 20 m² could comply if it's carefully designed."),
]


def page(S):
    return {"path": "new-tiny-home-laws-wa.html", "published": "2026-11-02", "type": "Question answer", "icon": "tiny",
            "card": "What's changed for tiny homes in WA since 2024, for homes on wheels and fixed ones.",
            "title": "New Tiny Home Laws in WA: What's Changed (2026)",
            "desc": "The tiny home rules in WA explained: 2024 R-Codes changes, the 5 night and 24 month rules for homes on wheels, Minister approvals, and permits for fixed tiny homes.",
            "eyebrow": "Question answer", "h1": "What are the new tiny home laws in WA?", "crumb": "New tiny home laws",
            "answer": "<p>There's no single new tiny home law. Since 2024, the R-Codes dropped the minimum lot size for granny flats, and the state has set out the rules: a tiny home <strong>on wheels</strong> can be lived in for <strong>up to 24 months</strong> with owner and council approval, then re-applied for. A <strong>fixed</strong> tiny home is a building and needs a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules in WA"), ("/fixed-tiny-home-permit", "Fixed tiny home permits"), ("/wheels-vs-fixed-tiny-home", "Wheels vs fixed tiny home")],
            "sources": [("Tiny houses fact sheet, December 2024 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf"),
                        ("Temporary accommodation and camping outside of caravan parks, updated June 2026 (WA Government)", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks"),
                        ("Granny flats information sheet (Department of Planning, Lands and Heritage)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf")]}
