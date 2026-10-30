"""carportpermit.com.au: carports in WA."""
import build as b
from content_shed import notfound

QL = "https://getmypermit.com.au/quote?permit=%s&from=carportpermit.com.au"

TREE = {
    "start": "c1", "depth": 4,
    "nodes": {
        "c1": {"q": "Where will the carport go?", "opts": [
            {"t": "In front of the house", "go": "c2"}, {"t": "Beside the house", "go": "c3"}, {"t": "Behind the house", "go": "r_permit"}]},
        "c2": {"q": "Will it stay open at the front, with no solid door?", "opts": [
            {"t": "Yes, open", "go": "c4"}, {"t": "No, it will have a door", "go": "r_garage"}]},
        "c4": {"q": "Will it take up 60% or less of the lot's width along the street?", "help": "On a 15 m wide lot, 60% is 9 m.", "opts": [
            {"t": "Yes, 60% or less", "go": "r_front_ok"}, {"t": "No, wider", "go": "r_front_da"}, {"t": "Not sure", "go": "r_front_ok"}]},
        "c3": {"q": "Will a post or the roof be on, or very close to, the side boundary?", "opts": [
            {"t": "No", "go": "r_permit"}, {"t": "Yes", "go": "r_boundary"}]},
        "r_permit": {"result": True, "title": "You'll need a building permit",
            "body": "<p>Carports nearly always need a building permit in WA. Away from the street and the boundary, a building permit is usually all you need.</p>",
            "cta": {"href": QL % "carport", "text": "Get my fixed price"}},
        "r_front_ok": {"result": True, "title": "You'll need a building permit, and planning approval is likely",
            "body": "<p>The R-Codes let an open carport sit closer to the street when it is no wider than 60% of the frontage and you can still see the house from the street. Many councils still ask for planning approval in the front setback, and some have their own rules. We check yours and apply for both if needed.</p>",
            "cta": {"href": QL % "carport", "text": "Get my fixed price"}},
        "r_front_da": {"result": True, "title": "You'll need planning approval and a building permit",
            "body": "<p>A carport wider than 60% of the frontage falls outside the standard rules, so it needs planning approval before the building permit. Councils can approve it, often with design changes, and neighbours may be consulted.</p>",
            "cta": {"href": QL % "carport", "text": "Get my fixed price"}},
        "r_garage": {"result": True, "title": "With a solid door, it's a garage",
            "body": "<p>A carport with a solid door is treated as a garage, and garages usually have to sit further back from the street. Visually permeable (see-through) doors are treated differently. You'll need a building permit, and planning approval in the front setback is very likely.</p>",
            "cta": {"href": QL % "carport", "text": "Get my fixed price"}},
        "r_boundary": {"result": True, "title": "You'll need a building permit, and maybe planning approval",
            "body": "<p>Carports on or close to a side boundary have to meet the R-Codes' boundary rules and fire-separation rules. If they don't, planning approval is needed first, and your neighbour may be asked for comments.</p>",
            "cta": {"href": QL % "carport", "text": "Get my fixed price"}},
    },
}

HOME_FAQS = [
    ("Do I need council approval for a carport in WA?",
     "Almost always you need a building permit. You also need planning approval if the carport doesn't meet the standard planning rules, which most often happens with carports in front of the house or on a side boundary."),
    ("How close to the street can a carport be?",
     "Under the R-Codes, an open carport can generally be built closer to the street than a house or garage: the street setback can be halved if the carport is no wider than 60% of the frontage and doesn't block the view between the house and the street. Councils can set their own rules on top."),
    ("Can I put a roller door on my carport?",
     "A solid door turns a carport into a garage under the planning rules, and garages usually have to sit further back. A visually permeable (see-through) door may be allowed. Check before you add one."),
    ("Does a carport need engineering?",
     "Yes. The permit needs proof the posts, beams, footings and tie-downs suit the wind rating at your address. Carport kit suppliers usually provide certified engineering."),
    ("Is a carport cheaper to approve than a garage?",
     "Often, yes. Carports are allowed closer to the street, so many avoid planning approval altogether. Council fees are also based on the value of the work, and carports usually cost less to build."),
    ("How long does it take?",
     "A building permit only: a few days to prepare, then up to 25 business days for a standard council decision. If planning approval is needed, it comes first and adds several weeks."),
]


