BODY = """
<h2>The rule: one caravan per lot</h2>
<p>A tiny home on wheels fitted out to live in is treated as a caravan in WA. Regulation 12 of the Caravan Parks and Camping Grounds Regulations 1997 says the owner or occupier of a lot must make sure that <strong>no more than one caravan is being used to camp on the lot at any one time</strong>, unless they have written approval. The fine for breaking this is up to <strong>$2,000</strong>.</p>

<h2>Who can approve more than one</h2>
<div class="table-wrap"><table>
<thead><tr><th>How long</th><th>Who approves</th></tr></thead><tbody>
<tr><td>Up to <strong>3 months</strong></td><td>Your local council</td></tr>
<tr><td>More than <strong>3 months</strong></td><td>The Minister</td></tr>
</tbody></table></div>
<p>Before giving approval, the council or Minister must be satisfied the land is suitable for camping, especially for safety, health and access to services.</p>

<h2>Short stays vs long stays</h2>
<ul>
<li><strong>Up to 5 nights in any 28 days</strong>: you can camp on land you own or have the right to use without approval (but still only one caravan at a time unless approved).</li>
<li><strong>Longer, one tiny home</strong>: apply to your council, which can approve up to <strong>24 consecutive months</strong>. If the council refuses, or sets conditions you don't accept, you can apply to the Minister within 35 days.</li>
<li><strong>Longer, two or more tiny homes</strong>: needs the Minister's written approval if it's more than 3 months.</li>
</ul>

<h2>It must stay mobile</h2>
<p>Regulation 15 says a caravan must keep its wheels and be able to be moved, under its own power or by towing, within <strong>24 hours</strong> of its services being disconnected. Taking the wheels off, or making it impossible to move, can carry a fine of up to $5,000. A tiny home that can't move is a building, with very different rules.</p>

<h2>What about fixed tiny homes?</h2>
<p>A tiny home without wheels is a building, not a caravan, so the one-caravan rule doesn't apply. Instead, councils assess it under planning rules, usually as a <strong>single house</strong> or a <strong>granny flat</strong> (ancillary dwelling). The Shires of Mundaring and Serpentine-Jarrahdale both treat fixed tiny homes this way. A second fixed tiny home on a lot with a house would usually need to meet the granny flat rules, including the 70 m² limit, to skip planning approval. Councils vary, so ask yours.</p>
<p>Learn more in <a href="/tiny-home-on-wheels-rules-wa">tiny home on wheels rules in WA</a>, <a href="/fixed-tiny-home-permit">fixed tiny home permits</a> and <a href="/tiny-home-council-application">the council application</a>.</p>
"""

FAQS = [
    ("Can I have more than one tiny home on my land in WA?",
     "Not on wheels without approval. The regulations allow only one caravan to be used for camping on a lot at a time. Your council can approve more for up to 3 months; longer needs the Minister's approval."),
    ("Who approves two tiny homes on wheels on one lot?",
     "Your local council for up to 3 months. For more than 3 months, the Minister must give written approval."),
    ("What is the fine for too many caravans on a lot in WA?",
     "Up to $2,000 under regulation 12 of the Caravan Parks and Camping Grounds Regulations 1997."),
    ("Can I take the wheels off my tiny home?",
     "Not if you want it treated as a caravan. Regulation 15 says it must keep its wheels and be movable within 24 hours of disconnecting services. Otherwise it's a building."),
    ("Can I have two fixed tiny homes on one block?",
     "Fixed tiny homes are assessed as a house or a granny flat. A second one on a lot with a house usually has to meet the granny flat rules, including 70 m² or less, to skip planning approval. Councils vary."),
]


def page(S):
    return {"path": "more-than-one-tiny-home.html", "published": "2026-11-09", "type": "Question answer", "icon": "tiny",
            "card": "The one-caravan rule, who can approve more, and the wheels rule.",
            "title": "Can You Have More Than One Tiny Home on Your Land in WA?",
            "desc": "More than one tiny home on your land in WA: the one-caravan-per-lot rule, council vs Minister approval, the $2,000 fine, the wheels rule and fixed tiny homes.",
            "eyebrow": "Question answer", "h1": "Can you have more than one tiny home on your land?", "crumb": "More than one tiny home",
            "answer": "<p><strong>Not without approval.</strong> WA's regulations allow only <strong>one caravan</strong> (including a tiny home on wheels) to be used for camping on a lot at a time. Your council can approve more for up to <strong>3 months</strong>. Longer than that needs the <strong>Minister's</strong> written approval. Breaking the rule can mean a fine of up to $2,000.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules in WA"), ("/fixed-tiny-home-permit", "Fixed tiny home permits"), ("/tiny-home-council-application", "Tiny home council application")],
            "sources": [("Caravan Parks and Camping Grounds Regulations 1997 (WA legislation)", "https://www.legislation.wa.gov.au/legislation/statutes.nsf/RedirectURL?OpenAgent&query=mrdoc_47625.pdf"),
                        ("Temporary accommodation and camping outside of caravan parks (WA Government)", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks")]}
