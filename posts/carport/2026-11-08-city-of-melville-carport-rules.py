BODY = """
<h2>Carport or garage?</h2>
<p>The City of Melville uses the R-Codes definitions. A <strong>carport</strong> is a roofed structure for vehicles that stays unenclosed, though it can have a see-through door. Add a <strong>solid door</strong> and it becomes a <strong>garage</strong>, which has stricter setback rules. See <a href="/enclose-a-carport">enclosing a carport</a>.</p>

<h2>When you don't need planning approval</h2>
<p>In a residential zone, a carport usually doesn't need planning approval if:</p>
<ul>
<li>It's at least <strong>3 m</strong> from the primary street and 3 m from any secondary street</li>
<li>It uses materials, style and roof pitch that suit the house</li>
<li>It keeps a clear view between the house and the street (or right of way)</li>
<li>It takes up no more than <strong>50%</strong> of the frontage at the building line</li>
<li>The property isn't on the City's Heritage List</li>
</ul>
<p>These come from the R-Codes and the City's Local Planning Policies 1.17 and 3.1. In other zones, planning approval is always required. If your carport doesn't meet these rules, the City suggests contacting it to discuss your plans.</p>

<h2>Carport vs garage in Melville</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Carport</th><th>Garage</th></tr></thead><tbody>
<tr><td>Primary street setback</td><td>3 m</td><td>4.5 m (3 m if the door is side-on and the street wall has windows)</td></tr>
<tr><td>Secondary street setback</td><td>3 m</td><td>3 m</td></tr>
<tr><td>Width limit</td><td>50% of frontage</td><td>50% (single storey) or 60% (two storey)</td></tr>
</tbody></table></div>

<h2>When you need a building permit</h2>
<p>Melville says a freestanding carport needs a building permit if any of these apply: it's over <strong>10 m²</strong>, over <strong>2.4 m</strong> high, or in wind region C or D. In practice almost every carport is over 10 m², so expect to need one. An attached carport needs a permit too.</p>

<h2>Fees and timeframes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Melville's published amount</th></tr></thead><tbody>
<tr><td>Building permit, carport or garage under $20,000</td><td><strong>$166.65</strong></td></tr>
<tr><td>Building permit over $20,000</td><td>0.19% application fee plus 0.137% Building Services Levy</td></tr>
<tr><td>Planning application under $50,000</td><td>$147</td></tr>
<tr><td>Verge bond (work over $20,000)</td><td>$1,900 plus a $100 inspection fee</td></tr>
</tbody></table></div>
<ul>
<li>Certified (BA1) applications: decided within <strong>10 working days</strong></li>
<li>Uncertified (BA2) applications: within <strong>25 working days</strong></li>
<li>If the City asks for more information, you have <strong>21 calendar days</strong> to provide it</li>
<li>Planning applications: about 60 days, or 90 days if neighbours or agencies are consulted</li>
</ul>
<p>Check your front setback with the <a href="/front-setback-carport-calculator">front setback carport calculator</a>, or read <a href="/carport-council-approval">carport council approval</a>.</p>
"""

FAQS = [
    ("Do I need approval for a carport in the City of Melville?",
     "Usually a building permit, yes, as most carports are over 10 m². Planning approval isn't needed in a residential zone if the carport is 3 m from the street, matches the house, keeps views to the street and is no wider than 50% of the frontage."),
    ("How close to the street can a carport be in Melville?",
     "3 m from the primary street and 3 m from a secondary street, without planning approval. A garage needs 4.5 m from the primary street."),
    ("How much is a carport building permit in Melville?",
     "Melville lists $166.65 for a carport or garage under $20,000. Over that, it's 0.19% plus the 0.137% levy, and a $1,900 verge bond plus $100 inspection fee."),
    ("How long does a carport permit take in Melville?",
     "10 working days for a certified (BA1) application and 25 working days for an uncertified (BA2) one."),
    ("Does a carport in a heritage property in Melville need planning approval?",
     "Yes. The planning exemption doesn't apply if the property is on the City's Heritage List."),
]


def page(S):
    return {"path": "city-of-melville-carport-rules.html", "published": "2026-11-08", "type": "Council guide", "icon": "pin",
            "card": "Setbacks, the 50% frontage rule, permit triggers, fees and timeframes in Melville.",
            "title": "City of Melville Carport Rules (2026)",
            "desc": "City of Melville carport rules: 3 m street setback, 50% frontage limit, when you need a building permit, the $166.65 fee, verge bonds and timeframes.",
            "eyebrow": "Council guide", "h1": "City of Melville carport rules", "crumb": "City of Melville carport rules",
            "answer": "<p>In a residential zone, a Melville carport usually needs no planning approval if it's <strong>3 m</strong> from the street, suits the house, keeps a view to the street and is no wider than <strong>50%</strong> of the frontage. Most need a building permit, which Melville lists at <strong>$166.65</strong> for work under $20,000.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/enclose-a-carport", "Enclosing a carport"), ("/front-setback-carport-calculator", "Front setback carport calculator"), ("/carport-council-approval", "Carport council approval")],
            "sources": [("Building a carport or garage (City of Melville)", "https://www.melvillecity.com.au/planning-and-building/building-or-renovating/building-a-carport-or-garage")]}
