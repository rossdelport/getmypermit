BODY = """
<h2>Fixed tiny homes are houses</h2>
<p>The Shire of Harvey treats a tiny home lived in on site as a house under the building code. That means:</p>
<ul>
<li>A <strong>building permit</strong> is needed before any site or building work starts.</li>
<li>A <strong>Certificate of Design Compliance</strong> from a registered building surveyor is needed, saying it meets the building code.</li>
<li>It must meet the code's fire separation rules for houses.</li>
</ul>

<h2>Check before you buy</h2>
<p>The Shire warns that many imported and expandable container homes can't show they meet Australian standards. Common gaps are structure, wind rating, energy efficiency, waterproofing and certified materials. Get full compliance paperwork from the seller <strong>before</strong> you pay a deposit.</p>

<h2>Where it can go</h2>
<ul>
<li>Not usually in the <strong>front yard</strong>. The front and corner setbacks follow the R-Codes for your density.</li>
<li>Side and rear setbacks follow the R-Codes, based on wall length and height.</li>
<li>To go closer, apply to the Shire's planners for a setback variation. Extra fees apply.</li>
</ul>

<h2>Bushfire areas</h2>
<p>If your lot is on the state's bushfire prone map, you need a <strong>BAL assessment</strong> by an accredited assessor. The rating decides how the tiny home must be built.</p>

<h2>Timeframes and owner-building</h2>
<div class="table-wrap"><table>
<thead><tr><th>Application</th><th>Shire decides within</th></tr></thead><tbody>
<tr><td>Certified (BA1)</td><td>10 working days</td></tr>
<tr><td>Uncertified (BA2)</td><td>25 working days</td></tr>
</tbody></table></div>
<p>You can owner-build a tiny home. If the work is worth over <strong>$20,000</strong>, you need owner-builder approval from the state first, or a registered builder.</p>
<p>See <a href="/fixed-tiny-home-permit">permits for fixed tiny homes</a>, <a href="/tiny-home-vs-transportable">tiny home vs transportable</a> and <a href="/buying-second-hand-tiny-home">buying second-hand</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a tiny home in the Shire of Harvey?",
     "Yes, for a tiny home lived in on site. It's treated as a house, so you need a building permit and a Certificate of Design Compliance."),
    ("Can I put a tiny home in my front yard in Harvey?",
     "Usually not. Tiny homes generally aren't allowed in the front setback area, and side and rear setbacks follow the R-Codes."),
    ("Can I owner-build a tiny home in Harvey?",
     "Yes. If it's worth over $20,000, you need owner-builder approval from the state before the permit can be issued."),
    ("Are container homes allowed in the Shire of Harvey?",
     "Only if they meet the building code. The Shire warns many imported expandable container homes can't prove this, so get paperwork before you buy."),
]


def page(S):
    return {"path": "shire-of-harvey-tiny-homes.html", "published": "2026-11-23", "type": "Council guide", "icon": "pin",
            "card": "Shire of Harvey tiny home rules: permits, container home warnings, setbacks and bushfire areas.",
            "title": "Shire of Harvey Tiny Home Rules (2026)",
            "desc": "Shire of Harvey tiny home rules: building permit and design compliance, warnings on imported container homes, front and side setbacks, bushfire BAL, owner-building and how long it takes.",
            "eyebrow": "Council guide", "h1": "Shire of Harvey tiny home rules", "crumb": "Harvey tiny homes",
            "answer": "<p>The Shire of Harvey treats a tiny home lived in on site as a <strong>house</strong>. It needs a <strong>building permit</strong> and a <strong>Certificate of Design Compliance</strong>, can't usually go in the front yard, and needs a BAL report in bushfire areas. The Shire decides in 10 working days (BA1) or 25 (BA2).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/fixed-tiny-home-permit", "Fixed tiny home permit"), ("/tiny-home-vs-transportable", "Tiny home vs transportable"), ("/buying-second-hand-tiny-home", "Buying a second-hand tiny home")],
            "sources": [("Building information sheet: tiny homes, Shire of Harvey", "https://www.harvey.wa.gov.au/wp-content/uploads/2026/09/Tiny-Homes.pdf")]}
