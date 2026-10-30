"""getmypermit.com.au: the umbrella site, the quote form and the full checker."""
import build as b
import content_help
from sites import SITES, PHONE, PHONE_TEL, QUOTE_EMAIL
import icons
import prices

Q = "/quote"

# The "Do I need approval?" checker for every project type. Results stay cautious: councils differ.
TREE = {
    "start": "start", "depth": 4,
    "nodes": {
        "start": {"q": "What are you planning to build?", "opts": [
            {"t": "Shed or outbuilding", "go": "shed1"}, {"t": "Garage", "go": "r_garage"},
            {"t": "Patio, pergola or verandah", "go": "pat1"}, {"t": "Deck", "go": "r_deck"},
            {"t": "Carport", "go": "car1"}, {"t": "Granny flat", "go": "gf1"}, {"t": "Tiny home", "go": "th1"},
            {"t": "Pool or spa", "go": "pool1"}, {"t": "It is already built", "go": "r_retro"}]},
        "shed1": {"q": "Will the shed stand on its own, not attached to the house or another building?", "opts": [
            {"t": "Yes, freestanding", "go": "shed2"}, {"t": "No, attached", "go": "r_shed_permit"}]},
        "shed2": {"q": "Is the floor area 10 m² or less?", "help": "For example 3 m x 3.3 m, or 2.5 m x 4 m.", "opts": [
            {"t": "Yes, 10 m² or less", "go": "shed3"}, {"t": "No, bigger", "go": "r_shed_permit"}, {"t": "Not sure", "go": "r_shed_permit"}]},
        "shed3": {"q": "Is it 2.4 m tall or less at the highest point?", "opts": [
            {"t": "Yes", "go": "r_shed_exempt"}, {"t": "No, taller", "go": "r_shed_permit"}]},
        "r_shed_exempt": {"result": True, "title": "You probably don't need a building permit",
            "body": "<p>In WA, a freestanding shed of 10 m² or less that is no taller than 2.4 m is usually exempt from a building permit. Planning rules still apply, such as boundary setbacks, heritage areas and easements, and the shed still has to be built properly.</p><p>Not sure about your block? We can check with your council for you.</p>",
            "cta": {"href": Q + "?permit=shed", "text": "Ask us to check"}},
        "r_shed_permit": {"result": True, "title": "You'll need a building permit",
            "body": "<p>Sheds over 10 m², taller than 2.4 m or attached to another building need a building permit before work starts. Some also need planning approval, for example in a heritage area or when built close to a boundary.</p><p>We prepare the site plan and forms and lodge it with your council.</p>",
            "cta": {"href": Q + "?permit=shed", "text": "Get a shed permit quote"}},
        "r_garage": {"result": True, "title": "You'll need a building permit",
            "body": "<p>Garages need a building permit in WA. Many also need planning approval, depending on where the garage sits on your lot and your council's setback rules.</p>",
            "cta": {"href": Q + "?permit=garage", "text": "Get a garage permit quote"}},
        "pat1": {"q": "Will it be attached to the house?", "opts": [
            {"t": "Yes, attached", "go": "r_patio_permit"}, {"t": "No, freestanding", "go": "pat2"}]},
        "pat2": {"q": "Will it have a roof covering?", "help": "Open beams or a shade sail count as no roof covering.", "opts": [
            {"t": "Yes, a solid roof", "go": "pat3"}, {"t": "No, open beams only", "go": "r_pergola_open"}]},
        "pat3": {"q": "Is it 10 m² or less and 2.4 m tall or less?", "opts": [
            {"t": "Yes", "go": "r_patio_exempt"}, {"t": "No", "go": "r_patio_permit"}, {"t": "Not sure", "go": "r_patio_permit"}]},
        "r_pergola_open": {"result": True, "title": "You might not need a building permit",
            "body": "<p>Open pergolas with no roof covering are often exempt up to a set size, but the limit differs between councils (some use 20 m² and 2.4 m tall). Adding a roof later usually means you need a permit.</p>",
            "cta": {"href": Q + "?permit=pergola", "text": "Ask us to check your council"}},
        "r_patio_exempt": {"result": True, "title": "You probably don't need a building permit",
            "body": "<p>A small freestanding patio of 10 m² or less and no taller than 2.4 m is usually exempt in WA. Planning rules such as boundary setbacks still apply.</p>",
            "cta": {"href": Q + "?permit=pergola", "text": "Ask us to check"}},
        "r_patio_permit": {"result": True, "title": "You'll need a building permit",
            "body": "<p>Patios and roofed pergolas that are attached to the house, or bigger than 10 m², need a building permit. Planning approval may also be needed if it is close to a boundary or in a heritage area.</p>",
            "cta": {"href": Q + "?permit=pergola", "text": "Get a patio permit quote"}},
        "r_deck": {"result": True, "title": "You'll most likely need a building permit",
            "body": "<p>Most decks in WA need a building permit, especially raised decks and decks attached to the house. A few councils treat very low, ground-level decks differently, so we confirm with your council before you build.</p>",
            "cta": {"href": Q + "?permit=deck", "text": "Get a deck permit quote"}},
        "car1": {"q": "Will the carport be in front of the house, in the street setback?", "opts": [
            {"t": "Yes, at the front", "go": "r_car_front"}, {"t": "No, beside or behind", "go": "r_car_permit"}, {"t": "Not sure", "go": "r_car_front"}]},
        "r_car_front": {"result": True, "title": "You'll likely need planning approval and a building permit",
            "body": "<p>Carports in the front setback often need development (planning) approval from your council as well as a building permit. Every council has its own setback rules, so the design may need small changes to get approved.</p>",
            "cta": {"href": Q + "?permit=carport", "text": "Get a carport permit quote"}},
        "r_car_permit": {"result": True, "title": "You'll need a building permit",
            "body": "<p>Carports nearly always need a building permit in WA. Planning approval can also apply, for example if the carport is on the boundary.</p>",
            "cta": {"href": Q + "?permit=carport", "text": "Get a carport permit quote"}},
        "gf1": {"q": "Is your lot zoned residential?", "help": "Most suburban Perth blocks are. Rural and farming zones are different.", "opts": [
            {"t": "Yes, residential", "go": "gf2"}, {"t": "No, rural", "go": "r_gf_rural"}, {"t": "Not sure", "go": "r_gf_check"}]},
        "gf2": {"q": "Will the granny flat be 70 m² or smaller?", "opts": [
            {"t": "Yes, 70 m² or less", "go": "r_gf_small"}, {"t": "No, bigger", "go": "r_gf_big"}]},
        "r_gf_small": {"result": True, "title": "You'll need a building permit, and probably not planning approval",
            "body": "<p>Since 10 April 2024, a granny flat of up to 70 m² that meets the R-Codes deemed-to-comply rules (including setbacks) can be built on a residential lot of any size without planning approval. A building permit is still always required.</p>",
            "cta": {"href": Q + "?permit=granny-flat", "text": "Get a granny flat quote"}},
        "r_gf_big": {"result": True, "title": "You'll need planning approval and a building permit",
            "body": "<p>A granny flat over 70 m² falls outside the standard rules, so it needs planning approval from your council as well as a building permit. Some councils may assess it as a second house.</p>",
            "cta": {"href": Q + "?permit=granny-flat", "text": "Get a granny flat quote"}},
        "r_gf_rural": {"result": True, "title": "You'll likely need planning approval and a building permit",
            "body": "<p>The planning exemption for granny flats is aimed at residential zones. On rural and farming land, many shires still need a development application, plus a building permit.</p>",
            "cta": {"href": Q + "?permit=granny-flat", "text": "Get a granny flat quote"}},
        "r_gf_check": {"result": True, "title": "You'll need a building permit. Planning depends on your zoning",
            "body": "<p>Every granny flat needs a building permit. Whether it also needs planning approval depends on your zoning and its size. Send us your address and we will check the zoning for you.</p>",
            "cta": {"href": Q + "?permit=granny-flat", "text": "Check my lot"}},
        "th1": {"q": "Is your tiny home on wheels?", "opts": [
            {"t": "Yes, on a trailer", "go": "th2"}, {"t": "No, on footings or a slab", "go": "r_th_fixed"}]},
        "th2": {"q": "How long will someone stay in it?", "opts": [
            {"t": "Just a few nights", "go": "r_th_short"}, {"t": "Longer, or to live in", "go": "r_th_long"}]},
        "r_th_short": {"result": True, "title": "The landowner's OK is usually enough",
            "body": "<p>In WA a tiny home on wheels is treated like a caravan. Very short stays of a few nights on private land only need the landowner's permission. Anything longer needs approval from your local government.</p>",
            "cta": {"href": Q + "?permit=tiny-home", "text": "Plan a longer stay"}},
        "r_th_long": {"result": True, "title": "You'll need local government approval",
            "body": "<p>Since 1 September 2024, councils in WA can approve a tiny home on wheels on private land for up to 24 months at a time, and the approval can be renewed. More than one on a lot needs approval from the Minister. Councils set their own conditions, such as water, power and waste.</p>",
            "cta": {"href": Q + "?permit=tiny-home", "text": "Get a tiny home quote"}},
        "r_th_fixed": {"result": True, "title": "You'll need a building permit",
            "body": "<p>A tiny home on footings or a slab is a building, so it needs a building permit like any house. If it is a second dwelling behind your house, the granny flat rules usually apply.</p>",
            "cta": {"href": Q + "?permit=tiny-home", "text": "Get a tiny home quote"}},
        "pool1": {"q": "Will it hold water deeper than 300 mm?", "opts": [
            {"t": "Yes", "go": "r_pool"}, {"t": "No, 300 mm or less", "go": "r_pool_small"}]},
        "r_pool": {"result": True, "title": "You'll need a building permit and a compliant pool barrier",
            "body": "<p>In WA, any pool or spa that can hold more than 300 mm of water needs a building permit, and a safety barrier that meets AS 1926.1 before it is filled. This includes above-ground pools, plunge pools and inflatable pools.</p>",
            "cta": {"href": "https://poolcouncilapproval.com.au/", "text": "See our pool permit service"}},
        "r_pool_small": {"result": True, "title": "You probably don't need a pool permit",
            "body": "<p>Pools and spas that cannot hold more than 300 mm of water are not treated as swimming pools under WA's rules. Always supervise children around any water.</p>",
            "cta": {"href": Q + "?permit=pool", "text": "Ask us a question"}},
        "r_retro": {"result": True, "title": "You'll need retrospective approval",
            "body": "<p>In WA, work built without a permit is approved after the fact with a Building Approval Certificate. A registered building surveyor inspects it and issues a Certificate of Building Compliance first. Some structures also need planning approval.</p>",
            "cta": {"href": "/retrospective-approval", "text": "How retrospective approval works"}},
    },
}

