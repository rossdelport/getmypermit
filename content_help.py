"""Trust blocks shared by every home page, plus the umbrella's How it works and jargon buster pages.

Lessons from councilapproval.com.au (see the GetMyPermit memory): show a clear promise strip under the hero,
name the customer's worries before selling, explain the whole journey, and own the jargon.
"""
import build as b
import prices
from sites import PHONE

# Under every home hero: honest promises instead of big claims we can't back yet.
def promises(site):
    if site["key"] == "gmp":
        price, label = "$990", "Total price for a shed, patio or carport permit, council fees included"
    else:
        name, price, note = prices.ITEMS[prices.SITE_ITEMS[site["key"]][0]]
        fees = "council fees included" if "included" in note else "plus council fees, shown before you pay"
        label = "Fixed price for a %s, %s" % (name.split(",")[0].lower(), fees)
    return b.section(b.stats([
        (price, label),
        ("1 day", "We usually reply with your fixed price within one business day"),
        ("$0", "If you don't need a permit, we tell you and it costs nothing"),
        ("Money back", "If council refuses and we can't get it approved, you get your money back"),
    ]), "section tight")


# The worries people have before they call. Unique wording on every site.
PAINS = {
    "gmp": ("Council paperwork shouldn't be your weekend job.", [
        ("Which form? Which rules?", "BA1 or BA2, the R-Codes, your council's local policies. The rules are public, but they are spread across a dozen documents."),
        ("The back and forth", "One missing drawing and council asks for more. Every round adds days or weeks."),
        ("Everyone is waiting", "Your builder has a start date, and nothing can begin until the permit is issued."),
    ]),
    "shed": ("Bought the shed. Now there's paperwork.", [
        ("Is it over 10 m&sup2;?", "Most useful sheds are. That means a site plan, forms and council fees before the slab goes down."),
        ("How close to the fence?", "Setbacks and wall heights decide whether you need planning approval as well."),
        ("The kit is on its way", "Delivery is booked, but your installer can't start until the permit is issued."),
    ]),
    "pergola": ("The outdoor area is planned. The approval isn't.", [
        ("Attached means a permit", "Almost every patio fixed to the house needs a building permit, even a small one."),
        ("Near the boundary?", "Posts and roofs close to a fence have their own limits, and some councils want planning approval too."),
        ("Your builder needs it first", "Most patio builders won't start until the permit is issued. Paperwork delays push back your summer."),
    ]),
    "carport": ("A carport sounds simple. Council often disagrees.", [
        ("Out the front?", "Carports in the front setback often need planning approval as well as a building permit."),
        ("Rules change by street", "Setbacks depend on your lot's R-Code, heritage areas and your council's own policy."),
        ("Two approvals, in order", "Planning approval comes first and the building permit follows. Getting the order wrong costs weeks."),
    ]),
    "granny": ("A granny flat is a big decision. The approval shouldn't hold it up.", [
        ("Does it fit the 70 m&sup2; rules?", "Meet the standard rules and you can skip planning approval. Miss one and you can't."),
        ("Lots of people to line up", "Designer, engineer, energy assessor, building surveyor and council all play a part."),
        ("Money on hold", "Your builder's deposit and your finance are waiting on one piece of paper."),
    ]),
    "tiny": ("Tiny homes are simple to live in. The rules aren't.", [
        ("Caravan or house?", "On wheels it is treated like a caravan. On footings it is a dwelling. The approval is completely different."),
        ("Every council is different", "Some welcome tiny homes. Others set strict limits on how long you can live in one."),
        ("Hard to get a straight answer", "Calls to council often end with \"it depends\". We find out what it depends on."),
    ]),
}


