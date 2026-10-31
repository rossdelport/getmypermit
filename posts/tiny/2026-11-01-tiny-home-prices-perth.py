BODY = """
<h2>What sellers advertise in 2026</h2>
<p>These are the sellers' own published starting prices. Sizes, inclusions and whether the home is on wheels differ, so compare like with like.</p>
<div class="table-wrap"><table>
<thead><tr><th>Seller (advertised)</th><th>Starting price</th><th>Notes</th></tr></thead><tbody>
<tr><td>Everyday Tiny Homes (Perth)</td><td>From $26,500</td><td>Also offers weekly payment options</td></tr>
<tr><td>Perth Tiny House</td><td>From $38,990</td><td>The "Lily" two-bedroom model</td></tr>
<tr><td>LJM Tiny Homes</td><td>Homes for sale from $65,200; builds from about $95,000 to $200,000+</td><td>Built in Queensland; delivery to Perth is extra (about 3 to 4 days)</td></tr>
<tr><td>Summit Tiny Homes</td><td>From $192,800</td><td>Standard display range designs</td></tr>
</tbody></table></div>
<p>The gap is huge because "tiny home" covers everything from a basic cabin to a fully built, code-compliant house.</p>

<h2>Costs on top of the price</h2>
<ul>
<li><strong>Delivery.</strong> Within the road limits (2.5 m wide, 4.3 m high) no transport permit is needed. Bigger loads need a Main Roads permit, and loads 4.3 m or higher also need Western Power's authorisation ($120 online in the Perth network). Homes built interstate add long-distance transport.</li>
<li><strong>Site work.</strong> A level pad, and for a fixed home, engineered footings.</li>
<li><strong>Connections.</strong> Power, water and sewer or septic, by licensed trades.</li>
<li><strong>Approvals.</strong> See below.</li>
</ul>

<h2>Approval costs</h2>
<p><strong>On wheels:</strong> no building permit. To live in it for more than 5 nights you need council approval under the caravan rules, for up to 24 months at a time. Fees vary by council; the Shire of Mundaring, for example, offers a $73 preliminary check.</p>
<p><strong>Fixed on footings:</strong> a building permit, with the same state fees as any house. For an uncertified application (BA2) the permit is 0.32% of the value, plus the Building Services Levy (0.137% over $45,000) and the Construction Training Fund levy (0.2% over $100,000).</p>
<div class="table-wrap"><table>
<thead><tr><th>Value of the home and work</th><th>Permit (BA2)</th><th>Building Services Levy</th><th>CTF levy</th><th>Total</th></tr></thead><tbody>
<tr><td>$80,000</td><td>$256.00</td><td>$109.60</td><td>Not payable</td><td><strong>$365.60</strong></td></tr>
<tr><td>$120,000</td><td>$384.00</td><td>$164.40</td><td>$240.00</td><td><strong>$788.40</strong></td></tr>
<tr><td>$192,800</td><td>$616.96</td><td>$264.14</td><td>$385.60</td><td><strong>$1,266.70</strong></td></tr>
</tbody></table></div>
<p>A fixed tiny home must meet the building code, including energy efficiency, and a bushfire report if the lot is bushfire-prone. Planning approval is extra if it doesn't meet the standard rules.</p>

<h2>Before you buy</h2>
<ul>
<li>Decide <strong>wheels or fixed</strong> first; it changes the approvals and what the home must meet. <a href="/wheels-vs-fixed-tiny-home">Compare them</a>.</li>
<li>If it will be fixed, ask the builder in writing whether it's designed to the National Construction Code.</li>
<li>Check your council's rules before paying a deposit.</li>
</ul>
"""

FAQS = [
    ("How much is a tiny home in Perth?",
     "Advertised starting prices in 2026 range from about $26,500 for a basic model to $192,800 for a fixed, display-range design, with many custom builds between $95,000 and $200,000. Delivery, site work and connections are extra."),
    ("What are the council costs for a tiny home in WA?",
     "On wheels, there's no building permit, but living in it longer than 5 nights needs council approval; fees vary. A fixed tiny home needs a building permit: about $789 in fees and levies for a $120,000 home lodged as a BA2."),
    ("Is it cheaper to buy a tiny home on wheels?",
     "Often the home itself is cheaper and there's no building permit, but council approval to live in it is time-limited (up to 24 months at a time), and it doesn't add permanent value to the land."),
    ("Does delivery cost extra?",
     "Usually. Homes within 2.5 m wide and 4.3 m high need no transport permit; bigger ones need Main Roads permits and possibly Western Power authorisation. Homes built interstate add long-distance transport."),
]


def page(S):
    return {"path": "tiny-home-prices-perth.html", "published": "2026-11-01", "type": "Cost guide", "icon": "price",
            "card": "Advertised tiny home prices in Perth for 2026, the costs on top, and worked examples of the approval fees.",
            "title": "Tiny Home Prices in Perth (2026): What They Cost and Approval Fees",
            "desc": "Tiny homes in Perth are advertised from about $26,500 to $192,800 in 2026. What's included, delivery and site costs, and the approval fees for homes on wheels and on footings.",
            "eyebrow": "Cost guide", "h1": "Tiny home prices in Perth (2026)", "crumb": "Tiny home prices",
            "answer": "<p>Perth sellers advertise tiny homes from about <strong>$26,500</strong> for a basic model up to <strong>$192,800</strong> for a fixed, display-range design, with many custom builds at <strong>$95,000 to $200,000+</strong>. Add delivery, site work and connections. A fixed home also needs a building permit: about <strong>$789</strong> in fees and levies for a $120,000 build.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/wheels-vs-fixed-tiny-home", "Wheels vs fixed tiny home"), ("/moving-a-tiny-home", "Moving a tiny home onto your land"), ("/fixed-tiny-home-permit", "Fixed tiny home permits")],
            "sources": [("Everyday Tiny Homes, WA Perth", "https://www.everydaytinyhomes.com.au/location/wa-perth/"),
                        ("Perth Tiny House", "https://www.perthtinyhouse.com.au/"),
                        ("Tiny Homes Perth (LJM Tiny Homes, August 2026)", "https://ljmtinyhomes.com.au/tiny-homes-perth/"),
                        ("Tiny home designs Perth (Summit Homes)", "https://www.summithomes.com.au/tiny-homes/tiny-home-designs/"),
                        ("Permits, orders and schemes: vehicle size limits (Main Roads WA)", "https://www.mainroads.wa.gov.au/heavy-vehicles/permit-order-scheme/"),
                        ("Oversize loads and powerline safety (Western Power)", "https://www.westernpower.com.au/issues-enquiries/requests-preferences/oversize-vehicles/"),
                        ("Tiny homes (Shire of Mundaring)", "https://www.mundaring.wa.gov.au/plan-build/residential-dwellings-and-housing-options/tiny-homes.aspx"),
                        ("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                        ("Construction Training Fund levy", "https://ctf.wa.gov.au/levy")]}