FAMILY = [
    ("shed", "Sheds and garages", "Outbuildings, workshops and garages. Most need a permit once they are over 10 m²."),
    ("pergola", "Pergolas, patios and decks", "Attached patios, verandahs, roofed pergolas and raised decks."),
    ("carport", "Carports", "Including carports in the front setback, which often need planning approval too."),
    ("granny", "Granny flats", "Up to 70 m² can skip planning approval on most residential lots. A permit is still required."),
    ("tiny", "Tiny homes", "On wheels or on a slab. We work out which approval yours needs and apply for you."),
]


def site_cards():
    out = '<div class="grid g3">'
    for key, title, text in FAMILY:
        s = SITES[key]
        out += ('<a class="card site-card" href="https://%s/" style="--c:%s"><div class="sc-top"></div><div class="sc-body">'
                '<span class="domain">%s</span><h3>%s</h3><p>%s</p><span class="more">Visit site &rarr;</span></div></a>') % (
            s["domain"], s["accent"], s["domain"], title, text)
    out += ('<a class="card site-card" href="https://poolcouncilapproval.com.au/" style="--c:#c8a46a"><div class="sc-top"></div><div class="sc-body">'
            '<span class="domain">poolcouncilapproval.com.au</span><h3>Pools and spas</h3><p>Pool permits and barrier compliance, including above-ground and plunge pools.</p>'
            '<span class="more">Visit site &rarr;</span></div></a>')
    return out + "</div>"


