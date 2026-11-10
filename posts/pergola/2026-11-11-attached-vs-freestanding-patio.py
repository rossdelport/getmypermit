BODY = """
<h2>Why attachment matters</h2>
<p>Whether your patio is fixed to the house is the biggest single thing that decides if it needs a building permit. The exemption for small structures only covers <strong>freestanding</strong> ones.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Attached patio</th><th>Freestanding patio</th></tr></thead><tbody>
<tr><td>Building permit</td><td><strong>Always</strong> needed (Wanneroo)</td><td>Not needed if 10 m² or less, 2.4 m high or less, and not in wind region C or D</td></tr>
<tr><td>Building code distance</td><td>Roof 900 mm from a side or rear boundary</td><td>900 mm from the boundary, or 900 mm from the house</td></tr>
<tr><td>Engineering</td><td>Includes how it connects to the house</td><td>Posts, footings and tie-downs</td></tr>
<tr><td>Planning approval</td><td>Same R-Codes rules for both: setbacks, open space and boundary walls</td><td>Same</td></tr>
</tbody></table></div>

<h2>The 10 m² exemption</h2>
<p>WA's building rules let you skip a permit for a small Class 10a structure only if it's freestanding, no more than <strong>10 m²</strong> in floor area, no more than <strong>2.4 m</strong> high, and not in wind region C or D. The City of Wanneroo applies it to patios and says <strong>every attached patio needs a building permit</strong>, whatever its size.</p>
<p>A typical backyard patio is bigger than 10 m², so it needs a permit either way. The exemption is mainly for small garden pergolas and gazebos. Wanneroo counts gazebos as patios too.</p>

<h2>Distances from the boundary and house</h2>
<p>The building code also sets fire separation distances. Wanneroo's sheet says the roof must be <strong>900 mm</strong> from a side or rear boundary, or 900 mm from the house if the patio is detached. The City of Cockburn says an attached patio must be 900 mm from a boundary, except one facing a road or public space. Joondalup's louvre roof guidance follows the same 900 mm rule.</p>
<p>Planning rules are separate. In Wanneroo, posts can sit on the boundary if the patio is no more than 10 m long and 2.7 m high, with the roof at least 500 mm back.</p>

<h2>Which should I choose?</h2>
<ul>
<li><strong>Attached</strong>: easier to keep dry between house and patio, but always needs a permit and connection details</li>
<li><strong>Freestanding</strong>: can avoid a permit if it's very small; a larger one still needs a permit</li>
</ul>
<p>Councils vary, so check yours. Try the <a href="/patio-approval-checker">patio approval checker</a>, read about <a href="/patio-on-boundary-wa">patios on the boundary</a>, or see <a href="/patio-plans-for-council">how to draw patio plans for council</a>.</p>
"""

FAQS = [
    ("Does an attached patio need a permit in WA?",
     "Yes. The City of Wanneroo says every attached patio needs a building permit, whatever its size, because the small-structure exemption only covers freestanding ones."),
    ("Does a freestanding patio need a permit?",
     "Not if it's 10 m² or less, no more than 2.4 m high, and not in wind region C or D. A freestanding patio bigger than that needs a permit."),
    ("How far must an attached patio be from the boundary?",
     "The building code generally needs the roof 900 mm from a side or rear boundary, as Wanneroo and Cockburn explain. Posts can be closer under the planning rules in some cases."),
    ("Is an attached patio harder to get approved?",
     "Not much. You need the same plans, plus details showing how it connects to the house."),
]


def page(S):
    return {"path": "attached-vs-freestanding-patio.html", "published": "2026-11-11", "type": "Comparison", "icon": "pergola",
            "card": "Why attaching a patio to the house always means a permit, and the distances that apply.",
            "title": "Attached vs Freestanding Patio: Permit Rules (WA)",
            "desc": "Attached or freestanding patio in WA: why attached patios always need a building permit, the 10 m² exemption, 900 mm distances and what councils ask for.",
            "eyebrow": "Comparison", "h1": "Attached vs freestanding patio", "crumb": "Attached vs freestanding patio",
            "answer": "<p>An <strong>attached</strong> patio always needs a building permit. A <strong>freestanding</strong> one can skip it only if it's 10 m² or less, no more than 2.4 m high, and not in wind region C or D. A typical backyard patio is bigger than that, so it needs a permit either way.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/patio-approval-checker", "Patio approval checker"), ("/patio-on-boundary-wa", "Patio on the boundary"), ("/patio-plans-for-council", "Patio plans for council")],
            "sources": [("Patios information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/357/patios_-_information_sheet.pdf"),
                        ("Pergolas, sheds, shade sails and water tanks (City of Cockburn)", "https://www.cockburn.wa.gov.au/Building-Planning-and-Roads/Applications-and-Permits/Pergolas-Sheds-Shade-Sails-and-Water-Tanks"),
                        ("Building a shed or outbuilding: Class 10a exemption (Town of Mosman Park)", "https://www.mosmanpark.wa.gov.au/build/building-or-renovating/building-a-shed-or-outbuilding/")]}
