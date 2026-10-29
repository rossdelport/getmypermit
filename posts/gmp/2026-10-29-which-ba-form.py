import build as b

Q = "/quote"

TREE = {
    "start": "f1", "depth": 3,
    "nodes": {
        "f1": {"q": "What do you need to do?", "opts": [
            {"t": "Build something new, or add on", "go": "f2"},
            {"t": "Get something already built approved", "go": "f4"},
            {"t": "Knock something down", "go": "r_ba5"},
            {"t": "The work is finished", "go": "r_ba7"},
            {"t": "Something else", "go": "f5"}]},
        "f2": {"q": "Has a private building surveyor already checked the plans and signed a certificate of design compliance (BA3)?",
               "help": "If you are not sure, the answer is probably no.", "opts": [
            {"t": "Yes", "go": "r_ba1"}, {"t": "No", "go": "f3"}]},
        "f3": {"q": "What are you building?", "opts": [
            {"t": "A house, granny flat, shed, patio, carport, deck, pool or fence", "go": "r_ba2"},
            {"t": "Units, a shop, an office or anything commercial", "go": "r_ba1_need"}]},
        "f4": {"q": "What kind of building is it?", "opts": [
            {"t": "A house, granny flat, shed, patio, carport, deck, pool or fence", "go": "r_ba13"},
            {"t": "Units, a shop, an office or anything commercial", "go": "r_ba9"}]},
        "f5": {"q": "Which of these fits best?", "opts": [
            {"t": "The work will affect my neighbour's land", "go": "r_ba20"},
            {"t": "My permit is about to run out", "go": "r_ba22"},
            {"t": "I'm changing builder or permit details", "go": "r_ba19"},
            {"t": "Work is stopping before it's finished", "go": "r_ba8"}]},
        "r_ba1": {"result": True, "title": "You need a BA1",
            "body": "<p>A <strong>BA1 (certified application)</strong> goes to your council with the surveyor's BA3 certificate and the plans it covers. Because the technical check is already done, council has 10 business days to decide. Fee: 0.19% of the value of the work for a house or outbuilding, at least $121.</p>",
            "cta": {"href": Q, "text": "Get us to prepare and lodge it"}},
        "r_ba2": {"result": True, "title": "You can use a BA2",
            "body": "<p>A <strong>BA2 (uncertified application)</strong> is the usual form for homeowners. Council does the technical check itself and has up to 25 business days to decide. It is only allowed for houses and Class 10 structures like sheds, patios, carports and pools. Fee: 0.32% of the value of the work, at least $121.</p>",
            "cta": {"href": Q, "text": "Get us to prepare and lodge it"}},
        "r_ba1_need": {"result": True, "title": "You need a BA1, with a BA3 first",
            "body": "<p>The uncertified BA2 is only for houses and Class 10 structures. For anything else, a private building surveyor checks the plans and signs a <strong>BA3 certificate of design compliance</strong>, then you lodge a <strong>BA1</strong> with council.</p>",
            "cta": {"href": Q, "text": "Ask us to organise it"}},
        "r_ba13": {"result": True, "title": "You need a BA13",
            "body": "<p>A <strong>BA13</strong> applies for a building approval certificate for work done without a permit. It goes in with a <strong>BA18 certificate of building compliance</strong> from a registered building surveyor, who inspects what was built. Fee: 0.38% of the value of the unauthorised work, at least $121.</p>",
            "cta": {"href": "/retrospective-approval", "text": "How retrospective approval works"}},
        "r_ba9": {"result": True, "title": "You need a BA9",
            "body": "<p>For commercial buildings and units, unauthorised work is fixed with an <strong>occupancy permit application (BA9)</strong>. A registered building surveyor needs to inspect and certify the work first.</p>",
            "cta": {"href": Q, "text": "Ask us about your building"}},
        "r_ba5": {"result": True, "title": "You need a BA5",
            "body": "<p>A <strong>BA5</strong> applies for a demolition permit. For a house, shed, carport or other Class 1 or 10 building the fee is $121. Small structures that don't need a building permit to put up usually don't need a demolition permit either. Asbestos removal has its own rules.</p>",
            "cta": {"href": Q, "text": "Ask us to check"}},
        "r_ba7": {"result": True, "title": "You need a BA7",
            "body": "<p>A <strong>BA7 notice of completion</strong> tells council the permitted work is finished. The builder named on the permit (or the owner-builder) lodges it within 7 days of finishing. There is no fee.</p>",
            "cta": {"href": Q, "text": "Ask us a question"}},
        "r_ba20": {"result": True, "title": "You need a BA20 or BA20A",
            "body": "<p>Use a <strong>BA20</strong> to ask your neighbour's consent when work will encroach on or affect their land, such as footings or a wall close to the boundary. Use a <strong>BA20A</strong> for protection structures, party walls, removing a dividing fence or getting access to their land. It goes to the neighbour before you apply for the permit.</p>",
            "cta": {"href": Q, "text": "Get help with your neighbour notice"}},
        "r_ba22": {"result": True, "title": "You need a BA22",
            "body": "<p>A <strong>BA22</strong> asks council for more time on a building or demolition permit. Lodge it before the permit expires. Fee: $121.</p>",
            "cta": {"href": Q, "text": "Ask us a question"}},
        "r_ba19": {"result": True, "title": "You need a BA19",
            "body": "<p>A <strong>BA19</strong> asks council to change the details on a building permit, such as the builder. Changes to the approved plans themselves usually need a new or amended application, so check with council first.</p>",
            "cta": {"href": Q, "text": "Ask us a question"}},
        "r_ba8": {"result": True, "title": "You need a BA8",
            "body": "<p>A <strong>BA8 notice of cessation</strong> tells council the builder has stopped work before it was finished, for example when a builder leaves a job. It records what was and wasn't done.</p>",
            "cta": {"href": Q, "text": "Ask us a question"}},
    },
}

