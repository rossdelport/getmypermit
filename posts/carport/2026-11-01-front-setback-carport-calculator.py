TOOL = """
<div class="tool" id="cp-tool">
  <h3>Front setback carport calculator</h3>
  <p style="color:var(--muted);font-size:15px;margin:0">Enter your lot and carport details. Nothing is sent anywhere.</p>
  <div class="fields">
    <div class="field"><label for="cp-front">Lot frontage (m) <span class="hint">width of the lot at the street</span></label><input id="cp-front" type="number" inputmode="decimal" min="0" step="0.1" value="15"></div>
    <div class="field"><label for="cp-w">Carport width (m)</label><input id="cp-w" type="number" inputmode="decimal" min="0" step="0.1" value="6"></div>
    <div class="field"><label for="cp-r">Your lot's R-Code</label><select id="cp-r"><option value="6">R20</option><option value="4">R30 or R40</option><option value="0">Other or not sure</option></select></div>
    <div class="field"><label for="cp-d">Distance from the front boundary to the carport (m)</label><input id="cp-d" type="number" inputmode="decimal" min="0" step="0.1" value="3"></div>
    <div class="field"><label for="cp-open">Open view between the house and the street?</label><select id="cp-open"><option value="1">Yes, open sides, no solid door</option><option value="0">No</option></select></div>
    <div class="field"><label for="cp-mat">Materials match the house?</label><select id="cp-mat"><option value="1">Yes</option><option value="0">No</option></select></div>
  </div>
  <div class="result" id="cp-out" aria-live="polite"></div>
</div>
<script>
(function () {
  function v(id) { var n = parseFloat(document.getElementById(id).value); return isNaN(n) ? 0 : n; }
  function r1(n) { return Math.round(n * 100) / 100; }
  function run() {
    var front = v("cp-front"), w = v("cp-w"), full = v("cp-r"), d = v("cp-d");
    var open = document.getElementById("cp-open").value === "1", mat = document.getElementById("cp-mat").value === "1";
    var maxW = r1(front * 0.6), html;
    if (!full) {
      html = "<h4>Check your R-Code first</h4><p>The street setback depends on your lot's R-Code. Your council's online map shows it. Under the 60% rule, your carport could be up to <strong>" + maxW + " m</strong> wide.</p>";
    } else if (d >= full) {
      html = "<h4>Behind the street setback</h4><p>At " + d + " m back, the carport is outside the " + full + " m street setback, so the 60% rule doesn't apply. It still needs a building permit, and side setbacks still apply.</p>";
    } else {
      var half = full / 2, fail = [];
      if (d < half) fail.push("it is " + d + " m from the front boundary; the closest allowed is " + half + " m (half the " + full + " m setback)");
      if (w > maxW) fail.push("it is " + w + " m wide; 60% of your " + front + " m frontage is " + maxW + " m");
      if (!open) fail.push("it blocks the view between the house and the street");
      if (!mat) fail.push("its materials don't match the house");
      html = fail.length
        ? "<h4>Likely needs planning approval</h4><p>Under the standard rules, a carport in the front setback can't go ahead without planning approval because " + fail.join("; ") + ".</p>"
        : "<h4>Meets the standard front setback rules</h4><p>At " + d + " m back and " + w + " m wide, it fits the reduced setback (" + half + " m) and the 60% width limit (" + maxW + " m). It likely skips planning approval, but still needs a building permit.</p>";
    }
    html += "<p>Eaves can project up to 0.75 m into the setback area.</p>";
    document.getElementById("cp-out").innerHTML = html;
  }
  document.querySelectorAll("#cp-tool input, #cp-tool select").forEach(function (el) { el.addEventListener("input", run); });
  run();
})();
</script>
"""