HOME_FAQS = [
    ("What does GetMyPermit actually do?",
     "We prepare and lodge building permit and council approval applications for you. That means the site plan and drawings, the application forms, owner consent, any engineering or surveyor certificates the job needs, lodging with your council and answering their questions until the permit is issued."),
    ("How much does it cost?",
     "Our prices are on every page, and they include council fees. Sheds, patios and carports are $990, garages and decks $1,190, pools $1,500 and retaining walls $1,690. Granny flats start at $2,950 plus council fees. See <a href=\"/pricing\">all prices</a>."),
    ("How long does a building permit take in WA?",
     "Once an application is lodged, a council has up to 25 business days to decide a standard (uncertified) application, or 10 business days for a certified application that comes with a private building surveyor's certificate. Getting the plans and documents ready usually takes a few days to a week."),
    ("Do you cover my council?",
     "We work with councils across the Perth metro area and regional Western Australia. Each council has its own forms and local rules, and we check your project against them before lodging."),
    ("Can you help if I already built without a permit?",
     "Yes. Unapproved patios, sheds and carports are common, and they often surface when a house is sold. We arrange the inspection and certificate from a registered building surveyor and lodge a Building Approval Certificate application. See <a href=\"/retrospective-approval\">retrospective approval</a>."),
    ("What if council asks for changes, or says no?",
     "Answering council's questions is part of our price, and we keep going until your permit is issued. We check your project against the rules before lodging, so a refusal is rare. And if council does refuse and we can't get it approved, we refund everything you paid us, except council's own lodgement fee. See <a href=\"/how-it-works\">how it works</a>."),
    ("Are you building surveyors?",
     "No. We are a permit paperwork service. When a job needs a registered building surveyor, an engineer or a draftsperson, we bring them in and manage them for you, so you still deal with one contact."),
]


def home(S):
    body = b.hero(S, "Building permits &middot; Perth &amp; WA",
                  "Building permits and council approvals, handled for you.",
                  "Planning a shed, patio, carport, granny flat, tiny home or pool in Western Australia? We find out exactly what your council needs, prepare the plans and forms, and lodge the application for you.",
                  ["Fixed price up front", "Perth and regional WA", "We deal with council"],
                  "One contact, start to finish", "Plans, forms, lodgement and every council question.",
                  second='<a class="btn btn-line" href="/do-i-need-approval">Do I need approval?</a>',
                  alt="Backyard of a modern Perth home with a pergola, garden shed and granny flat")
    body += b.section(b.intro("Choose your project", "What are you building?",
                              "Each project type has its own site with plain-English guides to the WA rules. Whichever you pick, your quote comes through here.") + site_cards())
    body += b.section(
        '<div class="split"><div>' + b.intro("Quick answer", "Do I need a permit in WA?",
            "The short version for the most common projects. Your council can add local rules, so we always confirm before you build.") +
        '<p><a class="btn btn-ink" href="/do-i-need-approval">Use the 20-second checker <span class="arr">&rarr;</span></a></p></div>'
        '<div class="prose"><div class="table-wrap"><table>'
        '<thead><tr><th>Project</th><th>Building permit?</th></tr></thead><tbody>'
        '<tr><td>Freestanding shed up to 10 m&sup2; and 2.4 m tall</td><td>Usually not</td></tr>'
        '<tr><td>Bigger shed, or any garage</td><td>Yes</td></tr>'
        '<tr><td>Patio attached to the house</td><td>Yes</td></tr>'
        '<tr><td>Carport</td><td>Yes, and planning approval if it is in the front setback</td></tr>'
        '<tr><td>Granny flat up to 70 m&sup2;</td><td>Yes (planning approval usually not needed)</td></tr>'
        '<tr><td>Tiny home on wheels, longer than a few nights</td><td>Local government approval instead</td></tr>'
        '<tr><td>Pool or spa deeper than 300 mm</td><td>Yes, plus a compliant barrier</td></tr>'
        '</tbody></table></div></div></div>', "section white")
    body += b.section(b.intro("How it works", "Three steps. Two of them are ours.", "", center=True) + b.steps([
        ("Tell us about your project", "Pick your project type and answer a few questions. It takes about two minutes, and you can add photos or plans later."),
        ("Get a fixed price, then we prepare it", "We draw the site plan, complete the forms and bring in an engineer or building surveyor if your job needs one."),
        ("We lodge and follow up", "We lodge with your council, answer their questions and keep you posted until your permit is issued."),
    ]) + '<p class="center" style="margin-top:28px"><a href="/how-it-works">See every step, who does what and how long it takes &rarr;</a></p>')
    body += b.section(b.stats([
        ("25 days", "The most a council can take to decide a standard (uncertified) building permit, in business days"),
        ("10 days", "For a certified application that comes with a private building surveyor's certificate"),
        ("70 m&sup2;", "The size of granny flat that can skip planning approval on most residential lots"),
        ("$50,000", "The maximum fine in WA for building without a permit, for a first offence"),
    ]), "section tight")
    body += b.section(b.split("granny", "A new granny flat in a Perth backyard at dusk",
        b.intro("Why GetMyPermit", "Built for homeowners who would rather not learn council forms.") + b.checks([
            "<strong>Fixed price.</strong> You know the total before we start.",
            "<strong>Local rules checked first.</strong> Setbacks, heritage areas, bushfire areas and easements, before anything is lodged.",
            "<strong>One contact.</strong> Draftspeople, engineers and building surveyors are organised by us.",
            "<strong>Honest answers.</strong> If you don't need a permit, we tell you, and it costs nothing.",
        ])), "section white")
    body += b.section('<div class="narrow">' + b.intro("Questions", "Common questions") + b.faq_block(HOME_FAQS) + "</div>")
    body += b.band(S, S["band_title"], S["band_text"])
    return {"path": "index.html", "title": "Building Permits & Council Approvals in Perth, WA | GetMyPermit",
            "desc": "We prepare and lodge building permits and council approvals for sheds, patios, carports, granny flats, tiny homes and pools in Perth and WA. Fixed price, no runaround.",
            "h1": "Building permits and council approvals, handled for you.", "body": body, "faqs": HOME_FAQS}


