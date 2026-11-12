BODY = """
<h2>What needs a permit in Wanneroo</h2>
<div class="table-wrap"><table>
<thead><tr><th>Project</th><th>Building permit?</th><th>Planning approval?</th></tr></thead><tbody>
<tr><td>Shed</td><td>Not for one shed under 10 m² and under 2.4 m high; yes for anything bigger</td><td>Usually not, if it meets the R-Codes</td></tr>
<tr><td>Patio</td><td>Not if freestanding, 10 m² or less and 2.4 m or less; every attached patio needs one</td><td>Usually not, if it meets the R-Codes</td></tr>
<tr><td>Carport</td><td>Always</td><td>Only for R-Code variations</td></tr>
<tr><td>Deck</td><td>Always, whatever its height or size</td><td>May be needed above 500 mm from natural ground</td></tr>
<tr><td>Granny flat</td><td>Always</td><td>May be needed</td></tr>
</tbody></table></div>
<p>When planning approval is needed, the City says it must be granted <strong>before</strong> the building permit.</p>

<h2>What to lodge</h2>
<p>For an uncertified (BA2) application, Wanneroo's information sheets ask for:</p>
<ul>
<li>A site plan at <strong>1:200</strong> or larger, with levels, setbacks, any septic system and a north point</li>
<li>Floor plan, elevations and sections at <strong>1:100</strong></li>
<li>Structural engineer's details, where the structure needs them</li>
<li>A Street and Verge Bond application, if it applies</li>
</ul>
<p>Wanneroo has separate BA1 and BA2 checklists for houses and granny flats, and a separate checklist for unauthorised work.</p>

<h2>Fees</h2>
<p>Building permit fees are set by the state: <strong>0.32%</strong> of the value for a BA2, or <strong>0.19%</strong> for a BA1, at least <strong>$121</strong>, plus the Building Services Levy ($61.65 up to $45,000). Wanneroo also charges a <strong>$140</strong> verge bond fee and a <strong>$2,200</strong> bond for work of $20,000 or more.</p>

<h2>How long it takes</h2>
<p>A complete BA1 must be decided within <strong>10 business days</strong> and a BA2 within <strong>25 business days</strong>. Planning approval usually takes up to <strong>60 days</strong>, or 90 with consultation. Use the <a href="/approval-timeline-calculator">approval timeline calculator</a> to work out yours.</p>
<p>Compare with <a href="/city-of-stirling-building-permits">City of Stirling building permits</a> or <a href="/city-of-swan-building-permits">City of Swan building permits</a>.</p>
"""

FAQS = [
    ("Do I need a building permit for a shed in Wanneroo?",
     "Not for one shed under 10 m² and under 2.4 m high. Bigger sheds need a building permit."),
    ("Does every carport in Wanneroo need a permit?",
     "Yes. The City of Wanneroo says a carport always needs a building permit. Planning approval is only needed for R-Code variations."),
    ("Does a low deck need a permit in Wanneroo?",
     "Yes. Wanneroo says all decking needs a building permit, regardless of height or floor area."),
    ("What is Wanneroo's verge bond?",
     "A $140 fee plus a $2,200 bond for work of $20,000 or more, to cover any damage to the verge."),
]


def page(S):
    return {"path": "city-of-wanneroo-building-permits.html", "published": "2026-11-13", "type": "Council guide", "icon": "pin",
            "card": "What needs a permit in the City of Wanneroo, what to lodge, fees and timeframes.",
            "title": "City of Wanneroo Building Permits Guide (2026)",
            "desc": "City of Wanneroo building permits: which sheds, patios, carports, decks and granny flats need approval, what to lodge, fees, verge bond and timeframes.",
            "eyebrow": "Council guide", "h1": "City of Wanneroo building permits",
            "crumb": "Wanneroo building permits",
            "answer": "<p>In the City of Wanneroo, <strong>carports, decks and granny flats always</strong> need a building permit. A single shed under <strong>10 m²</strong> and <strong>2.4 m</strong>, or a freestanding patio of 10 m² or less, usually doesn't. If planning approval is needed, it must come first.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/approval-timeline-calculator", "Approval timeline calculator"), ("/city-of-stirling-building-permits", "City of Stirling building permits"), ("/city-of-swan-building-permits", "City of Swan building permits")],
            "sources": [("Shed (outbuilding), City of Wanneroo", "https://www.wanneroo.wa.gov.au/directory_record/107/shed_also_referred_to_as_an_outbuilding"),
                        ("Carports, City of Wanneroo", "https://www.wanneroo.wa.gov.au/directory_record/115/carports"),
                        ("Decking, City of Wanneroo", "https://www.wanneroo.wa.gov.au/directory_record/328/decking"),
                        ("Patios information sheet (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Ancillary accommodation (granny flat), City of Wanneroo", "https://www.wanneroo.wa.gov.au/directory_record/111/ancillary_accommodation_granny_flat")]}
