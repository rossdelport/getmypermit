TOOL = """
<div class="tool" id="ob-tool">
  <h3>Do I need owner-builder approval?</h3>
  <p style="color:var(--muted);font-size:15px;margin:0">Answer four questions. Nothing is sent anywhere.</p>
  <div class="fields">
    <div class="field"><label for="ob-type">What are you building?</label><select id="ob-type"><option value="house">A house, extension or detached granny flat</option><option value="c10">A shed, garage or carport</option></select></div>
    <div class="field"><label for="ob-val">Estimated value of the work ($)</label><input id="ob-val" type="number" inputmode="decimal" min="0" step="1000" value="30000"></div>
    <div class="field"><label for="ob-bp">Does it need a building permit?</label><select id="ob-bp"><option value="yes">Yes</option><option value="no">No, it's exempt</option></select></div>
    <div class="field"><label for="ob-reg">Will a registered builder do the job?</label><select id="ob-reg"><option value="no">No, I'll manage it myself</option><option value="yes">Yes</option></select></div>
  </div>
  <div class="result" id="ob-out" aria-live="polite"></div>
</div>
<script>
(function () {
  function g(id) { return document.getElementById(id).value; }
  function money(n) { return "$" + n.toLocaleString("en-AU", {maximumFractionDigits: 0}); }
  function run() {
    var val = parseFloat(g("ob-val")); if (isNaN(val) || val < 0) val = 0;
    var limit = g("ob-type") === "c10" ? 50000 : 20000;
    var html;
    if (g("ob-bp") === "no") {
      html = "<h4>No owner-builder approval needed</h4><p>Owner-builder approval only applies to work that needs a building permit.</p>";
    } else if (g("ob-reg") === "yes") {
      html = "<h4>No owner-builder approval needed</h4><p>A registered builder takes on the job, so you don't need owner-builder approval.</p>";
    } else if (val > limit) {
      html = "<h4>Yes, you'll likely need owner-builder approval</h4><p>The work is over <strong>" + money(limit) + "</strong>, so you need owner-builder approval from the state before you apply for the building permit. It usually takes <strong>6 to 8 weeks</strong>, and you then have <strong>6 months</strong> to apply for the permit.</p>";
    } else {
      html = "<h4>Probably not</h4><p>The work is " + money(limit) + " or less, so you usually don't need owner-builder approval. You still need the building permit. Don't split one job into smaller jobs to stay under the limit.</p>";
    }
    document.getElementById("ob-out").innerHTML = html;
  }
  document.querySelectorAll("#ob-tool input, #ob-tool select").forEach(function (el) { el.addEventListener("input", run); el.addEventListener("change", run); });
  run();
})();
</script>
"""

BODY = TOOL + """
<h2>The two dollar limits</h2>
<div class="table-wrap"><table>
<thead><tr><th>Type of work</th><th>Owner-builder approval needed if the work is over</th></tr></thead><tbody>
<tr><td>House, extension, detached granny flat</td><td>$20,000</td></tr>
<tr><td>Shed, garage, carport (Class 10a)</td><td>$50,000</td></tr>
</tbody></table></div>
<p>These limits only matter if the work needs a building permit and you're not using a registered builder. You can't split one job into smaller jobs to stay under the limit.</p>

<h2>Who can be an owner-builder</h2>
<ul>
<li>You must own the land (or have a suitable lease), shown by a Certificate of Title or purchase contract from the last 3 months.</li>
<li>You must apply as a person, not a company or trust.</li>
<li>You need to show you know the job: usually by finishing an owner-builder course, or through past building registration. You also need a white card or blue card.</li>
<li>You can't have had an owner-builder permit in the last <strong>6 years</strong>, unless that's waived.</li>
<li>You can't plan to sell or rent the property straight away. For a house, you must plan to live there.</li>
</ul>
<p>A granny flat that shares walls or a roof with your house isn't a "detached house", so it doesn't fit the owner-builder rules for houses.</p>

<h2>After approval</h2>
<p>As owner-builder you're responsible for the work for <strong>7 years</strong>. If you sell within 7 years, you usually need home indemnity insurance that covers the buyer. You must still use licensed electricians and plumbers.</p>
<p>See <a href="/which-ba-form">which BA form you need</a>, <a href="/how-to-lodge-a-building-permit-online">how to lodge a building permit online</a>, or the <a href="/building-permit-fee-calculator">building permit fee calculator</a>.</p>
"""

FAQS = [
    ("When do I need owner-builder approval in WA?",
     "When the work needs a building permit, you're not using a registered builder, and it's worth more than $20,000, or more than $50,000 for a shed, garage or carport."),
    ("How long does owner-builder approval take?",
     "Usually about 6 to 8 weeks. Once it's granted, you have 6 months to apply for your building permit."),
    ("How often can I be an owner-builder in WA?",
     "Once every 6 years, unless the state agrees to waive that rule."),
    ("Can I build a granny flat as an owner-builder?",
     "Yes, if it's detached from the house. A granny flat that shares walls or a roof with the house doesn't fit the owner-builder rules for houses."),
]


def page(S):
    return {"path": "owner-builder-checker.html", "published": "2026-11-19", "type": "Free tool", "icon": "price",
            "card": "Check if you need owner-builder approval in WA: the $20,000 and $50,000 limits.",
            "title": "Owner-Builder Checker for WA (2026)",
            "desc": "Free owner-builder checker for WA: find out if you need owner-builder approval ($20,000 for houses, $50,000 for sheds and carports), who's eligible and how long it takes.",
            "eyebrow": "Free tool", "h1": "Owner-builder checker for WA", "crumb": "Owner-builder checker",
            "answer": "<p>In WA you need <strong>owner-builder approval</strong> if the work needs a building permit, you're not using a registered builder, and it's worth more than <strong>$20,000</strong> (or <strong>$50,000</strong> for a shed, garage or carport). Approval usually takes <strong>6 to 8 weeks</strong>, and you can only do it once every 6 years.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/which-ba-form", "Which BA form do I need?"), ("/how-to-lodge-a-building-permit-online", "Lodge a building permit online"), ("/building-permit-fee-calculator", "Building permit fee calculator")],
            "sources": [("Owner-builder approval, Government of Western Australia", "https://www.wa.gov.au/organisation/service-delivery/owner-builder-approval")]}