TILES = [
    ("shed", "Shed or outbuilding", "Workshops, garden sheds, studios", "shed"),
    ("garage", "Garage", "Freestanding or attached", "garage"),
    ("carport", "Carport", "Including front-of-house", "carport"),
    ("pergola", "Pergola or patio", "Verandahs and alfresco roofs", "pergola"),
    ("deck", "Deck", "Raised or attached decks", "deck"),
    ("granny-flat", "Granny flat", "Ancillary dwelling", "granny"),
    ("tiny-home", "Tiny home", "On wheels or on a slab", "tiny"),
    ("pool", "Pool or spa", "In-ground, above-ground, plunge", "pool"),
    ("retaining-wall", "Retaining wall", "Walls holding back soil", "wall"),
    ("retrospective", "Already built", "Retrospective approval", "retro"),
    ("bal", "BAL assessment", "Bushfire area report", "flame"),
    ("partner", "Builder or supplier", "Partner enquiry", "builder"),
]


def quote(S):
    tiles = "".join(
        '<div class="tile"><input type="checkbox" id="p-%s" name="permit" value="%s" data-key="%s">'
        '<label for="p-%s"><span class="ti">%s</span><span><strong>%s</strong><small>%s</small></span></label></div>' % (
            k, t, k, k, icons.get(ic, 20), t, d + ' &middot; <b>%s</b>' % prices.TILE_PRICE[k]) for k, t, d, ic in TILES)
    body = """
<section class="page-hero"><div class="wrap narrow">
  <p class="eyebrow">Free &middot; Takes 2 minutes &middot; No obligation</p>
  <h1>Get your fixed price within one business day</h1>
  <p class="lead">Answer a few quick questions about your project. We look up your council's rules and reply with one total price, usually by the next business day. If you don't need a permit at all, we tell you that instead, free.</p>
</div></section>
<section class="section" style="padding-top:48px"><div class="wrap qwrap">
<div class="qside">
  <div class="promise"><h3>One price, no surprises</h3><p>Your price includes the drawings, the forms, lodging and, for most projects, the council fees. You know the total before we start.</p></div>
  <div class="promise"><h3>Approved, or your money back</h3><p>If council asks for changes, we handle them at no extra cost. If council refuses and we can't get it approved, we refund everything you paid us, except council's own lodgement fee.</p></div>
  <div class="promise"><h3>What happens after you press send</h3><p>We read your details, check your council's rules and reply with your price, usually within one business day. Nothing is booked and nothing is charged until you say yes.</p></div>
</div>
<form id="quote-form" action="https://formsubmit.co/%s" method="POST">
  <input type="hidden" name="_subject" value="New quote request">
  <input type="hidden" name="_next" value="https://getmypermit.com.au/thanks">
  <input type="hidden" name="_template" value="table">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="Permits" value="">
  <input type="hidden" name="source" value="">
  <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="panel">
    <h2>1. What do you need approved?</h2>
    <p class="sub">Choose one or more.</p>
    <div class="tiles">%s</div>
    <p class="err" role="alert">Please choose at least one project type.</p>
  </div>
  <div class="panel">
    <h2>2. About the project</h2>
    <p class="sub">Rough answers are fine. We will ask if we need more.</p>
    <div class="fields">
      <div class="field full"><label for="f-desc">What are you building?</label><textarea id="f-desc" name="Project details" placeholder="For example: a 6 m x 4 m Colorbond shed at the back of the yard, 1 m from the side fence."></textarea></div>
      <div class="field"><label for="f-size">Approximate size <span class="hint">(m&sup2; or length x width)</span></label><input id="f-size" name="Size"></div>
      <div class="field"><label for="f-start">When do you want to start?</label><select id="f-start" name="Start"><option>As soon as possible</option><option>In 1 to 3 months</option><option>In 3 to 6 months</option><option>Just researching</option><option>It is already built</option></select></div>
      <fieldset class="field full"><legend>Do you have a builder or supplier?</legend><div class="radios">
        <label><input type="radio" name="Builder" value="Yes"> Yes</label>
        <label><input type="radio" name="Builder" value="No, building it myself"> No, building it myself</label>
        <label><input type="radio" name="Builder" value="Not yet"> Not yet</label></div></fieldset>
    </div>
  </div>
  <div class="panel">
    <h2>3. Your details</h2>
    <p class="sub">We only use these to quote and to handle your application.</p>
    <div class="fields">
      <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
      <div class="field full"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="f-address">Street address of the property</label><input id="f-address" name="Street address" autocomplete="street-address"></div>
      <div class="field"><label for="f-suburb">Suburb or town</label><input id="f-suburb" name="suburb" required></div>
      <div class="field full"><label for="f-heard">How did you hear about us?</label><select id="f-heard" name="Heard about us"><option value="">Choose one</option><option>Google search</option><option>ChatGPT or another AI assistant</option><option>Google ad</option><option>Facebook or Instagram</option><option>My builder or supplier</option><option>Friend or family</option><option>Other</option></select></div>
    </div>
    <div class="form-foot">
      <p>Free and no obligation. We only use your details to quote, and we never sell them. Photos or plans help, so feel free to reply to our email with them.</p>
      <button class="btn btn-accent" type="submit">Get my fixed price <span class="arr">&rarr;</span></button>
    </div>
  </div>
</form>
<p class="center" style="margin-top:28px;color:var(--muted)">Prefer to talk? Call <a href="tel:%s">%s</a>.</p>
</div></section>""" % (QUOTE_EMAIL, tiles, PHONE_TEL, PHONE)
    return {"path": "quote.html", "title": "Get a Fixed-Price Building Permit Quote | GetMyPermit",
            "desc": "Tell us what you are building in Perth or WA and get a fixed-price quote for your building permit or council approval, usually within one business day.",
            "h1": "Get your fixed price within one business day", "crumb": "Get a quote", "body": body}


