BODY = """
<h2>The state fees</h2>
<p>Building permit fees are set by the state, so they're the same at every WA council:</p>
<div class="table-wrap"><table>
<thead><tr><th>Charge</th><th>Rate</th></tr></thead><tbody>
<tr><td>BA2 (uncertified)</td><td>0.32% of the value, at least $121</td></tr>
<tr><td>BA1 (certified)</td><td>0.19% of the value, at least $121, plus a private surveyor</td></tr>
<tr><td>Building Services Levy</td><td>$61.65 for work up to $45,000</td></tr>
</tbody></table></div>

<h2>Examples</h2>
<div class="table-wrap"><table>
<thead><tr><th>Deck value (incl. GST)</th><th>BA2 fee</th><th>Levy</th><th>Total</th></tr></thead><tbody>
<tr><td>$15,000</td><td>$121.00</td><td>$61.65</td><td>$182.65</td></tr>
<tr><td>$30,000</td><td>$121.00</td><td>$61.65</td><td>$182.65</td></tr>
<tr><td>$40,000</td><td>$128.00</td><td>$61.65</td><td>$189.65</td></tr>
</tbody></table></div>
<p>For most backyard decks, the minimum fee applies, because 0.32% only goes over $121 once the deck is worth more than about $37,800.</p>

<h2>Other costs to budget for</h2>
<ul>
<li><strong>Plans and engineering.</strong> Councils usually want a site plan, elevations and structural details.</li>
<li><strong>Planning approval</strong>, if your deck needs it. The City of Wanneroo says it may be needed for decks higher than <strong>500 mm</strong> above natural ground, and must come before the building permit. Melville charges <strong>$147</strong> for planning approval on work up to $50,000.</li>
<li><strong>Verge bond.</strong> Some councils, such as Wanneroo, charge a fee and bond for larger jobs ($140 plus a $2,200 bond for work of $20,000 or more).</li>
<li><strong>Surveyor fee</strong> for a BA1.</li>
</ul>

<h2>Does every deck need a permit?</h2>
<p>The City of Wanneroo says <strong>all decking</strong> needs a building permit, whatever its height or size. Councils vary, so check yours before you build.</p>
<p>Read <a href="/deck-building-permit">deck building permits</a>, <a href="/patio-approval-cost-perth">patio approval costs</a>, or <a href="/city-of-wanneroo-patio-rules">City of Wanneroo patio rules</a>.</p>
"""

FAQS = [
    ("How much is a deck building permit in WA?",
     "For most decks, about $182.65 in state fees: the $121 minimum BA2 fee plus the $61.65 Building Services Levy. Plans, engineering and any planning approval are extra."),
    ("Do I need a permit for a low deck in Wanneroo?",
     "Yes. The City of Wanneroo says all decking needs a building permit, regardless of height or floor area."),
    ("When does a deck need planning approval?",
     "In Wanneroo, it may be needed if the deck is more than 500 mm above natural ground. It must come before the building permit."),
    ("Is a BA1 cheaper than a BA2 for a deck?",
     "The council fee is usually the same $121 minimum, but a BA1 also needs a private surveyor, who charges their own fee."),
]


def page(S):
    return {"path": "deck-permit-cost.html", "published": "2026-11-12", "type": "Cost guide", "icon": "deck",
            "card": "The state fees for a deck building permit in WA, worked examples, and the extra costs.",
            "title": "Deck Building Permit Cost in WA (2026)",
            "desc": "How much a deck building permit costs in WA in 2026: $121 minimum BA2 fee plus $61.65 levy for most decks, with examples and the extra costs to budget for.",
            "eyebrow": "Cost guide", "h1": "How much does a deck permit cost in WA?", "crumb": "Deck permit cost",
            "answer": "<p>For most backyard decks, the state fees come to about <strong>$182.65</strong>: the <strong>$121</strong> minimum BA2 fee plus the <strong>$61.65</strong> Building Services Levy. Plans, engineering and any planning approval cost extra. The City of Wanneroo says every deck needs a permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/deck-building-permit", "Deck building permits"), ("/patio-approval-cost-perth", "Patio approval cost in Perth"), ("/city-of-wanneroo-patio-rules", "City of Wanneroo patio rules")],
            "sources": [("Decking, City of Wanneroo", "https://www.wanneroo.wa.gov.au/directory_record/328/decking"),
                        ("Building approvals (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
