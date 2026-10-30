"""pergolabuildingpermit.com.au: pergolas, patios, verandahs and decks in WA."""
import build as b
from content_shed import notfound

QL = "https://getmypermit.com.au/quote?permit=%s&from=pergolabuildingpermit.com.au"

TREE = {
    "start": "p1", "depth": 4,
    "nodes": {
        "p1": {"q": "Will it be attached to the house?", "help": "Fixed to the wall, fascia or roof of the house counts as attached.", "opts": [
            {"t": "Yes, attached", "go": "p_near"}, {"t": "No, freestanding", "go": "p2"}]},
        "p2": {"q": "Will it have a roof covering?", "help": "Roof sheets, polycarbonate and opening louvres all count. Open beams don't.", "opts": [
            {"t": "Yes", "go": "p3"}, {"t": "No, open beams only", "go": "r_open"}]},
        "p3": {"q": "Is it 10 m² or less, and 2.4 m tall or less?", "opts": [
            {"t": "Yes", "go": "r_small"}, {"t": "No, bigger or taller", "go": "p_near"}]},
        "p_near": {"q": "Will it be within 1 m of a side or rear boundary, or in a heritage area?", "opts": [
            {"t": "No", "go": "r_permit"}, {"t": "Yes", "go": "r_both"}, {"t": "Not sure", "go": "r_permit"}]},
        "r_open": {"result": True, "title": "You might not need a building permit",
            "body": "<p>Freestanding pergolas with open beams and no roof covering are often exempt up to a set size, but the limit varies by council (some use 20 m² and 2.4 m tall). If you plan to add a roof later, get the permit now.</p>",
            "cta": {"href": QL % "pergola", "text": "Ask us to check your council"}},
        "r_small": {"result": True, "title": "You probably don't need a building permit",
            "body": "<p>A small freestanding roofed pergola or patio, 10 m² or less and no taller than 2.4 m, is usually exempt in WA. It still has to meet the planning rules, such as boundary setbacks.</p>",
            "cta": {"href": QL % "pergola", "text": "Ask us to double-check"}},
        "r_permit": {"result": True, "title": "You'll need a building permit",
            "body": "<p>Patios and roofed pergolas attached to the house, or bigger than 10 m², need a building permit. We prepare the site plan and forms, attach the engineering and lodge it with your council.</p>",
            "cta": {"href": QL % "pergola", "text": "Get a fixed-price quote"}},
        "r_both": {"result": True, "title": "You'll need a building permit, and maybe planning approval",
            "body": "<p>Close to a boundary or in a heritage area, a patio can also need planning approval, which comes before the building permit. Your neighbour may be asked for comments. We work out what your council needs and handle both.</p>",
            "cta": {"href": QL % "pergola", "text": "Get a fixed-price quote"}},
    },
}

HOME_FAQS = [
    ("What is the difference between a pergola and a patio?",
     "In everyday talk a pergola has open beams and a patio has a solid roof. Councils care about the roof, not the name. Once a pergola has roof sheets, polycarbonate or opening louvres, it is treated like a patio."),
    ("Does a louvred roof pergola need a permit?",
     "Usually, yes. Opening louvres are a roof covering, so a louvred pergola attached to the house, or bigger than 10 m&sup2;, needs a building permit. Louvre suppliers normally provide engineering for the permit."),
    ("Do I need engineering for a patio?",
     "Yes. The permit needs proof the frame, footings and tie-downs suit the wind rating at your address. Patio kit suppliers usually provide certified engineering. For a custom timber pergola, an engineer may need to design it."),
    ("Can I build a patio on the boundary?",
     "Often, yes, within limits. A patio post or roof close to a boundary has to meet setback and fire-separation rules. If it doesn't meet the R-Codes' standard rules, it needs planning approval first."),
    ("Does a shade sail need a permit?",
     "Small shade sails are often exempt, but larger sails, sails attached to the house and sails with tall posts may need a permit. Councils vary, so check before you install one."),
    ("How long does a pergola permit take?",
     "Allow a few days to prepare the application. Once lodged, council has up to 25 business days for a standard application, or 10 business days with a private building surveyor's certificate."),
]