def pains(site):
    title, items = PAINS[site["key"]]
    grid = '<div class="grid g3">' + "".join(
        '<div class="card"><h3>%s</h3><p>%s</p></div>' % (t, d) for t, d in items) + "</div>"
    end = ('<p class="center" style="margin-top:28px">That is the part we take off your hands. We do this every day, '
           'so you don\'t have to learn it for one project. <a href="https://getmypermit.com.au/how-it-works">See how it works</a>.</p>')
    if site["key"] == "gmp":
        end = end.replace("https://getmypermit.com.au", "")
    return b.section(b.intro("Sound familiar?", title, "", center=True) + grid + end, "section white")


# ---------- How it works (umbrella) ----------

HOW_FAQS = [
    ("What if council asks for more information?",
     "That is normal, and it is part of our price. We answer council's questions and update the drawings if needed until your permit is issued. While council waits for answers, its decision clock is paused, so we reply quickly."),
    ("What if my project can't be approved as planned?",
     "We check your project against the state rules and your council's policies before we lodge, so this is rare. If something won't pass, we tell you before lodging and explain what would, such as moving a shed further from the fence or lowering a wall. And our promise is simple: approved, or your money back. " + prices.PROMISE),
    ("What do I need to give you?",
     "Your address, what you are building and where it will go. Photos of the spot and your supplier's drawings help. Later you sign the application forms, which we send ready to sign by email."),
    ("Can my builder start once the permit is issued?",
     "Yes. Keep a copy on site. A WA building permit is usually valid for two years. When the work is finished, a notice of completion (form BA7) is lodged within 7 days."),
]

HOW_BODY = """
<h2>The whole journey, step by step</h2>
<p>Most people only deal with council once or twice in their life. Here is everything that happens, in order, so there are no surprises.</p>

<h3>Step 0. Free check: do you even need a permit?</h3>
<p>Use our <a href="/do-i-need-approval">20-second checker</a> or call us. If your project is exempt, we tell you, and it costs nothing.</p>

<h3>Step 1. Your fixed price</h3>
<p>Tell us what you are building and where. We usually reply within one business day with one total price. For most small projects that includes the council's fees. <a href="/pricing">See our prices</a>.</p>

<h3>Step 2. We check your council's rules</h3>
<p>Before drawing anything we look up your lot: its zoning and R-Code, setbacks, heritage or bushfire areas, easements and sewer lines. This is where most refusals are avoided.</p>

<h3>Step 3. We prepare the application</h3>
<p>We draw the site plan, prepare the drawings and fill in the forms. If your job needs an engineer, a registered building surveyor or a bushfire (BAL) assessor, we organise them. You sign the forms by email.</p>

<h3>Step 4. We lodge it with council</h3>
<p>We lodge the application and pay the fees. A standard (uncertified, BA2) application has up to 25 business days for a decision. A certified (BA1) application, which comes with a private building surveyor's certificate, has up to 10.</p>

<h3>Step 5. We answer council's questions</h3>
<p>Council often asks for something extra: a measurement, a detail, a signature. We handle it. Planning approval, if your project needs it, comes before the building permit.</p>

<h3>Step 6. Permit issued</h3>
<p>We send you the permit and explain any conditions in plain English. Your builder can start.</p>

<h3>Step 7. Finishing off</h3>
<p>When the work is done, a notice of completion (BA7) goes to council within 7 days. For pools, the safety barrier must be finished and inspected before you fill it.</p>

<h2>Who does what</h2>
<div class="table-wrap"><table>
<thead><tr><th>Task</th><th>Who</th></tr></thead><tbody>
<tr><td>Checking whether you need a permit</td><td>Us, free</td></tr>
<tr><td>Checking council and planning rules</td><td>Us</td></tr>
<tr><td>Site plan, drawings and forms</td><td>Us</td></tr>
<tr><td>Engineering, surveyor certificate, BAL report</td><td>Us, using registered professionals</td></tr>
<tr><td>Signing the forms</td><td>You (every owner on the title)</td></tr>
<tr><td>Lodging and paying council fees</td><td>Us</td></tr>
<tr><td>Answering council's questions</td><td>Us</td></tr>
<tr><td>Building it</td><td>You or your builder</td></tr>
</tbody></table></div>

<h2>How long it takes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>Usual time</th></tr></thead><tbody>
<tr><td>Quote</td><td>Within one business day</td></tr>
<tr><td>Preparing the application</td><td>A few days to a week (longer for granny flats)</td></tr>
<tr><td>Council decision, standard application</td><td>Up to 25 business days</td></tr>
<tr><td>Council decision, certified application</td><td>Up to 10 business days</td></tr>
<tr><td>Planning approval, if needed</td><td>Usually 60 days, or 90 if neighbours are asked for comments</td></tr>
</tbody></table></div>
<p>Want it faster? Our fast track (+$550) uses a certified application, so council has 10 business days instead of 25.</p>
"""


