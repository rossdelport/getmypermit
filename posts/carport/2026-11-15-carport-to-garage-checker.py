import build as b

Q = "/quote"

TREE = {
    "start": "c1", "depth": 3,
    "nodes": {
        "c1": {"q": "What kind of door do you want to add to your carport?", "opts": [
            {"t": "A solid door, like a roller or panel door", "go": "c2"},
            {"t": "An open, see-through door or gate", "go": "r_carport"},
            {"t": "Not sure yet", "go": "r_unsure"}]},
        "c2": {"q": "Which street does the carport face?", "opts": [
            {"t": "The main street at the front", "go": "c3"},
            {"t": "The side street on a corner block", "go": "c4"}]},
        "c3": {"q": "How far is the carport from the front boundary?", "help": "Measure from the front property boundary, not the kerb.", "opts": [
            {"t": "4.5 m or more", "go": "r_ok"},
            {"t": "Less than 4.5 m, but at least 0.5 m behind the front of the house", "go": "r_maybe"},
            {"t": "Less than 4.5 m and level with or in front of the house", "go": "r_da"}]},
        "c4": {"q": "How far is the carport from the side street boundary?", "opts": [
            {"t": "3 m or more", "go": "r_ok"},
            {"t": "Less than 3 m", "go": "r_da"}]},
        "r_carport": {"result": True, "title": "It can stay a carport",
            "body": "<p>Councils such as Joondalup and Melville let a carport have a door if it's <strong>visually permeable</strong> (you can see through it). It stays a carport, so the carport setbacks still apply. Adding the door is still building work, so check with council whether you need a <strong>building permit</strong>.</p>",
            "cta": {"href": Q, "text": "Ask us about your door"}},
        "r_unsure": {"result": True, "title": "The door decides it",
            "body": "<p>A see-through door usually keeps it a carport. A <strong>solid door</strong> makes it a <strong>garage</strong>, and garages have to sit further back from the street. Pick your door, then run the checker again.</p>",
            "cta": {"href": Q, "text": "Talk it through with us"}},
        "r_ok": {"result": True, "title": "It should meet the usual garage setback",
            "body": "<p>With a solid door it becomes a <strong>garage</strong>. Your distance meets the usual garage setback (4.5 m from the front, 3 m from a side street), so you may not need planning approval if everything else meets the R-Codes. You'll still need a <strong>building permit</strong>, and councils vary.</p>",
            "cta": {"href": Q, "text": "Get a fixed-price quote"}},
        "r_maybe": {"result": True, "title": "It may be allowed: check with council",
            "body": "<p>With a solid door it becomes a <strong>garage</strong>. Some councils, such as Stirling, allow a garage closer than 4.5 m if it's at least <strong>0.5 m behind the front of the house</strong>. Others may need planning approval. Check your council's rules, and you'll need a <strong>building permit</strong> either way.</p>",
            "cta": {"href": Q, "text": "Check it with us"}},
        "r_da": {"result": True, "title": "You'll probably need planning approval",
            "body": "<p>With a solid door it becomes a <strong>garage</strong>, and it's closer to the street than the usual garage setback. You'll probably need <strong>planning approval</strong> before the <strong>building permit</strong>, and council may say no. A see-through door could keep it a carport instead.</p>",
            "cta": {"href": Q, "text": "Get help with approval"}},
    },
}

BODY = """
{CHECKER}
<h2>Why a door changes everything</h2>
<p>Under the R-Codes, a carport and a garage are different things. Joondalup and Melville say a carport can have a door only if it's <strong>visually permeable</strong>. Put on a solid roller or panel door and it becomes a <strong>garage</strong>.</p>
<p>That matters because garages have to sit further from the street:</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Carport</th><th>Garage</th></tr></thead><tbody>
<tr><td>Front (primary) street, Melville</td><td>3 m</td><td>4.5 m</td></tr>
<tr><td>Side (secondary) street, Melville</td><td>Not listed</td><td>3 m</td></tr>
<tr><td>Front street at R20, Joondalup</td><td>3 m</td><td>4.5 m</td></tr>
<tr><td>Building permit</td><td>Yes</td><td>Yes</td></tr>
</tbody></table></div>
<p>Stirling allows a garage closer than 4.5 m if it's at least 0.5 m behind the front of the house. Councils vary, so check your own.</p>

<h2>You'll need a building permit</h2>
<p>Joondalup says a building permit is always needed to build or convert a carport or garage. Your plans will need to show the door, any new walls and the setbacks.</p>
<p>Read more in <a href="/enclose-a-carport">can you enclose a carport?</a> and <a href="/carport-vs-garage">carport vs garage</a>, or work out your setback with the <a href="/front-setback-carport-calculator">front setback calculator</a>.</p>
"""

FAQS = [
    ("Does adding a roller door make a carport a garage?",
     "Yes. Councils such as Joondalup and Melville say a carport can only have a visually permeable door. A solid roller door makes it a garage."),
    ("How far from the street does a garage need to be in WA?",
     "Usually 4.5 m from the front boundary and 3 m from a side street. Some councils, such as Stirling, allow closer if the garage is at least 0.5 m behind the front of the house."),
    ("Do I need a permit to convert a carport to a garage?",
     "Yes, a building permit. If the garage won't meet the setbacks, you'll probably need planning approval first."),
    ("Can I add a see-through door to my carport?",
     "Usually, yes. A visually permeable door keeps it a carport, so carport setbacks still apply."),
]


def page(S):
    return {"path": "carport-to-garage-checker.html", "published": "2026-11-15", "type": "Free tool", "icon": "garage",
            "card": "Three quick questions to see if your carport can become a garage, and what approval you need.",
            "title": "Carport to Garage Conversion Checker (WA)",
            "desc": "Free checker: see if your carport can be converted to a garage in WA, whether it meets garage setbacks and when you need planning approval or a building permit.",
            "eyebrow": "Free tool", "h1": "Can I convert my carport to a garage?", "crumb": "Carport to garage checker",
            "answer": "<p>Adding a <strong>solid door</strong> turns a carport into a <strong>garage</strong>. Garages usually need to be <strong>4.5 m</strong> from the front boundary or <strong>3 m</strong> from a side street, and always need a building permit. Answer three questions below.</p>",
            "body": BODY.replace("{CHECKER}", b.checker(S, TREE, "Carport to garage?", "Up to three quick questions.")), "faqs": FAQS,
            "related": [("/enclose-a-carport", "Can you enclose a carport?"), ("/carport-vs-garage", "Carport vs garage"), ("/front-setback-carport-calculator", "Front setback calculator")],
            "sources": [("Planning exemptions, City of Melville", "https://www.melvillecity.com.au/planning-and-building/planning-exemptions"),
                        ("Carport or garage, City of Joondalup", "https://www.joondalup.wa.gov.au/plan-and-build/residential-building-and-renovation-guides/carport-or-garage-and-converting-a-garage-to-a-habitable-room"),
                        ("Carports and garages information sheet, City of Stirling", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf")]}