def home(S):
    body = b.hero(S, "Pergola &amp; patio permits &middot; Perth &amp; WA",
                  "Pergola building permits in Perth, done for you.",
                  "Most pergolas and patios attached to the house need a building permit in Western Australia. We check your council's rules, prepare the plans and forms, and lodge the application, so your builder can start on time.",
                  ["Fixed price up front", "Engineering sorted", "Every Perth council"],
                  "Plans, forms and lodgement", "One contact until your permit is issued.",
                  alt="A timber and black steel pergola over a hardwood deck with outdoor dining")
    body += b.answer_check(S, "Do I need one?", "Do I need a permit for my pergola?",
        "<p>In WA you need a building permit for a pergola or patio that has a <strong>roof covering</strong> and is either <strong>attached to the house</strong> or <strong>bigger than 10 m&sup2;</strong> (or taller than 2.4 m). Open-beam pergolas are often exempt up to a size your council sets.</p>",
        ["Louvred roofs count as a roof covering.", "Most decks need a building permit too.",
         "Close to a boundary or in a heritage area, planning approval can be needed first."],
        TREE)
    body += b.section(b.intro("At a glance", "Pergola, patio and deck rules in WA",
        "Councils add local rules, but this is where most projects land.") +
        '<div class="prose"><div class="table-wrap"><table><thead><tr><th>Structure</th><th>Building permit</th><th>Notes</th></tr></thead><tbody>'
        '<tr><td>Open-beam pergola, freestanding</td><td>Often not, up to a size limit</td><td>Limit varies by council</td></tr>'
        '<tr><td>Roofed pergola or patio, freestanding, 10 m&sup2; or less and 2.4 m tall or less</td><td>Usually not</td><td>Planning rules still apply</td></tr>'
        '<tr><td>Patio or roofed pergola attached to the house</td><td>Yes</td><td>Engineering needed</td></tr>'
        '<tr><td>Louvred roof pergola</td><td>Usually yes</td><td>Louvres count as a roof</td></tr>'
        '<tr><td>Verandah</td><td>Yes</td><td>Treated like an attached patio</td></tr>'
        '<tr><td>Deck</td><td>Usually yes</td><td>Raised and attached decks especially</td></tr>'
        '<tr><td>Enclosing a patio with walls</td><td>Yes</td><td>May become a room, with more rules</td></tr>'
        '</tbody></table></div></div>')
    body += b.section(b.intro("How it works", "From sketch to approved", "", center=True) + b.steps([
        ("Send us the basics", "Your address, the size, and your builder's or supplier's quote or drawings if you have them."),
        ("We prepare everything", "Site plan, elevations, engineering and forms, checked against your council's setback rules."),
        ("We lodge and follow up", "We lodge, answer council's questions and send you the permit when it is issued."),
    ]), "section white")
    body += b.section(b.split("pergola", "An alfresco pergola with outdoor dining at a Perth home",
        b.intro("What we handle", "Everything between your design and your builder.") + b.checks([
            "<strong>Site plan</strong> showing the structure, the house and every boundary distance.",
            "<strong>Elevations</strong> with heights, from your supplier's drawings.",
            "<strong>Engineering</strong> from your supplier, or from an engineer we arrange.",
            "<strong>Forms and owner consent</strong>, ready to sign.",
            "<strong>Lodgement and follow-up</strong> until the permit is issued.",
        ])))
    body += b.section(b.intro("Guides", "Pergola, patio and deck guides") + b.guides([
        ("/do-i-need-council-approval-for-a-pergola", "Do I need approval for a pergola?", "Attached, freestanding, roofed or open: when a pergola needs a permit.", "question"),
        ("/patio-building-permit", "Patio building permits", "Attached patios, verandahs and enclosed patios, explained.", "pergola"),
        ("/deck-building-permit", "Deck building permits", "Why most decks need a permit, and what raised decks add.", "deck"),
    ]), "section white")
    body += b.section('<div class="narrow">' + b.intro("Questions", "Common questions") + b.faq_block(HOME_FAQS) + "</div>")
    body += b.band(S, S["band_title"], S["band_text"])
    return {"path": "index.html", "title": "Pergola Building Permit Perth & WA | Done For You, Fixed Price",
            "desc": "Need a pergola or patio building permit in Perth or WA? We check your council's rules, prepare the plans and engineering, and lodge it for you. Fixed price.",
            "h1": "Pergola building permits in Perth, done for you.", "body": body, "faqs": HOME_FAQS}


