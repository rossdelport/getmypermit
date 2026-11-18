BODY = """
<h2>Building permit</h2>
<p>In the City of Joondalup, a shed doesn't need a building permit if it's <strong>freestanding</strong>, no bigger than <strong>10 m²</strong>, no taller than <strong>2.4 m</strong>, and put together the way the maker says. Anything bigger needs a building permit. You can lodge online. The City has <strong>10 business days</strong> for a certified BA1 and <strong>25 business days</strong> for an uncertified BA2.</p>

<h2>Small sheds (up to 10 m²)</h2>
<p>You usually don't need planning approval for one small shed if:</p>
<ul>
<li>No more than <strong>two walls</strong> are within 600 mm of a boundary.</li>
<li>Walls and roof are no higher than <strong>2.7 m</strong>.</li>
<li>It isn't in the front or side street setback.</li>
<li>It doesn't eat into the open space and outdoor living area your lot needs.</li>
</ul>

<h2>Bigger sheds</h2>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Limit without planning approval</th></tr></thead><tbody>
<tr><td>Total area of all sheds</td><td>60 m² or 10% of the lot, whichever is less</td></tr>
<tr><td>Wall height</td><td>2.4 m</td></tr>
<tr><td>Ridge (roof peak) height</td><td>4.2 m</td></tr>
<tr><td>Side and rear setback</td><td>1 m for walls up to 14 m long, 1.5 m for longer walls</td></tr>
<tr><td>Street setback</td><td>Not in the front or side street setback</td></tr>
</tbody></table></div>
<p>If your shed breaks one of these, you can still apply for planning approval, which comes before the building permit. A planning application for work under $50,000 costs <strong>$147</strong> in 2025/26. Applying after you've built costs extra, as a penalty of twice the normal fee. Councils vary, so check your lot's zoning, especially on rural or special residential land.</p>
<p>Try the <a href="/shed-size-checker">shed size checker</a>, see <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a>, or read <a href="/how-many-sheds">how many sheds you can have</a>.</p>
"""

FAQS = [
    ("Do I need a permit for a shed in the City of Joondalup?",
     "Not if it's freestanding, up to 10 m² and up to 2.4 m high. Bigger sheds need a building permit."),
    ("How big can a shed be in Joondalup without planning approval?",
     "All sheds together can be up to 60 m² or 10% of the lot, whichever is less, with walls up to 2.4 m and a ridge up to 4.2 m."),
    ("How close to the fence can a shed be in Joondalup?",
     "A small shed (up to 10 m²) can have up to two walls within 600 mm of the boundary. Bigger sheds need 1 m for walls up to 14 m long, or 1.5 m for longer walls."),
    ("How much does planning approval for a shed cost in Joondalup?",
     "$147 for work under $50,000 in 2025/26. If you apply after building, there's an extra penalty of twice the fee."),
]


def page(S):
    return {"path": "city-of-joondalup-shed-rules.html", "published": "2026-11-19", "type": "Council guide", "icon": "pin",
            "card": "City of Joondalup shed rules: when you need a permit, size and height limits, and setbacks.",
            "title": "City of Joondalup Shed Rules (2026)",
            "desc": "City of Joondalup shed rules: no permit up to 10 m² and 2.4 m, 60 m² or 10% total limit, 2.4 m walls, 4.2 m ridge, setbacks and planning fees.",
            "eyebrow": "Council guide", "h1": "City of Joondalup shed rules", "crumb": "City of Joondalup shed rules",
            "answer": "<p>In Joondalup, a freestanding shed up to <strong>10 m²</strong> and <strong>2.4 m</strong> high needs no building permit. Bigger sheds need one. Without planning approval, all sheds together can be up to <strong>60 m² or 10%</strong> of the lot, with walls up to <strong>2.4 m</strong> and a ridge up to <strong>4.2 m</strong>, set back 1 m from the boundary.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/how-close-can-a-shed-be-to-the-fence", "How close to the fence"), ("/how-many-sheds", "How many sheds")],
            "sources": [("Outbuilding (shed), City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/outbuilding-(shed)"),
                        ("Requirements for building applications, City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/property-and-land-development/requirements-for-building-applications"),
                        ("Planning services fees and charges 2025/26, City of Joondalup", "https://www.joondalup.wa.gov.au/awcontent/Web/Documents/Budget,%20Fees%20and%20Financial%20Reports/Planning-Services-fees-and-charges-2025_26.pdf")]}
