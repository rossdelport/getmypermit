BODY = """
<h2>The rules for living in a caravan on private land</h2>
<p>WA law generally restricts caravans to licensed caravan parks. The Caravan Parks and Camping Grounds Regulations make exceptions for land you own or have a legal right to occupy:</p>
<div class="table-wrap"><table>
<thead><tr><th>How long</th><th>Whose approval</th></tr></thead><tbody>
<tr><td>Up to 5 nights</td><td>The property owner</td></tr>
<tr><td>Up to 24 months</td><td>The property owner <strong>and</strong> your council (or the Minister for Local Government)</td></tr>
<tr><td>After 24 months</td><td>Apply again, to the owner and council</td></tr>
<tr><td>Permanently</td><td>Not allowed outside a caravan park</td></tr>
</tbody></table></div>
<p>The same rules apply to a tiny home on wheels, because the law treats it as a caravan.</p>

<h2>What council can ask for</h2>
<p>Council's approval can come with health and safety conditions. The land must be suitable for living on, and council may require <strong>power, water, sewage and cooking facilities</strong>. Some councils have local laws with extra rules.</p>

<h2>Common reasons people do it</h2>
<ul>
<li>Living on site while building or renovating a house</li>
<li>Housing after a natural disaster</li>
<li>Supporting a family member ageing in place</li>
<li>Seasonal work</li>
</ul>

<h2>If council says no</h2>
<p>The Minister for Local Government can consider an approval if council refuses or cancels one. Council can't revoke a Minister's approval.</p>

<h2>What needs other approvals</h2>
<p>The caravan itself doesn't need a building permit. But anything you build around it, such as a patio or deck, may need planning approval and a building permit. Using a caravan outside a park without approval or an exemption can be an offence, even on your own land.</p>
"""

FAQS = [
    ("Can I live in a caravan on my own land in WA?",
     "Yes, for up to 5 nights with the owner's approval, or up to 24 months with approval from the owner and your council. You can apply again after 24 months, but you can't live in it permanently outside a caravan park."),
    ("Can I live in a caravan while building my house in WA?",
     "Yes, with council approval for up to 24 months. Council can require power, water, sewage and cooking facilities."),
    ("Do I need a permit to put a caravan on my property?",
     "The caravan itself doesn't need a building permit, but living in it for more than 5 nights needs council approval. A patio or deck built next to it may need planning approval and a building permit."),
    ("What if my council refuses?",
     "The Minister for Local Government can consider an approval, and council can't revoke a Minister's approval."),
]


def page(S):
    return {"path": "live-in-caravan-on-own-land-wa.html", "published": "2026-11-04", "type": "Question answer", "icon": "tiny",
            "card": "5 nights, 24 months, or never permanently: the rules for living in a caravan on your land.",
            "title": "Can You Live in a Caravan on Your Own Land in WA?",
            "desc": "Living in a caravan on your own land in WA: up to 5 nights with the owner's OK, up to 24 months with council approval, conditions councils set, and Minister approvals.",
            "eyebrow": "Question answer", "h1": "Can you live in a caravan on your own land in WA?", "crumb": "Caravan on your own land",
            "answer": "<p><strong>Yes, but not permanently.</strong> You can stay up to <strong>5 nights</strong> with the owner's approval, or up to <strong>24 months</strong> with approval from the owner and your council, then apply again. Council can require power, water, sewage and cooking facilities.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules"), ("/caravan-or-building-checker", "Caravan or building checker"), ("/tiny-home-council-application", "Tiny home council application")],
            "sources": [("Temporary accommodation and camping outside of caravan parks, updated June 2026 (WA Government)", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks"),
                        ("Tiny houses fact sheet, December 2024 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf")]}
