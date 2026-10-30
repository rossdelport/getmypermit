"""grannyflatpermit.com.au: granny flats (ancillary dwellings) in WA."""
import build as b
from content_shed import notfound

QL = "https://getmypermit.com.au/quote?permit=%s&from=grannyflatpermit.com.au"

TREE = {
    "start": "g1", "depth": 4,
    "nodes": {
        "g1": {"q": "Is your lot zoned residential?", "help": "Most suburban Perth lots are. Rural, rural residential and farming zones are different.", "opts": [
            {"t": "Yes, residential", "go": "g2"}, {"t": "No, rural", "go": "r_rural"}, {"t": "Not sure", "go": "r_unsure"}]},
        "g2": {"q": "Will the granny flat be 70 m² or smaller?", "help": "Measured as the internal floor area of the granny flat.", "opts": [
            {"t": "Yes, 70 m² or less", "go": "g3"}, {"t": "No, bigger", "go": "r_big"}]},
        "g3": {"q": "Will it meet the normal setbacks from the boundaries and the street?", "opts": [
            {"t": "Yes", "go": "r_exempt"}, {"t": "No, or not sure", "go": "r_da"}]},
        "r_exempt": {"result": True, "title": "Building permit yes, planning approval probably not",
            "body": "<p>Since 10 April 2024, a granny flat of up to 70 m² that meets the R-Codes' standard rules, including setbacks, can be built on a residential lot of any size without planning approval. You still need a building permit before work starts.</p>",
            "cta": {"href": QL % "granny-flat", "text": "Get my fixed price"}},
        "r_da": {"result": True, "title": "You'll likely need planning approval and a building permit",
            "body": "<p>A granny flat that doesn't meet the standard setbacks or other R-Codes rules needs planning approval first. Councils can and do approve these, sometimes with changes. Then the building permit follows.</p>",
            "cta": {"href": QL % "granny-flat", "text": "Get my fixed price"}},
        "r_big": {"result": True, "title": "You'll need planning approval and a building permit",
            "body": "<p>Over 70 m² is outside the granny flat (ancillary dwelling) rules, so it needs planning approval, and your council may assess it as a second house. A building permit follows.</p>",
            "cta": {"href": QL % "granny-flat", "text": "Talk to us about your options"}},
        "r_rural": {"result": True, "title": "You'll likely need planning approval and a building permit",
            "body": "<p>On rural and farming land, many shires still need a development application for a second dwelling, and some have their own size limits. A building permit is always needed.</p>",
            "cta": {"href": "/granny-flat-on-a-rural-lot", "text": "Read about rural lots"}},
        "r_unsure": {"result": True, "title": "We'll check your zoning for free",
            "body": "<p>Every granny flat needs a building permit. Whether it also needs planning approval depends on your zoning, its size and the setbacks. Send us your address and we'll check the zoning.</p>",
            "cta": {"href": QL % "granny-flat", "text": "Check my lot"}},
    },
}

HOME_FAQS = [
    ("Do I need council approval for a granny flat in WA?",
     "You always need a building permit. Since 10 April 2024 you usually don't need planning approval for a granny flat up to 70 m&sup2; on a residential lot, as long as it meets the R-Codes' standard rules, including setbacks."),
    ("Is there a minimum lot size for a granny flat in WA?",
     "Not any more on residential lots. The old 350 m&sup2; minimum lot size was removed in April 2024, so a compliant granny flat can go on a residential lot of any size if it fits within the setbacks and open space rules."),
    ("Can I rent out my granny flat?",
     "Yes. In WA anyone can live in a granny flat, not just family, and it can be rented out separately from the main house."),
    ("How big can a granny flat be in WA?",
     "Up to 70 m&sup2; of internal floor area under the R-Codes' ancillary dwelling rules. Bigger than that needs planning approval and may be assessed as a second house."),
    ("Does a granny flat need its own parking?",
     "The R-Codes set parking rules for granny flats, and the 2024 changes made them more flexible, particularly near public transport. Your council's local policy can add to them. We check this as part of the application."),
    ("Who can lodge the building permit?",
     "Your builder often does it as part of the build. If you are using a kit, a modular supplier or an owner-builder, we can prepare and lodge it for you."),
]


