import build as b

Q = "/quote"

TREE = {
    "start": "p1", "depth": 4,
    "nodes": {
        "p1": {"q": "Is the patio attached to your house?", "help": "Attached means fixed to the house wall, fascia or roof.", "opts": [
            {"t": "Yes, it's attached", "go": "p4"},
            {"t": "No, it stands on its own", "go": "p2"}]},
        "p2": {"q": "What kind of roof will it have?", "opts": [
            {"t": "A solid roof (metal, polycarbonate or similar)", "go": "p3"},
            {"t": "No roof, open slats or a shade sail", "go": "p3o"}]},
        "p3": {"q": "Is it 10 m² or less, and 2.4 m high or less?", "help": "10 m² is about 3.2 m x 3.2 m.", "opts": [
            {"t": "Yes, both", "go": "r_exempt"},
            {"t": "No, it's bigger or taller", "go": "p4"}]},
        "p3o": {"q": "Is it 20 m² or less, and 2.4 m high or less?", "opts": [
            {"t": "Yes, both", "go": "r_exempt_open"},
            {"t": "No, it's bigger or taller", "go": "p4"}]},
        "p4": {"q": "Will it be in the front yard, on a heritage property, or closer than 1 m to a side or back fence?", "help": "If you're not sure, choose 'Not sure'.", "opts": [
            {"t": "No, none of those", "go": "r_permit"},
            {"t": "Yes, one or more", "go": "r_permit_da"},
            {"t": "Not sure", "go": "r_permit_check"}]},
        "r_exempt": {"result": True, "title": "You probably don't need a building permit",
            "body": "<p>A freestanding patio of <strong>10 m² or less</strong> and no taller than <strong>2.4 m</strong> is exempt from a building permit under the WA Building Regulations. It still has to be built properly and meet the planning rules, such as setbacks. Planning approval can still be needed in the front yard or on a heritage property.</p>",
            "cta": {"href": Q, "text": "Ask us to double-check"}},
        "r_exempt_open": {"result": True, "title": "You probably don't need a building permit",
            "body": "<p>An open pergola or shade sail of <strong>20 m² or less</strong> and no taller than <strong>2.4 m</strong>, built with a house, is exempt from a building permit. Add a solid roof and the limit drops to 10 m². Planning rules still apply.</p>",
            "cta": {"href": Q, "text": "Ask us to double-check"}},
        "r_permit": {"result": True, "title": "You need a building permit",
            "body": "<p>Your patio needs a <strong>building permit</strong>, but probably not planning approval, as long as it meets the standard planning rules for your lot. Council fees are usually about $183 in total for a typical patio.</p>",
            "cta": {"href": Q, "text": "Get a fixed-price quote"}},
        "r_permit_da": {"result": True, "title": "Building permit, and likely planning approval",
            "body": "<p>Your patio needs a <strong>building permit</strong>. Because of where it sits, it will likely need <strong>planning (development) approval</strong> first too. Planning adds a $147 fee for work up to $50,000, and council has up to 60 days to decide. Some councils allow patio posts on the boundary in set cases, so it's worth checking.</p>",
            "cta": {"href": Q, "text": "Get a fixed-price quote"}},
        "r_permit_check": {"result": True, "title": "You need a building permit; planning depends on where it goes",
            "body": "<p>Your patio needs a <strong>building permit</strong>. Whether it also needs planning approval depends on your lot's R-Code, the setbacks and heritage listing. Send us your address and a rough sketch and we'll tell you.</p>",
            "cta": {"href": Q, "text": "Send us your details"}},
    },
}

