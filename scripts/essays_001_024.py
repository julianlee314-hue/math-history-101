#!/usr/bin/env python3
"""Essays for concepts 1–24 → merge into data/concept-histories.json"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def ep(n, eid, title, worlds, text):
    return {"n": n, "id": eid, "title": title, "worlds": worlds, "text": text.strip()}

# Existing batch-1 prose reused as primary MARK/early essays where it fits.
BATCH = [
{
  "id": 1, "slug": "counting", "name": "Counting",
  "artefacts": ["tally-stick"],
  "epochs": [
    ep(1,"mark","MARK",["mesopotamia","egypt-eastern-mediterranean"],
       """Long before writing, people needed a way to keep track of “how many” when memory alone would not do—animals, days, bundles of grain. The oldest candidates are notched bones: the Lebombo bone from southern Africa (roughly 43,000–44,000 years ago) and the better-known Ishango bone from the Congo region (about 20,000–25,000 years ago). Scholars still debate how much arithmetic those notches encode, but the basic move is clear: one mark for one thing. That one-to-one pairing is counting’s first technology. Mathera’s tally stick invites the same ancient gesture—make a mark, match it to the world—before symbols ever enter the picture."""),
    ep(3,"algorithm","ALGORITHM",["china","india","mesopotamia"],
       """Once tallies piled up, cultures invented faster procedures: grouping by tens or sixties, moving beads on an abacus, sliding counting rods. Chinese rod numerals and the Mesopotamian sexagesimal board turned counting into a repeatable recipe—carry when a place fills, empty a column, keep going. Counting stopped being only a pile of marks and became a method you could teach to a clerk."""),
    ep(6,"compute","COMPUTE",["american-global-computational","british-industrial-engineering"],
       """Electronic machines made counting automatic: punched cards, mechanical registers, then CPUs that increment billions of times a second. Spreadsheets and databases still rest on the ancient idea—one unit, one record—only now the tally stick is silicon and the “notch” is a bit."""),
  ]
},
{
  "id": 2, "slug": "cardinality", "name": "Cardinality",
  "artefacts": ["tally-stick", "ten-frame"],
  "epochs": [
    ep(1,"mark","MARK",["mesopotamia","egypt-eastern-mediterranean"],
       """Cardinality is the quiet leap from <em>marking</em> to <em>knowing</em>: the last number you say names the whole set. Shepherds who could not write still used tally sticks this way for centuries—match mark to sheep, then trust the final count. By the Neolithic Near East (roughly 8000–3000 BCE), clay tokens sorted by shape did similar work for commodities. A modern ten-frame is a small stage for the same idea: fill the frame until the last cell tells you “ten,” not ten separate ones. Once children grasp cardinality, counting stops being a chant and becomes an answer."""),
    ep(2,"write","WRITE",["greek-hellenistic","baghdad-islamic-persian"],
       """Greek mathematicians treated “how many” as something you could reason about—finite collections, magnitudes, and later the puzzle of infinity. When set language matured in the nineteenth century, cardinality became a precise relation: two sets share a size when you can pair their members one-to-one. The shepherd’s last notch and Cantor’s infinite sizes share that pairing idea."""),
  ]
},
{
  "id": 3, "slug": "number-representation", "name": "Number Representation",
  "artefacts": ["tally-stick", "clay-token"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","china","mesopotamia"],
       """Tallies record quantity; <em>representation</em> is inventing marks that stand for numbers even when the things are gone. Egyptian hieroglyphic numerals (from about 3000 BCE) used distinct signs for 1, 10, 100, 1,000 and up—still additive, not place-value. Chinese Shang oracle bones (late second millennium BCE) already show decimal groupings. Roman numerals later gave Europe a durable, if clumsy, public script. Each system answers the same problem the tally began: how do you make “seven” travel without seven goats?"""),
    ep(3,"algorithm","ALGORITHM",["india","baghdad-islamic-persian","china"],
       """Positional notation—especially the Hindu–Arabic digits with zero—changed what a written number could do. India developed the system; scholars in the Baghdad orbit transmitted and refined it; Chinese rod numerals had already practiced place-value on boards. Representation became a machine for calculation, not only a label."""),
    ep(4,"print","PRINT",["italian-commercial-renaissance","atlantic-scientific-revolution"],
       """Printing multiplied numeral systems into every counting-house and schoolbook. Standardized Arabic digits, printed arithmetic manuals, and later typefaces for algebraic symbols made one shared visual language for number across Europe and beyond."""),
  ]
},
{
  "id": 4, "slug": "ordering", "name": "Ordering",
  "artefacts": ["number-line"],
  "epochs": [
    ep(1,"mark","MARK",["mesopotamia","egypt-eastern-mediterranean"],
       """Ordering is noticing that numbers sit in a line: after three comes four, and five is farther still. People ordered long before they drew number lines—clay tokens lined up, notches read left to right, ranks of soldiers and rows of jars. What the number line adds (as a teaching tool mostly in the last few centuries) is a <em>picture</em> of order and distance at once. Place a chip at 4 and another at 9, and “between,” “before,” and “farther” become visible."""),
    ep(5,"mechanize","MECHANIZE",["atlantic-scientific-revolution","british-industrial-engineering"],
       """Ordered scales appeared on rulers, thermometers, and graph paper—physical number lines you could read at a glance. Mechanized instruments made order measurable: equal tick marks turned sequence into calibrated distance, ready for science and industry."""),
  ]
},
{
  "id": 5, "slug": "place-value", "name": "Place Value",
  "artefacts": ["coin-strip", "counting-rods"],
  "epochs": [
    ep(1,"mark","MARK",["mesopotamia","china"],
       """Place value is the idea that <em>where</em> a digit sits changes what it means—units, tens, sixties. Mesopotamia developed a sexagesimal (base-60) positional system by around 2000 BCE; Chinese counting rods gave East Asia a decimal place-value board from roughly the first millennium BCE. A coin strip or grouped tallies rehearses the same insight: ten ones become one ten, and position does the heavy lifting."""),
    ep(3,"algorithm","ALGORITHM",["india","baghdad-islamic-persian"],
       """The Hindu–Arabic system, with a true zero placeholder, matured in India and spread west through the Islamic world by the 8th–9th centuries CE. Europe’s slow switch from Roman numerals followed. Algorithms for addition and multiplication became compact precisely because place value packed magnitude into columns."""),
    ep(6,"compute","COMPUTE",["american-global-computational"],
       """Binary and hexadecimal place-value systems power every computer. Registers still “carry” when a place overflows—the same column logic as clay and rods, now at electronic speed."""),
  ]
},
{
  "id": 6, "slug": "addition", "name": "Addition",
  "artefacts": ["pan-balance", "ten-frame"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia"],
       """Adding is joining quantities—and for millennia the clearest physical model was the balance scale. Equal-arm balances appear in Egypt and Mesopotamia around the turn of the fourth to the third millennium BCE: put weights on one pan until they match the goods on the other. Egyptian scribes later formalized addition with doubling and unit-fraction tricks on papyrus. A ten-frame does a gentler classroom version of the same join: fill toward ten, then regroup."""),
    ep(3,"algorithm","ALGORITHM",["china","india","baghdad-islamic-persian"],
       """Column addition on counting boards and written numerals made joining quantities a taught procedure—align places, sum, carry. Chinese, Indian, and later Islamic arithmetics polished recipes that merchants and tax clerks could run the same way every time."""),
    ep(6,"compute","COMPUTE",["american-global-computational","british-industrial-engineering"],
       """Mechanical and electronic adders embodied the carry chain in gears and circuits. From Pascal’s calculator to the ALU on a chip, addition became the machine’s most basic verb."""),
  ]
},
{
  "id": 7, "slug": "subtraction", "name": "Subtraction",
  "artefacts": ["pan-balance"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia"],
       """Subtraction is the balance’s other half: take away until the pans agree, or find how much is missing. The same Bronze Age weighing cultures that added by stacking weights also compared and removed them; Egyptian and Babylonian texts treat “what remains” as a routine accounting move. In daily life, subtraction answered urgent questions—how much grain is left, how many days until the festival, how far short of the tax."""),
    ep(3,"algorithm","ALGORITHM",["india","china","italian-commercial-renaissance"],
       """Written subtraction algorithms—borrowing, complementary methods, abacus clearing—spread with positional numerals. Merchant manuals in Renaissance Italy drilled difference as carefully as sum, because ledgers live on both."""),
  ]
},
{
  "id": 8, "slug": "pattern-recognition", "name": "Pattern Recognition",
  "artefacts": ["series-chain"],
  "epochs": [
    ep(1,"mark","MARK",["mesopotamia","egypt-eastern-mediterranean"],
       """Humans spotted patterns in notches, seasons, and craft long before school arithmetic. Some readings of the Ishango bone (c. 20,000–25,000 years ago) see grouped marks that look like more than raw tallies—though that reading stays debated. By the Old Babylonian period (early second millennium BCE), clay tablets show deliberate numerical sequences and tables. Pattern recognition is the capacity that turns “one, two, three…” into “what comes next?”"""),
    ep(7,"intelligence","INTELLIGENCE",["american-global-computational","central-europe-19c-abstract"],
       """Modern mathematics and machine learning both amplify the ancient habit: find the rule that fits the marks. Symbolic search, statistical learning, and neural nets automate “what comes next?” at scales no scribe’s tablet could hold—yet the human spark remains noticing regularity in the first place."""),
  ]
},
{
  "id": 9, "slug": "classification", "name": "Classification",
  "artefacts": ["shape-tiles", "clay-token"],
  "epochs": [
    ep(1,"mark","MARK",["mesopotamia"],
       """Classification sorts the world into kinds—same shape, same size, same use. Neolithic clay tokens (from roughly the eighth millennium BCE onward in the Near East) already classified commodities by form: a cone for one measure, a disk for another. Sorting is also how early accounting and early geometry meet: you cannot tax or build fairly unless you can say which things belong together."""),
    ep(2,"write","WRITE",["greek-hellenistic","china"],
       """Definitions and taxonomies made classification speakable: Euclid’s common notions, Chinese categories in the Nine Chapters tradition, later set and type language. Shape tiles invite the same civic skill—group the triangles, set the circles aside—before names harden into axioms."""),
  ]
},
{
  "id": 10, "slug": "shape", "name": "Shape",
  "artefacts": ["shape-tiles", "compass-and-straightedge"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia"],
       """Shape is classification grown precise: not just “alike,” but circle, triangle, rectangle with shared properties. Egyptian rope stretchers (<em>harpedonaptai</em>) laid out foundations and fields with knotted cords from early dynastic times (from about 3000 BCE), and tomb scenes show survey teams at work after the Nile’s flood. Babylonian school texts computed areas of familiar figures. Egyptians and Mesopotamians mostly <em>used</em> shape; Greeks later named and proved."""),
    ep(2,"write","WRITE",["greek-hellenistic"],
       """With compass and straightedge, Greek geometers turned shapes into argued objects—definitions, postulates, theorems. Euclid’s <em>Elements</em> (c. 300 BCE) made the triangle and the circle the public language of exact form for two millennia."""),
  ]
},
{
  "id": 11, "slug": "position", "name": "Position",
  "artefacts": ["grid"],
  "epochs": [
    ep(2,"write","WRITE",["egypt-eastern-mediterranean","china","greek-hellenistic"],
       """Position answers “where?” relative to a frame. Egyptian artists used square grids to keep body proportions consistent in tomb painting; Chinese cartographers later mapped land with rectangular grids; Greek astronomers and then Ptolemy adapted coordinate ideas from the sky to the earth. A classroom grid is a miniature of those civic frames: rows and columns turn vague location into an address."""),
    ep(4,"print","PRINT",["atlantic-scientific-revolution","italian-commercial-renaissance"],
       """Printed maps, charts, and coordinate grids let position travel. Once latitude and longitude (and later Cartesian planes) sat on paper anyone could copy, “two right, three up” became a shared address system for earth and idea alike."""),
  ]
},
{
  "id": 12, "slug": "distance", "name": "Distance",
  "artefacts": ["ruler", "number-line"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia"],
       """Distance is how far apart two positions are—and civilizations standardized it early because trade and building demanded shared units. Egyptian royal cubit rods (attested by the Old Kingdom, around the mid-third millennium BCE) divided the forearm-based cubit into palms and fingers; Mesopotamia used the <em>nindan</em> and other survey measures; knotted ropes stretched fields after the flood. A ruler is that ancient rod in the hand; a number line makes distance countable as steps."""),
    ep(5,"mechanize","MECHANIZE",["atlantic-scientific-revolution","french-enlightenment-revolutionary","british-industrial-engineering"],
       """Precision instruments—vernier scales, survey chains, micrometers—turned distance into fine, repeatable readings. Metric reform in revolutionary France then industrial standards made “how far?” a negotiated global language."""),
  ]
},
{
  "id": 13, "slug": "units", "name": "Units",
  "artefacts": ["ruler", "measuring-cup"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia","china"],
       """A unit is an agreed “one” for measuring—cubit, shekel, <em>chi</em>, bushel. Early states stamped and guarded standards so tax and trade would not dissolve into argument. Cubit rods, weight stones, and grain measures made quantity comparable across markets and seasons."""),
    ep(5,"mechanize","MECHANIZE",["french-enlightenment-revolutionary","british-industrial-engineering"],
       """The metric system (1790s France) and later SI units turned local rods into a worldwide kit: metre, kilogram, second. Factories and laboratories needed interchangeable parts; interchangeable units were the paperwork that made those parts fit."""),
  ]
},
{
  "id": 14, "slug": "measurement", "name": "Measurement",
  "artefacts": ["ruler", "vernier-caliper"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia"],
       """Measurement assigns a number to a continuous feature—length, weight, time, volume. Surveyors after the Nile flood, temple architects, and merchants with balance pans all practiced it before theory caught up. The act is simple and civic: choose a unit, compare, record."""),
    ep(5,"mechanize","MECHANIZE",["atlantic-scientific-revolution","british-industrial-engineering"],
       """Telescopes, pendulums, vernier calipers, and planimeters embodied measurement in brass and steel. Error bars and significant figures followed: once instruments could see finer than the eye, measurement became a science of uncertainty as much as of size."""),
  ]
},
{
  "id": 15, "slug": "data-representation", "name": "Data Representation",
  "artefacts": ["data-marks", "clay-token", "manuscript-table"],
  "epochs": [
    ep(1,"mark","MARK",["mesopotamia"],
       """Clay tokens and sealed bullae (from the late Neolithic into the fourth millennium BCE in Mesopotamia) stored facts about goods before full writing. Marks on ledgers, notches on sticks, and inked columns are the same move: choose a form that stands for a fact so others can read it later."""),
    ep(3,"algorithm","ALGORITHM",["baghdad-islamic-persian","china","india"],
       """Tables—astronomical, commercial, fiscal—organized data into rows you could look up by procedure. Manuscript tables and counting-board layouts made representation actionable: find the row, apply the rule."""),
    ep(6,"compute","COMPUTE",["american-global-computational"],
       """Spreadsheets, databases, and binary encodings turned data representation into the bloodstream of modern work. The clay token’s promise—facts that outlive the moment—now lives in files and clouds."""),
  ]
},
{
  "id": 16, "slug": "estimation", "name": "Estimation",
  "artefacts": ["estimate-stick"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia"],
       """Estimation is knowing when “about” is enough—herd size at a glance, grain in a bin, days left in a journey. Farmers and captains practiced it long before schoolbooks named it. An estimate stick or rough tally accepts that some decisions cannot wait for perfect count."""),
    ep(5,"mechanize","MECHANIZE",["atlantic-scientific-revolution","british-industrial-engineering"],
       """Scientific estimation grew rules: order-of-magnitude thinking, significant digits, error bounds. Engineers designing bridges and gunners ranging shot needed good-enough numbers with known risk—estimation with a warranty."""),
  ]
},
{
  "id": 17, "slug": "repeated-operations-iteration", "name": "Repeated Operations / Iteration",
  "artefacts": ["iteration-crank"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia"],
       """Egyptian arithmetic loved doubling: to multiply, keep doubling and select the rows that sum to the multiplier (attested in Middle Kingdom papyrus traditions). Repetition was not laziness—it was a reliable engine. Babylonian reciprocal tables likewise turned hard division into look-up plus iteration."""),
    ep(3,"algorithm","ALGORITHM",["china","india","baghdad-islamic-persian"],
       """Iteration became an explicit method: approximate roots by repeating a step, refine a quotient, loop until stable. Chinese and Indian mathematical texts describe successive procedures; later algebraic algorithms made “do it again” a named strategy."""),
    ep(6,"compute","COMPUTE",["american-global-computational"],
       """Loops are the soul of software. From Jacquard patterns to <code>for</code> statements, machines formalized iteration so a crank—or a clock cycle—could repeat a rule without fatigue."""),
  ]
},
{
  "id": 18, "slug": "algorithms", "name": "Algorithms",
  "artefacts": ["recipe-tablet"],
  "epochs": [
    ep(1,"mark","MARK",["mesopotamia","egypt-eastern-mediterranean"],
       """An algorithm is a recipe that always works the same way. Babylonian clay tablets already prescribe step-by-step solutions for survey and accounting problems; Egyptian papyri do likewise for bread, beer, and slopes. The “recipe tablet” idea is older than the word."""),
    ep(3,"algorithm","ALGORITHM",["baghdad-islamic-persian","india","china"],
       """The word <em>algorithm</em> traces to al-Khwārizmī (9th century, Baghdad orbit), whose arithmetic and algebra texts taught procedures as public knowledge. Indian and Chinese traditions independently cultivated highly procedural mathematics—rod calculus, root extraction, simultaneous systems."""),
    ep(6,"compute","COMPUTE",["american-global-computational","british-industrial-engineering"],
       """From Ada Lovelace’s notes on the Analytical Engine to modern programming, algorithms became things machines execute. Complexity theory then asked how long a recipe takes—turning procedure into an object of science."""),
  ]
},
{
  "id": 19, "slug": "commutativity", "name": "Commutativity",
  "artefacts": ["swap-pans"],
  "epochs": [
    ep(2,"write","WRITE",["greek-hellenistic","baghdad-islamic-persian"],
       """Commutativity is the quiet fact that order often does not matter: 3+5 and 5+3 name the same join. Practitioners swapped addends and factors for millennia; Greek and later Islamic algebraists treated such symmetries as laws you could rely on when rearranging arguments."""),
    ep(4,"print","PRINT",["atlantic-scientific-revolution","central-europe-19c-abstract"],
       """Printed algebra made commutative laws explicit axioms of arithmetic and, later, of abstract structures. Naming the property—“commutative”—let textbooks and research papers swap freely without re-proving the obvious each time."""),
  ]
},
{
  "id": 20, "slug": "associativity", "name": "Associativity",
  "artefacts": ["nest-boxes"],
  "epochs": [
    ep(2,"write","WRITE",["greek-hellenistic","baghdad-islamic-persian"],
       """Associativity says grouping need not matter: (2+3)+4 equals 2+(3+4). Nesting boxes or regrouping pebbles show the idea in the hand. Algebraic writers who rearranged long sums depended on it even before the Latin name stuck."""),
    ep(4,"print","PRINT",["central-europe-19c-abstract","french-enlightenment-revolutionary"],
       """In nineteenth-century abstract algebra, associativity became a defining axiom for groups and rings. Print culture spread the checklist: closed, associative, identity, inverses—structure you could verify on paper."""),
  ]
},
{
  "id": 21, "slug": "identity-and-inverse-elements", "name": "Identity & Inverse Elements",
  "artefacts": ["cancel-weights"],
  "epochs": [
    ep(2,"write","WRITE",["india","baghdad-islamic-persian","greek-hellenistic"],
       """An identity leaves things unchanged (add 0, multiply by 1); an inverse undoes (add the opposite, multiply by the reciprocal). Indian and Islamic mathematicians treated zero and negatives with growing confidence; Greek geometry had “same” and “opposite” in its own vocabulary. Cancel-weights on a balance make the metaphor physical: what you add can be taken back."""),
    ep(4,"print","PRINT",["central-europe-19c-abstract"],
       """Group theory crystallized identity and inverse as axioms. Once printed textbooks required e and a⁻¹, every new algebraic system had to show its “do nothing” and “undo” elements up front."""),
  ]
},
{
  "id": 22, "slug": "inverse-operations", "name": "Inverse Operations",
  "artefacts": ["undo-latch"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia"],
       """Wherever people added, they subtracted; wherever they multiplied (by doubling or tables), they divided. Inverse operations are the undo pairs of everyday arithmetic—bake and unbake the quantity. Accounting lives on that latch: every credit imagines a debit."""),
    ep(3,"algorithm","ALGORITHM",["india","baghdad-islamic-persian","china"],
       """Procedural texts taught inverse steps explicitly: check a multiplication by division, reverse an equation by opposite moves. Algebra’s “do the same to both sides” is inverse thinking made into a method."""),
  ]
},
{
  "id": 23, "slug": "area", "name": "Area",
  "artefacts": ["area-model", "area-sweep"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia"],
       """Area began as field and floor—how much land after the flood, how many bricks for a wall. Egyptian and Babylonian problem texts compute areas of rectangles, triangles, and trapezoids with practical rules (exactness varied; some Egyptian circle rules are known to be approximate)."""),
    ep(2,"write","WRITE",["greek-hellenistic"],
       """Euclid and Archimedes made area a matter of proof: congruence, exhaustion, comparisons that did not rely on a single formula sheet. Area became something you could argue, not only survey."""),
    ep(5,"mechanize","MECHANIZE",["atlantic-scientific-revolution","british-industrial-engineering"],
       """Planimeters traced boundaries and read area off a dial—measurement without tiling. Analytic geometry and calculus then treated area as accumulated product, ready for engineering drawings and machine design."""),
  ]
},
{
  "id": 24, "slug": "volume", "name": "Volume",
  "artefacts": ["volume-jar"],
  "epochs": [
    ep(1,"mark","MARK",["egypt-eastern-mediterranean","mesopotamia","china"],
       """Volume answered container and earthwork questions: how much grain in a granary, how much earth in a ramp. Egyptian, Babylonian, and Chinese sources give procedures for boxes, cylinders, and truncated pyramids—sometimes exact, sometimes rule-of-thumb."""),
    ep(2,"write","WRITE",["greek-hellenistic"],
       """Archimedes’ results on spheres, cylinders, and crowns (3rd century BCE) showed volume could be chased with rigor. Cavalieri’s principle (17th century) later linked cross-sections to equal volumes—an idea with Chinese precursors debated by historians."""),
    ep(5,"mechanize","MECHANIZE",["atlantic-scientific-revolution","british-industrial-engineering"],
       """Integral calculus and measuring vessels turned volume into both theory and shop-floor practice. Displacement tanks, gauging rods, and computed solids kept the ancient jar question alive in laboratories and factories."""),
  ]
},
]

def main():
    path = DATA / "concept-histories.json"
    if path.exists():
        existing = {h["id"]: h for h in json.loads(path.read_text())}
    else:
        existing = {}
    for h in BATCH:
        existing[h["id"]] = h
    out = [existing[i] for i in sorted(existing)]
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(BATCH)} essays; file now has {len(out)} concepts")

if __name__ == "__main__":
    main()
