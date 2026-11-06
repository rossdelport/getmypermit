BODY = """
<h2>Why sewers matter for sheds</h2>
<p>Many Perth blocks have a Water Corporation sewer pipe running through the back or side yard, often along the rear fence. That's exactly where people like to put a shed. Building on top of or right next to the pipe can damage it, and stops crews getting to it for repairs. If they need to dig it up later, your shed may be in the way.</p>
<p>Water Corporation's own guidelines cover sheds, so this is a real check, not a technicality.</p>

<h2>Step 1: Find out if there's a pipe</h2>
<ul>
<li>Get free plans from <strong>Before You Dig Australia</strong> (online, or call 1100). They show the approximate location of water, sewer and drainage pipes.</li>
<li>Check your certificate of title for a registered <strong>easement</strong>. That's a strip of land the Water Corporation has a legal right to access.</li>
<li>Before heavy digging, confirm the exact spot by hand (potholing with a shovel).</li>
</ul>

<h2>Step 2: Work out how deep it is</h2>
<p>Find the nearest manhole (access chamber) on the plans. Its lid level minus the pipe level (the "invert") gives the depth. For example, 11.99 minus 10.14 means the pipe is about 1.85 m deep.</p>

<h2>Step 3: Check the clearance</h2>
<p>Water Corporation's guide for designers sets minimum gaps between a building and a sewer of 225 mm or smaller. A summary:</p>
<div class="table-wrap"><table>
<thead><tr><th>Sewer depth</th><th>With piles (any pipe)</th><th>No piles, PVC pipe</th><th>No piles, other pipe</th></tr></thead><tbody>
<tr><td>1.0 to 2.0 m</td><td>600 mm</td><td>1.5 m</td><td>1.5 to 2.5 m</td></tr>
<tr><td>2.1 to 3.0 m</td><td>600 mm</td><td>1.5 m</td><td>2.5 m</td></tr>
<tr><td>3.1 to 4.0 m</td><td>1.0 m</td><td>1.5 to 2.5 m</td><td>2.5 m</td></tr>
<tr><td>4.1 to 5.0 m</td><td>1.0 m</td><td>2.5 m</td><td>2.5 m</td></tr>
<tr><td>5.1 m or more</td><td>1.5 m</td><td>2.5 m or more</td><td>2.5 m or more</td></tr>
</tbody></table></div>
<p>The pipe size and material are written on the plans, for example "150P" means a 150 mm PVC pipe.</p>

<h2>Too close? Your options</h2>
<ol>
<li><strong>Move or redesign the shed.</strong> Water Corporation says this is the preferred option.</li>
<li><strong>Use piles.</strong> Footings that go at least 300 mm below the pipe's "zone of influence" (or down to solid rock) let you build closer. A structural engineer must design them, and the pile detail and site plan must be dated and signed by the engineer.</li>
<li><strong>Relocate the pipe.</strong> Possible in some cases, usually at your cost.</li>
</ol>
<p>Generally, you can build up to or even over an easement if you follow these rules. But it's always worth checking before you buy a shed.</p>

<h2>How this fits with your permit</h2>
<p>If your shed needs a building permit, your site plan should show easements and pipes. Councils check this. Find out if you need a permit with the <a href="/shed-size-checker">shed size checker</a>, and see <a href="/how-close-can-a-shed-be-to-the-fence">how close a shed can be to the fence</a> and <a href="/how-to-get-a-shed-permit">how to get a shed permit</a>.</p>
"""

FAQS = [
    ("Can I build a shed over a sewer pipe in WA?",
     "Usually not directly over it without special footings. Water Corporation sets minimum gaps between buildings and sewers. You can build closer if the shed sits on piles designed by a structural engineer."),
    ("How close can a shed be to a sewer line in Perth?",
     "It depends on the pipe depth and type. For a sewer 1 to 2 m deep, Water Corporation's guide says 1.5 m for PVC without piles, or 600 mm with piles."),
    ("Can I build on an easement in WA?",
     "Generally yes. Water Corporation says you can usually build up to or even over an easement, as long as you follow its requirements."),
    ("How do I find sewer pipes on my property?",
     "Get free plans from Before You Dig Australia online or by calling 1100, check your title for easements, then confirm the exact spot by hand digging."),
    ("Do I need an engineer for a shed near a sewer?",
     "If you need piles to build closer to the sewer, yes. A structural engineer must design them and sign the pile detail and site plan."),
]


def page(S):
    return {"path": "shed-over-sewer-or-easement.html", "published": "2026-11-07", "type": "Question answer", "icon": "shed",
            "card": "How to find the pipe, the clearance table, and what to do if you're too close.",
            "title": "Can You Build a Shed Over a Sewer or Easement in WA?",
            "desc": "Building a shed near a sewer or easement in Perth: how to find the pipe, Water Corporation clearance distances, piles, and how it affects your permit.",
            "eyebrow": "Question answer", "h1": "Can you build a shed over a sewer or easement?", "crumb": "Shed near a sewer",
            "answer": "<p><strong>Usually not right on top of it.</strong> Water Corporation sets minimum gaps between buildings and sewer pipes, based on the pipe's depth and type. For a typical PVC sewer 1 to 2 m deep, that's <strong>1.5 m</strong> without piles, or <strong>600 mm</strong> with engineer-designed piles. Easements can generally be built up to or over if you follow the rules.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/shed-size-checker", "Shed size checker"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/how-to-get-a-shed-permit", "How to get a shed permit")],
            "sources": [("Building on a residential property (Water Corporation)", "https://www.watercorporation.com.au/developing-and-building/working-near-assets/building-on-a-residential-property"),
                        ("Residential guidelines for designers (Water Corporation)", "https://pw-cdn.watercorporation.com.au/-/media/watercorp/documents/developing-and-building/building/residential-guidelines-for-designers.pdf")]}
