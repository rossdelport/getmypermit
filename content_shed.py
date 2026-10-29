"""shedbuildingpermit.com.au: sheds, garages and outbuildings in WA."""
import build as b
from sites import PHONE

TREE = {
    "start": "s1", "depth": 4,
    "nodes": {
        "s1": {"q": "Will the shed stand on its own, not attached to the house or another building?", "opts": [
            {"t": "Yes, freestanding", "go": "s2"}, {"t": "No, attached", "go": "r_permit"}]},
        "s2": {"q": "What is the floor area?", "help": "Length x width. A 3 m x 3 m shed is 9 m².", "opts": [
            {"t": "10 m² or less", "go": "s3"}, {"t": "More than 10 m²", "go": "s4"}, {"t": "Not sure", "go": "r_unsure"}]},
        "s3": {"q": "Is it 2.4 m tall or less at the highest point?", "opts": [
            {"t": "Yes", "go": "r_exempt"}, {"t": "No, taller", "go": "s4"}]},
        "s4": {"q": "Will it be within 1 m of a fence, in the front yard, or in a heritage area?", "opts": [
            {"t": "No", "go": "r_permit"}, {"t": "Yes", "go": "r_both"}, {"t": "Not sure", "go": "r_permit"}]},
        "r_exempt": {"result": True, "title": "You probably don't need a building permit",
            "body": "<p>A freestanding shed of 10 m² or less, no taller than 2.4 m, is usually exempt from a building permit in WA. Planning rules still apply: keep it out of the front yard, away from sewer lines and easements, and check heritage or bushfire rules for your street.</p>",
            "cta": {"href": "https://getmypermit.com.au/quote?permit=shed&from=shedbuildingpermit.com.au", "text": "Ask us to double-check"}},
        "r_permit": {"result": True, "title": "You'll need a building permit",
            "body": "<p>Sheds over 10 m², taller than 2.4 m or attached to another building need a building permit before work starts. We draw the site plan, fill in the forms and lodge it with your council.</p>",
            "cta": {"href": "https://getmypermit.com.au/quote?permit=shed&from=shedbuildingpermit.com.au", "text": "Get a fixed-price quote"}},
        "r_both": {"result": True, "title": "You'll need a building permit, and maybe planning approval",
            "body": "<p>A shed close to the boundary, in the front setback or in a heritage area may need planning approval as well as a building permit. Planning approval comes first, and your neighbour may be asked for comments. We work out exactly what your council needs.</p>",
            "cta": {"href": "https://getmypermit.com.au/quote?permit=shed&from=shedbuildingpermit.com.au", "text": "Get a fixed-price quote"}},
        "r_unsure": {"result": True, "title": "Measure the footprint and you'll know",
            "body": "<p>Multiply the length by the width of the shed's floor. If the answer is 10 or less, and the shed is 2.4 m tall or less and freestanding, you probably don't need a building permit. Anything bigger usually does.</p>",
            "cta": {"href": "https://getmypermit.com.au/quote?permit=shed&from=shedbuildingpermit.com.au", "text": "Or let us check for you"}},
    },
}

HOME_FAQS = [
    ("What size shed can I build without a permit in WA?",
     "A freestanding shed with a floor area of 10 m&sup2; or less and a height of 2.4 m or less usually doesn't need a building permit. That is roughly a 3 m x 3.3 m shed. It still has to meet planning rules such as setbacks from the boundary and the street."),
    ("Does a Colorbond shed need a permit?",
     "The material doesn't change the answer. A steel, timber or Colorbond shed follows the same rule: over 10 m&sup2;, over 2.4 m tall or attached to another building means you need a building permit."),
    ("Can I build a shed on the boundary in WA?",
     "Often, yes, but walls on or close to a boundary have to meet the R-Codes' limits for height and length. If your shed doesn't meet them, it needs planning approval and your neighbour may be asked for comments. We check this before anything is lodged."),
    ("Does a sea container need a permit?",
     "Many Perth councils treat a sea container kept on a property as an outbuilding, and some require planning approval or a building permit, especially for longer than a few months. Rules differ a lot between councils, so check before you have one delivered."),
    ("How long does a shed permit take?",
     "Once lodged, your council has up to 25 business days to decide a standard (uncertified) application, or 10 business days if it comes with a private building surveyor's certificate. Preparing the plans usually takes a few days."),
    ("My shed supplier says they can lodge it. Do I need you?",
     "Some suppliers handle permits well. Many only supply the engineering and leave the site plan, forms and council to you. That is the part we do, and we often work alongside suppliers."),
]


