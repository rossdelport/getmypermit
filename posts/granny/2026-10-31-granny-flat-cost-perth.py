BODY = """
<h2>What Perth builders advertise in 2026</h2>
<p>These are the builders' own published starting prices. They are a guide to the range, not quotes, and what's included differs.</p>
<div class="table-wrap"><table>
<thead><tr><th>Builder (advertised)</th><th>Starting price</th><th>What it covers</th></tr></thead><tbody>
<tr><td>Fox Granny Flats</td><td>From $119,000 (panel) or $145,000 (steel frame)</td><td>Starting prices; see their site for inclusions</td></tr>
<tr><td>Granny Flats WA</td><td>From $130,000 for a budget one-bed investor spec, move-in ready; can exceed $275,000</td><td>Move-in ready at the budget end</td></tr>
<tr><td>Summit Granny Flats</td><td>1-bed from $171,218; 2-bed from $183,555; 3-bed from $196,689</td><td>Base build only. Finishes (about $15,000 for 50 m&sup2;, $20,000 for 70 m&sup2;) and site works are extra</td></tr>
</tbody></table></div>
<p>One Perth builder puts construction at roughly <strong>$2,200 to $3,250 per m&sup2;</strong>. For the largest granny flat that can skip planning approval (70 m&sup2;), that's about $154,000 to $227,500.</p>

<h2>Costs on top of the build price</h2>
<ul>
<li><strong>Site works.</strong> Slope, soil, access for trucks and the distance to power, water and sewer. Builders say this is where most surprise costs come from, so get the site assessed before you sign.</li>
<li><strong>Finishes.</strong> Flooring, carpets, blinds, painting and air conditioning are not always in the base price.</li>
<li><strong>Bushfire (BAL) report and upgrades</strong>, if the lot is bushfire-prone.</li>
<li><strong>Verge bond.</strong> Many councils hold a refundable bond during building, for example $1,900 plus a $100 inspection fee at the City of Melville, or $2,200 plus a $140 admin fee at the City of Wanneroo.</li>
</ul>

<h2>The approval costs: worked examples</h2>
<p>Every granny flat needs a building permit. The fees are set by the state, so they're the same at every council. For a granny flat lodged as an uncertified application (BA2), the permit is 0.32% of the value. The Building Services Levy is 0.137% for work over $45,000, and the Construction Training Fund levy is 0.2% for work over $100,000 (paid straight to the fund).</p>
<div class="table-wrap"><table>
<thead><tr><th>Value of the build</th><th>Permit (BA2)</th><th>Building Services Levy</th><th>CTF levy</th><th>Total</th></tr></thead><tbody>
<tr><td>$150,000</td><td>$480.00</td><td>$205.50</td><td>$300.00</td><td><strong>$985.50</strong></td></tr>
<tr><td>$180,000</td><td>$576.00</td><td>$246.60</td><td>$360.00</td><td><strong>$1,182.60</strong></td></tr>
<tr><td>$200,000</td><td>$640.00</td><td>$274.00</td><td>$400.00</td><td><strong>$1,314.00</strong></td></tr>
</tbody></table></div>
<p>With a certified application (BA1) the permit fee drops to 0.19%, but you also pay a private building surveyor. Plans, engineering and the energy efficiency report are usually part of the builder's price.</p>
<p>A granny flat of up to 70 m&sup2; that meets all the standard planning rules doesn't need planning approval, which saves a fee and up to 60 days. <a href="/granny-flat-no-planning-approval">See when you can skip planning approval</a>.</p>
"""

FAQS = [
    ("How much does a granny flat cost in Perth in 2026?",
     "Perth builders advertise starting prices from about $119,000 to $196,000, depending on size and how much is included. Site works and finishes can add tens of thousands, so get a site assessment before you sign."),
    ("How much are council fees for a granny flat in WA?",
     "For a $150,000 granny flat lodged as a BA2, the permit is $480, the Building Services Levy $205.50 and the Construction Training Fund levy $300, about $985 in total. Planning approval, if needed, is extra."),
    ("What is the cheapest way to build a granny flat in Perth?",
     "Keep it to 70 m&sup2; or less and design it to meet the standard planning rules, so you skip planning approval. A simple design on a flat, accessible block near existing services keeps site works down."),
    ("Is a 2-bedroom granny flat much more expensive than a 1-bedroom?",
     "Not always. Summit Granny Flats, for example, advertises its 2-bedroom from $183,555 against $171,218 for its 1-bedroom, a difference of about $12,000 in base price."),
]


def page(S):
    return {"path": "granny-flat-cost-perth.html", "published": "2026-10-31", "type": "Cost guide", "icon": "price",
            "card": "What Perth builders charge in 2026, the costs on top, and worked examples of the council fees and levies.",
            "title": "Granny Flat Cost in Perth (2026): Builder Prices and Council Fees",
            "desc": "Granny flats in Perth start from about $119,000 to $196,000 in 2026, before site works and finishes. Builder prices compared and worked examples of the council fees and levies.",
            "eyebrow": "Cost guide", "h1": "Granny flat cost in Perth (2026)", "crumb": "Granny flat cost",
            "answer": "<p>Perth builders advertise granny flats from about <strong>$119,000 to $196,000</strong> in 2026, depending on size and what's included. <strong>Site works and finishes</strong> can add a lot on top. The council fees and levies are small by comparison: about <strong>$985 for a $150,000 build</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-no-planning-approval", "Granny flat with no planning approval"), ("/granny-flat-approval-process", "The granny flat approval process")],
            "sources": [("How much does a granny flat cost in WA? (Summit Homes, July 2026)", "https://www.summithomes.com.au/journal/how-much-does-a-granny-flat-cost-in-wa/"),
                        ("Fox Granny Flats", "https://www.foxgrannyflats.com.au/"),
                        ("Granny Flats WA", "https://www.grannyflatswa.com/"),
                        ("Granny flat cost in Perth 2026 (Boda Building Group)", "https://www.bodabuildinggroup.com.au/blog/building-a-granny-flat-in-perth/"),
                        ("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                        ("Building approvals and the Building Services Levy (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Construction Training Fund levy", "https://ctf.wa.gov.au/levy"),
                        ("Building a shed or outbuilding: verge bond (City of Melville)", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding"),
                        ("Patios information sheet with verge bond fees (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf")]}
