BODY = """
<h2>The rule: total floor area, not number</h2>
<p>The R-Codes (the state's housing rules, Volume 1, April 2026) don't set a fixed number of sheds. Instead, clause 5.4.3 gives you two choices:</p>
<div class="table-wrap"><table>
<thead><tr><th>Option</th><th>Limits</th></tr></thead><tbody>
<tr><td>A. One small shed</td><td>Only <strong>one</strong> per lot, up to <strong>10 m²</strong>, wall height up to <strong>2.7 m</strong>, no more than two walls on the boundary</td></tr>
<tr><td>B. Large or several sheds</td><td>All sheds together up to <strong>60 m²</strong> or <strong>10%</strong> of the lot, whichever is less. Wall height up to <strong>2.4 m</strong>, ridge up to <strong>4.2 m</strong>, normal setbacks</td></tr>
</tbody></table></div>
<p>For both, sheds can't sit in the front or side street setback, and they can't eat into the open space and outdoor living area your lot needs. If you meet these limits, you usually don't need planning approval on a normal residential lot.</p>

<h2>Examples</h2>
<div class="table-wrap"><table>
<thead><tr><th>Lot size</th><th>Total shed area allowed (option B)</th></tr></thead><tbody>
<tr><td>400 m²</td><td>40 m²</td></tr>
<tr><td>500 m²</td><td>50 m²</td></tr>
<tr><td>600 m² or more</td><td>60 m²</td></tr>
</tbody></table></div>
<p>So on a 500 m² lot, you could have a 30 m² workshop and a 20 m² garden shed, but not a third 15 m² shed without planning approval. A small existing shed that meets option A doesn't need to meet the bigger-shed setbacks when you add more.</p>

<h2>Building permits</h2>
<p>Planning rules and building permits are separate. Every shed bigger than <strong>10 m²</strong> or taller than <strong>2.4 m</strong> usually needs a building permit, even if it's within the total area. Rural and special zones often allow much bigger sheds. Councils vary, so check yours.</p>
<p>Try the <a href="/shed-size-checker">shed size checker</a>, read about <a href="/garden-shed-approval">garden shed approval</a>, or see <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a>.</p>
"""

FAQS = [
    ("Is there a limit on how many sheds I can have in Perth?",
     "There's no set number. On residential lots, all sheds together can usually be up to 60 m² or 10% of the lot, whichever is less, without planning approval."),
    ("Can I have two small sheds without approval?",
     "Only one small shed (up to 10 m²) gets the relaxed small-shed rules. A second shed is counted under the 60 m² or 10% total limit."),
    ("Does a detached garage count towards my shed area?",
     "Yes, usually. The R-Codes define an outbuilding as an enclosed, non-habitable structure detached from the house, which can include a detached garage. An open carport isn't enclosed, so it's normally treated separately."),
    ("What if I want more shed space than allowed?",
     "You can apply for planning approval. The council will look at how the sheds affect the street and the neighbours."),
]


def page(S):
    return {"path": "how-many-sheds.html", "published": "2026-11-18", "type": "Question answer", "icon": "shed",
            "card": "How many sheds you can have on a Perth lot: the 60 m² or 10% total rule explained.",
            "title": "How Many Sheds Can I Have in Perth? (2026)",
            "desc": "How many sheds can you have on a Perth lot? The R-Codes limit total shed area to 60 m² or 10% of the lot, plus one small shed up to 10 m².",
            "eyebrow": "Question answer", "h1": "How many sheds can I have on my property?", "crumb": "How many sheds",
            "answer": "<p>There's no fixed number. On a normal residential lot, you can have <strong>one small shed</strong> up to 10 m², or several sheds that together are no more than <strong>60 m² or 10% of the lot</strong>, whichever is less. Go over that and you'll usually need planning approval. Most sheds over 10 m² also need a building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/garden-shed-approval", "Garden shed approval"), ("/how-close-can-a-shed-be-to-the-fence", "How close to the fence")],
            "sources": [("Residential Design Codes Volume 1 (April 2026), clause 5.4.3", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Outbuilding (shed), City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/outbuilding-(shed)"),
                        ("Building a shed or outbuilding, City of Melville", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-shed-or-outbuilding")]}
