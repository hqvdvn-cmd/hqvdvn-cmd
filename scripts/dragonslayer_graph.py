"""Render the contribution graph being cut by the Dragonslayer as an animated SVG.

Usage:
  GITHUB_TOKEN=... python scripts/dragonslayer_graph.py <login> <out.svg>
  python scripts/dragonslayer_graph.py --demo <out.svg>
"""
import json, os, random, sys, urllib.request

CELL, GAP, PAD_X, PAD_Y = 11, 3, 20, 34
DUR = 9.0            # full loop, seconds
SWEEP = (0.6, 4.6)   # slash crosses the graph in this window
COLORS = ["#16181d", "#3d1010", "#6b1515", "#a31d1d", "#e0362c"]

QUERY = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
totalContributions weeks{contributionDays{contributionCount date weekday}}}}}}"""


def fetch(login, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    cal = json.load(urllib.request.urlopen(req))["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    counts = [d["contributionCount"] for w in cal["weeks"] for d in w["contributionDays"]]
    top = max(counts) or 1
    weeks = [[(d["weekday"], level(d["contributionCount"], top)) for d in w["contributionDays"]] for w in cal["weeks"]]
    return weeks, cal["totalContributions"]


def level(n, top):
    if n == 0:
        return 0
    return min(4, 1 + int(3 * n / top + 0.5))


def demo():
    rnd = random.Random(3)
    weeks = []
    for w in range(53):
        heat = 0.25 + 0.6 * (w / 52) ** 1.5
        weeks.append([(d, 0 if rnd.random() > heat else rnd.randint(1, 4)) for d in range(7)])
    return weeks, 1337


def render(weeks, total):
    cols = len(weeks)
    width = PAD_X * 2 + cols * (CELL + GAP) - GAP
    height = PAD_Y + 7 * (CELL + GAP) + 30
    t0, t1 = SWEEP
    pct = lambda t: f"{100 * t / DUR:.2f}%"
    cells = []
    for c, week in enumerate(weeks):
        hit = t0 + (t1 - t0) * c / max(1, cols - 1)
        for day, lvl in week:
            x = PAD_X + c * (CELL + GAP)
            y = PAD_Y + day * (CELL + GAP)
            fill = COLORS[lvl]
            if lvl == 0:
                cells.append(f'<rect class="z" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{fill}" style="animation-delay:{hit:.2f}s"/>')
                continue
            # two halves split along the slash diagonal
            a = f"M{x},{y}h{CELL}L{x},{y + CELL}z"
            b = f"M{x + CELL},{y}v{CELL}h-{CELL}z"
            cells.append(
                f'<g style="animation-delay:{hit:.2f}s"><path class="a" d="{a}" fill="{fill}" style="animation-delay:{hit:.2f}s"/>'
                f'<path class="b" d="{b}" fill="{fill}" style="animation-delay:{hit:.2f}s"/>'
                f'<rect class="f" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" style="animation-delay:{hit:.2f}s"/></g>'
            )
    gy = PAD_Y + 7 * (CELL + GAP) / 2
    span = 7 * (CELL + GAP) + 24
    # local timeline for every cell: cut at 0, regrow later in the loop
    k = lambda t: f"{100 * t / DUR:.2f}%"
    css = f"""
.a,.b,.f,.z{{animation:{DUR}s linear infinite both}}
.a{{animation-name:ca}} .b{{animation-name:cb}} .f{{animation-name:fl;fill:#fff;opacity:0}} .z{{animation-name:zf}}
@keyframes ca{{0%{{transform:none;opacity:1}}{k(.08)}{{transform:none;opacity:1}}{k(.9)}{{transform:translate(-5px,-9px) rotate(-14deg);opacity:0}}{k(5.6)}{{transform:none;opacity:0}}{k(6.3)},100%{{transform:none;opacity:1}}}}
@keyframes cb{{0%{{transform:none;opacity:1}}{k(.08)}{{transform:none;opacity:1}}{k(.9)}{{transform:translate(4px,10px) rotate(12deg);opacity:0}}{k(5.6)}{{transform:none;opacity:0}}{k(6.3)},100%{{transform:none;opacity:1}}}}
@keyframes fl{{0%{{opacity:0}}{k(.03)}{{opacity:.95}}{k(.35)},100%{{opacity:0}}}}
@keyframes zf{{0%,100%{{opacity:1}}{k(.05)}{{opacity:.35}}{k(.6)}{{opacity:1}}}}
.a,.b{{transform-box:fill-box;transform-origin:center}}
#slash{{animation:sw {DUR}s linear infinite}}
@keyframes sw{{0%{{transform:translateX({PAD_X - 60}px);opacity:0}}{pct(t0 - .15)}{{opacity:0;transform:translateX({PAD_X - 50}px)}}{pct(t0)}{{opacity:1;transform:translateX({PAD_X}px)}}{pct(t1)}{{opacity:1;transform:translateX({width - PAD_X}px)}}{pct(t1 + .25)},100%{{opacity:0;transform:translateX({width + 40}px)}}}}
text{{font:600 11px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:#8b8f98}}
.r{{fill:#e0362c}}
"""
    slash = f"""
<g id="slash">
  <path d="M-4,{gy - span / 2} Q14,{gy} -4,{gy + span / 2} Q4,{gy} -4,{gy - span / 2}z" fill="url(#arc)" filter="url(#glow)"/>
  <path d="M-46,{gy - 2} L-2,{gy - 1} L-2,{gy + 1} L-46,{gy + 2}z" fill="url(#trail)"/>
</g>"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Contribution graph cut by the Dragonslayer">
<defs>
  <linearGradient id="arc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e0362c" stop-opacity="0"/><stop offset=".5" stop-color="#fff"/><stop offset="1" stop-color="#e0362c" stop-opacity="0"/></linearGradient>
  <linearGradient id="trail" x1="0" x2="1"><stop offset="0" stop-color="#e0362c" stop-opacity="0"/><stop offset="1" stop-color="#ffb4a8"/></linearGradient>
  <filter id="glow" x="-200%" y="-20%" width="500%" height="140%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<style>{css}</style>
<rect width="100%" height="100%" rx="10" fill="#0d0f13"/>
<text x="{PAD_X}" y="22">STRUGGLE LOG</text>
<text x="{width - PAD_X}" y="22" text-anchor="end"><tspan class="r">{total:,}</tspan> contributions slain this year</text>
{''.join(cells)}
{slash}
</svg>"""


if __name__ == "__main__":
    if sys.argv[1] == "--demo":
        weeks, total = demo()
    else:
        weeks, total = fetch(sys.argv[1], os.environ["GITHUB_TOKEN"])
    open(sys.argv[2], "w").write(render(weeks, total))
