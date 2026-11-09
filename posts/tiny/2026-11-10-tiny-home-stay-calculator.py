import build as b

Q = "/quote"

TREE = {
    "start": "s1", "depth": 4,
    "nodes": {
        "s1": {"q": "Is the tiny home on wheels and able to be towed?", "help": "The caravan rules only apply to a genuine vehicle. The law says its wheels must stay on and it must be able to be moved within 24 hours.", "opts": [
            {"t": "Yes, wheels on and towable", "go": "s2"},
            {"t": "No, or the wheels will come off", "go": "r_building"}]},
        "s2": {"q": "How many caravans or tiny homes on wheels will people live in on the lot at the same time?", "opts": [
            {"t": "Just one", "go": "s3"},
            {"t": "Two or more", "go": "r_multi"}]},
        "s3": {"q": "How many nights will someone stay in it in any 28 days?", "opts": [
            {"t": "5 nights or fewer", "go": "r_short"},
            {"t": "More than 5 nights", "go": "s4"}]},
        "s4": {"q": "How long do you want to live in it altogether?", "opts": [
            {"t": "Up to 24 months", "go": "r_council"},
            {"t": "Longer than 24 months", "go": "r_longer"}]},
        "r_building": {"result": True, "title": "The caravan time limits don't apply: it's a building",
            "body": "<p>Without wheels, or if it can't be moved, a tiny home is treated as a <strong>building</strong>. It needs a <strong>building permit</strong>, and usually counts as a house or granny flat. Once approved, there's no limit on how long you can live in it.</p>",
            "cta": {"href": Q, "text": "Get a fixed-price quote"}},
        "r_multi": {"result": True, "title": "You need written approval for more than one",
            "body": "<p>Only <strong>one</strong> caravan can be lived in on a lot at a time without written approval. Your <strong>council</strong> can approve more for up to <strong>3 months</strong>. For longer, approval comes from the <strong>Minister</strong>. The fine for breaking this rule is up to <strong>$2,000</strong>.</p>",
            "cta": {"href": Q, "text": "Get help with the approval"}},
        "r_short": {"result": True, "title": "No approval needed",
            "body": "<p>You can stay in it for up to <strong>5 nights in any 28 days</strong> on land you own or have a legal right to occupy, without council approval. Keep it in a safe, healthy condition, with the wheels on.</p>",
            "cta": {"href": Q, "text": "Ask us a question"}},
        "r_council": {"result": True, "title": "You need council approval",
            "body": "<p>Apply in writing to your <strong>council</strong>. It can approve up to <strong>24 consecutive months</strong>, and must be satisfied the land is safe and has access to services. If the council doesn't decide within <strong>63 days</strong>, the application is treated as refused. If it's refused, you can apply to the <strong>Minister</strong> within 35 days.</p>",
            "cta": {"href": Q, "text": "Get help with the application"}},
        "r_longer": {"result": True, "title": "24 months is the most per approval",
            "body": "<p>A council or the Minister can approve up to <strong>24 consecutive months</strong> at a time. To keep living there, you'd need a new approval. For a permanent home, the other option is to take it off its wheels and get it approved as a <strong>building</strong>.</p>",
            "cta": {"href": Q, "text": "Talk through your options"}},
    },
}

BODY = """
{CHECKER}
<h2>The time limits at a glance</h2>
<div class="table-wrap"><table>
<thead><tr><th>How long</th><th>What you need</th></tr></thead><tbody>
<tr><td>Up to 5 nights in any 28 days</td><td>Nothing, on land you own or have a legal right to occupy</td></tr>
<tr><td>More than 5 nights, up to 24 consecutive months</td><td>Written approval from your council (or the Minister if the council refuses)</td></tr>
<tr><td>More than one caravan on the lot</td><td>Council approval up to 3 months; Minister beyond that</td></tr>
<tr><td>Permanently</td><td>Take it off its wheels and get a building permit</td></tr>
</tbody></table></div>
<p>These limits come from the state's Caravan Parks and Camping Grounds Regulations. Councils can add conditions, and some also need planning approval for a tiny home on wheels, so councils vary.</p>

<h2>Rules while you're there</h2>
<ul>
<li>The tiny home must keep its <strong>wheels on</strong> and be able to be moved within <strong>24 hours</strong> of its services being disconnected. The fine is up to $5,000.</li>
<li>It must be kept so it isn't a <strong>hazard to safety or health</strong>. The fine is also up to $5,000.</li>
<li>A council can cancel its approval if a condition is broken, but must give you 35 days' notice to respond first.</li>
</ul>
<p>Not sure if yours counts as a caravan? Try the <a href="/caravan-or-building-checker">caravan or building checker</a>. Read more about <a href="/tiny-home-on-wheels-rules-wa">tiny home on wheels rules</a> or <a href="/live-in-caravan-on-own-land-wa">living in a caravan on your own land</a>.</p>
"""

FAQS = [
    ("How long can I stay in a tiny home on wheels without approval in WA?",
     "Up to 5 nights in any 28 days, on land you own or have a legal right to occupy."),
    ("How long can a council approve a tiny home on wheels for?",
     "Up to 24 consecutive months. You can apply again after that."),
    ("What if the council doesn't answer my application?",
     "If it doesn't approve within 63 days, the application is treated as refused. You can then apply to the Minister within 35 days."),
    ("Can I have two tiny homes on wheels on my lot?",
     "Only with written approval. The council can approve more than one caravan for up to 3 months; the Minister for longer. The fine is up to $2,000."),
    ("Do I have to keep the wheels on?",
     "Yes. A caravan must keep its wheels and be able to be moved within 24 hours of services being disconnected. The fine is up to $5,000."),
]


def page(S):
    title = "How long can I stay?"
    return {"path": "tiny-home-stay-calculator.html", "published": "2026-11-10", "type": "Free tool", "icon": "clock",
            "card": "Four quick questions to see how long you can live in a tiny home on wheels, and what approval you need.",
            "title": "Tiny Home on Wheels Stay Calculator (WA)",
            "desc": "Free tool: find out how long you can live in a tiny home on wheels in WA. 5 nights without approval, up to 24 months with council approval, and the rules.",
            "eyebrow": "Free tool", "h1": "How long can I live in a tiny home on wheels?", "crumb": "Stay calculator",
            "answer": "<p>In WA you can stay up to <strong>5 nights in any 28 days</strong> without approval. For longer, your council can approve up to <strong>24 consecutive months</strong> at a time. Only one can be lived in per lot without extra approval. Answer up to four questions below.</p>",
            "body": BODY.replace("{CHECKER}", b.checker(S, TREE, title, "Up to four quick questions.")), "faqs": FAQS,
            "related": [("/caravan-or-building-checker", "Caravan or building checker"), ("/tiny-home-on-wheels-rules-wa", "Tiny home on wheels rules"), ("/live-in-caravan-on-own-land-wa", "Living in a caravan on your own land")],
            "sources": [("Caravan Parks and Camping Grounds Regulations 1997, regs 11 to 15 (WA legislation)", "https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_s1418.html"),
                        ("Temporary accommodation and camping outside of caravan parks, updated June 2026 (WA Government)", "https://www.wa.gov.au/government/publications/temporary-accommodation-and-camping-outside-of-caravan-parks")]}
