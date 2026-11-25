BODY = """
<h2>Why you need approval</h2>
<p>A shed, garage, carport or patio is built as a non-habitable building. Living in it changes its use, so it has to be brought up to the standard for a home. Councils such as the City of Armadale say turning a structure into a room you live in <strong>always</strong> needs a building permit, and so does any granny flat. The permit comes <strong>before</strong> work starts.</p>

<h2>Step 1: check it can be a granny flat</h2>
<ul>
<li><strong>Size:</strong> usually up to 70 m², not counting open verandahs or carports. Try the <a href="/granny-flat-size-calculator">size calculator</a>.</li>
<li><strong>How many:</strong> usually one granny flat per lot.</li>
<li><strong>Planning:</strong> if it meets the R-Codes deemed-to-comply rules for granny flats, it usually doesn't need planning approval. If not, get planning approval first. See <a href="/granny-flat-planning-approval">granny flat planning approval</a>.</li>
<li><strong>Parking:</strong> converting a carport only works if there's room elsewhere on the lot for a car.</li>
</ul>

<h2>Step 2: bring the building up to standard</h2>
<p>The City of Kalamunda's checklist for turning a patio, shed, carport or garage into a habitable room is a good guide. The main points:</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>What's usually needed</th></tr></thead><tbody>
<tr><td>Ceiling</td><td>At least 2.4 m high, lined, with a ceiling</td></tr>
<tr><td>Floor</td><td>Damp-proofed. An old slab or paving may need replacing with a new slab and membrane</td></tr>
<tr><td>Walls</td><td>Built to keep moisture out</td></tr>
<tr><td>Light</td><td>Windows or glass doors at least one-tenth of the floor area</td></tr>
<tr><td>Air</td><td>Natural ventilation</td></tr>
<tr><td>Bedrooms</td><td>Hard-wired smoke alarms may be needed</td></tr>
<tr><td>Energy</td><td>Proof it meets the building code's energy rules</td></tr>
<tr><td>Meter box</td><td>Moved to an outside wall if it's inside</td></tr>
<tr><td>No sewer?</td><td>A health application for an effluent system</td></tr>
</tbody></table></div>
<p>A structural engineer often has to check the existing frame and footings. Councils vary, so check your own council's list.</p>

<h2>Step 3: apply</h2>
<p>Lodge a BA1 (certified by a private building surveyor) or BA2 (checked by the council) with your plans and reports. Councils usually decide in 10 business days (BA1) or 25 (BA2). See <a href="/granny-flat-building-permit">the granny flat building permit</a>.</p>
"""

FAQS = [
    ("Can I turn my shed into a granny flat in WA?",
     "Often yes, but you need a building permit first, and the shed usually needs work such as a 2.4 m lined ceiling, damp-proof floor, windows, ventilation and energy efficiency upgrades."),
    ("Can I convert my garage into a granny flat?",
     "Usually, if it can meet the granny flat rules (often up to 70 m², one per lot) and the building standards for a home. A building permit is needed before work starts."),
    ("Can I turn my carport into a room?",
     "The City of Kalamunda says a carport can be converted only if there's enough space elsewhere on the lot for a vehicle shelter."),
    ("What ceiling height does a converted granny flat need?",
     "Usually at least 2.4 m for a habitable room, and the room must be lined with a ceiling."),
]


def page(S):
    return {"path": "convert-to-granny-flat.html", "published": "2026-11-26", "type": "How-to guide", "icon": "doc",
            "card": "How to turn a shed, garage or carport into a granny flat: approvals and the building upgrades councils ask for.",
            "title": "How to Convert a Shed or Garage into a Granny Flat (WA)",
            "desc": "How to turn an existing shed, garage, carport or patio into a granny flat in WA: the building permit, granny flat size rules, and the ceiling, floor, light, ventilation and energy upgrades councils ask for.",
            "eyebrow": "How-to guide", "h1": "How to turn an existing building into a granny flat", "crumb": "Convert to a granny flat",
            "answer": "<p>To turn a shed, garage or carport into a granny flat in WA, you need a <strong>building permit before work starts</strong>. The building usually needs upgrades such as a <strong>2.4 m</strong> lined ceiling, a damp-proof floor, windows of at least a tenth of the floor area and energy efficiency. Granny flats are usually capped at <strong>70 m²</strong>.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-building-permit", "Granny flat building permit"), ("/granny-flat-size-calculator", "Granny flat size calculator"), ("/granny-flat-planning-approval", "Granny flat planning approval")],
            "sources": [("Information sheet 3: converting a patio, shed, carport or garage into a habitable room (July 2025), City of Kalamunda", "https://www.kalamunda.wa.gov.au/docs/default-source/building/information-sheets/3bldinfosheet.pdf?sfvrsn=f0dad063_28"),
                        ("What can I build?, City of Armadale", "https://my.armadale.wa.gov.au/service/planning-and-building/building-services/what-can-i-build"),
                        ("Building information sheet: ancillary dwelling (June 2026), City of Armadale", "https://assets.ctfassets.net/p4i5hqtl4d48/40qQCMMHfyFz2fsz5rVvUq/618c3f6d9bd14b993fc41cc80e977718/Building_Services_Information_Sheet_-_Ancillary_Dwelling_-_June_2026.PDF")]}
