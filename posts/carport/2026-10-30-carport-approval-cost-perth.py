BODY = """
<h2>The building permit: worked examples</h2>
<p>Every carport needs a building permit, and the fees are set by the state, so every Perth council charges the same. With an uncertified application (BA2), where council checks the plans, the fee is 0.32% of the value of the work with a minimum of $121. The state's Building Services Levy adds $61.65 for work up to $45,000.</p>
<div class="table-wrap"><table>
<thead><tr><th>Carport value (incl. GST)</th><th>Permit fee (BA2)</th><th>Building Services Levy</th><th>Total to council</th></tr></thead><tbody>
<tr><td>$5,000 single carport</td><td>$121.00 (minimum)</td><td>$61.65</td><td><strong>$182.65</strong></td></tr>
<tr><td>$12,000 double carport</td><td>$121.00 (minimum)</td><td>$61.65</td><td><strong>$182.65</strong></td></tr>
<tr><td>$25,000 gable carport</td><td>$121.00 (minimum)</td><td>$61.65</td><td><strong>$182.65</strong></td></tr>
<tr><td>$40,000 large or custom carport</td><td>$128.00</td><td>$61.65</td><td><strong>$189.65</strong></td></tr>
</tbody></table></div>
<p>The minimum fee covers any carport up to about $37,800, which is most of them.</p>

<h2>Planning approval: more likely for carports</h2>
<p>Carports often go at the front of the house, so they are more likely than patios to need planning approval. A carport only skips planning approval if it meets all the standard rules, such as being no wider than 60% of the frontage, keeping a clear view between the house and the street, and sitting at least the reduced street setback. Carports on heritage-listed properties, or in heritage areas such as the City of Stirling's Mount Lawley, Menora and Inglewood, always need it.</p>
<p>When it is needed, the planning application fee for work up to $50,000 is <strong>$147</strong> at most councils in 2026-27. It adds time too: council has 60 days to decide, or 90 if it asks the neighbours for comments.</p>

<h2>Bonds and verge permits</h2>
<p>Some councils charge to protect the verge and footpath while you build. The City of Wanneroo, for example, requires a Street and Verge Bond Permit with every building permit:</p>
<div class="table-wrap"><table>
<thead><tr><th>Value of the work</th><th>Wanneroo verge permit</th></tr></thead><tbody>
<tr><td>Up to $20,000</td><td>$140 non-refundable admin fee, no bond</td></tr>
<tr><td>$20,000 or more</td><td>$140 admin fee plus a <strong>$2,200 refundable bond</strong></td></tr>
</tbody></table></div>
<p>Changing or widening the driveway crossover for the carport usually needs a separate crossover approval from council too.</p>

<h2>The other costs</h2>
<ul>
<li><strong>Plans.</strong> A site plan showing the carport, the street and side setbacks, and the frontage width, plus elevations.</li>
<li><strong>Engineering.</strong> Footing and frame details for your wind rating. Carport kits usually include this.</li>
<li><strong>Private building surveyor</strong>, only if you go certified (BA1) for a faster decision. Council's fee then drops to 0.19%.</li>
<li><strong>Bushfire report (BAL)</strong>, if the lot is bushfire-prone and the carport is attached to or near the house.</li>
</ul>

<h2>Typical totals</h2>
<p>For a carport that meets the standard rules, expect about <strong>$183 to council</strong>, plus any verge fee. If it needs planning approval, add <strong>$147</strong> and a few weeks. Plans and engineering are on top, and are often the biggest part of the cost. Our fixed price covers the plans, forms, lodging and dealing with council, so you know the total up front.</p>
"""

FAQS = [
    ("How much does carport approval cost in Perth?",
     "For most carports the council fees are the $121 minimum building permit fee plus the $61.65 Building Services Levy, about $183. Planning approval, if needed, adds $147 for work up to $50,000. Some councils add a verge permit fee or bond."),
    ("Why do carports need planning approval more often than patios?",
     "Because they often go in front of the house. Carports in the street setback have to meet rules on width, views to the street and how far back they sit. If they don't, planning approval is needed."),
    ("Is the carport permit fee different at each council?",
     "No. The building permit fee and levy are set by the state. Planning fees, verge permits and bonds can differ between councils."),
    ("Does a carport kit include council approval?",
     "Some kit suppliers include engineering and plans; a few lodge the permit for you. Many leave the site plan and council lodgement to you. Check what the quote says."),
]


def page(S):
    return {"path": "carport-approval-cost-perth.html", "published": "2026-10-30", "type": "Cost guide", "icon": "price",
            "card": "What council charges for a carport in 2026-27, when planning approval adds $147, and the verge bonds some councils charge.",
            "title": "Carport Council Approval Cost in Perth (2026-27 Fees)",
            "desc": "Carport approval in Perth usually costs about $183 in council fees and levies in 2026-27. When planning approval adds $147, verge permits and bonds, and worked examples.",
            "eyebrow": "Cost guide", "h1": "Carport council approval cost in Perth", "crumb": "Carport approval cost",
            "answer": "<p>For most carports, council charges the <strong>$121 minimum building permit fee plus the $61.65 Building Services Levy</strong>: about <strong>$183</strong> in 2026-27. If the carport needs planning approval (common for carports in front of the house), add <strong>$147</strong>. Some councils also charge a verge permit fee or bond.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-council-approval", "Carport council approval"), ("/carport-in-front-setback", "Carports in the front setback"), ("/carport-vs-garage", "Carport vs garage")],
            "sources": [("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                        ("Building approvals and the Building Services Levy (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf"),
                        ("Patios information sheet with verge bond fees, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf"),
                        ("Planning fees 2026-27 (City of Subiaco)", "https://www.subiaco.wa.gov.au/media/kuyntemn/planning-services-fee-schedule-2026-2027.pdf")]}