def home(S):
    body = b.hero(S, "Carport permits &middot; Perth &amp; WA",
                  "Carport permits in Perth, done for you.",
                  "Carports nearly always need a building permit in Western Australia, and the ones in front of the house often need planning approval too. We work out what your council needs, prepare the plans and lodge it all for you.",
                  ["Fixed price up front", "Planning and building", "Every Perth council"],
                  "Front-of-house carports", "We handle the planning approval as well.",
                  alt="A sleek flat-roof carport beside a modern Perth home")
    body += b.answer_check(S, "Do I need one?", "Do I need a permit for my carport?",
        "<p>Yes, a carport almost always needs a <strong>building permit</strong> in WA. It also needs <strong>planning approval</strong> if it doesn't meet the standard planning rules, which usually happens when it is <strong>in front of the house</strong> or <strong>on a side boundary</strong>.</p>",
        ["Open carports can sit closer to the street than garages.", "The 60% rule: no wider than 60% of the lot's frontage.",
         "A solid door makes it a garage, with stricter setbacks."],
        TREE)
    body += b.section(b.intro("The two approvals", "Planning approval and the building permit",
        "Many carports need both. Here is what each one checks.") +
        '<div class="grid g2">'
        '<div class="card"><div class="icon">' + b.icons.get("pin", 22) + '</div><h3>Planning approval</h3><p>Checks the carport suits the site and the street: how far it is from the street and the boundaries, how wide it is, and how it looks. Needed when the carport is outside the R-Codes\' standard rules or your council\'s local policy. It comes first.</p></div>'
        '<div class="card"><div class="icon">' + b.icons.get("shield", 22) + '</div><h3>Building permit</h3><p>Checks the carport is safe and meets the building code: the posts, beams, footings, tie-downs for your wind rating, and fire separation near boundaries. Needed for almost every carport.</p></div>'
        '</div>')
    body += b.section(b.intro("How it works", "From driveway to approved", "", center=True) + b.steps([
        ("Send us the basics", "Your address, the carport size and where it goes. Your supplier's quote or drawings help."),
        ("We check and prepare", "We check the setbacks and frontage rules, then prepare the site plan, elevations, engineering and forms."),
        ("We lodge and follow up", "Planning approval first if needed, then the building permit. We answer council's questions throughout."),
    ]), "section white")
    body += b.section(b.intro("Guides", "Carport permit guides") + b.guides([
        ("/carport-council-approval", "Carport council approval", "When a carport needs planning approval as well as a building permit.", "question"),
        ("/carport-in-front-setback", "Carports in the front setback", "The 60% rule, the halved setback and what councils add.", "car"),
        ("/retrospective-carport-approval", "Retrospective carport approval", "Already built? How to get an existing carport approved.", "retro"),
    ]))
    body += b.section('<div class="narrow">' + b.intro("Questions", "Common questions") + b.faq_block(HOME_FAQS) + "</div>", "section white")
    body += b.band(S, S["band_title"], S["band_text"])
    return {"path": "index.html", "title": "Carport Permit Perth & WA | Building Permit & Council Approval",
            "desc": "Need a carport permit in Perth or WA? We check the setback and frontage rules, prepare the plans and lodge your building permit and planning approval. Fixed price.",
            "h1": "Carport permits in Perth, done for you.", "body": body, "faqs": HOME_FAQS}


