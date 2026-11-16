BODY = """
<h2>Can you build one?</h2>
<p>Yes. The Town of Victoria Park says you can build an ancillary dwelling (granny flat) with a <strong>single house, grouped dwelling or multiple dwelling</strong>, whatever the size of your land, as long as it meets the R-Codes rules for setbacks, site cover, height, privacy and access.</p>

<h2>When you don't need planning approval</h2>
<p>You don't need development approval if the granny flat meets all the deemed-to-comply rules and the property <strong>isn't heritage-protected</strong>. Every granny flat on a heritage-listed property, or in a heritage area, needs development approval.</p>
<p>The main rules for a granny flat with a house (R-Codes Volume 1, Part B):</p>
<ul>
<li>Same lot as a single house or grouped dwelling.</li>
<li>No more than <strong>70 m²</strong> inside (including built-in furniture, not counting a garage).</li>
<li>Behind the street setback line.</li>
<li>The main house still keeps its required open space and outdoor living area.</li>
<li>All other R-Codes rules (privacy, boundary walls, setbacks) still apply.</li>
</ul>
<p>Not sure? The Town offers a paid <strong>deemed-to-comply check</strong> that tells you if you need a development application.</p>

<h2>Parking</h2>
<div class="table-wrap"><table>
<thead><tr><th>Where your lot is</th><th>Extra car bay for the granny flat</th></tr></thead><tbody>
<tr><td>Location A: within 800 m walk of a high-frequency train station, or 250 m of a high-frequency bus stop</td><td>None</td></tr>
<tr><td>Location B: everywhere else</td><td>One extra bay on the lot</td></tr>
</tbody></table></div>
<p>The main house must keep its own parking too. Developments under Part C of the R-Codes don't need an extra bay.</p>

<h2>Other things to know</h2>
<ul>
<li><strong>Who can live there:</strong> anyone. Family, friends or a tenant.</li>
<li><strong>Neighbours:</strong> you don't need their approval to apply. The Town may consult them if you ask to vary the rules.</li>
<li><strong>Timeframe:</strong> 60 days for a development application, or 90 if neighbours are consulted. Lodge online.</li>
<li><strong>Building permit:</strong> always needed, lodged with the Town.</li>
<li><strong>Rates:</strong> once it's finished, the Valuer-General reviews your property's rental value and the Town sends an updated rates notice.</li>
<li><strong>Services:</strong> you may need new meters or sub-meters for power, gas or water.</li>
</ul>
<p>See the <a href="/granny-flat-size-calculator">granny flat size calculator</a>, <a href="/granny-flat-parking">granny flat parking rules</a> and <a href="/granny-flat-no-planning-approval">when no planning approval is needed</a>.</p>
"""

FAQS = [
    ("Can I build a granny flat in the Town of Victoria Park?",
     "Yes, with a single house, grouped dwelling or multiple dwelling, on any lot size, if it meets the R-Codes rules."),
    ("Do I need planning approval for a granny flat in Victoria Park?",
     "Not if it meets all the deemed-to-comply rules and the property isn't heritage-protected. Heritage properties always need development approval."),
    ("Does a Victoria Park granny flat need its own car bay?",
     "Only in Location B, which is anywhere not close to a high-frequency train station or bus stop."),
    ("Who can live in a granny flat in Victoria Park?",
     "Anyone: a relative, a friend or a tenant."),
]


def page(S):
    return {"path": "town-of-victoria-park-granny-flat-rules.html", "published": "2026-11-17", "type": "Council guide", "icon": "pin",
            "card": "Town of Victoria Park granny flat rules: when you need approval, the 70 m² limit and parking.",
            "title": "Town of Victoria Park Granny Flat Rules (2026)",
            "desc": "Town of Victoria Park granny flat rules: when development approval isn't needed, heritage properties, the 70 m² limit, parking by location and timeframes.",
            "eyebrow": "Council guide", "h1": "Town of Victoria Park granny flat rules", "crumb": "Victoria Park granny flats",
            "answer": "<p>In the Town of Victoria Park, a granny flat up to <strong>70 m²</strong> doesn't need planning approval if it meets the R-Codes rules and the property isn't <strong>heritage-protected</strong>. It always needs a <strong>building permit</strong>. You may need one extra car bay, depending on how close you are to public transport.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-size-calculator", "Granny flat size calculator"), ("/granny-flat-parking", "Granny flat parking"), ("/granny-flat-no-planning-approval", "Granny flat without planning approval")],
            "sources": [("Ancillary dwelling (granny flat), Town of Victoria Park", "https://www.victoriapark.wa.gov.au/ancillary-dwelling-granny-flat.aspx"),
                        ("Ancillary dwelling information sheet, WA Planning", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf")]}