BODY = """
{CHECKER}
<p>WA uses numbered forms for every step of a building job. The finder above picks the right one in a few clicks. The table below lists the forms homeowners and small builders actually use, with the 2026-27 fees. These fees are set by the state, so they are the same at every council.</p>
<h2>All the common WA building forms</h2>
<div class="table-wrap"><table>
<thead><tr><th>Form</th><th>What it's for</th><th>Fee from 1 July 2026</th></tr></thead><tbody>
<tr><td>BA1</td><td>Building permit, certified (a private surveyor has already checked the plans)</td><td>0.19% of the value for a house or outbuilding, at least $121</td></tr>
<tr><td>BA2</td><td>Building permit, uncertified (council checks the plans). Houses and Class 10 structures only</td><td>0.32% of the value, at least $121</td></tr>
<tr><td>BA3</td><td>Certificate of design compliance, signed by a private building surveyor</td><td>The surveyor's own fee</td></tr>
<tr><td>BA5</td><td>Demolition permit</td><td>$121 for a house or outbuilding</td></tr>
<tr><td>BA7</td><td>Notice of completion, within 7 days of finishing</td><td>No fee</td></tr>
<tr><td>BA8</td><td>Notice of cessation, when work stops before it is finished</td><td>No fee</td></tr>
<tr><td>BA9</td><td>Occupancy permit (Class 2 to 9 buildings, such as units, shops and offices)</td><td>$121, or 0.18% for unauthorised work</td></tr>
<tr><td>BA13</td><td>Building approval certificate, mostly for work done without a permit</td><td>0.38% of the value of the unauthorised work, at least $121</td></tr>
<tr><td>BA18</td><td>Certificate of building compliance, signed by a registered building surveyor</td><td>The surveyor's own fee</td></tr>
<tr><td>BA19</td><td>Change the builder or other details on a building permit</td><td>Check with council</td></tr>
<tr><td>BA20 / BA20A</td><td>Neighbour notice and consent: encroaching, party walls, removing a dividing fence, access</td><td>No council fee</td></tr>
<tr><td>BA22</td><td>More time on a building or demolition permit</td><td>$121</td></tr>
</tbody></table></div>
<p>On top of the permit fee, the state's <strong>Building Services Levy</strong> is $61.65 for work up to $45,000 (0.137% above that). The Construction Training Fund levy only applies to work over $100,000 that starts on or after 1 July 2026.</p>

<h2>BA1 or BA2: which is better?</h2>
<p>Most homeowners use a <strong>BA2</strong>. You lodge your plans and council does the technical check. It costs less up front, but council can take up to 25 business days and may ask questions along the way.</p>
<p>A <strong>BA1</strong> is quicker at council (10 business days) because a private building surveyor has already checked everything and signed the BA3. You pay the surveyor as well, so it suits bigger jobs or tight deadlines. For units, shops and other commercial buildings, BA1 is the only option.</p>

<h2>Forms you might hear about that are gone</h2>
<p>BA11, BA12, BA15 and BA16 were discontinued on 1 May 2020. If a council checklist still mentions them, it is out of date. Always download forms from your council or the state's Building and Energy website so you have the current version.</p>
"""

