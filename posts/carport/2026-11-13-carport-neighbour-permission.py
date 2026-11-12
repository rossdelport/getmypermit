BODY = """
<h2>The short answer</h2>
<p>For a carport that meets the rules, you usually <strong>don't</strong> need your neighbour's permission. You need a <strong>building permit</strong> from the council, and planning approval only if the carport doesn't meet the R-Codes or council policy.</p>

<h2>When the neighbour gets involved</h2>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>What happens</th></tr></thead><tbody>
<tr><td>Carport meets the rules</td><td>No neighbour consent needed</td></tr>
<tr><td>Carport breaks a rule, such as a setback</td><td>Planning approval needed; the council may ask for neighbour comments</td></tr>
<tr><td>Work will go onto, or adversely affect, the neighbour's land</td><td>The building permit form asks for the neighbour's consent (form BA20) or a court order</td></tr>
</tbody></table></div>

<h2>Posts on the boundary</h2>
<p>Under the R-Codes (for most houses), a carport's posts can go <strong>right on the boundary</strong> without planning approval if the carport is no more than <strong>10 m long</strong> and <strong>2.7 m high</strong>, sits behind the front setback, and the roof edge is at least <strong>450 mm</strong> from the boundary. The building code may still need fire separation, so check your design.</p>
<p>Even when the rules allow it, building on the boundary often means working from the neighbour's side, for example to fix posts or gutters. If any work or footings will cross onto their land, that's when form BA20 applies.</p>

<h2>Neighbour comments on a planning application</h2>
<p>If your carport needs planning approval because it varies the rules, councils often consult neighbours. The City of Swan's checklist, for example, includes an R-Codes variation form with neighbour comments. Getting your neighbour's signature early can make this easier. Councils vary, so check yours.</p>

<h2>Strata properties</h2>
<p>If you live in a strata complex, you may also need approval from the strata company, separate from the council. See <a href="/strata-carport-approval">strata carport approval</a>.</p>
<p>Read <a href="/carport-on-boundary">building a carport on the boundary</a>, or <a href="/city-of-melville-carport-rules">City of Melville carport rules</a>.</p>
"""

FAQS = [
    ("Do I need my neighbour's permission to build a carport?",
     "Usually not, if the carport meets the rules. You need a building permit from the council, not the neighbour's consent."),
    ("Can I build a carport on the boundary without asking my neighbour?",
     "Under the R-Codes, posts can go on the boundary if the carport is no more than 10 m long and 2.7 m high, behind the front setback, with the roof 450 mm back. If work goes onto their land, you need their consent (BA20) or a court order."),
    ("What is form BA20?",
     "It's the form used when building work will encroach on or adversely affect neighbouring land. The BA1 and BA2 forms ask about it."),
    ("Will the council ask my neighbour?",
     "Only if the carport needs planning approval for a variation. Councils often consult affected neighbours then."),
]


def page(S):
    return {"path": "carport-neighbour-permission.html", "published": "2026-11-13", "type": "Question", "icon": "handshake",
            "card": "When a carport needs your neighbour's sign-off, and when it doesn't.",
            "title": "Do I Need My Neighbour's Permission for a Carport? (WA)",
            "desc": "Do you need your neighbour's permission for a carport in WA? Usually not if it meets the rules. When neighbour comments or form BA20 come in.",
            "eyebrow": "Question", "h1": "Do I need my neighbour's permission for a carport?",
            "crumb": "Neighbour permission",
            "answer": "<p><strong>Usually not.</strong> A carport that meets the rules needs a council building permit, not your neighbour's consent. Neighbours get involved if the carport needs <strong>planning approval</strong> for a variation (the council may consult them), or if work will go <strong>onto their land</strong> (form BA20).</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-on-boundary", "Carport on the boundary"), ("/strata-carport-approval", "Strata carport approval"), ("/city-of-melville-carport-rules", "City of Melville carport rules")],
            "sources": [("R-Codes Volume 1, April 2026 (WA Government)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Form BA1 application for building permit, certified (WA Government)", "https://www.wa.gov.au/media/54115/download?inline"),
                        ("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf")]}