def thanks(S):
    body = """
<section class="page-hero" style="border:0;padding:96px 0"><div class="wrap narrow center">
  <p class="eyebrow">Request received</p>
  <h1>Thanks, we have your details.</h1>
  <p class="lead" style="margin:0 auto">We will look at your project and reply with a fixed price or a couple of quick questions, usually within one business day. Keep an eye on your inbox, and check your junk folder just in case.</p>
  <div class="cta-row" style="justify-content:center"><a class="btn btn-ink" href="/">Back to home</a><a class="btn btn-line" href="tel:%s">Call %s</a></div>
</div></section>""" % (PHONE_TEL, PHONE)
    return {"path": "thanks.html", "title": "Thanks | GetMyPermit", "desc": "Your quote request has been sent.",
            "h1": "Thanks", "body": body, "noindex": True}


CHECK_FAQS = [
    ("Is this checker the final word?",
     "No. It reflects the general WA rules in the Building Regulations 2012 and the R-Codes. Councils can add their own local planning rules, and things like heritage areas, bushfire areas, easements and boundary walls can change the answer. We confirm with your council before you build."),
    ("What is the difference between a building permit and planning approval?",
     "A building permit checks that the structure is safe and meets the building code. Planning approval (also called development approval) checks that it suits the site and the street, for example setbacks, height and heritage. Some projects need both, and planning approval usually comes first."),
    ("What if my project doesn't need a permit?",
     "Then you can go ahead, as long as you still follow the planning rules and build it properly. If we find you don't need a permit, we tell you, and there is no charge."),
    ("What happens if I build without a permit?",
     "Your council can issue a notice to fix or remove the work, and fines in WA can reach $50,000 for a first offence. Unapproved work also tends to come up when you sell. If it is already built, <a href=\"/retrospective-approval\">retrospective approval</a> is usually possible."),
]


def checker_page(S):
    body = """
<section class="page-hero"><div class="wrap narrow">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span>Do I need approval?</nav>
  <p class="eyebrow">Free checker</p>
  <h1>Do I need council approval?</h1>
  <div class="answer"><span class="label">Short answer</span><p>In Western Australia, most garages, carports, attached patios, decks, granny flats and pools need a building permit. Small freestanding sheds and patios (10 m&sup2; or less and no taller than 2.4 m) usually don't. Use the checker below for your project.</p></div>
  <p class="updated">Last updated %s</p>
</div></section>
<section class="section" style="padding-top:56px"><div class="wrap narrow">%s</div></section>
<section class="section white"><div class="wrap narrow prose">
  <h2>The WA rules at a glance</h2>
  <p>These are the general rules from the WA Building Regulations 2012 and the Residential Design Codes (R-Codes). Your council's local planning scheme can add to them.</p>
  <div class="table-wrap"><table>
    <thead><tr><th>Project</th><th>Building permit</th><th>Planning approval</th></tr></thead><tbody>
    <tr><td>Freestanding shed or patio, 10 m&sup2; or less and 2.4 m tall or less</td><td>Usually not needed</td><td>Only if local rules apply</td></tr>
    <tr><td>Shed over 10 m&sup2; or 2.4 m, or attached</td><td>Needed</td><td>Sometimes (boundary, heritage)</td></tr>
    <tr><td>Garage</td><td>Needed</td><td>Often, depending on setbacks</td></tr>
    <tr><td>Patio or roofed pergola attached to the house</td><td>Needed</td><td>Sometimes (boundary, heritage)</td></tr>
    <tr><td>Open pergola with no roof covering</td><td>Often not needed up to a set size</td><td>Only if local rules apply</td></tr>
    <tr><td>Deck</td><td>Usually needed</td><td>Sometimes (raised decks, privacy)</td></tr>
    <tr><td>Carport</td><td>Needed</td><td>Often, if in the front setback</td></tr>
    <tr><td>Granny flat up to 70 m&sup2; on a residential lot</td><td>Needed</td><td>Not needed if it meets the R-Codes</td></tr>
    <tr><td>Tiny home on wheels, more than a few nights</td><td>Not a building</td><td>Local government approval, up to 24 months</td></tr>
    <tr><td>Pool or spa holding more than 300 mm of water</td><td>Needed, plus a barrier</td><td>Rarely</td></tr>
  </tbody></table></div>
  <p class="note">Already built something without a permit? See <a href="/retrospective-approval">retrospective approval</a>.</p>
</div></section>
%s
%s""" % (b.UPDATED, b.checker(S, TREE, "Check your project"),
         b.section('<div class="narrow">' + b.intro("Questions", "Common questions") + b.faq_block(CHECK_FAQS) + "</div>", "section tight"),
         b.band(S, "Want a definite answer?", "Send us your project and address. We check it against your council's rules and tell you exactly what you need, with a fixed price if you need a permit."))
    return {"path": "do-i-need-approval.html", "title": "Do I Need Council Approval in WA? Free 20-Second Checker",
            "desc": "Check if your shed, patio, pergola, carport, deck, granny flat, tiny home or pool needs a building permit or council approval in Western Australia.",
            "h1": "Do I need council approval?", "crumb": "Do I need approval?", "body": body, "faqs": CHECK_FAQS}


