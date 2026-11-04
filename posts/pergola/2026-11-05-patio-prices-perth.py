BODY = """
<h2>What Perth patio businesses advertise (2026)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Advertised prices</th></tr></thead><tbody>
<tr><td>Phoenix Patios</td><td>Flat roof from $250 to $400 per m²; gable roof from $350 to $600+ per m²; extras and finishes can add $2,000 to $10,000</td></tr>
<tr><td>Advanced Patios</td><td>Smaller flat roof patios $8,000 to $12,000; medium gable $12,000 to $18,000; large gable, dome or custom $18,000 to $25,000+</td></tr>
<tr><td>Patio Kits WA (kit only, you build it)</td><td>Flat roof kit $2,000 to $4,500; gable kit $3,500 to $7,000; dome kit $4,500 to $9,000</td></tr>
</tbody></table></div>
<p>These are the businesses' own published figures, not quotes. Your price depends on size, roof style, insulation, site access and the slab.</p>

<h2>Approvals on top</h2>
<p>Most patios need a <strong>building permit</strong>: every attached patio at councils like Wanneroo, and any freestanding patio over 10 m² or taller than 2.4 m. The state-set council fees are:</p>
<div class="table-wrap"><table>
<thead><tr><th>Patio value</th><th>BA2 fee</th><th>Levy</th><th>Total</th></tr></thead><tbody>
<tr><td>$10,000</td><td>$121</td><td>$61.65</td><td>$182.65</td></tr>
<tr><td>$20,000</td><td>$121</td><td>$61.65</td><td>$182.65</td></tr>
<tr><td>$40,000</td><td>$128</td><td>$61.65</td><td>$189.65</td></tr>
</tbody></table></div>
<p>Add planning approval ($147 for work up to $50,000 at councils like Melville) only if your patio breaks the standard rules, such as in the front yard or too close to a boundary. Some councils add a verge bond; Wanneroo, for example, charges $140, plus a $2,200 refundable bond for work of $20,000 or more.</p>

<h2>Is the permit in your quote?</h2>
<p>Some builders include drawings, engineering and the permit; others leave it to you. Ask, and get it in writing. See <a href="/patio-builder-permit-check">how to check your patio builder is handling the permit</a>.</p>

<h2>Protections on bigger jobs</h2>
<ul>
<li>Contracts from <strong>$7,500 to $500,000</strong> must be in writing, and the deposit can't be more than <strong>6.5%</strong>.</li>
<li>Permit work over <strong>$20,000</strong> needs home indemnity insurance.</li>
<li>Patios worth <strong>$50,000 or more</strong> need a registered builder.</li>
</ul>
"""

FAQS = [
    ("How much does a patio cost in Perth in 2026?",
     "Perth patio businesses advertise flat roof patios from about $250 to $400 per m² and gable patios from about $350 to $600+ per m². One builder lists $8,000 to $12,000 for smaller flat roof patios and $18,000 to $25,000+ for large custom ones."),
    ("How much is a patio permit in Perth?",
     "For a patio up to about $37,800 in value, the BA2 fee is the $121 minimum plus the $61.65 levy: $182.65 in total. Some councils add a verge bond."),
    ("Do patio prices include council approval?",
     "Not always. Ask your builder whether drawings, engineering and the permit are included, and get it in writing."),
    ("Can I build a patio kit myself?",
     "Yes. Since 1 July 2026, a homeowner can build a Class 10a structure like a patio worth under $50,000 without owner-builder approval, but it still needs a building permit if it's over the exemption limits."),
]


def page(S):
    return {"path": "patio-prices-perth.html", "published": "2026-11-05", "type": "Cost guide", "icon": "price",
            "card": "Advertised patio prices from Perth businesses, plus the council fees on top.",
            "title": "Patio Prices in Perth (2026), Approvals Included",
            "desc": "Patio prices in Perth for 2026 from local businesses' published figures: flat and gable roof patios per m², patio kits, plus building permit fees, verge bonds and planning.",
            "eyebrow": "Cost guide", "h1": "Patio prices in Perth (2026), approvals included", "crumb": "Patio prices Perth",
            "answer": "<p>Perth patio businesses advertise flat roof patios from about <strong>$250 to $400 per m²</strong> and gable patios from about <strong>$350 to $600+ per m²</strong>. Kits start around $2,000. Add <strong>$182.65</strong> in council permit fees for a typical patio, plus a verge bond at some councils.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-cost-perth", "Patio approval cost in Perth"), ("/patio-builder-permit-check", "Check your builder handles the permit"), ("/patio-building-permit", "Patio building permits")],
            "sources": [("How much is a patio in Perth? (Phoenix Patios)", "https://phoenixpatios.com.au/blog/patio-cost-perth/"),
                        ("How much does a patio cost in Perth? (Advanced Patios)", "https://www.advancedpatios.com.au/how-much-does-a-patio-cost-in-perth/"),
                        ("Patio kit cost in Perth (Patio Kits WA)", "https://patiokitswa.com.au/how-much-does-a-patio-kit-cost-in-perth-check-prices-instantly-with-our-online-calculator/"),
                        ("Building approvals: fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Building or renovating your home (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-or-renovating-your-home"),
                        ("Patios information sheet (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf")]}