NEED_BODY = """
<h2>Two questions decide it</h2>
<p>For a pergola in WA, the answer comes down to two things: <strong>does it have a roof covering</strong>, and <strong>is it attached to the house</strong>?</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Open beams</th><th>Roof covering</th></tr></thead><tbody>
<tr><td><strong>Freestanding</strong></td><td>Often exempt up to a size your council sets</td><td>Exempt if 10 m&sup2; or less and 2.4 m tall or less, otherwise a permit</td></tr>
<tr><td><strong>Attached to the house</strong></td><td>Check with council</td><td>Building permit needed</td></tr>
</tbody></table></div>

<h2>What counts as a roof covering?</h2>
<p>Metal roof sheets, polycarbonate, glass, shade cloth fixed as a roof, and opening or adjustable louvres all count. A pergola with only open timber or steel beams does not. If you plan to add a roof later, the pergola will need a permit then, so it is easier to get it at the start.</p>

<h2>Why "attached" matters</h2>
<p>A pergola fixed to the house puts load on the house's walls or roof. The permit checks that the connection, the posts and the footings can take it, including wind uplift. That is why attached patios need a permit at any size.</p>

<h2>Planning rules still apply</h2>
<p>Even when no building permit is needed, a pergola has to follow the planning rules:</p>
<ul>
<li><strong>Front setback.</strong> Pergolas and patios in front of the house usually need planning approval.</li>
<li><strong>Boundaries.</strong> Structures close to a side or rear boundary have setback and fire-separation rules.</li>
<li><strong>Heritage areas and estates</strong> may have their own design rules.</li>
<li><strong>Bushfire-prone areas</strong> can add construction requirements for structures near the house.</li>
</ul>
"""

NEED_FAQS = [
    ("Do I need council approval for a freestanding pergola?",
     "If it has open beams only, often not, up to a size limit your council sets. If it has a roof covering, it is exempt when it is 10 m&sup2; or less and no taller than 2.4 m. Bigger roofed pergolas need a permit."),
    ("Is a pergola with shade cloth exempt?",
     "Shade cloth fixed as a permanent roof is usually treated as a roof covering. Removable shade cloth or a small shade sail is often treated differently. Ask your council or us before you build."),
    ("What happens if I build a pergola without approval?",
     "Your council can issue a notice to fix or remove it, and fines in WA can reach $50,000 for a first offence. It can also hold up a sale. If it is already built, retrospective approval is usually possible."),
]


def need(S):
    return {"path": "do-i-need-council-approval-for-a-pergola.html", "kind": "article",
            "title": "Do I Need Council Approval for a Pergola in WA?",
            "desc": "When a pergola needs a building permit in WA: roofed or open, attached or freestanding, plus the 10 m² rule and the planning rules that still apply.",
            "eyebrow": "Do I need one?", "h1": "Do I need council approval for a pergola in WA?", "crumb": "Do I need approval for a pergola?",
            "answer": "<p>If your pergola has a <strong>roof covering</strong> and is <strong>attached to the house</strong>, yes, it needs a building permit. Freestanding roofed pergolas are exempt only if they are 10 m&sup2; or less and 2.4 m tall or less. Open-beam pergolas are often exempt up to a size your council sets.</p>",
            "body": NEED_BODY, "faqs": NEED_FAQS,
            "related": [("/", "Pergola building permits"), ("/patio-building-permit", "Patio building permits"), ("/deck-building-permit", "Deck building permits")]}


PATIO_BODY = """
<h2>Attached patios need a permit</h2>
<p>A patio is a roofed structure, usually open on at least two sides, used as an outdoor living area. When it is attached to the house, it needs a building permit in WA whatever its size. A freestanding patio only avoids a permit if it is 10 m&sup2; or less and 2.4 m tall or less.</p>

<h2>Verandahs and alfresco roofs</h2>
<p>A verandah is a roofed area along the side of the house, and it is treated much like an attached patio: it needs a building permit. Extending the main roof of the house over an alfresco area is building work to the house itself, and also needs a permit.</p>

<h2>Enclosing a patio</h2>
<p>Adding walls, windows or doors to a patio changes what it is. Depending on how enclosed it is, it can become a sunroom or a habitable room, which has extra rules for insulation, light, ventilation and energy efficiency. It needs a building permit, and sometimes planning approval. Talk to us before you enclose an approved patio, because the original permit won't cover it.</p>

<h2>What a patio permit application includes</h2>
<ul>
<li>Site plan showing the patio, the house and the distance to each boundary</li>
<li>Elevations showing heights and the roof pitch</li>
<li>Engineering for the frame, footings and connection to the house</li>
<li>The application form, owner consent and fees</li>
</ul>

<h2>Patios near the boundary</h2>
<p>The R-Codes allow patios fairly close to side and rear boundaries, but there are limits, and posts or roofs very close to the boundary can trigger fire-separation rules. If your patio doesn't meet the standard rules, it needs planning approval, and your neighbour may be asked for comments.</p>
"""

