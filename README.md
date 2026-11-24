<p align="right"><b>EN</b> · <a href="./README.ru.md">RU</a></p>

# hvvze

<img src="./assets/anim/guts.webp" width="27%" align="right" alt="Guts beneath the Eclipse, cape moving in the wind">

<img src="./assets/anim/typing.svg" alt="Building AI agents & eval harnesses. From rough prototype to shipped tool.">

I build AI agents, eval harnesses, and web tools, and take them from first prototype to production.

Currently working on **AIFRND × AIView**, **AIMTHFR**, and the **Astra + Jev** benchmark.

**Areas:** AI agents and workflows · evals and browser automation · web apps and Chrome extensions<br>
**How I work:** coding with Claude, Gemini, GPT, and DeepSeek agents in T3 Code

<a href="https://t.me/ilovemymoggedlife"><img src="./assets/buttons/telegram.svg" height="28" alt="Telegram @ilovemymoggedlife"></a>

<br clear="right">

<p align="center"><img src="./assets/anim/divider.svg" width="100%" alt=""></p>

## What I'm building

<table>
<tr>
<td width="80" align="center"><a href="https://aifrnd.org/"><img src="./assets/aifrnd-aiview-avatar.png" width="64" height="64" alt="AIFRND × AIView icon"></a></td>
<td>
<h3>AIFRND × AIView <sub>· live</sub></h3>
<p>An AI pipeline for interior design businesses that runs from the first client conversation to a visual brief. AIFRND qualifies the lead and collects requirements; AIView turns the brief and reference images into interior visuals.</p>
<p><img src="./assets/anim/aifrnd-aiview.webp" width="100%" alt="AIFRND qualifies a request, builds a brief, and AIView renders a visual"></p>
<p><a href="https://aifrnd.org/">Project site ↗</a></p>
</td>
</tr>
<tr>
<td width="80" align="center"><img src="./assets/aimthfr-avatar.png" width="64" height="64" alt="AIMTHFR icon"></td>
<td>
<h3>AIMTHFR <sub>· in development</sub></h3>
<p>An autonomous AI sales and chat operator for creator CRM platforms. It runs multi-turn conversations, keeps track of context, and can hand a chat over to a human operator without leaving the CRM.</p>
<p><img src="./assets/anim/aimthfr-v2.webp" width="100%" alt="AIMTHFR V2 managing a conversation inside the CRM with operator handoff"></p>
<p><a href="https://t.me/ilovemymoggedlife">Ask me about AIMTHFR ↗</a></p>
</td>
</tr>
</table>

<p align="center"><img src="./assets/anim/divider.svg" width="100%" alt=""></p>

## Benchmarks & experiments

<table>
<tr>
<td width="80" align="center"><a href="https://github.com/hqvdvn-cmd/astra-jev-benchmark"><img src="./assets/astra-jev-avatar.png" width="64" height="64" alt="Astra + Jev Benchmark icon"></a></td>
<td>
<h3>Astra + Jev Benchmark <sub>· DeepSWE paired pilot · Nov 2026</sub></h3>
<p>A paired comparison of plain Codex CLI (<code>gpt-6.2-sol</code>, <code>high</code>) and <a href="https://github.com/teo-nex/jev-codex-harness"><code>teo-nex/jev-codex-harness</code></a> (<code>cea6502</code>, <code>split-v17-terra6.1-default-sol6.2-hard</code>), built by <strong>Teo | Nexcore (<a href="https://github.com/teo-nex">@teo-nex</a>)</strong>. Both setups ran the same real DeepSWE repository tasks in isolated Docker containers with no network access.</p>
<p><strong>4 complete pairs (2026-11-24):</strong> plain Codex passed 4/4, <code>jev/auto</code> passed 2/4. With <code>jev/auto</code>, the prompt cache hit rate fell from 96.7% to 35.5% and uncached input grew 22.1× (431k → 9.54M). None of its 215 calls were routed to the cheaper <code>gpt-6.1-terra</code>. Task #5 stopped on HTTP 429.</p>
<p><a href="https://github.com/hqvdvn-cmd/astra-jev-benchmark"><img src="./assets/astra-jev-outcomes-en.png" width="100%" alt="DeepSWE paired pilot, 4 complete pairs: plain Codex passed 4/4 and jev-auto 2/4; uncached input 431k vs 9.54M (22.1×), about 482k with the cache fixed; output tokens 120.9k vs 147.0k (+21.5%); 0 of 215 calls routed to gpt-6.1-terra"></a></p>
<p><a href="https://github.com/hqvdvn-cmd/astra-jev-benchmark">Benchmark repo ↗</a> · <a href="https://github.com/hqvdvn-cmd/astra-jev-benchmark/blob/main/evidence/2026-11-24-deepswe-pilot-10-v1/summary.md">Pilot summary</a> · <a href="https://github.com/teo-nex/jev-codex-harness">jev-codex-harness</a></p>
</td>
</tr>
</table>

### Other public projects

<p>
<a href="https://github.com/hqvdvn-cmd/FanslyExtension"><img src="./assets/buttons/fansly-extension.svg" height="46" alt="FanslyExtension"></a>
<a href="https://github.com/hqvdvn-cmd/GutsPetCodex"><img src="./assets/buttons/guts-pet.svg" height="46" alt="GutsPet for Codex"></a>
<a href="https://github.com/hqvdvn-cmd/dota2todeadlock"><img src="./assets/buttons/dota2todeadlock.svg" height="46" alt="Dota 2 → Deadlock: item icons and effects mod"></a>
<a href="https://github.com/hqvdvn-cmd/sekiro-shura-deadlock"><img src="./assets/buttons/sekiro-shura.svg" height="46" alt="Sekiro → Deadlock: Wolf / Shura visual mod"></a>
<a href="https://github.com/hqvdvn-cmd/iwannabeimp"><img src="./assets/buttons/iwannabeimp.svg" height="46" alt="iwannabeimp: Among Us role-request mod"></a>
</p>

<p>
<a href="https://github.com/hqvdvn-cmd/GutsPetCodex"><img src="./assets/anim/gutspet.webp" width="49%" alt="GutsPet runs in, waves, tosses the Behelit and swings the Dragonslayer"></a>
<a href="https://github.com/hqvdvn-cmd/FanslyExtension"><img src="./assets/anim/fansly-extension.webp" width="49%" alt="Spicy Scripts: Smart Paste and scheduled sending in a chat"></a>
</p>

<p align="center"><img src="./assets/anim/divider.svg" width="100%" alt=""></p>

**Open to AI engineer and product builder roles, contract work, and collaborations.**<br>
Message me on Telegram: [@ilovemymoggedlife](https://t.me/ilovemymoggedlife).
