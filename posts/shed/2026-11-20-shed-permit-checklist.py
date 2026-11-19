TOOL = """
<div class="tool" id="sc-tool">
  <h3>Build your shed permit checklist</h3>
  <p style="color:var(--muted);font-size:15px;margin:0">Answer a few questions to see what documents you'll likely need. Nothing is sent anywhere.</p>
  <div class="fields">
    <div class="field"><label for="sc-form">Which application?</label><select id="sc-form"><option value="ba2">BA2 (council checks the plans)</option><option value="ba1">BA1 (private building surveyor certifies first)</option></select></div>
    <div class="field"><label for="sc-val">Value of the work over $50,000?</label><select id="sc-val"><option value="no">No</option><option value="yes">Yes</option></select></div>
    <div class="field"><label for="sc-bush">Bushfire-prone area, within 6 m of the house?</label><select id="sc-bush"><option value="no">No</option><option value="yes">Yes</option></select></div>
    <div class="field"><label for="sc-used">Second-hand shed?</label><select id="sc-used"><option value="no">No, new</option><option value="yes">Yes</option></select></div>
    <div class="field"><label for="sc-var">Breaks a standard rule (e.g. too tall or close to the boundary)?</label><select id="sc-var"><option value="no">No</option><option value="yes">Yes</option></select></div>
    <div class="field"><label for="sc-verge">Will trucks or materials use the verge?</label><select id="sc-verge"><option value="no">No</option><option value="yes">Yes</option></select></div>
  </div>
  <div class="result" id="sc-out" aria-live="polite"></div>
</div>
<script>
(function () {
  function g(id) { return document.getElementById(id).value; }
  function run() {
    var items = [
      "Completed application form (" + (g("sc-form") === "ba1" ? "BA1" : "BA2") + ")",
      "Site plan (usually 1:200) showing the shed, boundaries, setbacks, easements, sewer and soak wells",
      "Plans and elevations (usually 1:100), with a cross section",
      "Structural engineer's certification: footings, slab and tie-down"
    ];
    if (g("sc-form") === "ba1") items.push("Certificate of Design Compliance (BA3) from a registered building surveyor");
    if (g("sc-val") === "yes") items.push("Registered builder's details, or owner-builder approval");
    if (g("sc-bush") === "yes") items.push("Bushfire Attack Level (BAL) assessment");
    if (g("sc-used") === "yes") items.push("Recent engineer's sign-off that the second-hand shed is fit to re-use");
    if (g("sc-var") === "yes") items.push("Planning approval, or the council's R-Codes variation form with neighbour comments");
    if (g("sc-verge") === "yes") items.push("Verge permit application");
    document.getElementById("sc-out").innerHTML = "<h4>Your checklist (" + items.length + " items)</h4><ul><li>" + items.join("</li><li>") + "</li></ul><p>Councils vary, so check your council's own checklist before you lodge.</p>";
  }
  document.querySelectorAll("#sc-tool select").forEach(function (el) { el.addEventListener("change", run); });
  run();
})();
</script>
"""

BODY = TOOL + """
<h2>What most councils ask for</h2>
<p>For an uncertified shed application, the City of Swan's checklist asks for a site plan, working drawings with a cross section, structural engineer certification, and numbered documents. The Shire of Serpentine Jarrahdale asks for soak wells and easements on the site plan, and engineer-signed footing, slab and tie-down details.</p>

<h2>Extra items that catch people out</h2>
<ul>
<li><strong>Second-hand sheds:</strong> Serpentine Jarrahdale needs a recent engineer's sign-off.</li>
<li><strong>Bushfire areas:</strong> a shed within 6 m of the house may need to meet the house's BAL rating.</li>
<li><strong>Bigger jobs:</strong> over $50,000 you need a registered builder or owner-builder approval.</li>
<li><strong>Breaking a rule:</strong> if the shed doesn't meet the R-Codes' standard rules, you may need neighbour comments or planning approval first.</li>
</ul>
<p>See <a href="/how-to-get-a-shed-permit">how to get a shed permit</a>, how to draw a <a href="/shed-site-plan">shed site plan</a>, or <a href="/shed-permit-cost-wa">what a shed permit costs</a>.</p>
"""

FAQS = [
    ("What documents do I need for a shed permit in WA?",
     "Usually the application form, a site plan, plans and elevations, and a structural engineer's certification. Some sheds need more, such as a BAL assessment or owner-builder approval."),
    ("Does every shed need engineering?",
     "Most councils ask for an engineer's certification of the footings, slab and tie-down. Shed kits usually come with it."),
    ("Can I use a second-hand shed?",
     "Usually yes, but some councils, such as Serpentine Jarrahdale, need a recent engineer's sign-off that it's fit to re-use."),
    ("Do I need a BA3 for a shed?",
     "Only if you lodge a BA1. With a BA2, the council checks the plans itself."),
]


def page(S):
    return {"path": "shed-permit-checklist.html", "published": "2026-11-20", "type": "Free tool", "icon": "price",
            "card": "Build your own shed permit checklist: the documents WA councils usually ask for.",
            "title": "Shed Permit Checklist Builder for WA (2026)",
            "desc": "Free shed permit checklist for WA: answer six questions and see the documents you'll likely need, from site plan and engineering to BAL and verge permits.",
            "eyebrow": "Free tool", "h1": "Shed permit checklist builder", "crumb": "Shed permit checklist",
            "answer": "<p>Most WA councils want a <strong>site plan</strong>, <strong>plans and elevations</strong>, and a <strong>structural engineer's certification</strong> for a shed. You may also need a BA3, a BAL assessment, owner-builder approval or a verge permit, depending on your shed.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/how-to-get-a-shed-permit", "How to get a shed permit"), ("/shed-site-plan", "Shed site plan"), ("/shed-permit-cost-wa", "Shed permit cost in WA")],
            "sources": [("Checklist for an uncertified Class 10 application, City of Swan", "https://www.swan.wa.gov.au/awcontent/Web/Documents/PlanBuildSubdivisionSpecifications/GENERAL_CHECKLIST_FOR_AN_UNCERTIFIED_Class_10s.pdf"),
                        ("Sheds, garages and workshops, Shire of Serpentine Jarrahdale", "https://www.sjshire.wa.gov.au/planning-building-and-roads/building/building-advice/sheds-garages-and-workshops.aspx")]}
