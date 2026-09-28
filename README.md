# paper-drill

Autonomous academic discovery + Obsidian graph engine for network intrusion
detection research. Server (`workstation`, `114.71.220.60`) does everything;
this repo is mirrored via git. Mac only reads (Obsidian vault, ssh tunnel).

## What it does

Daily: ingest newest papers per scope → rank by embedding similarity →
LLM-extract (novelty/method/limitations/future-work/hubs/score) → write
Obsidian notes → cross-scope gap synthesis → dashboard regen → commit + push.
Backfill mode pages the 2024→now archive per quarter.

## Layout

- `pipeline/` — `ingest.py` (OpenAlex, 429 backoff, ID dedupe, new/backfill
  modes) · `rank.py` (zembed-1 cosine vs thesis, empty-safe) · `extract.py`
  (locked v2 prompt) · `writer.py` (notes, hub normalize, dedent) ·
  `gap.py` (daily ideas + `--cross` fusion) · `llm.py` (shared chain) ·
  `dashboard.py` (Dashboard.md) · `dashboard_server.py` (:18080 web UI) ·
  `deepseek_web.py` / `glm_web.py` (zendriver web clients, token auth)
- `config/scopes/` — `ivn` (CAN), `iot-ids`, `nids`, `edge-ai`. Thesis +
  keywords + datasets each. Papers/concepts vault shared (cross-pollination
  by design); state/cursor/ideas per scope.
- `vault/` — `papers/`, `concepts/`, `ideas/` (+`cross-*.md`), `Dashboard.md`.
  Generated on server, pushed for Mac Obsidian.
- `ops/` — `daily.sh` (scope loop + cross, flock, cron.log), `dashboard.sh`.
- `notebooks/` — `01` extraction probe · `02` embedding shootout ·
  `03` idea probe · `04` deepseek-web probe · `05` glm-web probe.
- `.scratch/research-assist/` — wayfinder map + decision tickets.

## LLM chain (order matters)

DeepSeek-web → GLM-web → Qwen-local (`llama.cpp :8080`) → skip.
`llm.py` detects content failures (`at capacity`, `Thinking...` indicators).
Qwen = last resort (simple tasks). Secrets in server `~/.paper-drill.env` +
repo `.env` (gitignored, never commit). Daily never overwrites good notes
with stubs; cross refuses empty input loudly.

## Deploy

User cron `0 2 * * * .../ops/daily.sh` (flock, cron.log). Dashboard `:18080`
localhost-only (`ssh -L 18080:localhost:18080 workstation`). Push via
`credential.helper='!/snap/bin/gh auth git-credential'` (snap gh path;
plain `gh auth setup-git` silently no-ops). Chrome lives in `.browsers/`
(gitignored, 954M — never commit; GitHub caps 100M).

## Agent workflow rules

1. Ponytail full: laziest diff that holds; YAGNI; stdlib first.
2. Every function gets a one-line docstring (AGENTS.md).
3. Server-first: iterate in `/mnt/data2/ntmduy/paper-drill` over ssh;
   commit here only on working states. Builders (no ssh tool) work local.
4. Never print/commit secrets. Never commit `.browsers/`, `cron.log`,
   `.env`, Obsidian workspace files.
5. `pkill -f` self-matches over ssh — kill by port (`fuser -k`) instead.
6. Verify with real runs; mocked-only verification hides live bugs (429s,
   empty-list crashes both escaped mocks once).

## Current CONS (honest, 2026-09-28)

1. Corpus thin: ~10 papers. Daily finds 0 new most days; backfill pilot
   (ivn Q1-2024) done, full 2024→now loop not yet launched.
2. Hub sprawl: ~80% of `[[Concept - X]]` single-use; reuse prompt helps,
   no canonical registry/merge pass yet.
3. Limitations thin: abstracts rarely state them; full-text `publisher_fetch`
   (IEEE verified inst 44445) not wired — extraction quality capped.
4. Browser LLM fragility: web clients break on site deploys (selectors),
   capacity nights, token expiry; chain degrades gracefully but slowly
   (one browser launch per call, 5+ min per paper end-to-end).
5. Scores: LLM-parsed, fallback rank*10 on old notes (0.9–10 spread ok).
6. No citation edges: S2 refs/cites never wired; graph = hubs + ideas links
   only, papers don't backlink ideas notes.
7. Cron env drift: secrets live outside git; new keys must be added by hand
   on server or nightlies silently skip (now logged).
8. Single-server SPOF: no backups; `.browsers/` + models unversioned.
