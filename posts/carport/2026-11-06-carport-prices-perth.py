BODY = """
<h2>What Perth businesses advertise</h2>
<p>These are the businesses' own published price guides, checked in November 2026. They are not quotes, and they change.</p>
<div class="table-wrap"><table>
<thead><tr><th>Type</th><th>Advertised range</th><th>Source</th></tr></thead><tbody>
<tr><td>DIY single carport kit (materials only)</td><td>$2,000 to $5,000</td><td>Phoenix Patios</td></tr>
<tr><td>DIY double carport kit (materials only)</td><td>$4,000 to $7,500</td><td>Phoenix Patios</td></tr>
<tr><td>Single carport, installed</td><td>$5,500 to $8,500</td><td>Phoenix Patios</td></tr>
<tr><td>Double carport, installed</td><td>$7,000 to $12,500+</td><td>Phoenix Patios</td></tr>
<tr><td>Double carport kit</td><td>From $7,500 (low wind areas), with WA pricing 20% higher</td><td>Modern Steel Buildings</td></tr>
</tbody></table></div>
<p>Phoenix Patios also lists site preparation at $1,500 to $6,000 and stormwater drainage at $500 to $1,500, and says gable roofs cost 20 to 30% more than flat (skillion) roofs.</p>

<h2>What pushes the price up</h2>
<ul>
<li><strong>Size and height</strong>: a double (about 6 m x 6 m) costs more than a single (about 3 m x 6 m). Extra height for a 4WD or caravan adds more.</li>
<li><strong>Roof style</strong>: flat is cheapest; gable costs more.</li>
<li><strong>Ground</strong>: sloping or uneven ground, or a new slab, adds to the bill.</li>
<li><strong>Extras</strong>: drainage, lighting or an EV charger (licensed electrician needed).</li>
</ul>

<h2>The approval costs</h2>
<p>Most carports in WA need a building permit. The government fees are small next to the build:</p>
<div class="table-wrap"><table>
<thead><tr><th>Fee</th><th>Amount</th><th>On a $10,000 carport</th></tr></thead><tbody>
<tr><td>Building permit (BA2, uncertified)</td><td>0.32% of the value, at least $121</td><td>$121</td></tr>
<tr><td>Building Services Levy</td><td>$61.65 for work up to $45,000</td><td>$61.65</td></tr>
<tr><td><strong>Total government fees</strong></td><td></td><td><strong>$182.65</strong></td></tr>
</tbody></table></div>
<p>A carport in the front setback, or one that doesn't meet the R-Codes, may also need planning approval, which has its own fee. You'll also usually need engineering for the structure, which kit suppliers often include.</p>
<p>See the full breakdown in <a href="/carport-approval-cost-perth">carport approval cost in Perth</a>, or check whether yours needs planning approval with the <a href="/front-setback-carport-calculator">front setback carport calculator</a>.</p>

<h2>Comparing quotes</h2>
<p>Ask each supplier what's included: engineering, the permit application, footings or slab, drainage and the wind rating for your area. A cheap kit quote may leave the approval and site work to you.</p>
"""

FAQS = [
    ("How much does a carport cost in Perth?",
     "Perth businesses advertise about $5,500 to $8,500 for an installed single carport and $7,000 to $12,500+ for an installed double. DIY kits start around $2,000 to $5,000 for a single."),
    ("How much is a double carport kit in Perth?",
     "Advertised prices range from about $4,000 to $7,500 for materials only, depending on the supplier, roof style and wind rating."),
    ("How much does carport council approval cost in Perth?",
     "Government fees for a $10,000 carport are about $182.65: a $121 minimum BA2 permit fee plus the $61.65 levy. Planning approval, if needed, is extra."),
    ("Do I need council approval for a carport in WA?",
     "Usually, yes. Most carports need a building permit, and some also need planning approval, for example in the front setback."),
]


def page(S):
    return {"path": "carport-prices-perth.html", "published": "2026-11-06", "type": "Cost guide", "icon": "price",
            "card": "Advertised kit and installed prices, plus the approval fees on top.",
            "title": "Carport Prices in Perth (2026), Approvals Included",
            "desc": "What carports cost in Perth in 2026: advertised kit and installed prices from local businesses, what pushes the price up, and the permit fees on top.",
            "eyebrow": "Cost guide", "h1": "Carport prices in Perth (2026), approvals included", "crumb": "Carport prices",
            "answer": "<p>Perth businesses advertise <strong>$5,500 to $8,500</strong> for an installed single carport and <strong>$7,000 to $12,500+</strong> for an installed double. DIY kits start around <strong>$2,000</strong>. On top of that, government permit fees for a $10,000 carport are about <strong>$182.65</strong>, plus planning approval if your council needs it.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-approval-cost-perth", "Carport approval cost in Perth"), ("/carport-council-approval", "Carport council approval"), ("/front-setback-carport-calculator", "Front setback carport calculator")],
            "sources": [("How much does a carport cost in Perth? (Phoenix Patios, January 2026)", "https://phoenixpatios.com.au/blog/carport-cost-perth/"),
                        ("Carport kit price guide (Modern Steel Buildings)", "https://modernsteelbuildings.com.au/product/carport-kits-prices-latest-specials/"),
                        ("Building approvals: forms, fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