def how_it_works(S):
    return {"path": "how-it-works.html", "kind": "article",
            "title": "How Getting a Building Permit Works in WA, Step by Step | GetMyPermit",
            "desc": "Every step of getting a building permit in Perth and WA, from the free check to the notice of completion, with who does what and how long each part takes.",
            "updated": "2026-10-30", "eyebrow": "How it works", "h1": "How getting your permit works, step by step", "crumb": "How it works",
            "answer": "<p>You tell us what you are building. We check your council's rules, prepare the plans and forms, lodge them and answer council's questions until your permit is issued. Council then has up to 25 business days to decide a standard application, or 10 for a certified one. You sign the forms and build.</p>",
            "body": HOW_BODY, "faqs": HOW_FAQS,
            "related": [("/do-i-need-approval", "Do I need approval?"), ("/permit-jargon", "Permit jargon buster"), ("/pricing", "Our prices")]}


# ---------- Jargon buster (umbrella) ----------

TERMS = [
    ("Ancillary dwelling", "The planning name for a granny flat: a small second home on the same lot as the main house. In WA, one up to 70 m&sup2; that meets the standard rules doesn't need planning approval, but it still needs a building permit.", "https://grannyflatpermit.com.au/granny-flat-rules-wa"),
    ("BA1 (certified application)", "The building permit application that comes with a Certificate of Design Compliance from a private registered building surveyor. Council has up to 10 business days to decide it.", "/which-ba-form"),
    ("BA2 (uncertified application)", "The standard building permit application, where council's own surveyor checks the plans. Only allowed for houses, granny flats and outbuildings like sheds, patios and carports. Council has up to 25 business days.", "/which-ba-form"),
    ("BA7 (notice of completion)", "The form that tells council the building work is finished. It is lodged within 7 days of completing the work.", None),
    ("BA13 (building approval certificate)", "The application used to get approval for building work that was done without a permit. It is lodged with a certificate of building compliance (BA18) from a building surveyor.", "/retrospective-approval"),
    ("BAL (bushfire attack level)", "A rating from BAL-LOW to BAL-FZ that measures how exposed a building is to bushfire. In a bushfire prone area, many projects need a BAL assessment, and the rating decides how the building must be built.", None),
    ("Building permit", "Approval that a structure is safe and meets the building code. Most garages, carports, patios, decks, granny flats and pools in WA need one before work starts.", "/do-i-need-approval"),
    ("Building Services Levy", "A state levy added to every building permit. It is $61.65 for work worth up to $45,000.", "/pricing"),
    ("Certificate of Design Compliance (CDC)", "A certificate (form BA3) from a registered building surveyor saying the plans meet the building code. It turns your application into a faster certified (BA1) application.", None),
    ("Class 10", "The building code's category for non-habitable structures. Class 10a covers sheds, garages, carports and patios. Class 10b covers fences, pools and retaining walls.", None),
    ("Deemed-to-comply", "Meeting the standard measure in the R-Codes, such as a set distance from the boundary. If a project meets every deemed-to-comply rule, it often doesn't need planning approval.", None),
    ("Development approval (planning approval)", "Approval that a project suits the site and street: setbacks, height, overlooking and heritage. It is separate from the building permit and, when needed, comes first.", "/do-i-need-approval"),
    ("Easement", "A strip of your land that someone else has a right to use, often for pipes or power. You usually can't build over one without permission.", None),
    ("Exempt work", "Small structures that don't need a building permit, like a freestanding shed of 10 m&sup2; or less and no taller than 2.4 m. Exempt work still has to follow planning rules.", "/what-doesnt-need-a-building-permit"),
    ("Heritage area", "A place or street protected for its character. Changes there, even small ones, usually need planning approval.", None),
    ("Natural ground level", "The level of the ground before any digging or filling. Heights are measured from it, which matters on sloping blocks.", None),
    ("Outbuilding", "The planning name for a shed, garage or workshop that isn't attached to the house. On most house lots the R-Codes cap their total size at 60 m&sup2; or 10% of the lot, whichever is less.", "https://shedbuildingpermit.com.au/"),
    ("Owner-builder", "A homeowner who manages their own building work instead of using a registered builder. In WA, work worth more than $20,000 needs owner-builder approval first.", None),
    ("Patio", "In the R-Codes, an unenclosed structure with a roof that keeps out the rain. Patios attached to a house need a building permit.", "https://pergolabuildingpermit.com.au/"),
    ("R-Codes (Residential Design Codes)", "WA's state planning rules for homes. They set setbacks, building heights, site cover, privacy and the size of sheds and granny flats.", None),
    ("Registered building surveyor", "A licensed professional who checks plans and buildings against the building code. They issue design compliance and building compliance certificates.", None),
    ("Retrospective approval", "Getting approval for something already built without a permit. In WA this is done with a building approval certificate (BA13).", "/retrospective-approval"),
    ("Setback", "The distance between a building and a boundary. The front (primary street) setback is the area between your house and the street, where carports and sheds have strict limits.", "https://carportpermit.com.au/carport-in-front-setback"),
    ("Site plan", "A drawing of your lot from above, showing the boundaries, existing buildings and the new work with its distances to each boundary. Usually drawn at 1:200.", None),
]