APPROVAL_BODY = """
<h2>Two kinds of approval</h2>
<p>"Council approval" for a carport can mean two different things. A <strong>building permit</strong> checks the structure is safe and meets the building code. <strong>Planning approval</strong> (also called development approval) checks the carport suits the site and the street. Almost every carport needs a building permit. Some also need planning approval, and that one comes first.</p>

<h2>When a carport needs planning approval</h2>
<p>A carport only needs planning approval if it doesn't meet the standard ("deemed-to-comply") rules in the R-Codes and your council's local planning policies. The common reasons are:</p>
<ul>
<li><strong>Too close to the street.</strong> In front of the house, closer than the rules allow.</li>
<li><strong>Too wide.</strong> More than 60% of the lot's frontage.</li>
<li><strong>On a side boundary</strong> beyond the R-Codes' limits for boundary walls and structures.</li>
<li><strong>Heritage areas and special estates</strong> with their own design rules.</li>
<li><strong>Corner lots</strong>, where sightlines for cars and people matter.</li>
</ul>

<h2>How long each takes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Approval</th><th>Typical time</th></tr></thead><tbody>
<tr><td>Building permit, standard (uncertified)</td><td>Up to 25 business days after lodgement</td></tr>
<tr><td>Building permit, certified (with a private surveyor's certificate)</td><td>Up to 10 business days after lodgement</td></tr>
<tr><td>Planning approval</td><td>Often 4 to 8 weeks, longer if neighbours are consulted</td></tr>
</tbody></table></div>

<h2>What we do</h2>
<p>We check your carport against the R-Codes and your council's policies before anything is lodged. If small changes, such as moving it back half a metre or narrowing it, would avoid planning approval, we tell you. If planning approval is needed, we prepare the application and the reasons it should be approved, then the building permit.</p>
"""

APPROVAL_FAQS = [
    ("Does my neighbour have to agree to my carport?",
     "Not usually. If planning approval is needed for something that affects them, such as a carport on the shared boundary, the council may ask them for comments. The council decides, not the neighbour."),
    ("Can I start building once planning approval is through?",
     "No. You still need the building permit before work starts. Planning approval is the first step, not the last."),
]


def approval(S):
    return {"path": "carport-council-approval.html", "kind": "article",
            "title": "Carport Council Approval in WA | Planning vs Building Permit",
            "desc": "Do you need council approval for a carport in WA? The difference between planning approval and a building permit, what triggers each, and how long they take.",
            "eyebrow": "Council approval", "h1": "Carport council approval in WA", "crumb": "Carport council approval",
            "answer": "<p>Almost every carport in WA needs a <strong>building permit</strong>. It also needs <strong>planning approval</strong> when it doesn't meet the standard planning rules, most often because it is too close to the street, too wide or on a side boundary. Planning approval comes first.</p>",
            "body": APPROVAL_BODY, "faqs": APPROVAL_FAQS,
            "related": [("/carport-in-front-setback", "Carports in the front setback"), ("/retrospective-carport-approval", "Retrospective carport approval"), ("https://shedbuildingpermit.com.au/garage-building-permit", "Garage permits")]}


FRONT_BODY = """
<h2>Why front carports are different</h2>
<p>The street setback is the area between the front boundary and the house. Planning rules keep it fairly open so streets look good and are safe. Carports are allowed into it more than garages, because they are open and you can see through them.</p>

<h2>The standard rule</h2>
<p>Under the R-Codes, a carport can generally go closer to the street than the normal setback for your lot (in many cases, half of it) when:</p>
<ul>
<li>it is <strong>no wider than 60% of the frontage</strong> of the lot, and</li>
<li>it <strong>doesn't block the view</strong> between the house and the street.</li>
</ul>
<p>For example, on an R20 lot with a 6 m street setback, that can mean a carport 3 m from the front boundary.</p>
<div class="table-wrap"><table>
<thead><tr><th>Lot frontage</th><th>60% of frontage</th></tr></thead><tbody>
<tr><td>10 m</td><td>6 m</td></tr>
<tr><td>12.5 m</td><td>7.5 m</td></tr>
<tr><td>15 m</td><td>9 m</td></tr>
<tr><td>20 m</td><td>12 m</td></tr>
</tbody></table></div>

<h2>Councils add their own rules</h2>
<p>Many Perth councils have a local planning policy for carports and garages. They can allow carports closer to the street (some as close as 1.5 m) or be stricter, and they often have rules about roof style, materials and matching the house. That is why we check your council's policy for your street before designing.</p>

<h2>Doors and walls</h2>
<p>A solid door, or solid walls on the street side, turn a carport into a garage under the planning rules, and garages normally have to sit further back. If you want a door, a visually permeable (see-through) one keeps it a carport.</p>
"""

