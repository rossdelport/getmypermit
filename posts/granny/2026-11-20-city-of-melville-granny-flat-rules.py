BODY = """
<h2>When you don't need planning approval</h2>
<p>In a residential zone, the City of Melville says you usually don't need planning approval if:</p>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Limit</th></tr></thead><tbody>
<tr><td>Goes with</td><td>A single house on the same lot</td></tr>
<tr><td>Lot size</td><td>At least <strong>450 m²</strong></td></tr>
<tr><td>Size</td><td>Up to <strong>70 m²</strong> plot ratio area</td></tr>
<tr><td>Parking</td><td>One extra bay, unless within 800 m of a train station or 250 m of a high-frequency bus route</td></tr>
<tr><td>Design</td><td>Meets all the R-Codes and local planning policies</td></tr>
</tbody></table></div>
<p>Note the <strong>450 m²</strong> lot size: on a smaller lot, check with the City first. In any zone other than residential, you always need planning approval. Councils vary.</p>
<p>Granny flats are only allowed where the title has <strong>no common property</strong>, so green title or survey strata only. You can't subdivide it off, but you <strong>can rent it</strong> to anyone, not just family.</p>

<h2>Fees and timeframes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Cost or time</th></tr></thead><tbody>
<tr><td>Planning application (under $50,000)</td><td>$147</td></tr>
<tr><td>Planning decision</td><td>60 days, or 90 with consultation</td></tr>
<tr><td>Building permit (under $20,000)</td><td>$166.65</td></tr>
<tr><td>Building permit (over $20,000)</td><td>0.19% plus 0.137% Building Services Levy</td></tr>
<tr><td>Verge bond (over $20,000)</td><td>$1,900, plus $100 inspection fee</td></tr>
<tr><td>Construction Training Fund levy (over $20,000)</td><td>0.2%, paid directly to the Fund since 1 July 2026</td></tr>
<tr><td>Building permit decision</td><td>BA1 10 working days, BA2 25 working days</td></tr>
<tr><td>Written planning advice</td><td>$73</td></tr>
</tbody></table></div>
<p>If the City asks for more information on a building permit, you have <strong>21 days</strong> to provide it or it may be refused. Every granny flat needs a building permit before work starts.</p>
<p>Use the <a href="/granny-flat-size-calculator">granny flat size calculator</a>, read about the <a href="/granny-flat-minimum-lot-size">minimum lot size</a>, or see <a href="/rent-out-granny-flat-wa">renting out a granny flat</a>.</p>
"""

FAQS = [
    ("Do I need council approval for a granny flat in the City of Melville?",
     "You always need a building permit. You usually don't need planning approval in a residential zone if the lot is at least 450 m², the granny flat is up to 70 m², and you add a parking bay."),
    ("Can I rent out a granny flat in Melville?",
     "Yes. The City says it can be rented to people who aren't related to the people in the main house. It can't be subdivided off."),
    ("How much is a building permit for a granny flat in Melville?",
     "$166.65 under $20,000. Over that, 0.19% of the contract price plus the 0.137% Building Services Levy, plus a $1,900 verge bond and $100 inspection fee."),
    ("Can I build a granny flat on a strata lot in Melville?",
     "Only if the title has no common property, such as survey strata without common property."),
]


def page(S):
    return {"path": "city-of-melville-granny-flat-rules.html", "published": "2026-11-20", "type": "Council guide", "icon": "pin",
            "card": "City of Melville granny flat rules: the 450 m² lot rule, 70 m² size, parking, fees and timeframes.",
            "title": "City of Melville Granny Flat Rules (2026)",
            "desc": "City of Melville granny flat rules: no planning approval on 450 m²+ residential lots up to 70 m², parking, strata limits, renting, and building permit fees and timeframes.",
            "eyebrow": "Council guide", "h1": "City of Melville granny flat rules", "crumb": "City of Melville granny flat rules",
            "answer": "<p>In Melville, a granny flat usually needs no planning approval in a residential zone if the lot is at least <strong>450 m²</strong>, it's up to <strong>70 m²</strong>, and there's an extra parking bay (unless you're near high-frequency transport). It always needs a <strong>building permit</strong>. You can rent it out, but not subdivide it.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-size-calculator", "Granny flat size calculator"), ("/granny-flat-minimum-lot-size", "Granny flat minimum lot size"), ("/rent-out-granny-flat-wa", "Renting out a granny flat")],
            "sources": [("Building a Granny Flat or Ancillary Dwelling, City of Melville", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-granny-flat-or-ancillary-dwelling")]}
