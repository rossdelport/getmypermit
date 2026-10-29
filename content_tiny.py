"""tinyhomepermit.com.au: tiny homes in WA, on wheels or fixed."""
import build as b
from content_shed import notfound

QL = "https://getmypermit.com.au/quote?permit=%s&from=tinyhomepermit.com.au"

TREE = {
    "start": "t1", "depth": 4,
    "nodes": {
        "t1": {"q": "Is your tiny home on wheels?", "help": "Built on a registrable trailer, able to be towed.", "opts": [
            {"t": "Yes, on wheels", "go": "t2"}, {"t": "No, on footings or a slab", "go": "t4"}]},
        "t2": {"q": "How long will someone stay in it?", "opts": [
            {"t": "A few nights", "go": "r_short"}, {"t": "Weeks, months or to live in", "go": "t3"}]},
        "t3": {"q": "How many caravans or tiny homes will be on the lot?", "opts": [
            {"t": "Just one", "go": "r_lg"}, {"t": "More than one", "go": "r_minister"}]},
        "t4": {"q": "Will there also be a main house on the lot?", "opts": [
            {"t": "Yes, it's a second dwelling", "go": "r_granny"}, {"t": "No, it's the only home", "go": "r_house"}]},
        "r_short": {"result": True, "title": "The landowner's OK is usually enough",
            "body": "<p>In WA a tiny home on wheels is treated like a caravan. Very short stays of a few nights on private land only need the landowner's permission. Anything longer needs approval from the local government.</p>",
            "cta": {"href": QL % "tiny-home", "text": "Plan a longer stay"}},
        "r_lg": {"result": True, "title": "You'll need local government approval",
            "body": "<p>Since 1 September 2024, WA councils can approve one tiny home on wheels on private land for up to 24 months, and the approval can be renewed. Councils set conditions, such as access to water, toilet and shower facilities, power, waste and fire safety.</p>",
            "cta": {"href": QL % "tiny-home", "text": "Get a fixed-price quote"}},
        "r_minister": {"result": True, "title": "You'll need the Minister's approval",
            "body": "<p>More than one caravan or tiny home on wheels on a private lot, for longer stays, needs approval from the Minister for Local Government. The application usually goes through your council first.</p>",
            "cta": {"href": QL % "tiny-home", "text": "Talk to us about it"}},
        "r_granny": {"result": True, "title": "It's a granny flat: building permit needed",
            "body": "<p>A fixed tiny home behind a main house is assessed as an ancillary dwelling (granny flat). It needs a building permit, and usually no planning approval if it is 70 m² or less, on a residential lot and meets the setbacks.</p>",
            "cta": {"href": QL % "tiny-home", "text": "Get a fixed-price quote"}},
        "r_house": {"result": True, "title": "It's a house: building permit needed",
            "body": "<p>A fixed tiny home that is the only home on the lot is a house under the building rules. It needs a building permit, must meet the building code like any home, and may need planning approval depending on your zoning.</p>",
            "cta": {"href": QL % "tiny-home", "text": "Get a fixed-price quote"}},
    },
}

HOME_FAQS = [
    ("Can I live in a tiny home on wheels in WA?",
     "Yes, with approval. Since 1 September 2024 your local government can approve a tiny home on wheels on private land for up to 24 months at a time, and the approval can be renewed. Councils set conditions to suit the site."),
    ("Does a tiny home on wheels need a building permit?",
     "No. A tiny home on wheels is treated as a caravan, not a building, so the approval comes under the caravan and camping rules. Anything permanent you add, like a deck or a carport, may need its own approval."),
    ("Can I put a tiny home in my backyard in Perth?",
     "Often, yes. On wheels, you need your council's approval for stays longer than a few nights. On a slab or footings, it is a granny flat and needs a building permit."),
    ("Do I need council approval to have a tiny home on my parents' land?",
     "Yes, for anything longer than a short stay. The landowner gives consent, and the application goes to the local government."),
    ("Can I have more than one tiny home on a lot?",
     "More than one caravan or tiny home on wheels on a private lot needs the Minister for Local Government's approval, on top of the council's involvement."),
    ("What do councils usually ask for?",
     "A site plan, details of the tiny home, the landowner's consent, and how water, toilet and shower facilities, power and waste will be handled. Some councils also look at bushfire safety and setbacks."),
]