RETRO_BODY = """
<h2>What is retrospective approval?</h2>
<p>Retrospective approval is how you get building work approved after it has been built. In Western Australia the document you end up with is a <strong>Building Approval Certificate</strong>. It confirms the structure meets the building standards, so it can stay.</p>
<p>It is common for patios, sheds, carports, decks, enclosed alfresco areas and pools that were built by a previous owner, or built without anyone realising a permit was needed.</p>

<h2>When do people need it?</h2>
<ul>
<li><strong>Selling a house.</strong> A buyer's building inspection or settlement agent spots a structure that isn't on council records.</li>
<li><strong>A council letter.</strong> The council has noticed the work, often from aerial photos or a neighbour's complaint.</li>
<li><strong>Insurance or finance.</strong> An insurer or lender asks whether the structure is approved.</li>
<li><strong>Peace of mind.</strong> You bought a house and want to know everything on it is legal.</li>
</ul>

<h2>How the process works in WA</h2>
<ol>
<li><strong>Check council records.</strong> We find out what your council already has on file for the property.</li>
<li><strong>Measure and draw.</strong> We prepare as-built plans of the structure and a site plan.</li>
<li><strong>Surveyor inspection.</strong> A registered building surveyor inspects the work and, if it meets the standards, issues a Certificate of Building Compliance (form BA18). Some councils require this to come from a private surveyor.</li>
<li><strong>Planning approval, if needed.</strong> If the structure breaks a planning rule, such as a front setback, retrospective planning approval comes first.</li>
<li><strong>Lodge the application.</strong> We lodge the Building Approval Certificate application (form BA13) with the certificate, plans and fees.</li>
<li><strong>Certificate issued.</strong> The council issues the Building Approval Certificate (form BA14).</li>
</ol>

<h2>What if the structure doesn't comply?</h2>
<p>Sometimes the surveyor finds something that needs fixing first, such as missing tie-downs, undersized footings or a pool barrier with gaps. In that case you get a list of what to change. Once it is fixed, the certificate can be issued. In a small number of cases, usually serious planning problems, a council can require the structure to be changed or removed.</p>

<h2>What does it cost?</h2>
<p>It starts with a $495 site check. We inspect the structure and tell you exactly what is needed, and the $495 comes off your approval price. Approvals start from $1,950 plus council fees, which include the building surveyor's certificate. Councils charge more for retrospective work than for a normal permit, and we show you their fee before you pay.</p>

<h2>Is it worth doing?</h2>
<p>Usually, yes. Building without a permit is an offence in WA, with fines of up to $50,000 for a first offence. Getting approval does not cancel that offence, but councils generally prefer owners who come forward to fix things. An approved structure is also much easier to sell, insure and finance.</p>
"""

RETRO_FAQS = [
    ("How long does retrospective approval take?",
     "Allow about four to eight weeks in total. Most of that is the surveyor's inspection and certificate and the council's assessment. If planning approval is needed too, add the time for that application."),
    ("Can I get retrospective approval for a pool?",
     "Yes. The pool and its barrier are inspected against the standards, and the barrier has to comply before the certificate is issued. Our sister site <a href=\"https://poolcouncilapproval.com.au/\">Pool Council Approval</a> covers pools in detail."),
    ("The previous owner built it. Is it still my problem?",
     "Unfortunately, yes. Approval stays with the property, so the current owner is the one who applies. It is still worth doing, because it makes the property easier to sell later."),
    ("Do I need to be home for the inspection?",
     "Someone needs to give the surveyor access to the structure. It usually takes under an hour."),
]


def retro(S):
    return {"path": "retrospective-approval.html", "kind": "article", "permit": "retrospective",
            "title": "Retrospective Building Approval in WA | Building Approval Certificate",
            "desc": "Built a patio, shed, carport or pool without a permit in WA? Here is how retrospective approval (a Building Approval Certificate) works, what it costs and how we handle it.",
            "eyebrow": "Retrospective approval", "h1": "Retrospective building approval in WA",
            "crumb": "Retrospective approval",
            "answer": "<p>If something was built without a permit in WA, you can usually get it approved afterwards with a <strong>Building Approval Certificate</strong>. A registered building surveyor inspects the work and certifies it first, then the application goes to your council. We organise the whole thing.</p>",
            "body": RETRO_BODY, "faqs": RETRO_FAQS,
            "related": [("/do-i-need-approval", "Do I need approval?"), ("https://shedbuildingpermit.com.au/retrospective-shed-approval", "Retrospective shed approval"),
                        ("https://carportpermit.com.au/retrospective-carport-approval", "Retrospective carport approval")],
            "band_title": "Selling soon? Let's get it approved.", "band_text": "Send us photos and the address. We tell you what is involved and give you a fixed price."}


