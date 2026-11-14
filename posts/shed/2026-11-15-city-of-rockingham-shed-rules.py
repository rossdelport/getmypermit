BODY = """
<h2>Building permit</h2>
<p>The City of Rockingham lists <strong>garden sheds, garages and workshops</strong> among the work that needs a building permit. The only shed that's exempt under the state's Building Regulations is a <strong>freestanding</strong> shed that is:</p>
<ul>
<li>no bigger than <strong>10 m²</strong> in floor area, and</li>
<li>no more than <strong>2.4 m</strong> high, and</li>
<li>not in wind region C or D.</li>
</ul>
<p>Anything bigger, taller or attached to the house needs a permit before you start. A permit lapses if work hasn't started within 12 months, and the work must be finished within 24 months.</p>

<h2>Planning approval</h2>
<p>Good news for most Rockingham homes. The City says it has, for many years, <strong>not required planning applications</strong> for minor development such as sheds, garages, patios and pools on residential land. These are usually dealt with by a building permit only.</p>
<p>There are exceptions:</p>
<ul>
<li><strong>Special Residential and Special Rural zones</strong> need town planning consent for any development, including a shed, and for any change to the building envelope.</li>
<li>If the shed doesn't meet the standard R-Codes rules (for example, it's too big or too close to the boundary), you may need an <strong>R-Codes approval</strong> as well as the building permit. Call Building Services on 9528 0333 to check.</li>
</ul>

<h2>Fees</h2>
<p>From the City's Building Services fee sheet (updated 7 July 2026):</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Fee</th></tr></thead><tbody>
<tr><td>Uncertified permit (BA2)</td><td>0.32% of the cost, minimum $121</td></tr>
<tr><td>Certified permit (BA1)</td><td>0.19% of the cost, minimum $121</td></tr>
<tr><td>Building services levy</td><td>0.137% of the cost, minimum $61.65</td></tr>
<tr><td>R-Codes variation, work up to $50,000</td><td>$147</td></tr>
<tr><td>Deemed-to-comply check</td><td>$295</td></tr>
<tr><td>Copy of a site or floor plan</td><td>$25</td></tr>
</tbody></table></div>
<p>So a $10,000 shed lodged with a BA2 costs about <strong>$121 + $61.65 = $182.65</strong> in council fees, because both are below their minimums. See <a href="/shed-permit-cost-wa">shed permit cost in WA</a> for more.</p>

<h2>Who can build it</h2>
<p>The City's page says permits for work over $20,000 go to a registered builder or owner-builder. Since <strong>1 July 2026</strong>, the state allows Class 10a buildings such as sheds and garages under $50,000 to be built without a registered builder or owner-builder approval. You still need the building permit first.</p>

<h2>How to apply</h2>
<ol>
<li>Check your zone and R-Code on the City's online maps.</li>
<li>Get your shed plans and engineering from the supplier.</li>
<li>Download the BA1 or BA2 form from the Building and Energy website.</li>
<li>Lodge online through the City's Rock Port portal.</li>
</ol>
<p>Check your size first with the <a href="/shed-size-checker">shed size checker</a>, or read about <a href="/garden-shed-approval">garden shed approval</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a shed in Rockingham?",
     "Yes, unless it's freestanding, no more than 10 m², no more than 2.4 m high and not in wind region C or D."),
    ("Do I need planning approval for a shed in Rockingham?",
     "Usually not on residential land. The City deals with sheds by building permit only. Special Residential and Special Rural lots need town planning consent, and sheds that don't meet the R-Codes may need an R-Codes approval."),
    ("How much is a shed permit in the City of Rockingham?",
     "A BA2 is 0.32% of the cost (minimum $121) plus a 0.137% levy (minimum $61.65). For a $10,000 shed that's about $182.65."),
    ("How do I lodge a shed permit in Rockingham?",
     "Online through the City's Rock Port portal, using a BA1 or BA2 form from the Building and Energy website. Call 9528 0333 with questions."),
]


def page(S):
    return {"path": "city-of-rockingham-shed-rules.html", "published": "2026-11-15", "type": "Council guide", "icon": "pin",
            "card": "When a shed in Rockingham needs a building permit or planning approval, plus fees.",
            "title": "City of Rockingham Shed Rules (2026)",
            "desc": "City of Rockingham shed rules: building permit over 10 m² or 2.4 m, when planning approval applies, fees from the 2026 fee sheet and how to lodge.",
            "eyebrow": "Council guide", "h1": "City of Rockingham shed rules", "crumb": "Rockingham shed rules",
            "answer": "<p>In Rockingham, a shed needs a <strong>building permit</strong> unless it's freestanding, no more than <strong>10 m²</strong> and <strong>2.4 m</strong> high. On residential land the City usually <strong>doesn't need a planning application</strong> for a shed, but Special Residential and Special Rural lots do.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/garden-shed-approval", "Garden shed approval"), ("/shed-permit-cost-wa", "Shed permit cost in WA")],
            "sources": [("Building applications and permits, City of Rockingham", "https://rockingham.wa.gov.au/planning-and-building/lodge-an-application/building-applications-and-permits"),
                        ("Development applications, City of Rockingham", "https://rockingham.wa.gov.au/planning-and-building/lodge-an-application/development-applications"),
                        ("Types of building work for which a building permit is not required, City of Rockingham", "https://rockingham.wa.gov.au/getContentAsset/9f5008ff-5a61-4b36-9593-3041aebec963/3ca954ad-3848-47c6-8f97-68cebe0b47a2/Exempted-Building-Permits.pdf?language=en"),
                        ("Building Services fee sheet, City of Rockingham", "https://rockingham.wa.gov.au/getContentAsset/d92d0adf-466c-4d62-bb92-fc64ccf62f7d/3ca954ad-3848-47c6-8f97-68cebe0b47a2/Building-Services-Fee-Sheet.pdf?language=en")]}
