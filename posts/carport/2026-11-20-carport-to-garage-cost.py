BODY = """
<h2>Typical costs in Perth</h2>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Typical price</th></tr></thead><tbody>
<tr><td>Standard garage door, supplied and installed</td><td>$3,000 to $5,000</td></tr>
<tr><td>Custom or premium garage door</td><td>$5,000 to $15,000</td></tr>
<tr><td>Garage door motor</td><td>$770 to $990</td></tr>
<tr><td>WiFi phone control add-on</td><td>$280 to $380</td></tr>
<tr><td>Walls to close in the sides</td><td>Get quotes: depends on size and materials</td></tr>
<tr><td>Building permit, BA2 (state fee)</td><td>0.32% of the work (min $121) plus $61.65 levy for work up to $45,000</td></tr>
</tbody></table></div>
<p>Door prices are from a Perth garage door company's 2026 price list. Wall costs vary too much to give a fair range, so get two or three quotes. Your council may charge its own fees, and some councils vary.</p>

<h2>Why the rules can add cost</h2>
<p>Adding a solid door turns a carport into a garage, and a garage has stricter rules:</p>
<ul>
<li><strong>Setback:</strong> under the R-Codes, garages usually sit at least <strong>4.5 m</strong> from the front boundary. Carports can often be closer. If yours is closer than 4.5 m, you may need planning approval or a see-through door instead.</li>
<li><strong>Frontage:</strong> garage doors usually can't take up more than <strong>50%</strong> of the lot frontage.</li>
<li><strong>Permit:</strong> you always need a building permit to convert a carport to a garage.</li>
</ul>
<p>Since 1 July 2026, you don't need a registered builder for a garage or carport job under <strong>$50,000</strong>.</p>
<p>Use the <a href="/carport-to-garage-checker">carport to garage checker</a>, compare a <a href="/carport-vs-garage">carport vs garage</a>, or read about <a href="/enclose-a-carport">enclosing a carport</a>.</p>
"""

FAQS = [
    ("How much does it cost to convert a carport to a garage in Perth?",
     "A standard garage door alone is usually $3,000 to $5,000 installed, plus $770 to $990 for a motor. Walls and permit fees are extra, so get quotes."),
    ("Do I need a permit to turn my carport into a garage?",
     "Yes. Converting a carport to a garage needs a building permit, and may need planning approval if it's closer than 4.5 m to the street."),
    ("Can I put a roller door on my carport?",
     "A solid roller door makes it a garage, so garage rules apply. A see-through door can usually keep it a carport."),
    ("Do I need a registered builder to convert a carport?",
     "Not if the work is under $50,000. That limit applies to garages and carports from 1 July 2026."),
]


def page(S):
    return {"path": "carport-to-garage-cost.html", "published": "2026-11-20", "type": "Cost guide", "icon": "price",
            "card": "What it costs to turn a carport into a garage in Perth: doors, motors, walls and permits.",
            "title": "Carport to Garage Conversion Cost in Perth (2026)",
            "desc": "Carport to garage conversion cost in Perth: garage doors $3,000 to $5,000 installed, motors $770 to $990, permit fees, and the setback rules that can add cost.",
            "eyebrow": "Cost guide", "h1": "Carport to garage conversion cost", "crumb": "Carport to garage cost",
            "answer": "<p>In Perth, a standard garage door is usually <strong>$3,000 to $5,000</strong> installed, plus <strong>$770 to $990</strong> for a motor. Add the cost of walls and a <strong>building permit</strong>. If the carport is closer than <strong>4.5 m</strong> to the street, you may also need planning approval.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-to-garage-checker", "Carport to garage checker"), ("/carport-vs-garage", "Carport vs garage"), ("/enclose-a-carport", "Enclosing a carport")],
            "sources": [("Garage door cost guides, Capital Garage Doors", "https://capitalgaragedoors.com.au/cost-guides"),
                        ("Carports and garages information sheet, City of Stirling", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf"),
                        ("Planning exemptions, City of Melville", "https://www.melvillecity.com.au/planning-and-building/planning-exemptions"),
                        ("Building or renovating your home, Building and Energy", "https://www.wa.gov.au/organisation/building-and-energy/building-or-renovating-your-home")]}
