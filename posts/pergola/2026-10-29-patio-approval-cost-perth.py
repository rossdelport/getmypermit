BODY = """
<h2>The council part: worked examples</h2>
<p>For a patio, the fees are set by the state's Building Regulations, so every Perth council charges the same. Most homeowners lodge an uncertified application (BA2), where council checks the plans. The fee is 0.32% of the value of the work, with a minimum of $121. On top of that is the state's Building Services Levy: $61.65 for work up to $45,000.</p>
<div class="table-wrap"><table>
<thead><tr><th>Patio value (incl. GST)</th><th>Permit fee (BA2)</th><th>Building Services Levy</th><th>Total to council</th></tr></thead><tbody>
<tr><td>$8,000</td><td>$121.00 (minimum)</td><td>$61.65</td><td><strong>$182.65</strong></td></tr>
<tr><td>$15,000</td><td>$121.00 (minimum)</td><td>$61.65</td><td><strong>$182.65</strong></td></tr>
<tr><td>$30,000</td><td>$121.00 (minimum)</td><td>$61.65</td><td><strong>$182.65</strong></td></tr>
<tr><td>$45,000</td><td>$144.00</td><td>$61.65</td><td><strong>$205.65</strong></td></tr>
<tr><td>$60,000</td><td>$192.00</td><td>$82.20</td><td><strong>$274.20</strong></td></tr>
</tbody></table></div>
<p>So for almost every backyard patio, the council and levy part comes to about <strong>$183</strong>. The minimum fee covers any patio up to about $37,800. The Construction Training Fund levy doesn't apply, because from 1 July 2026 it only applies to work over $100,000.</p>

<h2>If you use a certified application (BA1)</h2>
<p>With a BA1, a private building surveyor checks the plans first and signs a certificate of design compliance. Council's fee drops to 0.19% (still at least $121), but you also pay the surveyor. In return, council has 10 business days to decide instead of up to 25. It is worth it when you are in a hurry or the job is complicated.</p>

<h2>If you also need planning approval</h2>
<p>A patio that meets the standard planning rules only needs a building permit. One that doesn't, for example because it is too close to a boundary, in the front setback or on a heritage property, needs planning (development) approval first. For work up to $50,000, the planning application fee is <strong>$147</strong> at most councils in 2026-27. It also adds time, as council has up to 60 days to decide.</p>

<h2>The other costs</h2>
<ul>
<li><strong>Plans.</strong> A site plan showing the patio and its distance to each boundary, plus a floor plan and elevations. Many patio companies supply drawings; some leave the site plan to you.</li>
<li><strong>Engineering.</strong> Footing, post and beam details for your wind rating. Usually included by the patio supplier.</li>
<li><strong>Private building surveyor.</strong> Only if you go certified (BA1). Prices vary, so get a quote.</li>
<li><strong>Bushfire report (BAL).</strong> Only if your lot is in a bushfire-prone area and the patio is attached to or near the house.</li>
<li><strong>Verge or street bond.</strong> Some councils charge to protect the verge during building. The City of Wanneroo, for example, charges a $140 admin fee with every building permit, plus a $2,200 refundable bond if the work is worth $20,000 or more.</li>
</ul>

<h2>Is a patio permit worth it?</h2>
<p>For a typical patio, the council part costs less than $200. Building without a required permit can lead to fines of up to $50,000, an order to change or remove the patio, and problems when you sell. Approving it afterwards costs more: a building approval certificate is 0.38% of the value plus a surveyor's inspection.</p>

<h2>Do you even need one?</h2>
<p>Some small patios are exempt. The City of Wanneroo, for example, says a freestanding patio of 10 m&sup2; or less and no taller than 2.4 m doesn't need a building permit. Most patios attached to a house do need one. <a href="/patio-building-permit">See when a patio needs a permit</a>.</p>
"""

FAQS = [
    ("How much is a patio permit in Perth?",
     "For most patios the council fee is the $121 minimum plus the $61.65 Building Services Levy, about $183 in total. Bigger patios over about $37,800 pay a little more. Plans, engineering and any surveyor are extra."),
    ("Is the patio permit fee the same at every council?",
     "Yes. The building permit fee and the Building Services Levy are set by the state, so they are the same at every WA council. Planning fees and bonds can differ."),
    ("Who pays for the patio permit, me or the patio company?",
     "It depends on your contract. Some patio companies include the permit in their price, others leave it to you. Check the quote for the words 'council approval included'."),
    ("How long does a patio permit take?",
     "Council has up to 25 business days for an uncertified (BA2) application, or 10 business days for a certified (BA1) one. Preparing the plans usually takes a few days."),
]


def page(S):
    return {"path": "patio-approval-cost-perth.html", "published": "2026-10-29", "updated": "2026-10-30", "type": "Cost guide", "icon": "price",
            "card": "What council actually charges for a patio permit in 2026-27, with worked examples, plus the other costs to plan for.",
            "title": "Patio Approval Cost in Perth (2026-27 Fees, Worked Examples)",
            "desc": "A patio building permit in Perth usually costs about $183 in council fees and levies in 2026-27. Worked examples, BA1 vs BA2, planning fees and the other costs.",
            "eyebrow": "Cost guide", "h1": "Patio approval cost in Perth (2026)", "crumb": "Patio approval cost",
            "answer": "<p>For most patios, council charges the <strong>$121 minimum permit fee plus the $61.65 Building Services Levy</strong>, so about <strong>$183</strong> in 2026-27. The fee only goes up for patios worth more than about $37,800. Plans, engineering and planning approval (if needed) are extra.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-building-permit", "Patio building permits"), ("/do-i-need-council-approval-for-a-pergola", "Do I need approval for a pergola?"), ("/deck-building-permit", "Deck building permits")],
            "sources": [("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                        ("Building approvals and the Building Services Levy (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                        ("Planning fees 2026-27 (City of Subiaco)", "https://www.subiaco.wa.gov.au/media/kuyntemn/planning-services-fee-schedule-2026-2027.pdf"),
                        ("Construction Training Fund levy", "https://ctf.wa.gov.au/levy"),
                        ("Patios information sheet with verge bond fees, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf")]}
