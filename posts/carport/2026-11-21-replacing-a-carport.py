BODY = """
<h2>Taking the old one down</h2>
<div class="table-wrap"><table>
<thead><tr><th>Old carport</th><th>Demolition permit?</th></tr></thead><tbody>
<tr><td>Freestanding, under 40 m², no asbestos, not brick, not heritage</td><td>Usually <strong>no</strong></td></tr>
<tr><td>Attached to the house, brick, heritage-listed, or has asbestos</td><td>Usually <strong>yes</strong></td></tr>
</tbody></table></div>
<p>That's how the Town of Cottesloe sets it out; councils vary. Old carport roofs can contain <strong>asbestos</strong>. Take care and follow Department of Health and WorkSafe guidance before you touch it.</p>

<h2>Putting the new one up</h2>
<p>A new carport is new building work, even in the same spot. It usually needs a <strong>building permit</strong> unless it's freestanding, no more than <strong>10 m²</strong> and <strong>2.4 m</strong> high.</p>
<p>It's assessed under <strong>today's</strong> rules, not the rules when the old one was built. If the old carport was never approved, the new one doesn't get any credit for it. The R-Codes rules that most often matter:</p>
<ul>
<li><strong>Front setback:</strong> a carport can usually sit at half the normal street setback if it's no wider than 60% of the frontage, keeps a clear view of the house, and matches the house's roof, colours and materials.</li>
<li><strong>Boundary:</strong> posts can usually go on the side boundary if the carport is no more than 10 m long and 2.7 m high, behind the street setback, with the roof and gutters at least 450 mm off the boundary.</li>
</ul>
<p>If it breaks one of these, you'll usually need planning approval first.</p>

<h2>Just replacing the roof sheets?</h2>
<p>Building and Energy says changing a roof cover to a material of a different weight or shape will likely need a building permit, and the roof must be tied down properly. Some councils, such as Cottesloe, list even like-for-like re-roofing as needing a permit. Ask your council first.</p>
<p>Since 1 July 2026, a carport job under <strong>$50,000</strong> doesn't need a registered builder.</p>
<p>Read <a href="/carport-council-approval">when a carport needs council approval</a>, the <a href="/carport-in-front-setback">front setback rules</a>, or <a href="/retrospective-carport-approval">approval for an existing carport</a>.</p>
"""

FAQS = [
    ("Do I need a permit to replace my carport in WA?",
     "Usually yes. A new carport is new building work and needs a building permit unless it's freestanding, 10 m² or less and 2.4 m or less high."),
    ("Do I need a permit to demolish an old carport?",
     "Usually not if it's freestanding, under 40 m², not brick, not heritage-listed and has no asbestos. Otherwise you usually do."),
    ("Can I rebuild my carport in the same spot?",
     "Only if the new one meets today's setback and boundary rules, or you get planning approval."),
    ("Does re-roofing a carport need approval?",
     "It can. Changing to a different roof material will likely need a building permit, and some councils need one even for like-for-like sheets."),
]


def page(S):
    return {"path": "replacing-a-carport.html", "published": "2026-11-21", "type": "Question answer", "icon": "carport",
            "card": "Replacing an old carport in WA: demolition, the new permit and today's setback rules.",
            "title": "Do I Need Approval to Replace a Carport? (WA)",
            "desc": "Replacing an old carport in WA: when demolition needs a permit, why the new carport needs a building permit, today's setback rules, asbestos and re-roofing.",
            "eyebrow": "Question answer", "h1": "Do I need approval to replace an old carport?", "crumb": "Replacing a carport",
            "answer": "<p>Usually <strong>yes</strong>. The new carport is new building work, so it needs a <strong>building permit</strong> and must meet <strong>today's</strong> setback rules. Taking down a small freestanding carport usually needs no permit, unless it's over 40 m², brick, heritage-listed or has <strong>asbestos</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-council-approval", "Carport council approval"), ("/carport-in-front-setback", "Carport in the front setback"), ("/retrospective-carport-approval", "Retrospective carport approval")],
            "sources": [("Do I need a building permit?, Town of Cottesloe", "https://www.cottesloe.wa.gov.au/Profiles/cottesloe/Assets/ClientData/Do-I-need-a-Building-Permit.pdf"),
                        ("Changing your roof cover? fact sheet, Building and Energy", "https://www.wa.gov.au/system/files/2024-10/changing_your_roof_cover_factsheet.pdf"),
                        ("Residential Design Codes Volume 1, WAPC", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf")]}