def home(S):
    body = b.hero(S, "Shed building permits &middot; Perth &amp; WA",
                  "Shed building permits in Perth, done for you.",
                  "Most sheds over 10 m&sup2; need a building permit in Western Australia. We check your council's rules, draw the site plan, fill in the forms and lodge the application, so your shed goes up legally and on time.",
                  ["Fixed price up front", "Site plan drawn for you", "Every Perth council"],
                  "Ready to lodge in days", "Then council has up to 25 business days to decide.",
                  alt="A new charcoal steel shed with a roller door in a Perth backyard")
    body += b.answer_check(S, "Do I need one?", "Do I need a permit for my shed?",
        "<p>In WA you need a building permit for a shed that is <strong>bigger than 10 m&sup2;</strong>, <strong>taller than 2.4 m</strong> or <strong>attached to another building</strong>. Smaller freestanding sheds are usually exempt, but still have to meet planning rules.</p>",
        ["Garages always need a building permit.", "Sheds near a boundary or in a heritage area can need planning approval too.",
         "Large sheds on house lots are capped by the R-Codes (in summary, 60 m&sup2; or 10% of the lot, whichever is less) unless the council approves more."],
        TREE)
    body += b.section(b.intro("What goes in", "What a shed permit application needs",
        "This is the paperwork a WA council expects for a typical shed. We prepare or collect all of it.") +
        '<div class="prose"><div class="table-wrap"><table><thead><tr><th>Document</th><th>What it shows</th><th>Who sorts it</th></tr></thead><tbody>'
        '<tr><td>Application form (BA1 or BA2)</td><td>BA2 is the standard route where council checks the plans. BA1 is faster and comes with a private surveyor\'s certificate.</td><td>Us</td></tr>'
        '<tr><td>Site plan</td><td>The lot, boundaries, existing buildings, the shed\'s position and its distance to each boundary, usually at 1:200.</td><td>Us</td></tr>'
        '<tr><td>Floor plan and elevations</td><td>Size, height, doors and wall heights.</td><td>Us, from your supplier\'s drawings</td></tr>'
        '<tr><td>Engineering</td><td>Footings, frame and tie-down details for the wind rating at your address.</td><td>Your shed supplier, or an engineer we arrange</td></tr>'
        '<tr><td>Owner\'s signature</td><td>Consent from every owner on the title.</td><td>You (we send it ready to sign)</td></tr>'
        '<tr><td>Fees and levies</td><td>Council\'s fee and the state levies, based on the value of the work.</td><td>Paid at lodgement</td></tr>'
        '</tbody></table></div></div>', "section")
    body += b.section(b.intro("How it works", "From backyard idea to approved shed", "", center=True) + b.steps([
        ("Send us the basics", "Your address, the shed size and where it will go. A photo of the spot helps."),
        ("We prepare everything", "Site plan, drawings and forms, checked against your council's setback and planning rules."),
        ("We lodge and follow up", "We lodge it, answer council's questions and send you the permit when it is issued."),
    ]), "section white")
    body += b.prose_section("""
<h2>What does a shed permit cost in WA?</h2>
<p>There are two parts. The first is the <strong>council's fee and the state levies</strong>. These are set by the Building Regulations and are worked out from the value of the shed. For a typical backyard shed they usually come to a few hundred dollars, because minimum fees apply.</p>
<p>The second is the cost of <strong>preparing the application</strong>: the site plan, drawings and forms. That is our fixed price, and it includes lodging and dealing with council until the permit is issued. If your job needs engineering or a private building surveyor, we include that in the quote too, so you see one total.</p>
<h2>Building the shed before the permit</h2>
<p>Don't. In WA it is an offence to build without a required permit, and fines can reach $50,000 for a first offence. Councils can also order changes or removal. If it is already up, see <a href="/retrospective-shed-approval">retrospective shed approval</a>.</p>
""")
    body += b.section(b.intro("Guides", "Shed permit guides") + b.guides([
        ("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?", "The 10 m&sup2; rule, how to measure, and the planning rules that still apply.", "question"),
        ("/garage-building-permit", "Garage building permits", "Why garages always need a permit, and when they need planning approval too.", "garage"),
        ("/retrospective-shed-approval", "Retrospective shed approval", "Already built? How to get an existing shed approved.", "retro"),
    ]), "section white")
    body += b.section('<div class="narrow">' + b.intro("Questions", "Common questions") + b.faq_block(HOME_FAQS) + "</div>")
    body += b.band(S, S["band_title"], S["band_text"])
    return {"path": "index.html", "title": "Shed Building Permit Perth & WA | Done For You, Fixed Price",
            "desc": "Need a shed building permit in Perth or WA? We check your council's rules, draw the site plan and lodge your application. Fixed price, no runaround.",
            "h1": "Shed building permits in Perth, done for you.", "body": body, "faqs": HOME_FAQS}