def home(S):
    body = b.hero(S, "Granny flat permits &middot; Perth &amp; WA",
                  "Granny flat permits in WA, done for you.",
                  "Since April 2024, most granny flats up to 70 m&sup2; on residential lots can skip planning approval in Western Australia. You still need a building permit. We check your lot against the rules, line up the plans and engineering, and lodge it with your council.",
                  ["Fixed price up front", "The 70 m&sup2; check done for you", "Kit, modular or custom"],
                  "Up to 70 m&sup2;, no planning approval", "On most residential lots, if it meets the R-Codes.",
                  alt="A modern one-bedroom granny flat in a Perth backyard at dusk")
    body += b.answer_check(S, "Do I need approval?", "Do I need council approval for a granny flat?",
        "<p>Every granny flat in WA needs a <strong>building permit</strong>. Since 10 April 2024 most don't need <strong>planning approval</strong> if they are <strong>70 m&sup2; or smaller</strong>, on a <strong>residential lot</strong>, and meet the R-Codes' standard rules such as setbacks.</p>",
        ["No minimum lot size on residential lots any more.", "Anyone can live in it, and it can be rented out.",
         "Rural lots often still need a development application."],
        TREE, "Check your granny flat")
    body += b.section(b.intro("What changed", "The 2024 granny flat rules in WA, in plain English",
        "The WA Government changed the R-Codes to make granny flats easier to build. Here is what that means.") +
        '<div class="prose"><div class="table-wrap"><table><thead><tr><th></th><th>Before</th><th>Since 10 April 2024</th></tr></thead><tbody>'
        '<tr><td>Planning approval</td><td>Often needed, especially on smaller lots</td><td>Not needed if 70 m&sup2; or less and R-Code compliant on a residential lot</td></tr>'
        '<tr><td>Minimum lot size</td><td>Applied</td><td>Removed for residential lots</td></tr>'
        '<tr><td>Maximum size</td><td>70 m&sup2;</td><td>70 m&sup2;</td></tr>'
        '<tr><td>Parking</td><td>Extra bay usually required</td><td>More flexible</td></tr>'
        '<tr><td>Building permit</td><td>Required</td><td>Still required</td></tr>'
        '</tbody></table></div></div>')
    body += b.section(b.intro("How it works", "From backyard to building permit", "", center=True) + b.steps([
        ("Tell us about your lot", "Your address, the granny flat design or the kit you like, and where it will go."),
        ("We check and prepare", "Zoning, size and setbacks first. Then drawings, energy efficiency, engineering and forms."),
        ("We lodge and follow up", "We lodge with your council, answer their questions and send you the permit."),
    ]), "section white")
    body += b.section(b.split("granny", "A granny flat with a small timber deck in a Perth backyard",
        b.intro("What a granny flat application needs", "More than a shed, less than a house.") + b.checks([
            "<strong>Site plan</strong> with setbacks, open space and the main house.",
            "<strong>Floor plans, elevations and sections</strong> of the granny flat.",
            "<strong>Engineering</strong> for the slab or footings and the frame.",
            "<strong>Energy efficiency assessment</strong> to the building code.",
            "<strong>Bushfire assessment</strong> if the lot is in a bushfire-prone area.",
            "<strong>Forms, owner consent and fees</strong>, then lodgement.",
        ])))
    body += b.section(b.intro("Guides", "Granny flat guides") + b.guides([
        ("/granny-flat-rules-wa", "Granny flat rules in WA", "Size, setbacks, lot size, parking and who can live there.", "granny"),
        ("/granny-flat-approval-process", "The approval process", "Step by step, from checking your lot to the building permit.", "plan"),
        ("/granny-flat-on-a-rural-lot", "Granny flats on rural lots", "Why rural and farming zones are different.", "pin"),
    ]), "section white")
    body += b.section('<div class="narrow">' + b.intro("Questions", "Common questions") + b.faq_block(HOME_FAQS) + "</div>")
    body += b.band(S, S["band_title"], S["band_text"])
    return {"path": "index.html", "title": "Granny Flat Building Permit WA | Approval Done For You",
            "desc": "Need a granny flat building permit in Perth or WA? We check the 70 m² rules for your lot, prepare the plans and lodge your application. Fixed price.",
            "h1": "Granny flat permits in WA, done for you.", "body": body, "faqs": HOME_FAQS}