BODY = """
{CHECKER}
<h2>How the checker decides</h2>
<p>A building permit and planning approval are two separate things. The checker works through both.</p>
<div class="table-wrap"><table>
<thead><tr><th>Your patio</th><th>Building permit?</th></tr></thead><tbody>
<tr><td>Attached to the house</td><td><strong>Yes</strong>, any size</td></tr>
<tr><td>Freestanding, solid roof, 10 m&sup2; or less and 2.4 m or lower</td><td>No</td></tr>
<tr><td>Open pergola or shade sail with a house, 20 m&sup2; or less and 2.4 m or lower</td><td>No</td></tr>
<tr><td>Anything bigger or taller</td><td><strong>Yes</strong></td></tr>
</tbody></table></div>
<p>These exemptions come from the WA Building Regulations, so they are the same at every council. They don't apply in the cyclone wind regions in the north of the state.</p>

<h2>Planning approval</h2>
<p>Most backyard patios don't need planning approval if they meet the standard rules (the "deemed-to-comply" rules in the R-Codes). The usual reasons a patio needs it are:</p>
<ul>
<li>It sits in the <strong>front setback</strong> (the front yard).</li>
<li>The property is <strong>heritage-listed</strong> or in a heritage area.</li>
<li>It is <strong>too close to a side or back boundary</strong>. The City of Wanneroo, for example, wants patios 1 m back, but allows posts on the boundary if the patio is no longer than 10 m and no higher than 2.7 m, with the roof 500 mm back.</li>
</ul>
<p>Rules differ a little between councils, so treat the checker as a guide.</p>

<h2>Exempt doesn't mean anything goes</h2>
<p>An exempt patio still has to be built to the building code and meet the planning rules. If you later enclose it, it stops being a patio altogether. <a href="/enclose-a-patio-approval">See the rules for enclosing a patio</a>.</p>
"""

FAQS = [
    ("What size patio can I build without council approval in WA?",
     "A freestanding patio with a solid roof of 10 m&sup2; or less and no taller than 2.4 m doesn't need a building permit. An open pergola or shade sail can be up to 20 m&sup2;. A patio attached to the house needs a permit at any size."),
    ("Do all attached patios need a building permit?",
     "Yes. The size exemption only covers freestanding structures, so a patio fixed to the house needs a building permit."),
    ("Does a patio need planning approval?",
     "Usually not, if it meets the standard planning rules. It's likely to need it in the front setback, on a heritage property, or too close to a boundary."),
    ("Is this checker the final word?",
     "No. It follows the state rules, but councils apply some planning rules differently. Ask us or your council to confirm before you build."),
]


def page(S):
    return {"path": "patio-approval-checker.html", "published": "2026-10-31", "type": "Free tool", "icon": "check",
            "card": "Three quick questions to see whether your patio needs a building permit, planning approval, or neither.",
            "title": "Patio Approval Checker: Do I Need a Permit for My Patio? (WA)",
            "desc": "Free patio approval checker for WA. Answer three questions to see if your patio needs a building permit, planning approval or neither, with the size limits explained.",
            "eyebrow": "Free tool", "h1": "Patio approval checker", "crumb": "Patio approval checker",
            "answer": "<p>A patio <strong>attached to the house always needs a building permit</strong>. A freestanding one with a solid roof is exempt up to <strong>10 m&sup2; and 2.4 m high</strong> (20 m&sup2; for an open pergola or shade sail). Planning approval is only likely in the front yard, on heritage properties or close to a boundary. Use the checker below for your patio.</p>",
            "body": BODY.replace("{CHECKER}", b.checker(S, TREE, "Patio approval checker", "Up to four quick questions. Takes about 20 seconds.")),
            "faqs": FAQS,
            "related": [("/patio-building-permit", "Patio building permits"), ("/patio-approval-cost-perth", "Patio approval cost in Perth"), ("/enclose-a-patio-approval", "Enclosing a patio")],
            "sources": [("Do I need a permit? Exempt structures (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit"),
                        ("Patios information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Building a shed or outbuilding: wind regions C and D (City of Melville)", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding"),
                        ("Planning fees 2026-27 (City of Subiaco)", "https://www.subiaco.wa.gov.au/media/kuyntemn/planning-services-fee-schedule-2026-2027.pdf")]}
