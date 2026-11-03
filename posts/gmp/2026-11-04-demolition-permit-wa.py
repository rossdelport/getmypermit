BODY = """
<h2>When you need a demolition permit</h2>
<p>In WA, pulling down a building usually needs a <strong>demolition permit</strong> from your council, applied for on form <strong>BA5</strong>. There's a state exemption for small backyard structures:</p>
<ul>
<li>a patio, shed or pool of <strong>40 m² or less</strong> doesn't need a demolition permit</li>
<li>as long as it has <strong>no asbestos</strong></li>
<li>and the property isn't <strong>heritage-listed</strong></li>
</ul>
<p>Anything bigger, anything with asbestos, and any house needs a BA5.</p>

<h2>What it costs</h2>
<div class="table-wrap"><table>
<thead><tr><th>Charge</th><th>Amount</th></tr></thead><tbody>
<tr><td>BA5 for a house or Class 10 structure (shed, garage, carport, patio)</td><td>$121</td></tr>
<tr><td>BA5 for other buildings (Class 2 to 9)</td><td>$121 per storey</td></tr>
<tr><td>Building Services Levy</td><td>Payable on demolition permits too: $61.65 for work up to $45,000, or 0.137% of the value above that</td></tr>
<tr><td>Extending the permit (BA22)</td><td>$121</td></tr>
</tbody></table></div>
<p>These fees are set by the state, so they're the same at every council.</p>

<h2>Demolition and planning approval</h2>
<p>A demolition permit is a building approval. If the property is heritage-listed or in a heritage area, check with your council's planning team first, as the exemption doesn't apply and other approvals may be needed.</p>

<h2>Removing a structure that was never approved</h2>
<p>If you're pulling down a shed or patio that never had a permit, demolishing it is one way to fix the problem. The same 40 m² exemption applies. If you'd rather keep it, see <a href="/retrospective-approval">retrospective approval</a>.</p>
"""

FAQS = [
    ("Do I need a permit to demolish a shed in WA?",
     "Not if the shed is 40 m² or less, has no asbestos and the property isn't heritage-listed. Otherwise you need a demolition permit (form BA5) from your council."),
    ("How much is a demolition permit in WA?",
     "$121 for a house or Class 10 structure like a shed, garage or patio, plus the Building Services Levy. The fee is the same at every council."),
    ("Which form do I use for a demolition permit?",
     "Form BA5, Application for demolition permit, lodged with your council."),
    ("Can I demolish a patio without a permit?",
     "Yes, if it's 40 m² or less, has no asbestos and the property isn't heritage-listed."),
]


def page(S):
    return {"path": "demolition-permit-wa.html", "published": "2026-11-04", "type": "Question answer", "icon": "doc",
            "card": "When you need a BA5 to pull something down, the 40 m² exemption, and what it costs.",
            "title": "Do I Need a Demolition Permit in WA? (BA5 Guide)",
            "desc": "When you need a demolition permit in WA: the 40 m² exemption for sheds, patios and pools, asbestos and heritage, the BA5 form, and the $121 fee plus levy.",
            "eyebrow": "Question answer", "h1": "Do I need a demolition permit in WA?", "crumb": "Demolition permits",
            "answer": "<p>Usually <strong>yes</strong>, on form <strong>BA5</strong>. The exception: a patio, shed or pool of <strong>40 m² or less</strong>, with no asbestos, on a property that isn't heritage-listed. A BA5 for a house or Class 10 structure costs <strong>$121</strong> plus the Building Services Levy.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/what-doesnt-need-a-building-permit", "What doesn't need a building permit"), ("/retrospective-approval", "Retrospective approval"), ("/which-ba-form", "Which BA form do I need?")],
            "sources": [("Do I need a permit? (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit"),
                        ("Building approvals: forms, fees and levy (Building and Energy)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