def home(S):
    body = b.hero(S, "Tiny home approvals &middot; Perth &amp; WA",
                  "Tiny home approvals in WA, sorted.",
                  "On wheels or on a slab, a tiny home in Western Australia needs the right approval. Since September 2024, councils can approve a tiny home on wheels for up to 24 months at a time. We work out which approval yours needs and apply for you.",
                  ["Fixed price up front", "On wheels or fixed", "Perth and regional WA"],
                  "Up to 24 months, renewable", "Council approval for tiny homes on wheels.",
                  alt="A timber-clad tiny home on wheels on a rural West Australian property")
    body += b.answer_check(S, "Which approval?", "Do I need approval for my tiny home?",
        "<p>A <strong>tiny home on wheels</strong> is treated as a caravan in WA. Stays longer than a few nights on private land need <strong>local government approval</strong>, for up to 24 months at a time. A <strong>fixed tiny home</strong> is a building and needs a <strong>building permit</strong>.</p>",
        ["One tiny home on wheels per lot is the norm; more needs the Minister's approval.", "Decks and carports added to a tiny home may need their own approval.",
         "Fixed tiny homes behind a house follow the granny flat rules."],
        TREE, "Check your tiny home")
    body += b.section(b.intro("Two paths", "On wheels or fixed: what's the difference?", "") +
        '<div class="prose"><div class="table-wrap"><table><thead><tr><th></th><th>Tiny home on wheels</th><th>Fixed tiny home</th></tr></thead><tbody>'
        '<tr><td>Treated as</td><td>A caravan</td><td>A building (house or granny flat)</td></tr>'
        '<tr><td>Approval</td><td>Local government approval under the caravan and camping rules</td><td>Building permit, plus planning approval in some cases</td></tr>'
        '<tr><td>How long</td><td>Up to 24 months at a time, renewable</td><td>Permanent</td></tr>'
        '<tr><td>Building code</td><td>Doesn\'t apply to the tiny home itself</td><td>Applies in full, including energy efficiency</td></tr>'
        '<tr><td>More than one on a lot</td><td>Needs the Minister\'s approval</td><td>Depends on zoning and planning rules</td></tr>'
        '</tbody></table></div></div>')
    body += b.section(b.intro("How it works", "From driveway to approved", "", center=True) + b.steps([
        ("Tell us about it", "The tiny home, the land, who owns it, and how long you want to stay."),
        ("We prepare the application", "Site plan, tiny home details, landowner consent and how water, power and waste are handled."),
        ("We lodge and follow up", "We lodge with your council, answer their questions and send you the approval and its conditions."),
    ]), "section white")
    body += b.section(b.split("tiny", "A tiny home on wheels under gum trees at golden hour",
        b.intro("What councils look for", "Show them it's safe, serviced and sensible.") + b.checks([
            "<strong>Facilities.</strong> Drinking water, a toilet and shower, either in the tiny home or close by.",
            "<strong>Waste.</strong> How grey water and sewage are handled, especially off-sewer.",
            "<strong>Power and gas</strong> connections done by licensed trades.",
            "<strong>Fire safety</strong>, including bushfire-prone areas.",
            "<strong>Placement</strong>: setbacks, access and not blocking driveways.",
        ])))
    body += b.section(b.intro("Guides", "Tiny home guides") + b.guides([
        ("/tiny-home-on-wheels-rules-wa", "Tiny homes on wheels in WA", "The caravan rules, the 24-month approvals and the conditions councils set.", "tiny"),
        ("/fixed-tiny-home-permit", "Fixed tiny home permits", "When a tiny home is a building, and how the granny flat rules help.", "granny"),
        ("/tiny-home-council-application", "Applying to your council", "What goes in an application and how long it takes.", "doc"),
    ]), "section white")
    body += b.section('<div class="narrow">' + b.intro("Questions", "Common questions") + b.faq_block(HOME_FAQS) + "</div>")
    body += b.band(S, S["band_title"], S["band_text"])
    return {"path": "index.html", "title": "Tiny Home Permit WA | Approval for Tiny Homes on Wheels & Fixed",
            "desc": "Need approval for a tiny home in Perth or WA? We handle council approvals for tiny homes on wheels (up to 24 months) and building permits for fixed tiny homes.",
            "h1": "Tiny home approvals in WA, sorted.", "body": body, "faqs": HOME_FAQS}