RULES_BODY = """
<h2>What counts as a granny flat?</h2>
<p>The planning rules call it an <strong>ancillary dwelling</strong>: a small, self-contained home on the same lot as a main house. It can have its own kitchen, bathroom and entrance. It is not a separate lot, so it can't be sold on its own.</p>

<h2>The main rules</h2>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>In summary</th></tr></thead><tbody>
<tr><td>Size</td><td>Up to 70 m&sup2; internal floor area</td></tr>
<tr><td>Lot size</td><td>No minimum on residential lots since April 2024</td></tr>
<tr><td>Planning approval</td><td>Not needed if it meets the R-Codes' standard rules on a residential lot</td></tr>
<tr><td>Setbacks</td><td>Must meet the normal R-Codes and local setbacks from the boundaries and street</td></tr>
<tr><td>Open space</td><td>The lot still needs its required open space</td></tr>
<tr><td>Who can live there</td><td>Anyone, and it can be rented out</td></tr>
<tr><td>Parking</td><td>Set by the R-Codes and local policy, more flexible since 2024</td></tr>
<tr><td>Building permit</td><td>Always required</td></tr>
</tbody></table></div>

<h2>When you still need planning approval</h2>
<ul>
<li>The granny flat is <strong>bigger than 70 m&sup2;</strong>.</li>
<li>It doesn't meet the <strong>setbacks</strong> or other standard rules.</li>
<li>The lot is in a <strong>rural or special zone</strong>, or your council's scheme says so.</li>
<li>The lot is in a <strong>heritage area</strong> or affected by special controls.</li>
</ul>

<h2>Other things that can apply</h2>
<ul>
<li><strong>Bushfire-prone areas</strong> need a Bushfire Attack Level (BAL) assessment, and construction to suit.</li>
<li><strong>Water and sewer.</strong> Connections need the Water Corporation's approval, and you can't build over sewer lines without it.</li>
<li><strong>Strata lots and estates</strong> can have their own restrictions on the title.</li>
</ul>
"""

RULES_FAQS = [
    ("Is the 70 m&sup2; measured inside or outside?",
     "It is the internal floor area of the granny flat, measured inside the external walls. Verandahs and decks are not counted in that figure, but they still count towards site cover and setbacks."),
    ("Can a granny flat be two storeys?",
     "It can, but it must still be within 70 m&sup2; and meet the setback, height and privacy rules. Upper floors often trigger privacy setbacks, which can mean planning approval."),
    ("Can I convert my garage or shed into a granny flat?",
     "Sometimes. It has to meet the rules for a dwelling, including insulation, ventilation, fire separation and energy efficiency, and it needs a building permit for the change of use."),
]


def rules(S):
    return {"path": "granny-flat-rules-wa.html", "kind": "article",
            "title": "Granny Flat Rules in WA (2026) | Size, Lot Size, Approval",
            "desc": "The granny flat rules in WA in plain English: the 70 m² limit, no minimum lot size, setbacks, parking, renting it out, and when planning approval is still needed.",
            "eyebrow": "WA rules", "h1": "Granny flat rules in WA", "crumb": "Granny flat rules in WA",
            "answer": "<p>In WA a granny flat (ancillary dwelling) can be up to <strong>70 m&sup2;</strong>, on a residential lot of <strong>any size</strong>, and doesn't need planning approval if it meets the R-Codes' standard rules. Anyone can live in it. A <strong>building permit</strong> is always required.</p>",
            "body": RULES_BODY, "faqs": RULES_FAQS,
            "related": [("/granny-flat-approval-process", "The approval process"), ("/granny-flat-on-a-rural-lot", "Granny flats on rural lots"), ("https://tinyhomepermit.com.au/", "Tiny homes")]}


PROCESS_BODY = """
<h2>Step by step</h2>
<ol>
<li><strong>Check the lot.</strong> Zoning, R-Code density, easements, sewer lines, bushfire mapping and any heritage or estate controls.</li>
<li><strong>Fit the design.</strong> Make sure the granny flat is 70 m&sup2; or less and meets the setbacks, open space and privacy rules. Small changes here can avoid planning approval altogether.</li>
<li><strong>Planning approval, only if needed.</strong> If the design can't meet the standard rules, we prepare and lodge a development application first.</li>
<li><strong>Drawings and reports.</strong> Floor plans, elevations, sections, engineering, an energy efficiency assessment and a BAL assessment if the lot is bushfire-prone.</li>
<li><strong>Building permit.</strong> We lodge the application, either the standard route (council checks it) or the certified route with a private building surveyor's certificate.</li>
<li><strong>Build and inspections.</strong> Your builder builds it, and the council may inspect along the way.</li>
<li><strong>Finish up.</strong> Once complete, the builder lodges a notice of completion and the services are connected.</li>
</ol>

<h2>How long it takes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>Typical time</th></tr></thead><tbody>
<tr><td>Checks, design and documents</td><td>2 to 4 weeks</td></tr>
<tr><td>Planning approval (if needed)</td><td>About 6 to 8 weeks, sometimes longer</td></tr>
<tr><td>Building permit, standard route</td><td>Up to 25 business days after lodgement</td></tr>
<tr><td>Building permit, certified route</td><td>Up to 10 business days after lodgement</td></tr>
</tbody></table></div>

<h2>Builder, kit or modular?</h2>
<p>A registered builder will often handle the permit as part of the build. With a kit or a modular granny flat, the permit is often left to you. That is where we come in: we take the supplier's drawings and engineering and turn them into a complete application for your lot.</p>
"""

