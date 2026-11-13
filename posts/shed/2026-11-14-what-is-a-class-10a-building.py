BODY = """
<h2>The building classes, in short</h2>
<p>The National Construction Code (NCC) sorts every building into a class based on how it's used. The class decides which building rules apply.</p>
<div class="table-wrap"><table>
<thead><tr><th>Class</th><th>What it covers</th></tr></thead><tbody>
<tr><td>Class 1a</td><td>A house, or a townhouse or row house</td></tr>
<tr><td>Class 10a</td><td>Non-habitable buildings: sheds, carports and private garages</td></tr>
<tr><td>Class 10b</td><td>Structures: fences, masts, antennas, retaining walls, swimming pools</td></tr>
<tr><td>Class 10c</td><td>A private bushfire shelter</td></tr>
<tr><td>Class 7b and 8</td><td>Warehouses, storage buildings and workshops used for business</td></tr>
</tbody></table></div>

<h2>What "non-habitable" means for your shed</h2>
<p>A Class 10a building isn't made for living or sleeping in. If you want to use a shed as a bedroom or granny flat, it becomes a different class (usually Class 1a), with much stricter rules for things like ceiling height, light, ventilation and fire safety.</p>
<p>A <strong>private garage</strong> is also Class 10a: one that goes with a house, or a single-storey garage for no more than 3 vehicles.</p>

<h2>When a shed isn't Class 10a</h2>
<p>The NCC says farm buildings depend on how they're used. A shed for one tractor may be Class 10a. A shed for lots of machinery could be Class 7a, or Class 8 if mechanics regularly work in it. A shed used as a business workshop is usually not Class 10a either.</p>

<h2>Why the class matters for approval</h2>
<p>In WA, the building permit forms ask for the building class. Class 10 buildings, along with houses, can use the uncertified <strong>BA2</strong> application, where the council checks the plans. Most other classes need a certified <strong>BA1</strong>. Building permit fees for Class 1 and 10 are 0.32% (BA2) or 0.19% (BA1) of the value, at least $121.</p>
<p>Check your shed with the <a href="/shed-size-checker">shed size checker</a>, or read <a href="/shed-vs-garage">shed vs garage</a> and <a href="/toilet-or-shower-in-a-shed">adding a toilet or shower to a shed</a>.</p>
"""

FAQS = [
    ("Is a shed a Class 10a building?",
     "Yes. The NCC lists sheds, carports and private garages as Class 10a non-habitable buildings."),
    ("Can I sleep in a Class 10a shed?",
     "No. Class 10a is non-habitable. To live or sleep in it, it would need to be approved as a different class, usually Class 1a."),
    ("What is the difference between Class 10a and 10b?",
     "Class 10a is a non-habitable building like a shed or garage. Class 10b is a structure like a fence, retaining wall or swimming pool."),
    ("Does a Class 10a shed need a building permit in WA?",
     "Usually, unless it's freestanding, 10 m² or less and 2.4 m or less high. Councils vary."),
]


def page(S):
    return {"path": "what-is-a-class-10a-building.html", "published": "2026-11-14", "type": "Question", "icon": "question",
            "card": "What Class 10a means for sheds, garages and carports, and why it matters for your permit.",
            "title": "What Is a Class 10a Building? (Sheds, Garages, Carports)",
            "desc": "A Class 10a building is a non-habitable building like a shed, carport or private garage. What it means for your shed and your WA building permit.",
            "eyebrow": "Question", "h1": "What is a Class 10a building?", "crumb": "Class 10a building",
            "answer": "<p>A <strong>Class 10a</strong> building is a <strong>non-habitable</strong> building, such as a <strong>shed, carport or private garage</strong>, under the National Construction Code. You can't live or sleep in it. In WA, Class 10 buildings can use the uncertified BA2 building permit application.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/shed-vs-garage", "Shed vs garage"), ("/toilet-or-shower-in-a-shed", "Toilet or shower in a shed")],
            "sources": [("Building classifications, NCC (Australian Building Codes Board)", "https://ncc.abcb.gov.au/ncc-navigator/building-classifications"),
                        ("Building approvals (WA Government)", "https://www.wa.gov.au/organisation/building-and-energy/building-approvals")]}
