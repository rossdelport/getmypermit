BODY = """
<h2>Approvals you need</h2>
<ul>
<li><strong>Planning approval:</strong> generally yes. The City of Vincent says carports usually need development approval unless they fully meet its Built Form Policy and the R-Codes. Heritage-listed places always need it.</li>
<li><strong>Building permit:</strong> always.</li>
</ul>
<p>The City has <strong>60 days</strong> to decide a development application, or 90 days if it goes to community consultation. Approval lasts 2 years.</p>

<h2>Where it can go</h2>
<p>Vincent prefers carports at the side or rear, reached from a laneway (right of way) or the secondary street. A carport off the main street is generally only supported if there's no laneway or side street. A carport in front of the house usually won't meet the front setback, so it relies on things like other approved carports in the street.</p>

<h2>Setbacks</h2>
<div class="table-wrap"><table>
<thead><tr><th>Boundary</th><th>Usual setback</th></tr></thead><tbody>
<tr><td>Laneway</td><td>1 m, more if needed to leave 6 m of reversing space</td></tr>
<tr><td>Secondary street</td><td>1.5 m (R35 or less) or 1.0 m (R40 or higher)</td></tr>
<tr><td>Primary street</td><td>Average setback of the five houses either side</td></tr>
<tr><td>Side boundary</td><td>1 m if up to 14 m long and 3.5 m high</td></tr>
</tbody></table></div>
<p>Try the <a href="/front-setback-carport-calculator">front setback calculator</a> and see <a href="/carport-corner-block">carports on corner blocks</a>.</p>

<h2>Size and design</h2>
<ul>
<li><strong>Width:</strong> no more than 50% of the lot width, or 6 m, whichever is less.</li>
<li><strong>Open sides:</strong> no more than two solid sides. Any gate or door must be at least 50% see-through.</li>
<li><strong>Parking bay:</strong> at least 5.4 m long and 2.4 m wide per car, plus 0.3 m next to posts or walls. Two cars side by side need 5.4 m x 5.4 m.</li>
<li><strong>Sight lines:</strong> keep a 1.5 m x 1.5 m clear area where the driveway meets the front boundary.</li>
</ul>
<p>The City's info sheet dates from 2022, so check the current Built Form Policy for your lot. Call the City on 9273 6000. See also <a href="/double-carport-narrow-lot">double carports on narrow lots</a>.</p>
"""

FAQS = [
    ("Does a carport need planning approval in the City of Vincent?",
     "Generally yes, unless it fully meets the City's Built Form Policy and the R-Codes. Heritage-listed places always need it."),
    ("How wide can a carport be in Vincent?",
     "No more than 50% of the lot width or 6 m, whichever is less."),
    ("Can I build a carport in front of my house in Vincent?",
     "It's generally only supported when there's no laneway or secondary street access, and it fits with other approved carports in the street."),
    ("How long does Vincent take to decide a carport application?",
     "The City has 60 days to decide a development application, or 90 days if it needs community consultation."),
]


def page(S):
    return {"path": "city-of-vincent-carport-rules.html", "published": "2026-11-26", "type": "Council guide", "icon": "pin",
            "card": "City of Vincent carport rules: planning approval, laneway access, setbacks, width and design.",
            "title": "City of Vincent Carport Rules (2026)",
            "desc": "City of Vincent carport rules: when planning approval is needed, where carports can go, laneway and street setbacks, the 6 m width limit, see-through gates and parking bay sizes.",
            "eyebrow": "Council guide", "h1": "City of Vincent carport rules", "crumb": "Vincent carport rules",
            "answer": "<p>In the City of Vincent, a carport <strong>always</strong> needs a building permit and <strong>generally</strong> needs planning approval too. The City prefers carports off a laneway or side street, no wider than <strong>50%</strong> of the lot or <strong>6 m</strong>, with no more than two solid sides.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/front-setback-carport-calculator", "Front setback carport calculator"), ("/carport-corner-block", "Carport on a corner block"), ("/double-carport-narrow-lot", "Double carport on a narrow lot")],
            "sources": [("Planning information sheet: carports and garages (August 2022), City of Vincent", "https://www.vincent.wa.gov.au/Profiles/vincent/Assets/ClientData/Planning_Information_Sheets/Planning_Information_Sheet_-_Carports_and_Garages_-_August_2022.pdf")]}
