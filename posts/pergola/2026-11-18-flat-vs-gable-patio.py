BODY = """
<h2>Side by side</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Flat (skillion) roof</th><th>Gable (pitched) roof</th></tr></thead><tbody>
<tr><td>Look</td><td>Low, simple, modern</td><td>Peaked, adds a feeling of height and space</td></tr>
<tr><td>Airflow and light</td><td>Less, can trap heat under the roof</td><td>More, the peak lets hot air rise and out</td></tr>
<tr><td>Height</td><td>Lower, easier to fit under gutters</td><td>Taller at the ridge</td></tr>
<tr><td>Cost</td><td>Cheaper</td><td>Usually about 10 to 15% more for a kit</td></tr>
<tr><td>Council approval</td><td>Usually needs a building permit</td><td>Usually needs a building permit</td></tr>
</tbody></table></div>

<h2>Real kit prices in Perth</h2>
<p>Patio &amp; Shed Kits WA (Bellevue) publishes prices for attached kits. These are kit-only prices including GST, not installed:</p>
<div class="table-wrap"><table>
<thead><tr><th>Size (long × wide)</th><th>Attached flat</th><th>Attached gable</th></tr></thead><tbody>
<tr><td>6 × 4 m</td><td>$4,140</td><td>$4,760</td></tr>
<tr><td>6 × 6 m</td><td>$5,460</td><td>$6,140</td></tr>
<tr><td>8 × 5 m</td><td>$5,900</td><td>$6,600</td></tr>
<tr><td>10 × 6 m</td><td>$8,100</td><td>$8,900</td></tr>
</tbody></table></div>
<p>Installation, footings, electrical and council fees are extra.</p>

<h2>Approval differences</h2>
<p>Both styles usually need a building permit, because the only exemption is for a freestanding structure up to 10 m² and 2.4 m high. The roof style matters most near a boundary. A gable's taller ridge and end walls can push you over the height limits councils use for boundary structures, so a flat roof is often easier on a side boundary. Councils vary, so check your height limits before you order.</p>
<p>See <a href="/attached-vs-freestanding-patio">attached vs freestanding patios</a>, <a href="/patio-prices-perth">patio prices in Perth</a>, or the rules for a <a href="/patio-on-boundary-wa">patio on the boundary</a>.</p>
"""

FAQS = [
    ("Is a flat or gable patio cheaper?",
     "Flat is cheaper. Published Perth kit prices show gable kits costing about 10 to 15% more than flat kits of the same size."),
    ("Is a gable patio cooler than a flat patio?",
     "Usually yes. The higher peak lets hot air rise and escape, and gives more light and airflow."),
    ("Do I need council approval for a gable patio?",
     "Usually yes, the same as a flat patio. Only freestanding structures up to 10 m² and 2.4 m high are exempt."),
    ("Which roof is better near a boundary?",
     "A flat roof is often easier, because a gable's taller ridge can go over the height limits councils use for boundary structures."),
]


def page(S):
    return {"path": "flat-vs-gable-patio.html", "published": "2026-11-18", "type": "Comparison", "icon": "pergola",
            "card": "Flat vs gable patio roofs in Perth: look, airflow, real kit prices and approval.",
            "title": "Flat vs Gable Patio: Cost and Approval in Perth (2026)",
            "desc": "Flat vs gable patio in Perth: compare look, airflow and real kit prices (gable about 10-15% more), plus how the roof style affects council approval.",
            "eyebrow": "Comparison", "h1": "Flat vs gable patio", "crumb": "Flat vs gable patio",
            "answer": "<p>A <strong>flat</strong> patio is cheaper and lower. A <strong>gable</strong> patio costs about <strong>10 to 15% more</strong> for a kit but gives better airflow, more light and a taller feel. Both usually need a <strong>building permit</strong>. Near a boundary, a flat roof is often easier to get approved because it's lower.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/attached-vs-freestanding-patio", "Attached vs freestanding patio"), ("/patio-prices-perth", "Patio prices in Perth"), ("/patio-on-boundary-wa", "Patio on the boundary")],
            "sources": [("Attached flat kit prices, Patio & Shed Kits WA", "https://patiokitswa.com.au/attached-flat-kit-prices/"),
                        ("Gable attached prices, Patio & Shed Kits WA", "https://patiokitswa.com.au/gable-attached-prices/"),
                        ("Sheds, pergolas and outdoor structures, City of Bayswater", "https://www.bayswater.wa.gov.au/home-and-property/renovating-your-home-or-property/sheds,-pergolas-and-outdoor-structures")]}