FAQS = [
    ("What is the difference between a BA1 and a BA2?",
     "A BA1 is a certified application: a private building surveyor has already checked the plans and signed a BA3 certificate, so council has 10 business days to decide. A BA2 is uncertified: council checks the plans itself and has up to 25 business days. BA2 is only allowed for houses and Class 10 structures."),
    ("Who lodges the BA7?",
     "The builder named on the building permit, or the owner-builder, lodges the BA7 notice of completion within 7 days of finishing the work."),
    ("Do I need a form for a small shed or patio?",
     "Not if it is exempt. A freestanding shed or patio of 10 m&sup2; or less and no taller than 2.4 m usually doesn't need a building permit, so there is no form to lodge. Planning rules can still apply."),
    ("Can I fill in the forms myself?",
     "Yes. Owners can lodge their own BA2. Most people get stuck on the site plan, the drawings and council's follow-up questions, which is the part we do for a fixed price."),
]


def page(S):
    p = {"path": "which-ba-form.html", "published": "2026-10-29", "type": "Free tool", "icon": "doc",
         "card": "Answer two quick questions and see which WA building form you need, with the 2026-27 fee.",
         "title": "Which BA Form Do I Need? Free WA Building Form Finder (2026)",
         "desc": "BA1, BA2, BA7, BA13 or BA20? Answer two quick questions and see which WA building form you need, what it is for and the 2026-27 fee.",
         "eyebrow": "Free tool", "h1": "Which BA form do I need?", "crumb": "Which BA form do I need?",
         "answer": "<p>To build, most homeowners lodge a <strong>BA2</strong> (council checks the plans) or a <strong>BA1</strong> (a private surveyor has already checked them). Use a <strong>BA5</strong> to demolish, a <strong>BA7</strong> when the work is finished, and a <strong>BA13</strong> to approve something built without a permit. The finder below tells you which one fits your job.</p>",
         "body": BODY.replace("{CHECKER}", b.checker(S, TREE, "WA building form finder", "Two quick questions. Takes about 15 seconds.")),
         "faqs": FAQS, "permit": "",
         "related": [("/do-i-need-approval", "Do I need council approval?"), ("/retrospective-approval", "Retrospective approval"), ("/for-builders", "For builders and suppliers")],
         "sources": [("Building Regulations 2012 fees from 1 July 2026 (City of Fremantle)", "https://www.fremantle.wa.gov.au/wp-content/uploads/2025/04/2026-Fees-and-charges-Building-Regulations-2012.pdf"),
                     ("Building approvals and the Building Services Levy (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals"),
                     ("Industry Bulletin 114: approved building forms (Building and Energy)", "https://www.wa.gov.au/system/files/2024-10/ib_114_updated_building_commissioner_approved_forms_issued_for_use_under_the_building_act_2011.pdf"),
                     ("Construction Training Fund levy", "https://ctf.wa.gov.au/levy")]}
    return p