FRONT_FAQS = [
    ("Can a carport go right up to the front boundary?",
     "Not under the standard rules. Some council policies allow carports quite close to the street, but very few allow them on the front boundary. Anything closer than the rules allow needs planning approval."),
    ("Does a corner lot change things?",
     "Yes. Corner lots have a primary and a secondary street, and there are rules about keeping sightlines clear near driveways and the corner."),
]


def front(S):
    return {"path": "carport-in-front-setback.html", "kind": "article",
            "title": "Carport in the Front Setback in WA | The 60% Rule Explained",
            "desc": "Can you build a carport in front of your house in WA? How the R-Codes' 60% frontage rule and reduced setback work, and what Perth councils add.",
            "eyebrow": "Front of house", "h1": "Carports in the front setback", "crumb": "Carports in the front setback",
            "answer": "<p>Yes, often. Under the R-Codes an open carport can usually be built closer to the street than the normal setback if it is <strong>no wider than 60% of the frontage</strong> and <strong>doesn't block the view</strong> between the house and the street. Councils can add their own rules, and anything outside them needs planning approval.</p>",
            "body": FRONT_BODY, "faqs": FRONT_FAQS,
            "related": [("/carport-council-approval", "Carport council approval"), ("/", "Carport permits")]}


RETRO_BODY = """
<h2>Unapproved carports are common</h2>
<p>Carports are often added years after a house is built, and plenty went up without a permit. They usually come to light when the house is sold, when a council notices them, or when an insurer asks.</p>

<h2>How it works</h2>
<ol>
<li><strong>We check the carport and council records.</strong> Photos, measurements and what your council has on file.</li>
<li><strong>As-built plans.</strong> We draw the carport as it stands, with a site plan showing setbacks from the street and boundaries.</li>
<li><strong>Planning approval, if needed.</strong> If the carport is closer to the street or wider than the rules allow, retrospective planning approval comes first.</li>
<li><strong>Surveyor inspection.</strong> A registered building surveyor checks the structure and issues a Certificate of Building Compliance.</li>
<li><strong>Building Approval Certificate.</strong> We lodge the application with your council, which issues the certificate.</li>
</ol>

<h2>Common issues</h2>
<ul>
<li><strong>Front setback.</strong> The most common planning issue with older carports.</li>
<li><strong>Tie-downs and footings.</strong> The surveyor needs to see how the posts are fixed down.</li>
<li><strong>Doors added later.</strong> A solid roller door may need to come off, or the structure assessed as a garage.</li>
</ul>
"""

RETRO_FAQS = [
    ("Will the council make me remove my carport?",
     "Rarely, if it is structurally sound. Planning problems are usually solved with approval or small changes. Removal is a last resort."),
    ("How long does retrospective carport approval take?",
     "About four to eight weeks without planning approval. If planning approval is needed, allow several more weeks."),
]


def retro(S):
    return {"path": "retrospective-carport-approval.html", "kind": "article", "permit": "retrospective",
            "title": "Retrospective Carport Approval in WA | Unapproved Carports",
            "desc": "Carport built without a permit in WA? How retrospective approval works, the common front-setback issues, and how we handle it for you.",
            "eyebrow": "Already built", "h1": "Retrospective carport approval in WA", "crumb": "Retrospective carport approval",
            "answer": "<p>An unapproved carport can usually be approved afterwards. If it breaks a planning rule, such as the front setback, retrospective planning approval comes first. Then a registered building surveyor certifies it and your council issues a <strong>Building Approval Certificate</strong>.</p>",
            "body": RETRO_BODY, "faqs": RETRO_FAQS,
            "related": [("/carport-in-front-setback", "Carports in the front setback"), ("https://getmypermit.com.au/retrospective-approval", "Retrospective approval for any structure")],
            "band_title": "Selling with an unapproved carport?", "band_text": "Send us photos and your address. We tell you what's involved and give you a fixed price."}


def pages(S):
    return [home(S), approval(S), front(S), retro(S), notfound(S)]
