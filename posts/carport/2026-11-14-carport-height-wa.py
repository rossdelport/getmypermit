BODY = """
<h2>There's no single height limit</h2>
<p>WA doesn't set one maximum height for every carport. Height matters in three places: on the <strong>boundary</strong>, in the <strong>front setback</strong>, and for the <strong>building permit exemption</strong>.</p>

<h2>On or near the boundary</h2>
<div class="table-wrap"><table>
<thead><tr><th>Lot type</th><th>Carport can go on the boundary without planning approval if</th></tr></thead><tbody>
<tr><td>Most houses (R-Codes Part B: R40 and below)</td><td>No more than <strong>2.7 m high</strong> and 10 m long, behind the front setback, roof edge at least 450 mm from the boundary</td></tr>
<tr><td>Denser lots (R-Codes Part C: R50 and above)</td><td>Less than 10 m long, wall height up to <strong>3 m</strong>, ridge up to <strong>4.2 m</strong></td></tr>
</tbody></table></div>
<p>The City of Wanneroo's carport sheet uses the same 2.7 m and 10 m limits, with the roof 500 mm back. If your carport is taller, it needs to be set back from the boundary, or you need planning approval.</p>

<h2>Gable roofs add height</h2>
<p>A gable or pitched roof is taller at the peak than a flat roof. If you're building near the boundary, check the whole carport, not just the posts, against the limits above. See <a href="/flat-vs-gable-carport">flat vs gable carports</a>.</p>

<h2>Height and the building permit</h2>
<p>Don't rely on the small-structure exemption. Councils such as Wanneroo and Stirling say a carport <strong>always</strong> needs a building permit, whatever its height.</p>

<h2>In the front setback</h2>
<p>Councils focus on how a carport in front of the house looks. The City of Melville, for example, wants a carport in the front setback to match the house's materials, style and <strong>roof pitch</strong>, and leave a clear view to the street. Councils vary, so check yours.</p>
<p>Read <a href="/carport-on-boundary">carport on the boundary</a> or <a href="/carport-size-without-approval">carport size without approval</a>.</p>
"""

FAQS = [
    ("How high can a carport be in WA?",
     "There's no single limit. On the boundary of most house lots it must be no more than 2.7 m high and 10 m long to avoid planning approval. Away from the boundary, height is less restricted."),
    ("Can a carport on the boundary be higher than 2.7 m?",
     "On most house lots, not without planning approval. On R50 and denser lots, the R-Codes allow up to 3 m wall height and 4.2 m ridge."),
    ("Does a low carport avoid a building permit?",
     "No. Councils such as Wanneroo and Stirling say a carport always needs a building permit."),
    ("Does a gable carport count the peak height?",
     "Yes, the whole structure counts, so a gable roof can push a boundary carport over the limit."),
]


def page(S):
    return {"path": "carport-height-wa.html", "published": "2026-11-14", "type": "Question", "icon": "carport",
            "card": "The height limits that matter for a carport on the boundary, in the front setback and for the permit.",
            "title": "How High Can a Carport Be in WA? (2026 Rules)",
            "desc": "How high can a carport be in WA? On the boundary of most house lots, 2.7 m and 10 m long without planning approval. Part C lots, gable roofs and permits.",
            "eyebrow": "Question", "h1": "How high can a carport be in WA?", "crumb": "Carport height",
            "answer": "<p>There's no single limit. On the <strong>boundary</strong> of most house lots, a carport can be up to <strong>2.7 m high</strong> and 10 m long without planning approval. On denser R50+ lots, up to 3 m wall height and 4.2 m ridge. A carport <strong>always</strong> needs a building permit, whatever its height.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-on-boundary", "Carport on the boundary"), ("/carport-size-without-approval", "Carport size without approval"), ("/flat-vs-gable-carport", "Flat vs gable carport")],
            "sources": [("R-Codes Volume 1, April 2026 (WA Government)", "https://www.wa.gov.au/system/files/2026-08/r-codes-volume-1-10-april-2026.pdf"),
                        ("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf"),
                        ("Planning exemptions, City of Melville", "https://www.melvillecity.com.au/planning-and-building/planning-exemptions")]}