NEED_BODY = """
<h2>The 10 m&sup2; rule</h2>
<p>WA's Building Regulations list some small structures that don't need a building permit. For sheds, the key test is that the shed is <strong>freestanding</strong>, has a <strong>floor area of 10 m&sup2; or less</strong> and is <strong>no taller than 2.4 m</strong>. Miss any one of the three and you need a permit.</p>
<div class="table-wrap"><table>
<thead><tr><th>Shed size</th><th>Floor area</th><th>Building permit?</th></tr></thead><tbody>
<tr><td>2.3 m x 2.3 m</td><td>5.3 m&sup2;</td><td>Usually not (if 2.4 m tall or less)</td></tr>
<tr><td>3 m x 3 m</td><td>9 m&sup2;</td><td>Usually not (if 2.4 m tall or less)</td></tr>
<tr><td>3 m x 3.3 m</td><td>9.9 m&sup2;</td><td>Usually not (if 2.4 m tall or less)</td></tr>
<tr><td>3 m x 4 m</td><td>12 m&sup2;</td><td>Yes</td></tr>
<tr><td>6 m x 6 m</td><td>36 m&sup2;</td><td>Yes</td></tr>
<tr><td>Any size, attached to the house</td><td>Any</td><td>Yes</td></tr>
</tbody></table></div>

<h2>How to measure</h2>
<p><strong>Floor area</strong> is the length times the width of the floor inside the walls. <strong>Height</strong> is measured from the natural ground level to the highest point of the roof. On a sloping block, the high point is measured from the lowest side, so a shed can be taller than you expect.</p>

<h2>"Freestanding" means not touching anything</h2>
<p>A shed that shares a wall with the house, the garage or a patio, or whose roof joins another roof, is not freestanding. It needs a building permit at any size.</p>

<h2>No permit doesn't mean no rules</h2>
<p>Even an exempt shed has to follow the planning rules and be built properly. Things that catch people out:</p>
<ul>
<li><strong>Front yard.</strong> Sheds in the street setback area usually need planning approval.</li>
<li><strong>Boundaries.</strong> Walls on or near a boundary have height and length limits in the R-Codes.</li>
<li><strong>Easements and sewers.</strong> You generally can't build over a sewer line or easement without permission from the Water Corporation or the easement owner.</li>
<li><strong>Heritage and special areas.</strong> Heritage-listed places and some estates have their own rules.</li>
<li><strong>Bushfire-prone areas.</strong> Sheds close to the house can need extra construction measures.</li>
</ul>

<h2>Bigger sheds on house lots</h2>
<p>For bigger sheds, the R-Codes set standard limits for outbuildings on a house lot. In summary: all outbuildings together up to 60 m&sup2; or 10% of the lot (whichever is less), walls up to 2.4 m high, a roof ridge up to 4.2 m, and not in the street setback. Councils can vary these in their local planning policies. A shed outside them needs planning approval, and some councils allow larger sheds on bigger lots.</p>
"""

NEED_FAQS = [
    ("Is a 3 x 3 shed exempt in WA?",
     "Usually, yes. A 3 m x 3 m shed is 9 m&sup2;, so if it is freestanding and no taller than 2.4 m it normally doesn't need a building permit. Check the planning rules for where you put it."),
    ("Does a garden shed on pavers need a permit?",
     "The base doesn't decide it. Size, height and whether it is freestanding do. A small kit shed on pavers that meets the 10 m&sup2; and 2.4 m limits is usually exempt."),
    ("Do I need a permit for a cubby house or a playhouse?",
     "The same test applies. A small freestanding cubby within the size and height limits is usually exempt. A large or elevated one may need a permit."),
    ("Who checks if my shed is exempt?",
     "Nobody signs off an exempt shed, so it is up to you to get it right. If you are not sure, ask your council or ask us, and we will tell you for free."),
]


