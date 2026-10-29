TOOL = """
<div class="tool" id="shed-tool">
  <h3>Shed size checker</h3>
  <p style="color:var(--muted);font-size:15px;margin:0">Enter your shed's size. Nothing is sent anywhere.</p>
  <div class="fields">
    <div class="field"><label for="st-l">Length (m)</label><input id="st-l" type="number" inputmode="decimal" min="0" step="0.1" value="3"></div>
    <div class="field"><label for="st-w">Width (m)</label><input id="st-w" type="number" inputmode="decimal" min="0" step="0.1" value="3"></div>
    <div class="field"><label for="st-wall">Wall height (m) <span class="hint">at the eaves</span></label><input id="st-wall" type="number" inputmode="decimal" min="0" step="0.1" value="2.1"></div>
    <div class="field"><label for="st-top">Highest point (m) <span class="hint">top of the roof</span></label><input id="st-top" type="number" inputmode="decimal" min="0" step="0.1" value="2.4"></div>
    <div class="field"><label for="st-att">Is it attached to the house or another building?</label><select id="st-att"><option value="0">No, freestanding</option><option value="1">Yes, attached</option></select></div>
    <div class="field"><label for="st-lot">Lot size (m&sup2;) <span class="hint">optional</span></label><input id="st-lot" type="number" inputmode="decimal" min="0" step="1" placeholder="e.g. 600"></div>
    <div class="field full"><label for="st-other">Other sheds or outbuildings already on the lot (m&sup2;) <span class="hint">optional</span></label><input id="st-other" type="number" inputmode="decimal" min="0" step="0.1" value="0"></div>
  </div>
  <div class="result" id="st-out" aria-live="polite"></div>
</div>
<script>
(function () {
  function v(id) { var n = parseFloat(document.getElementById(id).value); return isNaN(n) ? 0 : n; }
  function run() {
    var l = v("st-l"), w = v("st-w"), wall = v("st-wall"), top = v("st-top"), lot = v("st-lot"), other = v("st-other");
    var attached = document.getElementById("st-att").value === "1";
    var area = Math.round(l * w * 10) / 10, why = [], plan = [];
    if (attached) why.push("it is attached to another building");
    if (area > 10) why.push("its floor area is " + area + " m&sup2;, more than 10 m&sup2;");
    if (top > 2.4) why.push("it is " + top + " m tall, more than 2.4 m");
    if (!attached) {
      if (wall > 2.4) plan.push("walls over 2.4 m high");
      if (top > 4.2) plan.push("a roof over 4.2 m high");
      if (lot > 0) {
        var cap = Math.min(60, lot * 0.1), total = Math.round((area + other) * 10) / 10;
        if (total > cap) plan.push("all outbuildings together (" + total + " m&sup2;) over the " + Math.round(cap * 10) / 10 + " m&sup2; limit for your lot");
      } else if (area + other > 60) plan.push("all outbuildings together over 60 m&sup2;");
    }
    var title = why.length ? "You'll need a building permit" : "You probably don't need a building permit";
    if (plan.length) title += ", and probably planning approval";
    var html = "<h4>" + title + "</h4><p>Floor area: <strong>" + area + " m&sup2;</strong>.</p>";
    html += why.length ? "<p>A permit is needed because " + why.join(" and ") + ".</p>"
                       : "<p>It is freestanding, 10 m&sup2; or less and 2.4 m tall or less, so it is usually exempt.</p>";
    if (plan.length) html += "<p>It goes past the standard R-Codes limits for outbuildings: " + plan.join("; ") + ". That usually means planning approval before the building permit.</p>";
    if (attached) html += "<p>An attached shed is assessed as part of the house, so the house setback rules apply.</p>";
    html += "<p>Distance to a side or rear fence under the standard rules: <strong>" + (Math.max(l, w) > 9 ? "1.5 m" : "1 m") + "</strong>. Closer needs your council's policy or planning approval. <a href=\\"/how-close-can-a-shed-be-to-the-fence\\">How close can a shed be to the fence?</a></p>";
    document.getElementById("st-out").innerHTML = html;
  }
  document.querySelectorAll("#shed-tool input, #shed-tool select").forEach(function (el) { el.addEventListener("input", run); });
  run();
})();
</script>
"""

