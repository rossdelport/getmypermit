BODY = """
<h2>Building permit: always</h2>
<p>The Town of Bassendean says anyone building a new granny flat (ancillary accommodation), or adding to or altering one, needs a <strong>building permit before work starts</strong>. That includes changes to the floor, walls or roof, and turning a room from habitable to non-habitable (or the other way), or a wet area into a dry one. See <a href="/granny-flat-building-permit">granny flat building permits</a>.</p>
<p>Non-structural fit-out, such as tiling, cabinets, new light or tap fittings, rendering and painting, doesn't need a permit. It still has to meet the building standards.</p>

<h2>Planning approval</h2>
<p>Under WA's planning rules, a granny flat of up to <strong>70 m²</strong> that meets the R-Codes deemed-to-comply rules usually doesn't need planning approval. The Town says other approvals, such as planning, septic or Heritage Council approval, may be needed <strong>before</strong> the building permit, so check these first. See <a href="/granny-flat-no-planning-approval">granny flats without planning approval</a>.</p>

<h2>BA1 or BA2?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Form</th><th>Who issues the design certificate</th><th>Town's time limit</th></tr></thead><tbody>
<tr><td>BA1 (certified)</td><td>An independent building surveying contractor</td><td>10 business days</td></tr>
<tr><td>BA2 (uncertified)</td><td>The Town</td><td>25 business days</td></tr>
</tbody></table></div>
<p>The Town says most applications get a response sooner.</p>

<h2>What to send</h2>
<ul>
<li>The completed application form and fees.</li>
<li>An owner-builder certificate, or the builder's home indemnity insurance certificate, if the work is over $20,000.</li>
<li>Plans, such as site, floor, elevation and section drawings, plus structural details, energy efficiency details, termite treatment and a BAL assessment if needed.</li>
<li>Neighbour consent forms (BA20 or BA20A) if you'll remove a shared fence, go onto their land, encroach, or dig near the boundary.</li>
<li>A Construction Training Fund levy receipt, if your job needs one.</li>
</ul>
<p>The Town prefers applications by email to mail@bassendean.wa.gov.au. If the job needs a new crossover, use of the verge or a drainage connection, lodge the Town's infrastructure permit form too. Check your size with the <a href="/granny-flat-size-calculator">granny flat size calculator</a>.</p>
"""

FAQS = [
    ("Do I need a building permit for a granny flat in Bassendean?",
     "Yes. The Town of Bassendean says a building permit is needed before building or altering a granny flat."),
    ("Do I need planning approval for a granny flat in Bassendean?",
     "Usually not if it's up to 70 m² and meets the R-Codes deemed-to-comply rules, but heritage, septic or other approvals may be needed first."),
    ("How long does Bassendean take to issue a building permit?",
     "Up to 10 business days for a certified (BA1) application and 25 for an uncertified (BA2) one. The Town says most are faster."),
    ("When do I need my neighbour's consent in Bassendean?",
     "If the work removes a shared fence, needs access to their land, encroaches onto it, or could undermine it. Use the BA20 or BA20A forms."),
]


def page(S):
    return {"path": "town-of-bassendean-granny-flat-rules.html", "published": "2026-11-28", "type": "Council guide", "icon": "pin",
            "card": "Town of Bassendean granny flat rules: building permits, planning, BA1 vs BA2 times and neighbour consent.",
            "title": "Town of Bassendean Granny Flat Rules (2026)",
            "desc": "Town of Bassendean granny flat rules: when you need a building permit, the 70 m² planning exemption, BA1 and BA2 timeframes, owner-builder and insurance rules, neighbour consent and what to send.",
            "eyebrow": "Council guide", "h1": "Town of Bassendean granny flat rules", "crumb": "Bassendean granny flats",
            "answer": "<p>In the Town of Bassendean, every new granny flat needs a <strong>building permit</strong> before work starts. Planning approval usually isn't needed if it's up to <strong>70 m²</strong> and meets the R-Codes. The Town decides certified applications within <strong>10 business days</strong> and uncertified ones within <strong>25</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-building-permit", "Granny flat building permit"), ("/granny-flat-no-planning-approval", "Granny flat without planning approval"), ("/granny-flat-size-calculator", "Granny flat size calculator")],
            "sources": [("Building or altering a dwelling or ancillary accommodation: information sheet, Town of Bassendean", "https://www.bassendean.wa.gov.au/Profiles/bassendean/Assets/ClientData/Document-Centre/Building_Services/Information_Sheets/Building_or_Altering_a_Dwelling_or_Ancillary_Accomodation_.pdf"),
                        ("Ancillary dwelling (granny flat) information sheet, Department of Planning WA", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf?sfvrsn=31c1ea2d_4")]}
