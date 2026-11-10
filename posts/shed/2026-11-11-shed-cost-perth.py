BODY = """
<h2>What Perth suppliers advertise</h2>
<p>Prices vary a lot with size, wind rating, doors and site work. Here's what two Perth suppliers publish:</p>
<div class="table-wrap"><table>
<thead><tr><th>Shed</th><th>Advertised price</th><th>Source</th></tr></thead><tbody>
<tr><td>Small garden shed, 3 x 3 m</td><td>$2,200 to $4,200 installed</td><td>Phoenix Patios</td></tr>
<tr><td>Single garage, 3.5 x 6 m</td><td>$10,000 to $18,000 installed</td><td>Phoenix Patios</td></tr>
<tr><td>Double garage or workshop, 6 x 6 m</td><td>$16,000 to $30,000 installed</td><td>Phoenix Patios</td></tr>
<tr><td>Large workshop, 6 x 9 m</td><td>$22,000 to $40,000 installed</td><td>Phoenix Patios</td></tr>
<tr><td>Double garage kit, 6 x 6 m</td><td>From $10,385 (kit only)</td><td>Modern Steel Buildings</td></tr>
<tr><td>3-bay garage kit, 6 x 9 m</td><td>From $12,795 (kit only)</td><td>Modern Steel Buildings</td></tr>
</tbody></table></div>
<p>Modern Steel Buildings says its prices are for standard low-to-medium wind ratings. Phoenix Patios says a DIY kit can save 20 to 40% on labour.</p>

<h2>Where the money goes</h2>
<p>Phoenix Patios breaks down a typical single garage (about $12,000 to $18,000 installed) like this:</p>
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th>Typical cost</th></tr></thead><tbody>
<tr><td>Shed kit (frame, cladding, roof, doors)</td><td>$4,500 to $7,500</td></tr>
<tr><td>Concrete slab</td><td>$3,000 to $5,000</td></tr>
<tr><td>Engineering and council fees</td><td>$500 to $1,500</td></tr>
<tr><td>Installation</td><td>$3,000 to $5,000</td></tr>
</tbody></table></div>

<h2>The approval costs, in detail</h2>
<p>The council's part is set by state rules and is smaller than most people expect:</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Amount</th></tr></thead><tbody>
<tr><td>Uncertified permit fee (BA2)</td><td>0.32% of the value, minimum $121</td></tr>
<tr><td>Certified permit fee (BA1)</td><td>0.19% of the value, minimum $121, plus a private building surveyor's fee</td></tr>
<tr><td>Building Services Levy</td><td>$61.65 for work up to $45,000</td></tr>
<tr><td>Structural engineering</td><td>Some kit suppliers include it; otherwise the engineer's fee</td></tr>
<tr><td>Council extras</td><td>Councils vary. Wanneroo, for example, needs a Street and Verge Bond Permit with every building permit.</td></tr>
</tbody></table></div>
<p>Example: a $20,000 shed lodged on a BA2 pays the $121 minimum fee plus the $61.65 levy, so <strong>$182.65</strong> in state fees. The value has to include labour, materials and GST, not just the kit.</p>

<h2>Costs people forget</h2>
<ul>
<li>Site levelling, tree clearing and access for the truck</li>
<li>Drainage, gutters and downpipes</li>
<li>Extra doors, windows and insulation</li>
<li>A bushfire (BAL) assessment if the shed is near the house in a bushfire-prone area</li>
<li>Planning approval if the shed doesn't meet the R-Codes or your council's rules</li>
</ul>
<p>See the full fee breakdown in <a href="/shed-permit-cost-wa">shed permit cost</a>, compare <a href="/kit-shed-vs-custom-shed">kit and custom sheds</a>, or check your size with the <a href="/shed-size-checker">shed size checker</a>.</p>
"""

FAQS = [
    ("How much does a shed cost in Perth?",
     "Phoenix Patios advertises $2,200 to $4,200 installed for a 3 x 3 m garden shed and $16,000 to $30,000 for a 6 x 6 m double garage. Modern Steel Buildings lists 6 x 6 m kits from $10,385."),
    ("How much are council fees for a shed in WA?",
     "An uncertified permit (BA2) is 0.32% of the value with a $121 minimum, plus a $61.65 levy for work up to $45,000. A $20,000 shed pays $182.65 in state fees."),
    ("Is a kit shed cheaper than an installed shed?",
     "Usually. Phoenix Patios says doing it yourself can save 20 to 40% on labour. You still need the slab, engineering and permit."),
    ("Does the value for the permit include labour?",
     "Yes. The value must include goods, labour, services and GST, not just the kit price."),
]


def page(S):
    return {"path": "shed-cost-perth.html", "published": "2026-11-11", "type": "Cost guide", "icon": "price",
            "card": "Advertised Perth shed prices, what the money goes on, and the real approval costs.",
            "title": "Shed Cost in Perth, Approvals Included (2026)",
            "desc": "What a shed costs in Perth in 2026: advertised kit and installed prices, a cost breakdown, and the real council fees, levy and extras for approval.",
            "eyebrow": "Cost guide", "h1": "What a Perth shed really costs, approvals included", "crumb": "Shed cost in Perth",
            "answer": "<p>Perth suppliers advertise about <strong>$2,200 to $4,200</strong> installed for a small 3 x 3 m garden shed and <strong>$16,000 to $30,000</strong> for a 6 x 6 m double garage. State permit fees are small: a $20,000 shed lodged on a BA2 pays <strong>$182.65</strong>. Engineering, the slab and site work make up more of the cost.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-permit-cost-wa", "Shed permit cost"), ("/kit-shed-vs-custom-shed", "Kit vs custom shed"), ("/shed-size-checker", "Shed size checker")],
            "sources": [("How much does a custom shed cost in Perth (Phoenix Patios)", "https://phoenixpatios.com.au/blog/custom-shed-cost-perth/"),
                        ("Perth shed kits (Modern Steel Buildings)", "https://modernsteelbuildings.com.au/product/perth-shed-kits/"),
                        ("Building approvals: fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