BODY = TOOL + """
<h2>The rules the checker uses</h2>
<p>Two sets of rules decide what a shed needs. The checker applies the standard version of each.</p>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Limit</th><th>If you go over</th></tr></thead><tbody>
<tr><td>Building permit exemption (Building Regulations)</td><td>Freestanding, floor area 10 m&sup2; or less, 2.4 m tall or less</td><td>Building permit needed</td></tr>
<tr><td>Wall height (R-Codes)</td><td>2.4 m</td><td>Planning approval usually needed</td></tr>
<tr><td>Roof height (R-Codes)</td><td>4.2 m to the top of the roof</td><td>Planning approval usually needed</td></tr>
<tr><td>Total size of all outbuildings (R-Codes)</td><td>60 m&sup2; or 10% of the lot, whichever is less</td><td>Planning approval usually needed</td></tr>
<tr><td>Side and rear setback (R-Codes)</td><td>1 m for walls up to 9 m long, 1.5 m if longer</td><td>Planning approval, unless a local policy allows it</td></tr>
<tr><td>Front yard</td><td>Not in the street setback</td><td>Planning approval</td></tr>
</tbody></table></div>
<p>Heights are measured from natural ground level. On a sloping block, or where the floor is raised, the shed can be taller than the kit says.</p>

<h2>Common shed sizes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Shed</th><th>Floor area</th><th>Building permit (if freestanding and 2.4 m tall or less)</th></tr></thead><tbody>
<tr><td>2.3 m x 1.5 m garden shed</td><td>3.5 m&sup2;</td><td>Usually not</td></tr>
<tr><td>3 m x 3 m</td><td>9 m&sup2;</td><td>Usually not</td></tr>
<tr><td>3 m x 3.3 m</td><td>9.9 m&sup2;</td><td>Usually not</td></tr>
<tr><td>3.7 m x 3 m</td><td>11.1 m&sup2;</td><td>Yes</td></tr>
<tr><td>6 m x 6 m garage-style shed</td><td>36 m&sup2;</td><td>Yes</td></tr>
<tr><td>9 m x 7 m</td><td>63 m&sup2;</td><td>Yes, and over the 60 m&sup2; outbuilding limit</td></tr>
</tbody></table></div>

<h2>What the checker can't see</h2>
<ul>
<li><strong>Your council's local policies.</strong> Some allow bigger sheds on large lots, or sheds closer to the fence.</li>
<li><strong>Rural and special rural zones</strong>, which have their own outbuilding rules.</li>
<li><strong>Heritage areas, estates and bushfire-prone lots</strong>, which can add requirements.</li>
<li><strong>Sewer lines and easements</strong> that you can't build over.</li>
</ul>
<p>If the checker says you need a permit, we can prepare and lodge it for you, including the site plan.</p>
"""

FAQS = [
    ("What size shed can I build without a permit in WA?",
     "A freestanding shed with a floor area of 10 m&sup2; or less and no taller than 2.4 m usually doesn't need a building permit. It still has to meet the planning rules for where it goes."),
    ("How big can a shed be on a residential lot in WA?",
     "Under the standard R-Codes rules, all outbuildings together can be up to 60 m&sup2; or 10% of the lot, whichever is less, with walls up to 2.4 m and a roof up to 4.2 m. Bigger needs planning approval."),
    ("How do I measure the floor area of a shed?",
     "Multiply the length by the width of the floor. A 3 m x 3.3 m shed is 9.9 m&sup2;."),
    ("Does the checker work for rural properties?",
     "Only roughly. Rural zones have their own outbuilding rules in each council's scheme, which often allow bigger sheds."),
]


def page(S):
    return {"path": "shed-size-checker.html", "published": "2026-10-30", "type": "Free tool", "icon": "shed",
            "card": "Enter your shed's size and lot size. See if you need a building permit or planning approval, and how far from the fence it goes.",
            "title": "Shed Size Checker WA: Do I Need a Permit? (Free Calculator)",
            "desc": "Free WA shed size checker. Enter length, width, height and lot size to see if your shed needs a building permit or planning approval, and the setback from the fence.",
            "eyebrow": "Free tool", "h1": "Shed size checker: permit or no permit?", "crumb": "Shed size checker",
            "answer": "<p>In WA a shed needs a <strong>building permit</strong> if it is bigger than <strong>10 m&sup2;</strong>, taller than <strong>2.4 m</strong> or attached to another building. It usually needs <strong>planning approval</strong> too if its walls are over 2.4 m, its roof is over 4.2 m, or all your outbuildings add up to more than 60 m&sup2; or 10% of the lot. Enter your sizes below to check.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/do-i-need-a-permit-for-a-shed", "Do I need a permit for a shed?"), ("/how-close-can-a-shed-be-to-the-fence", "How close can a shed be to the fence?"), ("/garage-building-permit", "Garage building permits")],
            "sources": [("Do I need a permit? (City of Gosnells)", "https://www.gosnells.wa.gov.au/Building-Development-and-Business/Building-Permits/Do-I-need-a-permit"),
                        ("Outbuildings information sheet (City of Joondalup)", "https://api.joondalup.wa.gov.au/files/Outbuildings.pdf")]}