def need(S):
    return {"path": "do-i-need-a-permit-for-a-shed.html", "kind": "article",
            "title": "Do I Need a Permit for a Shed in WA? The 10 m² Rule Explained",
            "desc": "In WA a freestanding shed of 10 m² or less and 2.4 m tall or less usually doesn't need a building permit. Here is how to measure, and the rules that still apply.",
            "eyebrow": "Do I need one?", "h1": "Do I need a permit for a shed in WA?", "crumb": "Do I need a permit for a shed?",
            "answer": "<p>Usually not, if the shed is <strong>freestanding</strong>, <strong>10 m&sup2; or smaller</strong> and <strong>2.4 m tall or less</strong>. Bigger, taller or attached sheds need a building permit. Every shed, permit or not, still has to follow the planning rules.</p>",
            "body": NEED_BODY, "faqs": NEED_FAQS,
            "related": [("/", "Shed building permits"), ("/garage-building-permit", "Garage building permits"), ("/retrospective-shed-approval", "Retrospective shed approval")]}


GARAGE_BODY = """
<h2>Garages always need a building permit</h2>
<p>A garage is a building designed to house cars, with walls on all sides and usually a roller or panel door. In WA every garage needs a building permit, whether it is attached to the house or stands on its own. The permit checks the slab, the frame, the tie-downs and, if it is near a boundary or the house, fire separation.</p>

<h2>Garage, carport or shed?</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Garage</th><th>Carport</th><th>Shed</th></tr></thead><tbody>
<tr><td>Enclosed</td><td>Yes, with a door</td><td>Open on at least two sides</td><td>Yes</td></tr>
<tr><td>Building permit</td><td>Always</td><td>Almost always</td><td>Over 10 m&sup2; or 2.4 m tall</td></tr>
<tr><td>Front setback</td><td>Usually set back further</td><td>Can be closer if open and narrow enough</td><td>Usually not allowed without approval</td></tr>
</tbody></table></div>
<p>A carport with a solid door added is treated as a garage, so it then has to meet the garage rules.</p>

<h2>When a garage needs planning approval too</h2>
<p>The R-Codes set standard rules for garages on house lots. A garage that meets them only needs a building permit. One that doesn't needs planning approval first. The common triggers are:</p>
<ul>
<li><strong>Too close to the street.</strong> Garages usually have to be set back further from the street than carports.</li>
<li><strong>Too wide.</strong> Garage doors facing the street are limited to a share of the lot's frontage.</li>
<li><strong>Boundary walls.</strong> A garage wall built on the side boundary has limits on its height and length.</li>
<li><strong>Heritage areas and estates</strong> with their own design rules.</li>
</ul>

<h2>What we prepare</h2>
<ul>
<li>A site plan showing the garage, setbacks and existing buildings</li>
<li>Floor plan and elevations, from your builder's or supplier's drawings</li>
<li>Engineering for the slab and frame (from your supplier or an engineer we arrange)</li>
<li>The application forms and owner consent, then lodgement and follow-up</li>
</ul>
"""

GARAGE_FAQS = [
    ("Do I need a permit to convert a garage into a room?",
     "Yes. Turning a garage into a bedroom, office or living space changes how the building is used, so it needs a building permit, and often planning approval too. It also has to meet the rules for habitable rooms, such as ceiling height, insulation, ventilation and light."),
    ("Can a garage be built on the boundary?",
     "Often, yes, as a boundary wall within the R-Codes' height and length limits. Outside those limits it needs planning approval, and the wall has to meet fire-separation rules."),
    ("How long does a garage permit take?",
     "Allow a week or so to prepare the documents, then up to 25 business days for a standard council decision. If planning approval is needed, that comes first and adds time."),
]


