BODY = """
<h2>The small shed exemption</h2>
<p>Many Perth councils say a garden shed doesn't need a building permit if it is:</p>
<ul>
<li><strong>Freestanding</strong> (not attached to the house or another building)</li>
<li><strong>10 m² or less</strong> in floor area</li>
<li><strong>2.4 m or less</strong> in height</li>
</ul>
<p>The City of Joondalup adds that it must be installed to the manufacturer's instructions. The City of Melville adds that it must not be in wind region C or D. Gosnells, Kwinana, Bayswater and Mundaring publish the same 10 m² and 2.4 m limits. Councils vary, so check yours.</p>
<p>A 3 x 3 m shed is 9 m², so it usually fits. A 3 x 3.5 m shed is 10.5 m², so it usually doesn't.</p>

<h2>Planning rules still apply</h2>
<p>No building permit doesn't mean anything goes. The City of Joondalup says a small shed of 10 m² or less only skips planning approval if:</p>
<ul>
<li>No more than <strong>two walls</strong> are within 600 mm of a boundary</li>
<li>It's <strong>not in the street setback</strong> (in front of the house)</li>
<li>Walls and ridge are no higher than <strong>2.7 m</strong></li>
<li>You keep enough <strong>open space</strong> and <strong>outdoor living area</strong></li>
</ul>

<h2>When you do need approval</h2>
<div class="table-wrap"><table>
<thead><tr><th>Your shed</th><th>Usually needs</th></tr></thead><tbody>
<tr><td>Over 10 m² or over 2.4 m high</td><td>Building permit</td></tr>
<tr><td>Attached to the house or a patio</td><td>Building permit</td></tr>
<tr><td>In front of the house</td><td>Planning approval as well</td></tr>
<tr><td>Bigger than 60 m² or 10% of the lot (Joondalup)</td><td>Planning approval as well</td></tr>
<tr><td>Second-hand shed</td><td>Engineer sign-off (Serpentine-Jarrahdale) if a permit is needed</td></tr>
</tbody></table></div>

<h2>Bigger sheds in Joondalup</h2>
<p>For larger sheds, Joondalup's deemed-to-comply limits are: no more than <strong>60 m² or 10% of the site</strong> (whichever is less), walls up to <strong>2.4 m</strong>, ridge up to <strong>4.2 m</strong>, and set back <strong>1 m</strong> from side and rear boundaries (1.5 m if the wall is longer than 14 m).</p>
<p>Check yours with the <a href="/shed-size-checker">shed size checker</a>, or read <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a> and <a href="/city-of-wanneroo-shed-rules">City of Wanneroo shed rules</a>.</p>
"""

FAQS = [
    ("Do I need council approval for a garden shed in Perth?",
     "Usually not a building permit if it's freestanding, 10 m² or less and 2.4 m or less high. Planning rules like setbacks still apply, and councils vary."),
    ("Is a 3 x 3 m shed exempt?",
     "Usually yes. It's 9 m², under the 10 m² limit, as long as it's freestanding and no higher than 2.4 m."),
    ("Can I put a garden shed against the fence?",
     "Joondalup allows a small shed with up to two walls within 600 mm of a boundary without planning approval. Councils vary."),
    ("Can I put a garden shed in my front yard?",
     "Usually not without planning approval. Joondalup says a small shed in the street setback needs it."),
]


def page(S):
    return {"path": "garden-shed-approval.html", "published": "2026-11-12", "type": "Question", "icon": "shed",
            "card": "When a small garden shed needs no permit, and the planning rules that still apply.",
            "title": "Do I Need Council Approval for a Garden Shed? (Perth, WA)",
            "desc": "Do you need council approval for a garden shed in Perth? Usually not if it's freestanding, 10 m² or less and 2.4 m high. The planning rules that still apply.",
            "eyebrow": "Question", "h1": "Do I need council approval for a garden shed?",
            "crumb": "Garden shed approval",
            "answer": "<p>Usually <strong>no building permit</strong> if the shed is <strong>freestanding</strong>, <strong>10 m² or less</strong> and <strong>2.4 m or less</strong> high. Councils such as Joondalup, Melville, Gosnells and Bayswater publish this. You still need to follow planning rules, like keeping it out of the front setback.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/city-of-wanneroo-shed-rules", "City of Wanneroo shed rules")],
            "sources": [("Outbuilding (shed), City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/outbuilding-(shed)"),
                        ("Outbuildings fact sheet (WA Government)", "https://www.wa.gov.au/system/files/2021-06/FS-outbuildings.pdf"),
                        ("Sheds, garages and workshops, Shire of Serpentine-Jarrahdale", "https://www.sjshire.wa.gov.au/planning-building-and-roads/building/building-advice/sheds-garages-and-workshops.aspx")]}