def jargon(S):
    body = "<p>Council letters and forms are full of codes and terms. Here they are in plain English, in A to Z order.</p>\n<dl class=\"terms\">"
    for name, text, link in TERMS:
        tid = name.split(" (")[0].lower().replace(" ", "-")
        more = ' <a href="%s">Read more</a>' % link if link else ""
        body += '<dt id="%s">%s</dt><dd>%s%s</dd>' % (tid, name, text, more)
    body += "</dl>"
    ld = {"@type": "DefinedTermSet", "@id": "https://getmypermit.com.au/permit-jargon#terms",
          "name": "WA building permit jargon buster", "hasDefinedTerm": [
              {"@type": "DefinedTerm", "name": b.strip(n), "description": b.strip(t).replace("&sup2;", "²"),
               "url": "https://getmypermit.com.au/permit-jargon#" + n.split(" (")[0].lower().replace(" ", "-")}
              for n, t, _ in TERMS]}
    return {"path": "permit-jargon.html", "kind": "article",
            "title": "Building Permit Jargon Buster: WA Terms in Plain English | GetMyPermit",
            "desc": "BA1, BA2, BA7, R-Codes, setbacks, CDC, Class 10 and more. WA building permit and council approval terms explained in plain English.",
            "updated": "2026-10-30", "eyebrow": "Jargon buster", "h1": "Building permit jargon, in plain English", "crumb": "Jargon buster",
            "answer": "<p>The two terms that matter most: a <strong>building permit</strong> checks a structure is safe, and <strong>planning approval</strong> checks it suits the site and street. Some projects need both. The rest of this page explains the forms and codes you will see along the way.</p>",
            "body": body, "ld": [ld],
            "related": [("/how-it-works", "How it works"), ("/do-i-need-approval", "Do I need approval?")]}
