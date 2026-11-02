import build as b

Q = "/quote"

TREE = {
    "start": "t1", "depth": 3,
    "nodes": {
        "t1": {"q": "Does your tiny home sit on wheels?", "opts": [
            {"t": "Yes, it's on a trailer or wheels", "go": "t2"},
            {"t": "No, or the wheels will come off", "go": "r_building"}]},
        "t2": {"q": "Is it built to be towed on the road, as a way of getting from place to place?", "help": "The state says a vehicle must be a means of transport, not just something that can be moved.", "opts": [
            {"t": "Yes, it can be towed on the road", "go": "t3"},
            {"t": "No, it's too big to tow on the road", "go": "r_park"},
            {"t": "Not sure", "go": "r_unsure"}]},
        "t3": {"q": "How long do you want to live in it on the property?", "opts": [
            {"t": "5 nights or less", "go": "r_caravan_short"},
            {"t": "Up to 24 months", "go": "r_caravan_24"},
            {"t": "Permanently", "go": "r_caravan_perm"}]},
        "r_building": {"result": True, "title": "It's a building",
            "body": "<p>Without wheels, a tiny home is treated as a <strong>building</strong>. It needs a <strong>building permit</strong> and has to meet the National Construction Code. On a residential lot it's usually a single house or a granny flat (up to 70 m²), and it can skip planning approval if it meets all the standard R-Codes rules.</p>",
            "cta": {"href": Q, "text": "Get a fixed-price quote"}},
        "r_park": {"result": True, "title": "It may be a park home",
            "body": "<p>A home on wheels that's too big to be towed on the road can be classed as a <strong>park home</strong>. Park homes can only be lived in inside a licensed caravan park. To keep it on your own land, it would need to be treated as a building, with a building permit.</p>",
            "cta": {"href": Q, "text": "Ask us about your home"}},
        "r_unsure": {"result": True, "title": "It depends on how it's built",
            "body": "<p>A tiny home on wheels is a <strong>caravan</strong> only if it's a genuine vehicle that can be towed. If it can't, it may be a park home or a building. Send us the maker's specifications and we'll tell you which.</p>",
            "cta": {"href": Q, "text": "Send us the details"}},
        "r_caravan_short": {"result": True, "title": "It's a caravan: owner's OK is enough",
            "body": "<p>As a caravan, it doesn't need a building permit. You can stay in it for <strong>up to 5 nights</strong> with the property owner's approval.</p>",
            "cta": {"href": Q, "text": "Ask us a question"}},
        "r_caravan_24": {"result": True, "title": "It's a caravan: you need council approval",
            "body": "<p>As a caravan, it doesn't need a building permit. To live in it for <strong>up to 24 months</strong> you need approval from the owner and your <strong>council</strong>. Council can ask for power, water, sewage and cooking facilities. You can apply again after 24 months.</p>",
            "cta": {"href": Q, "text": "Get help with the application"}},
        "r_caravan_perm": {"result": True, "title": "Permanent living isn't allowed in a caravan",
            "body": "<p>The regulations don't allow a caravan to be lived in <strong>permanently</strong> outside a caravan park. Your options are approvals of up to 24 months at a time, or taking the wheels off and getting it approved as a building.</p>",
            "cta": {"href": Q, "text": "Talk through your options"}},
    },
}

BODY = """
{CHECKER}
<h2>Why it matters</h2>
<p>In WA, a tiny home is either a <strong>caravan</strong> or a <strong>building</strong>. It can't be both. That one question decides which laws apply, whether you need a building permit and how long you can live in it.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Caravan (on wheels, towable)</th><th>Building (no wheels)</th></tr></thead><tbody>
<tr><td>Building permit</td><td>Not needed</td><td>Needed</td></tr>
<tr><td>Building code (NCC)</td><td>Doesn't apply</td><td>Must comply</td></tr>
<tr><td>Planning approval</td><td>Generally not needed</td><td>Not needed if it meets the R-Codes; otherwise yes</td></tr>
<tr><td>How long you can live in it</td><td>5 nights (owner's OK), up to 24 months with council approval</td><td>Permanently, once approved</td></tr>
</tbody></table></div>

<h2>What counts as a vehicle</h2>
<p>The state's tiny house fact sheet says a vehicle must be a <strong>means of transport</strong>, not just capable of being moved. A tribunal case in 2018 (Henville and City of Armadale) found that vehicles and buildings are mutually exclusive. If you take the wheels off a caravan, it becomes a building and has to meet building rules.</p>

<h2>Park homes</h2>
<p>A park home is a home on wheels that doesn't need a vehicle licence because it's too big to be towed on the road. Park homes can only be lived in inside a licensed caravan park.</p>
"""

FAQS = [
    ("Is a tiny home on wheels a caravan in WA?",
     "Yes, if it's a genuine vehicle fitted for living in. The state says a vehicle must be a means of transport, not just able to be moved."),
    ("Can a tiny home be both a caravan and a building?",
     "No. A 2018 tribunal case (Henville and City of Armadale) found that vehicles and buildings are mutually exclusive."),
    ("What happens if I take the wheels off my tiny home?",
     "It stops being a caravan and becomes a building. It then needs a building permit and has to meet the National Construction Code."),
    ("Can I live in a tiny home on wheels permanently in WA?",
     "Not outside a caravan park. You can live in it for up to 24 months at a time with owner and council approval, then apply again."),
]


def page(S):
    return {"path": "caravan-or-building-checker.html", "published": "2026-11-03", "type": "Free tool", "icon": "tiny",
            "card": "Three quick questions to see if your tiny home is a caravan or a building, and what that means.",
            "title": "Caravan or Building? Tiny Home Checker (WA)",
            "desc": "Free checker: find out if your WA tiny home counts as a caravan, a park home or a building, and what that means for permits and how long you can live in it.",
            "eyebrow": "Free tool", "h1": "Is my tiny home a caravan or a building?", "crumb": "Caravan or building?",
            "answer": "<p>If your tiny home is on wheels and built to be towed, it's a <strong>caravan</strong>: no building permit, but you can only live in it for up to 24 months at a time with council approval. Without wheels, it's a <strong>building</strong> that needs a building permit. Answer three questions below.</p>",
            "body": BODY.replace("{CHECKER}", b.checker(S, TREE, "Caravan or building?", "Up to three quick questions.")), "faqs": FAQS,
            "related": [("/wheels-vs-fixed-tiny-home", "Wheels vs fixed tiny home"), ("/new-tiny-home-laws-wa", "New tiny home laws in WA"), ("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules")],
            "sources": [("Tiny houses fact sheet, December 2024 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-12/fact_sheet_tiny-housesv3.pdf"),
                        ("Temporary accommodation and camping outside of caravan parks, updated June 2026 (WA Government)", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks")]}