def garage(S):
    return {"path": "garage-building-permit.html", "kind": "article", "permit": "garage",
            "title": "Garage Building Permit in WA | Attached & Freestanding Garages",
            "desc": "Every garage in WA needs a building permit, and many need planning approval too. What triggers it, how garages differ from carports and sheds, and how we handle it.",
            "eyebrow": "Garages", "h1": "Garage building permits in WA", "crumb": "Garage building permit",
            "answer": "<p>Yes, every garage in WA needs a building permit, attached or freestanding. Many also need <strong>planning approval</strong> if they are close to the street, wide across the frontage or built on a boundary. We work out which and handle both.</p>",
            "body": GARAGE_BODY, "faqs": GARAGE_FAQS,
            "related": [("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("https://carportpermit.com.au/", "Carport permits"), ("/retrospective-shed-approval", "Retrospective approval")]}


RETRO_BODY = """
<h2>It happens a lot</h2>
<p>Unapproved sheds are one of the most common things found when a house is sold. Some were put up by a previous owner, some by people who thought a kit shed didn't need a permit. Either way, it can usually be approved after the fact.</p>

<h2>How retrospective shed approval works in WA</h2>
<ol>
<li><strong>We look at what's there.</strong> Photos, measurements and what your council has on file.</li>
<li><strong>As-built plans.</strong> We draw the shed as it stands, with a site plan showing its position and setbacks.</li>
<li><strong>Surveyor inspection.</strong> A registered building surveyor checks the shed and, if it meets the standards, issues a Certificate of Building Compliance.</li>
<li><strong>Planning approval if needed.</strong> If the shed breaks a planning rule, such as a boundary setback, that approval comes first.</li>
<li><strong>Lodgement.</strong> We lodge a Building Approval Certificate application with your council.</li>
<li><strong>Approved.</strong> The council issues the Building Approval Certificate and the shed is on record.</li>
</ol>

<h2>Common problems with older sheds</h2>
<ul>
<li><strong>No footing details.</strong> The surveyor needs to know how the shed is held down. Sometimes a small dig at a corner answers it.</li>
<li><strong>Missing engineering.</strong> Kit sheds come with engineering. If the paperwork is lost, the supplier can often reissue it, or an engineer can assess it.</li>
<li><strong>Too close to a boundary or over a sewer.</strong> These are planning issues and may need approval or a change.</li>
</ul>
<p>If something needs fixing, you get a clear list. Once it is fixed, the certificate can be issued.</p>
"""

RETRO_FAQS = [
    ("Will council make me pull it down?",
     "It is rare for a sound shed in a sensible spot. Most unapproved sheds are approved, sometimes after small changes. Removal is usually only ordered for serious safety or planning problems."),
    ("Do I need retrospective approval for a small shed?",
     "Not if the shed would have been exempt in the first place: freestanding, 10 m&sup2; or less and 2.4 m tall or less. In that case there is nothing to approve."),
    ("How long does it take?",
     "Usually four to eight weeks, depending on the surveyor's inspection and the council's workload. Add more time if planning approval is needed."),
]


def retro(S):
    return {"path": "retrospective-shed-approval.html", "kind": "article", "permit": "retrospective",
            "title": "Retrospective Shed Approval in WA | Unapproved Sheds Sorted",
            "desc": "Shed built without a permit? How retrospective approval works in WA, what the surveyor checks, common problems with older sheds, and how we handle it for you.",
            "eyebrow": "Already built", "h1": "Retrospective shed approval in WA", "crumb": "Retrospective shed approval",
            "answer": "<p>A shed built without a permit can usually be approved afterwards with a <strong>Building Approval Certificate</strong>. A registered building surveyor inspects and certifies it, then the application goes to your council. We organise the whole process.</p>",
            "body": RETRO_BODY, "faqs": RETRO_FAQS,
            "related": [("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("https://getmypermit.com.au/retrospective-approval", "Retrospective approval for any structure")],
            "band_title": "Selling with an unapproved shed?", "band_text": "Send us photos and your address. We tell you what's involved and give you a fixed price."}


def notfound(S):
    body = """<section class="page-hero" style="border:0;padding:110px 0"><div class="wrap narrow center">
<p class="eyebrow">Page not found</p><h1>That page has moved or never existed.</h1>
<div class="cta-row" style="justify-content:center"><a class="btn btn-ink" href="/">Go to the home page</a><a class="btn btn-line" href="%s">Get a quote</a></div>
</div></section>""" % b.quote_link(S)
    return {"path": "404.html", "title": "Page not found", "desc": "Page not found.", "h1": "Page not found", "body": body, "noindex": True}


def pages(S):
    return [home(S), need(S), garage(S), retro(S), notfound(S)]