BODY = TOOL + """
<h2>The rules the calculator uses</h2>
<p>A carport in front of the house is allowed into the street setback under the standard planning rules (the "deemed-to-comply" rules), as long as it meets all of these:</p>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Limit</th></tr></thead><tbody>
<tr><td>Normal street setback</td><td>6 m on an R20 lot; 4 m on an R30 or R40 lot</td></tr>
<tr><td>How far a carport can come forward</td><td>Up to half the setback: 3 m from the boundary on R20, 2 m on R30 or R40</td></tr>
<tr><td>Width</td><td>No more than 60% of the lot frontage</td></tr>
<tr><td>Views</td><td>An unobstructed view between the house and the street (no solid door)</td></tr>
<tr><td>Materials</td><td>Compatible with the house</td></tr>
<tr><td>Eaves</td><td>Can project up to 0.75 m into the setback</td></tr>
</tbody></table></div>
<p>These numbers come from the City of Wanneroo's carport information sheet, which applies the R-Codes to most R20 and R30 lots. Other councils use the same R-Codes but can have local policies, and estates with a Local Development Plan can be different.</p>

<h2>Worked example</h2>
<p>A 15 m wide R20 lot. 60% of 15 m is <strong>9 m</strong>, so a 6 m double carport is fine on width. The normal setback is 6 m, halved to <strong>3 m</strong>. So the carport can come forward to 3 m from the front boundary, as long as it's open to the street and matches the house.</p>

<h2>Other things to check</h2>
<ul>
<li><strong>Side boundary.</strong> At Wanneroo, carports need 1 m from the side boundary to the post (1.5 m if longer than 14 m). Posts on the boundary are allowed if the carport is no longer than 10 m and no higher than 2.7 m, with the roof 500 mm back, but only behind the street setback.</li>
<li><strong>Corner lots.</strong> 1.5 m from the secondary street.</li>
<li><strong>Heritage.</strong> Heritage-listed properties and heritage areas need planning approval regardless.</li>
<li><strong>Building permit.</strong> Every carport needs one, even when planning approval isn't needed.</li>
</ul>
"""

FAQS = [
    ("How close to the front boundary can a carport be in WA?",
     "Under the standard rules, up to half the normal street setback: 3 m from the boundary on an R20 lot (half of 6 m) or 2 m on an R30 or R40 lot (half of 4 m), if the carport meets the width, view and materials rules."),
    ("What is the 60% rule for carports?",
     "A carport in the front setback can't be wider than 60% of the lot's frontage. On a 15 m wide lot, that's 9 m."),
    ("Can a carport have a garage door in the front setback?",
     "Not under the standard rules. A carport must keep an unobstructed view between the house and the street, so a solid door means planning approval."),
    ("Does a front carport that meets the rules still need a permit?",
     "Yes. Meeting the standard rules means you can skip planning approval, but every carport still needs a building permit."),
]


def page(S):
    return {"path": "front-setback-carport-calculator.html", "published": "2026-11-01", "type": "Free tool", "icon": "carport",
            "card": "Check the 60% width rule and how far forward your carport can go, with your lot's numbers.",
            "title": "Front Setback Carport Calculator: the 60% Rule (WA)",
            "desc": "Free calculator for carports in front of the house in WA. Check the 60% frontage rule and the reduced street setback, and see if you can skip planning approval.",
            "eyebrow": "Free tool", "h1": "Front setback carport calculator", "crumb": "Front setback calculator",
            "answer": "<p>A carport can come forward into the street setback by up to <strong>half</strong> (to 3 m from the boundary on R20 lots, 2 m on R30 and R40) if it's <strong>no wider than 60% of the frontage</strong>, open to views from the street and matches the house. Put your numbers in below.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/carport-in-front-setback", "Carports in the front setback"), ("/carport-size-without-approval", "Carport size without approval"), ("/carport-council-approval", "Carport council approval")],
            "sources": [("Carports information sheet, July 2025 (City of Wanneroo)", "https://www.wanneroo.wa.gov.au/download/downloads/id/354/carports_-_information_sheet.pdf"),
                        ("Carports and garages information sheet (City of Stirling)", "https://stirling.wa.gov.au/awcontent/Web/Documents/Carports-and-Garages-Information-Sheet.pdf")]}