WHEELS_BODY = """
<h2>A tiny home on wheels is a caravan</h2>
<p>Under WA law, a tiny home built on a trailer is treated as a caravan. Living in one on private land is covered by the Caravan Parks and Camping Grounds rules, not the building permit system. That is good news: it means a simpler application, and the tiny home itself doesn't have to meet the building code.</p>

<h2>What changed in September 2024</h2>
<p>From 1 September 2024 the WA Government changed the caravan and camping regulations so that local governments can approve a caravan or tiny home on wheels on private land for up to <strong>24 months</strong>. The approval can be renewed for further periods. Before that, long stays were much harder to get approved.</p>

<h2>How long can you stay?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Stay</th><th>Who approves</th></tr></thead><tbody>
<tr><td>A few nights</td><td>The landowner</td></tr>
<tr><td>Longer, up to 24 months</td><td>The landowner and the local government</td></tr>
<tr><td>Beyond 24 months</td><td>A new or extended approval from the local government</td></tr>
<tr><td>More than one caravan or tiny home on a lot</td><td>The Minister for Local Government</td></tr>
</tbody></table></div>
<p>Councils differ in exactly how they apply the short-stay limit, so check with yours, or ask us.</p>

<h2>Conditions councils set</h2>
<ul>
<li>Access to drinking water, a toilet and a shower</li>
<li>Safe disposal of grey water and sewage</li>
<li>Licensed power and gas connections</li>
<li>Fire safety and bushfire measures</li>
<li>Where it sits on the lot, and keeping it roadworthy</li>
</ul>
<p>Some councils have their own tiny home policy, and some allow only one tiny home on wheels per property.</p>

<h2>Decks, verandahs and carports</h2>
<p>Permanent structures built next to a tiny home, like a deck, a verandah or a carport, are buildings. They may need a building permit, even though the tiny home doesn't.</p>
"""

WHEELS_FAQS = [
    ("Does my tiny home on wheels need to be registered?",
     "If it is towed on public roads, the trailer needs to be registered and roadworthy. Councils may also ask that it stays mobile, rather than being fixed to the ground."),
    ("What if my tiny home is taken off its wheels?",
     "Once it is fixed to the ground on footings, it is usually treated as a building and needs a building permit. See <a href=\"/fixed-tiny-home-permit\">fixed tiny home permits</a>."),
    ("Can I live in a tiny home on wheels on vacant land?",
     "Sometimes. Some councils allow it, often while you build a house, but conditions about water, toilets and waste are stricter when there is no existing home on the lot."),
]


def wheels(S):
    return {"path": "tiny-home-on-wheels-rules-wa.html", "kind": "article",
            "title": "Tiny Home on Wheels Rules in WA (2026) | 24-Month Approvals",
            "desc": "The rules for living in a tiny home on wheels in WA: treated as a caravan, council approval for up to 24 months since September 2024, conditions and decks.",
            "eyebrow": "On wheels", "h1": "Tiny homes on wheels: the WA rules", "crumb": "Tiny homes on wheels in WA",
            "answer": "<p>In WA a tiny home on wheels is treated as a <strong>caravan</strong>. Since <strong>1 September 2024</strong>, your local government can approve one on private land for up to <strong>24 months</strong> at a time, and the approval can be renewed. More than one on a lot needs the Minister's approval.</p>",
            "body": WHEELS_BODY, "faqs": WHEELS_FAQS,
            "related": [("/tiny-home-council-application", "Applying to your council"), ("/fixed-tiny-home-permit", "Fixed tiny home permits")]}


FIXED_BODY = """
<h2>Fixed means it's a building</h2>
<p>A tiny home on footings, piers or a slab is a building. That means it needs a <strong>building permit</strong> before it is placed or built, and it has to meet the National Construction Code like any home: structure, fire safety, ceiling heights, light and ventilation, and energy efficiency.</p>

<h2>Behind an existing house: the granny flat route</h2>
<p>A fixed tiny home on the same lot as a main house is an <strong>ancillary dwelling</strong>, or granny flat. Since April 2024 it doesn't need planning approval if it is <strong>70 m&sup2; or less</strong>, on a residential lot, and meets the R-Codes' standard rules such as setbacks. Our sister site <a href="https://grannyflatpermit.com.au/">Granny Flat Permit</a> covers this in detail.</p>

<h2>As the only home on the lot</h2>
<p>A fixed tiny home as the main home on a lot is assessed as a house. It needs a building permit, and planning approval where your zoning or the R-Codes require it. Rural lots often need extra approvals for water and wastewater.</p>

<h2>Modular and transportable tiny homes</h2>
<p>Factory-built tiny homes delivered by truck still need a building permit for your lot. The application covers the footings or tie-downs, the connections to services and the home itself, using the manufacturer's documents.</p>

<h2>What we prepare</h2>
<ul>
<li>Site plan with setbacks and open space</li>
<li>Floor plans and elevations, from your builder or manufacturer</li>
<li>Footing and tie-down engineering</li>
<li>Energy efficiency assessment, and a BAL assessment if bushfire-prone</li>
<li>Forms, owner consent and lodgement</li>
</ul>
"""