PROCESS_FAQS = [
    ("Do I need a registered builder for a granny flat?",
     "In WA, building work for someone else worth over $20,000 generally needs a registered building contractor. Owner-builders need an owner-builder approval first. Ask us if you're not sure which applies."),
    ("Can you help with a modular or prefab granny flat?",
     "Yes. Modular granny flats still need a building permit for your lot, covering the footings, connections and placement. We prepare it from the manufacturer's documents."),
]


def process(S):
    return {"path": "granny-flat-approval-process.html", "kind": "article",
            "title": "Granny Flat Approval Process in WA | Step by Step",
            "desc": "How to get a granny flat approved in WA, step by step: checking your lot, fitting the 70 m² rules, planning approval if needed, and the building permit.",
            "eyebrow": "The process", "h1": "The granny flat approval process in WA", "crumb": "Granny flat approval process",
            "answer": "<p>Check the lot, fit the design to the 70 m&sup2; and setback rules, get planning approval only if the design can't meet them, then prepare the drawings and reports and lodge the <strong>building permit</strong>. Councils decide within 25 business days on the standard route.</p>",
            "body": PROCESS_BODY, "faqs": PROCESS_FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-on-a-rural-lot", "Granny flats on rural lots")]}


RURAL_BODY = """
<h2>Why rural lots are different</h2>
<p>The 2024 planning exemption for granny flats is built around the R-Codes, which apply to residential zones. Rural, rural residential and farming zones are controlled by each shire's local planning scheme instead, and many of them still require a <strong>development application</strong> for a second dwelling.</p>

<h2>What shires usually look at</h2>
<ul>
<li><strong>Size.</strong> Some shires allow larger ancillary dwellings on big rural lots, others keep a 70 m&sup2; limit.</li>
<li><strong>Location.</strong> Often it has to be close to the main house, sharing the driveway.</li>
<li><strong>Bushfire.</strong> Most rural land is bushfire-prone, so a BAL assessment and bushfire management measures are needed.</li>
<li><strong>Water and waste.</strong> Without scheme water or sewer, you need rainwater storage and an approved on-site wastewater system.</li>
<li><strong>Access</strong> for emergency vehicles.</li>
</ul>

<h2>Our approach</h2>
<p>We start with your shire's local planning scheme and policies, then prepare the development application with the supporting reports, followed by the building permit and the wastewater application if you need one.</p>
"""

RURAL_FAQS = [
    ("Can I put a tiny home on wheels on my rural lot instead?",
     "Possibly. In WA a tiny home on wheels is treated as a caravan, and your shire can approve it on private land for up to 24 months at a time. See our sister site <a href=\"https://tinyhomepermit.com.au/\">Tiny Home Permit</a>."),
    ("Do I need a separate septic approval?",
     "If the granny flat isn't connected to sewer, its wastewater system needs approval, usually from the shire's health service. We can include that in your application."),
]


def rural(S):
    return {"path": "granny-flat-on-a-rural-lot.html", "kind": "article",
            "title": "Granny Flats on Rural Lots in WA | Development Approval",
            "desc": "Building a granny flat on a rural or farming lot in WA? Why the 2024 exemption often doesn't apply, what shires look at, and how we handle the approvals.",
            "eyebrow": "Rural lots", "h1": "Granny flats on rural lots in WA", "crumb": "Granny flats on rural lots",
            "answer": "<p>On rural, rural residential and farming land, the 2024 granny flat exemption often doesn't apply. Most shires still need a <strong>development application</strong>, plus a <strong>building permit</strong>, and usually bushfire and wastewater approvals too.</p>",
            "body": RURAL_BODY, "faqs": RURAL_FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-approval-process", "The approval process"), ("https://tinyhomepermit.com.au/", "Tiny homes")]}


def pages(S):
    return [home(S), rules(S), process(S), rural(S), notfound(S)]