BUILDER_FAQS = [
    ("Which businesses do you work with?",
     "Shed and garage suppliers, patio and pergola builders, carport companies, granny flat builders, tiny home makers and pool and plunge pool suppliers across Perth and WA."),
    ("Can you use our standard drawings and engineering?",
     "Yes. If you have standard plans or engineering certificates for your products, we use them on every job, which keeps each application quick and consistent."),
    ("Who does the customer deal with?",
     "Whatever suits you. We can deal with your customer directly and keep you updated, or work only through you."),
    ("How do you charge?",
     "Our public prices with 10 to 15% off for regular work, invoiced monthly. Sheds, patios and carports are normally $990, so partners pay from about $840 a job. See <a href=\"/pricing\">all prices</a>."),
]


def builders(S):
    body = b.hero(S, "For builders &amp; suppliers", "Sell and build. We'll handle council.",
                  "Council paperwork slows jobs down and ties up your office. Send your jobs to us and we prepare and lodge the applications for your customers, with updates at every step.",
                  ["Fixed price per job", "Your standard plans reused", "Updates to you and your customer"],
                  "Your jobs, approved", "We lodge and chase council for you.",
                  second='<a class="btn btn-line" href="tel:%s">Call %s</a>' % (PHONE_TEL, PHONE), img="shed",
                  alt="A new steel shed on a slab in a Perth backyard")
    body = body.replace(b.quote_link(S), "/quote?permit=partner", 1)
    body += b.section(b.intro("Who it's for", "Made for businesses that build things people need approved.") + b.cards([
        ("shed", "Shed and garage suppliers", "Kit sheds, workshops and garages, with your standard engineering.", None),
        ("pergola", "Patio and pergola builders", "Attached patios, verandahs, carports and decks.", None),
        ("granny", "Granny flat builders", "Ancillary dwellings, including the 70 m&sup2; planning exemption check.", None),
        ("tiny", "Tiny home makers", "Local government approvals for tiny homes on wheels, and permits for fixed homes.", None),
        ("pool", "Pool and plunge pool suppliers", "Pool permits and barrier compliance for your customers.", None),
        ("carport", "Carport companies", "Front-setback carports with planning approval and a building permit.", None),
    ]))
    body += b.section(b.intro("How it works", "A simple hand-off.", "", center=True) + b.steps([
        ("Send us the job", "Your customer's details, the site address and your product drawings. One email is enough."),
        ("We prepare and lodge", "Site plan, forms, owner consent, engineering and surveyor certificates where needed, then lodgement."),
        ("You get the permit", "We answer council's questions and send the permit to you and your customer the day it is issued."),
    ]), "section white")
    body += b.section('<div class="narrow">' + b.intro("Questions", "Common questions") + b.faq_block(BUILDER_FAQS) + "</div>")
    body += b.band(S, "Let's talk partner rates.", "Tell us what you sell and roughly how many jobs a month. We will come back with a per-job price.").replace(b.quote_link(S), "/quote?permit=partner")
    return {"path": "for-builders.html", "title": "Council Approvals for Builders & Suppliers in WA | GetMyPermit",
            "desc": "We prepare and lodge building permits for shed, patio, carport, granny flat, tiny home and pool businesses in Perth and WA. Fixed price per job.",
            "h1": "Sell and build. We'll handle council.", "crumb": "For builders", "body": body, "faqs": BUILDER_FAQS, "img": "shed"}


ABOUT_BODY = """
<h2>What we do</h2>
<p>GetMyPermit prepares and lodges building permit and council approval applications for people in Perth and Western Australia. Most of our work is for homeowners adding something to their property, and for the businesses that build those things: sheds, garages, carports, patios, pergolas, decks, granny flats, tiny homes and pools.</p>
<p>We started because the same question kept coming up from people buying backyard projects: "Do I need council approval, and how do I get it?" The rules are public, but they are spread across state regulations, the R-Codes and each council's own forms and policies. We put that work in one place.</p>

<h2>What we are, and what we are not</h2>
<p>We are a permit paperwork service. We prepare drawings and forms, check your project against your council's rules, lodge the application as your agent with your signed consent, and follow it through.</p>
<p>We are not a council and we are not building surveyors. When a job needs a registered building surveyor, a structural engineer or a draftsperson, we bring them in and manage them, so you still have one contact.</p>

<h2>How we work</h2>
<ul>
<li><strong>Fixed prices.</strong> You get the total before we start.</li>
<li><strong>Honest advice.</strong> If you don't need a permit, we say so.</li>
<li><strong>Checked sources.</strong> Our guides are based on the WA Building Regulations 2012, the Residential Design Codes and councils' published information, and we update them when the rules change.</li>
</ul>

<h2>Our sites</h2>
<p>Each project type has its own site with detailed guides:</p>
<ul>
<li><a href="https://shedbuildingpermit.com.au/">Shed Building Permit</a> for sheds and garages</li>
<li><a href="https://pergolabuildingpermit.com.au/">Pergola Building Permit</a> for pergolas, patios and decks</li>
<li><a href="https://carportpermit.com.au/">Carport Permit</a> for carports</li>
<li><a href="https://grannyflatpermit.com.au/">Granny Flat Permit</a> for granny flats</li>
<li><a href="https://tinyhomepermit.com.au/">Tiny Home Permit</a> for tiny homes</li>
<li><a href="https://poolcouncilapproval.com.au/">Pool Council Approval</a> for pools and spas</li>
</ul>
"""