PATIO_FAQS = [
    ("Does a patio kit come with engineering?",
     "Most reputable patio suppliers in Perth provide engineering certification for their kits. We use it in your application. If yours doesn't, we can arrange an engineer."),
    ("Can my patio builder lodge the permit?",
     "Some do. Many leave it to the homeowner, or charge extra. We can handle it for you or work alongside your builder."),
    ("How much does a patio permit cost?",
     "Our price is $990 in total for a patio or pergola, and $1,190 for a deck, with council fees included. Custom engineering is $450 extra, only if your kit doesn't come with it. See <a href=\"/pricing\">our prices</a>."),
]


def patio(S):
    return {"path": "patio-building-permit.html", "kind": "article",
            "title": "Patio Building Permit in WA | Attached Patios & Verandahs",
            "desc": "Attached patios and verandahs need a building permit in WA. What's needed, the boundary rules, enclosing a patio, and how we prepare and lodge it for you.",
            "eyebrow": "Patios", "h1": "Patio building permits in WA", "crumb": "Patio building permit",
            "answer": "<p>Yes, a patio attached to the house needs a building permit in WA, at any size. A freestanding patio is exempt only if it is <strong>10 m&sup2; or less and 2.4 m tall or less</strong>. Patios close to a boundary can also need planning approval.</p>",
            "body": PATIO_BODY, "faqs": PATIO_FAQS,
            "related": [("/do-i-need-council-approval-for-a-pergola", "Do I need approval for a pergola?"), ("/deck-building-permit", "Deck building permits"), ("https://carportpermit.com.au/", "Carport permits")]}


DECK_BODY = """
<h2>Most decks need a building permit</h2>
<p>In WA most decks need a building permit, especially decks that are raised off the ground or attached to the house. The permit checks the footings, the frame, the connection to the house and, for higher decks, the balustrade.</p>
<p>Some councils treat a small, freestanding deck sitting almost on the ground differently. Because the answer varies, we confirm it with your council before you build.</p>

<h2>Raised decks</h2>
<p>A deck high enough that someone could fall from it needs a balustrade that meets the building code. Raised decks can also need planning approval, because they can look into a neighbour's yard or windows. The R-Codes have <strong>visual privacy</strong> setbacks for raised outdoor areas, and a deck that doesn't meet them may need screening or approval.</p>

<h2>Decks with a roof</h2>
<p>If the deck has a pergola or patio roof over it, the roof is assessed as a patio or pergola as well. We cover both in one application.</p>

<h2>Decks around pools</h2>
<p>A deck next to a pool can affect the pool barrier, for example by creating a place for a child to climb over the fence. The barrier rules apply on top of the deck permit. See our sister site <a href="https://poolcouncilapproval.com.au/">Pool Council Approval</a>.</p>

<h2>What we prepare</h2>
<ul>
<li>Site plan with the deck, house and boundary distances</li>
<li>Deck plan and elevations showing heights, joists, bearers and footings</li>
<li>Balustrade details for raised decks</li>
<li>Engineering if the deck needs it, forms, consent and lodgement</li>
</ul>
"""

DECK_FAQS = [
    ("Do I need a permit for a low deck in WA?",
     "Sometimes not, but it depends on your council and the design. A small freestanding deck close to the ground is the most likely to be exempt. Attached or raised decks need a permit."),
    ("How high can a deck be without a balustrade?",
     "The building code requires a balustrade where there is a fall of more than 1 m. Many people add one on lower decks too, for safety."),
    ("Does a deck need planning approval?",
     "A raised deck may, if it doesn't meet the R-Codes' visual privacy setbacks from the boundary, or if it is in the front setback or a heritage area."),
]


def deck(S):
    return {"path": "deck-building-permit.html", "kind": "article", "permit": "deck",
            "title": "Deck Building Permit in WA | Raised & Attached Decks",
            "desc": "Most decks in WA need a building permit, especially raised and attached decks. Privacy rules, balustrades, decks near pools, and how we handle the application.",
            "eyebrow": "Decks", "h1": "Deck building permits in WA", "crumb": "Deck building permit",
            "answer": "<p>Most decks in WA need a building permit, especially <strong>raised decks</strong> and decks <strong>attached to the house</strong>. Raised decks can also need planning approval because of privacy rules. A few councils treat very low freestanding decks as exempt, so we check yours first.</p>",
            "body": DECK_BODY, "faqs": DECK_FAQS,
            "related": [("/patio-building-permit", "Patio building permits"), ("/do-i-need-council-approval-for-a-pergola", "Do I need approval for a pergola?"), ("https://poolcouncilapproval.com.au/", "Pool permits")]}


def pages(S):
    return [home(S), need(S), patio(S), deck(S), notfound(S)]
