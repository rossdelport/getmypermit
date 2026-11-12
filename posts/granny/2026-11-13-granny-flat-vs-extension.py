BODY = """
<h2>Side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Granny flat</th><th>House extension</th></tr></thead><tbody>
<tr><td>Size limit</td><td>70 m² internal floor area (deemed-to-comply)</td><td>No 70 m² cap; limited by open space and setbacks</td></tr>
<tr><td>Separate home</td><td>Yes, self-contained with its own kitchen and bathroom</td><td>No, part of the house</td></tr>
<tr><td>Can be rented out</td><td>Yes, to anyone (since 2024)</td><td>Only as part of the house</td></tr>
<tr><td>Can be sold separately</td><td>No, it can't be subdivided</td><td>No</td></tr>
<tr><td>Building permit</td><td>Always</td><td>Always</td></tr>
<tr><td>Planning approval</td><td>Usually not, if it meets the rules</td><td>Usually not, if it meets the rules</td></tr>
<tr><td>Parking</td><td>Usually 1 extra bay, unless near frequent transport</td><td>The granny flat parking rule doesn't apply</td></tr>
</tbody></table></div>

<h2>Approvals: much the same</h2>
<p>Both need a <strong>building permit</strong>. Neither needs planning approval if it meets the R-Codes deemed-to-comply rules and council policy, and the lot isn't heritage listed. The City of Melville, for example, says a single house that meets the R-Codes needs no planning approval.</p>
<p>The extra rules for a granny flat: it must be no more than <strong>70 m²</strong>, sit <strong>behind the street setback</strong>, and leave the house with enough open space. Under the R-Codes, a granny flat on most house lots needs <strong>one extra parking bay</strong>, unless it's within 800 m walk of a train station on a frequent line or 250 m of a frequent bus stop.</p>

<h2>Open space applies to both</h2>
<p>Whatever you build, you must keep enough of the lot open. The City of Melville quotes <strong>50%</strong> open space for R15 to R25 lots and 45% for R30 to R40. A big extension or a granny flat can hit this limit first.</p>

<h2>Which suits you?</h2>
<ul>
<li><strong>Granny flat</strong> if you want a separate home for family, a tenant, or privacy.</li>
<li><strong>Extension</strong> if you want more space in the house itself, or more than 70 m².</li>
</ul>
<p>Advertised granny flat prices in Perth start from about $119,000 for a panel build (Fox) and can go over $275,000. We haven't included extension prices, because we couldn't find reliable published figures. See <a href="/granny-flat-cost-perth">granny flat costs in Perth</a>, <a href="/granny-flat-rules-wa">granny flat rules in WA</a> or <a href="/subdivide-granny-flat">subdividing a granny flat</a>.</p>
"""

FAQS = [
    ("Is a granny flat or an extension easier to get approved?",
     "They're similar. Both need a building permit, and neither needs planning approval if it meets the R-Codes. A granny flat has extra rules: 70 m², behind the street setback, and usually a parking bay."),
    ("Can I rent out an extension?",
     "Only as part of the house. A granny flat can be rented separately to anyone, including people unrelated to the household."),
    ("Can a granny flat be bigger than 70 m²?",
     "Not under the deemed-to-comply rules. Bigger needs planning approval, and the council may refuse it. If you need more space, an extension may suit better."),
    ("Does a house extension need a parking bay?",
     "The R-Codes extra bay rule is for granny flats. An extension doesn't trigger it, but check the house still keeps its required parking."),
]


def page(S):
    return {"path": "granny-flat-vs-extension.html", "published": "2026-11-13", "type": "Comparison", "icon": "granny",
            "card": "Size limits, renting, parking and approvals: granny flat vs house extension.",
            "title": "Granny Flat vs House Extension: Approvals Compared (WA)",
            "desc": "Granny flat vs house extension in WA: 70 m² limit, renting to anyone, parking bay and open space. Both need a building permit. Which suits you?",
            "eyebrow": "Comparison", "h1": "Granny flat vs house extension",
            "crumb": "Granny flat vs extension",
            "answer": "<p>Both need a <strong>building permit</strong>, and neither usually needs planning approval if it meets the R-Codes. A <strong>granny flat</strong> is a separate home of up to <strong>70 m²</strong> that you can rent to anyone, but usually needs an extra parking bay. An <strong>extension</strong> has no 70 m² cap but stays part of the house.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-cost-perth", "Granny flat cost in Perth"), ("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/subdivide-granny-flat", "Can I subdivide a granny flat?")],
            "sources": [("Granny flats info sheet (Department of Planning, Lands and Heritage)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf"),
                        ("R-Codes Volume 1, April 2026 (WA Government)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Planning exemptions, City of Melville", "https://www.melvillecity.com.au/planning-and-building/planning-exemptions")]}
