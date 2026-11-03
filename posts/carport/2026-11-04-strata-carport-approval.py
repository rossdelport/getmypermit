BODY = """
<h2>Two sets of approvals</h2>
<p>On a strata property you need the <strong>strata company's</strong> approval as well as the usual <strong>council</strong> approvals. Landgate says the strata company's approval is in addition to any planning or building approval. In a strata scheme it must be in place before any work starts.</p>

<h2>Step 1: Work out what kind of strata you're in</h2>
<div class="table-wrap"><table>
<thead><tr><th>Scheme type</th><th>When you need the strata company's approval for a carport</th></tr></thead><tbody>
<tr><td><strong>Strata scheme</strong> (lot boundaries are the building)</td><td>Always, before work starts, for any structural alteration to your lot</td></tr>
<tr><td><strong>Survey-strata scheme</strong> (lot boundaries are on the ground)</td><td>Only if the carport would breach your lot's plot ratio or open space limits, unless your by-laws say otherwise</td></tr>
</tbody></table></div>
<p>Check your strata plan or ask your strata manager if you're not sure which you have. Also read your <strong>by-laws</strong>: the default ones say you must give the strata company 14 days' written notice before altering the structure of your lot.</p>

<h2>Step 2: Apply to the strata company</h2>
<p>Approval can be a <strong>resolution without dissent</strong> at a meeting, or the <strong>written approval of every lot owner</strong>. Your application must include:</p>
<ul>
<li>plans and specifications</li>
<li>the area of the carport and all existing structures, and whether you'll exceed open space or plot ratio limits</li>
<li>its location and size compared with the boundary and other structures</li>
<li>the materials, the colours visible from outside, and how and when it will be built</li>
<li>any by-law it might break, and any effect on easements or covenants</li>
</ul>

<h2>Step 3: Know the time limits</h2>
<ul>
<li>Voting must open within <strong>35 days</strong> of the strata company receiving your application.</li>
<li>An owner who doesn't object in writing within <strong>42 days</strong> is treated as approving.</li>
<li>The strata company is treated as approving if it doesn't object in writing within <strong>77 days</strong>.</li>
</ul>

<h2>Grounds for saying no</h2>
<p>Owners can only refuse for set reasons, and must give them. For example, the carport would breach open space or plot ratio, break a by-law, interfere with an easement or covenant, look out of keeping with the rest of the development, or affect structural soundness. If an owner refuses without valid grounds, the refusal doesn't count. If you're refused, you can apply to the <strong>State Administrative Tribunal</strong> for an exemption.</p>

<h2>Step 4: Council approvals</h2>
<p>Then it's the usual process: a building permit for every carport, and planning approval if it doesn't meet the R-Codes. The City of Stirling's carport guide notes strata lots may need this separate strata approval too.</p>
"""

FAQS = [
    ("Do I need strata approval for a carport?",
     "In a strata scheme, yes, always, before work starts. In a survey-strata scheme, only if the carport would breach your lot's plot ratio or open space limits, unless your by-laws say otherwise."),
    ("How long does strata approval take in WA?",
     "Voting must open within 35 days. Owners who don't object within 42 days, and a strata company that doesn't object within 77 days, are treated as approving."),
    ("Can my neighbours stop my carport?",
     "Only on set grounds, such as breaching open space or plot ratio, breaking a by-law or being out of keeping with the development. They must state their grounds, and you can apply to the State Administrative Tribunal if refused."),
    ("Do I still need council approval on a strata lot?",
     "Yes. Strata approval is in addition to the building permit, and planning approval if needed."),
]


def page(S):
    return {"path": "strata-carport-approval.html", "published": "2026-11-04", "type": "How-to guide", "icon": "carport",
            "card": "Strata company approval, time limits, what owners can object to, then council.",
            "title": "How to Get a Carport Approved on a Strata Property (WA)",
            "desc": "Carports on strata lots in WA: strata vs survey-strata, what to include in your application, the 35, 42 and 77 day time limits, grounds for refusal, and council approvals.",
            "eyebrow": "How-to guide", "h1": "How to get a carport approved on a strata property", "crumb": "Strata carport approval",
            "answer": "<p>You need the <strong>strata company's approval</strong> on top of council's. In a strata scheme it's always needed; in a survey-strata scheme only if you'd breach plot ratio or open space. Owners who don't object within <strong>42 days</strong> are treated as approving. Then apply for the building permit.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-council-approval", "Carport council approval"), ("/city-of-stirling-carport-rules", "City of Stirling carport rules"), ("/carport-size-without-approval", "Carport size without approval")],
            "sources": [("Renovations in a strata titles scheme fact sheet (Landgate)", "https://www.landgate.wa.gov.au/siteassets/documents/strata-and-community-titles/strata-titles/learn-about-strata/getting-things-done---fact-sheet.pdf"),
                        ("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf")]}
