ROOMS = [("Living and kitchen", 6, 4.5), ("Bedroom 1", 3.4, 3.2), ("Bedroom 2", 3, 3), ("Bathroom", 2.6, 2.1), ("Laundry", 1.8, 1.6), ("Hall and other", 4, 1.2)]

ROWS = "".join(
    '<div class="field"><label for="gf-l%d">%s length (m)</label><input id="gf-l%d" type="number" inputmode="decimal" min="0" step="0.1" value="%s"></div>'
    '<div class="field"><label for="gf-w%d">%s width (m)</label><input id="gf-w%d" type="number" inputmode="decimal" min="0" step="0.1" value="%s"></div>'
    % (i, n, i, l, i, n, i, w) for i, (n, l, w) in enumerate(ROOMS))

TOOL = """
<div class="tool" id="gf-tool">
  <h3>Granny flat floor area calculator</h3>
  <p style="color:var(--muted);font-size:15px;margin:0">Measure each room inside the walls. Set a room to 0 if you don't need it. Nothing is sent anywhere.</p>
  <div class="fields">""" + ROWS + """</div>
  <div class="result" id="gf-out" aria-live="polite"></div>
</div>
<script>
(function () {
  function v(id) { var n = parseFloat(document.getElementById(id).value); return isNaN(n) || n < 0 ? 0 : n; }
  function run() {
    var total = 0;
    for (var i = 0; i < %d; i++) total += v("gf-l" + i) * v("gf-w" + i);
    total = Math.round(total * 10) / 10;
    var left = Math.round((70 - total) * 10) / 10, html;
    if (total <= 70) {
      html = "<h4>" + total + " m² of 70 m²</h4><p>That's within the 70 m² limit, with <strong>" + left + " m²</strong> to spare.</p>";
    } else {
      html = "<h4>" + total + " m², over by " + (-left) + " m²</h4><p>That's over the 70 m² limit for a granny flat on most residential lots. Shrink a room, or you'll need planning approval (and council may still say no).</p>";
    }
    html += "<p>Rooms only. Ask your council how it measures, as walls, verandahs and other areas may be treated differently.</p>";
    document.getElementById("gf-out").innerHTML = html;
  }
  document.querySelectorAll("#gf-tool input").forEach(function (el) { el.addEventListener("input", run); });
  run();
})();
</script>
""" % len(ROOMS)

BODY = TOOL + """
<h2>The 70 m² rule</h2>
<p>Under the state's residential rules (the R-Codes), a granny flat (an "ancillary dwelling") is limited to an internal floor area of <strong>70 m²</strong>. The state's guidance says that's enough for a one or two-bedroom home. There's no minimum lot size any more, and it can be attached to the house, inside it, or separate.</p>

<h2>How to measure</h2>
<p>The R-Codes guidance says internal floor areas are measured from the <strong>finished inside surface of the walls</strong>. That's why the calculator asks for room sizes inside the walls. The outside footprint of the building will be bigger.</p>
<p>We haven't found clear state guidance on whether every council counts things like verandahs or a store room the same way, so check with your council before you finalise the plans.</p>

<h2>Bigger than 70 m²?</h2>
<p>Some councils allow more on large or rural lots through their own local planning policies, so check yours. Otherwise, anything over 70 m² needs planning approval and may not be supported. A granny flat always needs a building permit too.</p>
"""

FAQS = [
    ("What is the maximum size of a granny flat in WA?",
     "70 m² of internal floor area on most residential (R-Coded) lots, under the R-Codes. Some councils allow more on large or rural lots."),
    ("How is granny flat floor area measured?",
     "The R-Codes guidance says internal floor areas are measured from the finished inside surface of the walls. Check with your council how it treats verandahs and other areas."),
    ("Can I fit two bedrooms in 70 m²?",
     "Yes. The state's guidance says 70 m² allows for a one or two-bedroom home."),
    ("What if my granny flat is over 70 m²?",
     "It needs planning approval and council may not support it, unless your council has a local policy allowing more on your type of lot."),
]


def page(S):
    return {"path": "granny-flat-size-calculator.html", "published": "2026-11-02", "type": "Free tool", "icon": "granny",
            "card": "Add up your rooms and see if your granny flat fits the 70 m² limit.",
            "title": "Granny Flat Size Calculator: the 70 m² Rule (WA)",
            "desc": "Free calculator: add up your granny flat's rooms and check the 70 m² internal floor area limit in WA, with how to measure and what happens if you go over.",
            "eyebrow": "Free tool", "h1": "Granny flat 70 m² calculator", "crumb": "Size calculator",
            "answer": "<p>In WA, a granny flat can have up to <strong>70 m² of internal floor area</strong>, measured inside the walls. That's enough for one or two bedrooms. Add up your rooms below to see how close you are.</p>",
            "body": BODY, "faqs": FAQS,
            "related": [("/granny-flat-rules-wa", "Granny flat rules in WA"), ("/granny-flat-minimum-lot-size", "Granny flat minimum lot size"), ("/granny-flat-cost-perth", "Granny flat cost in Perth")],
            "sources": [("R-Codes Volume 1 Explanatory Guidelines, 2024 (WA Planning Commission)", "https://www.wa.gov.au/system/files/2024-04/r-codes-vol-1-explanatory-guideline_2024-mar2024.pdf"),
                        ("Granny flats information sheet (Department of Planning, Lands and Heritage)", "https://www.planning.wa.gov.au/docs/default-source/planning-reform/pr-info-sheet-granny-flat.pdf")]}
