BODY = """
<h2>Side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Flat (skillion) roof</th><th>Gable (pitched) roof</th></tr></thead><tbody>
<tr><td>Price</td><td>Lower</td><td>Usually 20 to 30% more (Phoenix Patios)</td></tr>
<tr><td>Height</td><td>Lower, easier to keep under height limits</td><td>Taller at the peak</td></tr>
<tr><td>Look</td><td>Simple, modern</td><td>Can match a pitched house roof</td></tr>
<tr><td>On the boundary</td><td>Easier to keep within 2.7 m</td><td>Check the extra height still complies</td></tr>
<tr><td>Building permit</td><td>Needed</td><td>Needed</td></tr>
</tbody></table></div>

<h2>Cost</h2>
<p>Phoenix Patios advertised installed double carports from about <strong>$7,000 to $12,500+</strong> in January 2026, and says a gable roof costs <strong>20 to 30% more</strong>. Prices vary by size, wind rating and site.</p>

<h2>Approval: the roof shape doesn't change the need for a permit</h2>
<p>Both styles need a building permit. The City of Wanneroo and the City of Stirling both say a carport always needs one.</p>
<p>Where roof shape matters is <strong>height</strong>. Under the R-Codes, a carport's posts can sit on the boundary if it's no more than <strong>10 m long</strong> and <strong>2.7 m high</strong>, sits behind the front setback, and the roof edge is at least <strong>450 mm</strong> from the boundary (Wanneroo's sheet says 500 mm). A gable's peak adds height, so check your design against these limits.</p>

<h2>Matching the house</h2>
<p>For carports in the front setback, councils look at whether the carport suits the house. Wanneroo's reduced setback needs <strong>compatible materials</strong>, and Stirling says materials should match. A gable often blends in better with a pitched-roof house. Councils vary, so check yours.</p>

<h2>Which should you pick?</h2>
<ul>
<li><strong>Flat</strong> if you want the lowest price, a modern look, or need to stay under a height limit on the boundary.</li>
<li><strong>Gable</strong> if you want it to match a pitched-roof house and don't mind paying more.</li>
</ul>
<p>See <a href="/carport-prices-perth">carport prices in Perth</a>, <a href="/carport-on-boundary">building a carport on the boundary</a>, or <a href="/attached-vs-freestanding-carport">attached vs freestanding carports</a>.</p>
"""

FAQS = [
    ("Is a gable carport more expensive than a flat one?",
     "Usually yes. Phoenix Patios says a gable roof adds 20 to 30% to the price."),
    ("Does a gable carport need council approval?",
     "Yes. Both flat and gable carports need a building permit. Councils such as Wanneroo and Stirling say a carport always does."),
    ("Can a gable carport go on the boundary?",
     "Only if it meets the limits: under the R-Codes, posts on the boundary are allowed if the carport is no more than 10 m long and 2.7 m high and behind the front setback. Check the peak height."),
    ("Which carport roof looks best?",
     "A gable often matches a pitched-roof house. A flat roof suits a modern house. Councils like the carport to suit the house."),
]


def page(S):
    return {"path": "flat-vs-gable-carport.html", "published": "2026-11-12", "type": "Comparison", "icon": "carport",
            "card": "Price, height, looks and approval: how a flat-roof carport compares with a gable.",
            "title": "Flat vs Gable Carport: Cost and Approval (Perth, WA)",
            "desc": "Flat vs gable carport in Perth: a gable usually costs 20 to 30% more, is taller, and both need a building permit. Height and boundary rules to check.",
            "eyebrow": "Comparison", "h1": "Flat vs gable carport", "crumb": "Flat vs gable",
            "answer": "<p>A <strong>flat</strong> carport is cheaper and lower. A <strong>gable</strong> usually costs <strong>20 to 30% more</strong> but can match a pitched-roof house. Both need a <strong>building permit</strong>. The main approval difference is height: on the boundary, a carport must usually be no more than <strong>2.7 m</strong> high.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-prices-perth", "Carport prices in Perth"), ("/carport-on-boundary", "Carport on the boundary"), ("/attached-vs-freestanding-carport", "Attached vs freestanding carport")],
            "sources": [("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf"),
                        ("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf"),
                        ("R-Codes Volume 1, April 2026 (WA Government)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf")]}
