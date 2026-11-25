<p align="right"><a href="./README.md">EN</a> · <b>RU</b></p>

# hvvze

<img src="./assets/anim/guts.webp" width="27%" align="right" alt="Гатс под Затмением, плащ развевается на ветру">

<img src="./assets/anim/typing-ru.svg" alt="Строю ИИ-агентов и eval-харнессы. От прототипа до рабочего продукта.">

Встраиваю LLM в реальные рабочие процессы (квалификация заявок, CRM-чаты, расширения для Chrome) и гоняю код-харнессы в оффлайн-Docker, прежде чем верить заявлениям на слово.

Сейчас делаю **AIFRND × AIView**, **AIMTHFR** и **Astra + Jev**. Основная разработка идёт в **T3 Code** с агентами Claude, Gemini, GPT и DeepSeek.

<a href="https://t.me/ilovemymoggedlife"><img src="./assets/buttons/telegram.svg" height="28" alt="Telegram @ilovemymoggedlife"></a>

<br clear="right">

<p align="center"><img src="./assets/anim/divider.svg" width="100%" alt=""></p>

## Что я строю

<table>
<tr>
<td width="80" align="center"><a href="https://aifrnd.org/"><img src="./assets/aifrnd-aiview-avatar.png" width="64" height="64" alt="Иконка AIFRND × AIView"></a></td>
<td>
<h3>AIFRND × AIView <sub>· live</sub></h3>
<p>ИИ-пайплайн для интерьерного бизнеса: от первого разговора с клиентом до визуального брифа. AIFRND квалифицирует заявку и собирает требования, AIView по брифу и референсам делает визуализации интерьера.</p>
<p><img src="./assets/anim/aifrnd-aiview.webp" width="100%" alt="AIFRND квалифицирует заявку, собирает бриф, AIView делает визуал"></p>
<p><a href="https://aifrnd.org/">Сайт проекта ↗</a></p>
</td>
</tr>
<tr>
<td width="80" align="center"><img src="./assets/aimthfr-avatar.png" width="64" height="64" alt="Иконка AIMTHFR"></td>
<td>
<h3>AIMTHFR <sub>· в разработке</sub></h3>
<p>Автономный ИИ-оператор продаж и чатов для CRM-платформ креаторов. Ведёт многоходовые диалоги, помнит контекст переписки и может передать чат живому оператору, не выходя из CRM.</p>
<p><img src="./assets/anim/aimthfr-v2.webp" width="100%" alt="AIMTHFR V2 ведёт диалог в CRM с передачей оператору"></p>
<p><a href="https://t.me/ilovemymoggedlife">Спросить про AIMTHFR ↗</a></p>
</td>
</tr>
</table>

<p align="center"><img src="./assets/anim/divider.svg" width="100%" alt=""></p>

## Бенчмарки и эксперименты

<table>
<tr>
<td width="80" align="center"><a href="https://github.com/hqvdvn-cmd/astra-jev-benchmark"><img src="./assets/astra-jev-avatar.png" width="64" height="64" alt="Иконка Astra + Jev Benchmark"></a></td>
<td>
<h3>Astra + Jev Benchmark <sub>· парный пилот DeepSWE · ноябрь 2026</sub></h3>
<p>Парное сравнение чистого Codex CLI (<code>gpt-6.2-sol</code>, <code>high</code>) и <a href="https://github.com/teo-nex/jev-codex-harness"><code>teo-nex/jev-codex-harness</code></a> (<code>cea6502</code>, <code>split-v17-terra6.1-default-sol6.2-hard</code>). Харнесс написал <strong>Teo | Nexcore (<a href="https://github.com/teo-nex">@teo-nex</a>)</strong>. Обе конфигурации решали одни и те же реальные задачи DeepSWE в изолированных Docker-контейнерах без доступа к сети.</p>
<p><strong>4 полные пары (2026-11-24):</strong> чистый Codex решил 4 из 4, <code>jev/auto</code> — 2 из 4. У <code>jev/auto</code> доля попаданий в кэш промпта упала с 96.7% до 35.5%, а некэшированный вход вырос в 22.1 раза (431k → 9.54M). Ни один из 215 вызовов не ушёл в более дешёвую <code>gpt-6.1-terra</code>. Задача #5 остановилась на HTTP 429.</p>
<p><a href="https://github.com/hqvdvn-cmd/astra-jev-benchmark/blob/main/README.ru.md"><img src="./assets/astra-jev-outcomes-ru.png" width="100%" alt="Парный пилот DeepSWE, 4 полные пары: чистый Codex решил 4 из 4, jev-auto — 2 из 4; некэшированный вход 431k и 9.54M (22.1×), около 482k при починенном кэше; выходные токены 120.9k и 147.0k (+21.5%); 0 из 215 вызовов ушло в gpt-6.1-terra"></a></p>
<p><a href="https://github.com/hqvdvn-cmd/astra-jev-benchmark/blob/main/README.ru.md">Репозиторий бенчмарка ↗</a> · <a href="https://github.com/hqvdvn-cmd/astra-jev-benchmark/blob/main/evidence/2026-11-24-deepswe-pilot-10-v1/summary.md">Сводка пилота</a> · <a href="https://github.com/teo-nex/jev-codex-harness">jev-codex-harness</a></p>
</td>
</tr>
</table>

### Другие открытые проекты

<p>
<a href="https://github.com/hqvdvn-cmd/FanslyExtension"><img src="./assets/buttons/fansly-extension.svg" height="46" alt="FanslyExtension"></a>
<a href="https://github.com/hqvdvn-cmd/GutsPetCodex"><img src="./assets/buttons/guts-pet.svg" height="46" alt="GutsPet для Codex"></a>
<a href="https://github.com/hqvdvn-cmd/dota2todeadlock"><img src="./assets/buttons/dota2todeadlock.svg" height="46" alt="Dota 2 → Deadlock: мод с иконками и эффектами предметов"></a>
<a href="https://github.com/hqvdvn-cmd/sekiro-shura-deadlock"><img src="./assets/buttons/sekiro-shura.svg" height="46" alt="Sekiro → Deadlock: визуальный мод для Yamato"></a>
<a href="https://github.com/hqvdvn-cmd/holliday-bandit-deadlock"><img src="./assets/buttons/holliday-bandit.svg" height="46" alt="Holliday Bandit: бандитский скин-ремодель для Holliday в Deadlock"></a>
<a href="https://github.com/hqvdvn-cmd/iwannabeimp"><img src="./assets/buttons/iwannabeimp.svg" height="46" alt="iwannabeimp: мод для Among Us"></a>
</p>

<p>
<a href="https://github.com/hqvdvn-cmd/GutsPetCodex"><img src="./assets/anim/gutspet.webp" width="49%" alt="GutsPet вбегает, машет рукой, подкидывает Бехелит и рубит Драконобором"></a>
<a href="https://github.com/hqvdvn-cmd/FanslyExtension"><img src="./assets/anim/fansly-extension.webp" width="49%" alt="Spicy Scripts: Smart Paste и отложенная отправка в чате"></a>
</p>

<p align="center"><img src="./assets/anim/divider.svg" width="100%" alt=""></p>

**Открыт к ролям AI engineer и product builder, контрактной работе и совместным проектам.**<br>
Пиши в Telegram: [@ilovemymoggedlife](https://t.me/ilovemymoggedlife).