def about(S):
    return {"path": "about.html", "kind": "article", "title": "About GetMyPermit | Building Permit Service in Perth, WA",
            "desc": "GetMyPermit is a Perth-based permit paperwork service. We prepare and lodge building permits and council approvals for homeowners and builders across WA.",
            "eyebrow": "About us", "h1": "About GetMyPermit", "crumb": "About",
            "answer": "<p>GetMyPermit is a Perth-based service that prepares and lodges building permit and council approval applications for homeowners and builders across Western Australia. We handle the plans, forms and council, and bring in surveyors and engineers when a job needs them.</p>",
            "body": ABOUT_BODY, "related": [("/do-i-need-approval", "Do I need approval?"), ("/for-builders", "For builders")]}


PRIVACY_BODY = """
<h2>What we collect</h2>
<p>When you ask for a quote we collect the details you enter: your name, phone, email, the property address and information about your project. If you email us photos or plans, we keep those too.</p>
<h2>How we use it</h2>
<p>We use your details to quote, to prepare and lodge your application, and to keep you updated. To do that we may share them with your council, and with a building surveyor, engineer or draftsperson working on your job. We do not sell your details.</p>
<h2>How the form works</h2>
<p>Our quote form is delivered to our inbox by FormSubmit, an email form service. Our websites are hosted on GitHub Pages and use Google Fonts.</p>
<h2>Your choices</h2>
<p>You can ask us what we hold about you, or ask us to delete it, by calling %s. Some records may need to be kept while an application is open.</p>
""" % PHONE


def privacy(S):
    return {"path": "privacy.html", "kind": "article", "title": "Privacy | GetMyPermit", "desc": "How GetMyPermit collects and uses your details.",
            "eyebrow": "Privacy", "h1": "Privacy", "crumb": "Privacy",
            "answer": "<p>We only collect what we need to quote and to handle your application, we only share it with the people working on your job, and we never sell it.</p>",
            "body": PRIVACY_BODY}


def notfound(S):
    body = """<section class="page-hero" style="border:0;padding:110px 0"><div class="wrap narrow center">
<p class="eyebrow">Page not found</p><h1>That page has moved or never existed.</h1>
<div class="cta-row" style="justify-content:center"><a class="btn btn-ink" href="/">Go to the home page</a><a class="btn btn-line" href="/quote">Get a quote</a></div>
</div></section>"""
    return {"path": "404.html", "title": "Page not found", "desc": "Page not found.", "h1": "Page not found", "body": body, "noindex": True}


PORTFOLIO = [
    ("gmp", "GetMyPermit", "Our main site. One place to get a fixed-price quote for any building permit or council approval in WA."),
    ("shed", "Shed Building Permit", "Permits for sheds, garages and workshops, plus free tools like the shed size checker."),
    ("pergola", "Pergola Building Permit", "Approvals for pergolas, patios, verandahs and decks, with real council costs."),
    ("carport", "Carport Permit", "Carport approvals, including carports in the front setback that need planning approval."),
    ("granny", "Granny Flat Permit", "Granny flat approvals in WA, including the 70 m² rule that skips planning approval."),
    ("tiny", "Tiny Home Permit", "Approvals for tiny homes on wheels and on footings, council by council."),
]

POOL_LOGO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0369a1"/>'
             '<path d="M8 40c6 0 6-4 12-4s6 4 12 4 6-4 12-4 6 4 12 4M8 50c6 0 6-4 12-4s6 4 12 4 6-4 12-4 6 4 12 4" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>'
             '<path d="M20 26l8 8 16-18" stroke="#7dd3fc" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def portfolio(S):
    cards = ""
    rows = [(SITES[k]["domain"], SITES[k]["accent"], icons.favicon(SITES[k]["accent"]), n, t) for k, n, t in PORTFOLIO]
    rows.append(("poolcouncilapproval.com.au", "#0369a1", POOL_LOGO, "Pool Council Approval",
                 "Pool and spa approvals, barrier checks and done-for-you plunge pool packages in Perth."))
    for domain, accent, logo, name, text in rows:
        cards += ('<a class="card site-card" href="https://%s/" style="--c:%s"><div class="sc-top"></div><div class="sc-body">'
                  '<div class="sc-logo">%s</div><h3>%s</h3><span class="domain">%s</span><p>%s</p>'
                  '<span class="more">Visit site &rarr;</span></div></a>') % (domain, accent, logo, name, domain, text)
    body = """
<section class="page-hero"><div class="wrap narrow">
  <p class="eyebrow">Our websites</p>
  <h1>All our sites</h1>
  <p class="lead">Each site covers one type of project in depth. They all lead to the same team and the same fixed-price quote.</p>
</div></section>
<section class="section" style="padding-top:48px"><div class="wrap"><div class="grid g3">%s</div></div></section>
""" % cards
    return {"path": "all.html", "title": "All Our Sites | GetMyPermit", "h1": "All our sites",
            "desc": "Every site in the GetMyPermit family: sheds, pergolas and patios, carports, granny flats, tiny homes and pools in WA.",
            "body": body}


def pages(S):
    return [home(S), quote(S), thanks(S), checker_page(S), retro(S), builders(S), about(S), privacy(S), portfolio(S), notfound(S),
            content_help.how_it_works(S), content_help.jargon(S)]