FIXED_FAQS = [
    ("Is a fixed tiny home cheaper to approve than a granny flat?",
     "The approval process is the same, because it is the same type of building. The difference is usually in the build itself."),
    ("Can I put my tiny home on wheels onto footings later?",
     "You can, but it then becomes a building and needs a building permit, and it must meet the building code. Some tiny homes built for the road won't meet it without changes."),
]


def fixed(S):
    return {"path": "fixed-tiny-home-permit.html", "kind": "article",
            "title": "Fixed Tiny Home Permit in WA | Building Permit & Granny Flat Rules",
            "desc": "A tiny home on footings or a slab is a building in WA and needs a building permit. How the granny flat rules apply, modular tiny homes, and what we prepare.",
            "eyebrow": "Fixed tiny homes", "h1": "Fixed tiny home permits in WA", "crumb": "Fixed tiny home permits",
            "answer": "<p>A tiny home fixed to the ground is a <strong>building</strong>, so it needs a <strong>building permit</strong>. Behind an existing house it follows the granny flat rules, which usually means no planning approval if it is 70 m&sup2; or less on a residential lot.</p>",
            "body": FIXED_BODY, "faqs": FIXED_FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny homes on wheels"), ("https://grannyflatpermit.com.au/granny-flat-rules-wa", "Granny flat rules in WA")]}


APPLY_BODY = """
<h2>What goes in a tiny home on wheels application</h2>
<ul>
<li><strong>The application form</strong> for your local government, under the caravan and camping regulations.</li>
<li><strong>Landowner consent</strong>, if you don't own the land.</li>
<li><strong>A site plan</strong> showing where the tiny home will sit, its distance from boundaries and buildings, and access.</li>
<li><strong>Details of the tiny home</strong>: size, photos, and its registration if it is towed on roads.</li>
<li><strong>Services</strong>: drinking water, toilet and shower, how grey water and sewage are handled, power and gas.</li>
<li><strong>How long</strong> you want the approval for, up to 24 months.</li>
<li><strong>Fees</strong>, which vary between councils.</li>
</ul>

<h2>How long it takes</h2>
<p>It varies between councils. Simple applications on a lot with a house are often decided in a few weeks. Applications needing the Minister's approval, or on lots without services, take longer.</p>

<h2>Tips that help an application</h2>
<ul>
<li>Show the tiny home has its own toilet and shower, or easy access to the main house's.</li>
<li>Explain how waste water is handled, with plumber's details if it connects to sewer.</li>
<li>Keep it clear of boundaries and driveways, and out of the front yard.</li>
<li>Talk to the neighbours early. It costs nothing and avoids complaints later.</li>
</ul>

<h2>Renewing your approval</h2>
<p>Before your approval runs out, you can apply to extend it for a further period. We keep a note of your expiry date and can handle the renewal.</p>
"""

APPLY_FAQS = [
    ("Can my council refuse a tiny home?",
     "Yes. Councils weigh up health, safety and amenity. Refusals often come down to missing facilities, waste water or fire safety, which a good application addresses up front."),
    ("Is there a fee?",
     "Councils charge an application fee, which varies. We include it in our fixed quote so you know the total."),
]


def apply(S):
    return {"path": "tiny-home-council-application.html", "kind": "article",
            "title": "Tiny Home Council Application in WA | What to Include",
            "desc": "How to apply to your WA council for a tiny home on wheels: what goes in the application, the services councils check, timeframes and renewing your approval.",
            "eyebrow": "Applying", "h1": "Applying to your council for a tiny home", "crumb": "Applying to your council",
            "answer": "<p>For a tiny home on wheels, you apply to your <strong>local government</strong> with the landowner's consent, a site plan, details of the tiny home and how <strong>water, toilet, shower, waste and power</strong> are handled. Approvals can run for up to 24 months and be renewed.</p>",
            "body": APPLY_BODY, "faqs": APPLY_FAQS,
            "related": [("/tiny-home-on-wheels-rules-wa", "Tiny homes on wheels"), ("/fixed-tiny-home-permit", "Fixed tiny home permits")]}


def pages(S):
    return [home(S), wheels(S), fixed(S), apply(S), notfound(S)]
