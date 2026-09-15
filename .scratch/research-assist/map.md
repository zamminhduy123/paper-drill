## Destination

Full autonomous discovery app running daily on campus server (4x GPU, llama.cpp Qwen-27B + local embeddings), ingesting newest Applied AI/ML/DL papers first then expanding, writing citation + concept + semantic Markdown into `vault/` synced via git for local Obsidian Connected-Papers view.

## Notes

- Domain: Applied AI/ML/DL. Stack: Python Docker + systemd timer, OpenAlex + arXiv + S2, campus IEEE verified (Soonchunhyang inst 44445).
- Skills every session should consult: grilling, domain-modeling, research, prototype.
- Standing preferences: zero external cost, open-abstracts-first, git text-only vault (no PDFs/state.db), local graph depth 2.

## Decisions so far

- [Domain = Applied AI/ML/DL, arXiv + OpenAlex + S2](.scratch/research-assist/issues/00-prior.md): open-only v1, PubMed deferred.
- [Vault = new, papers/concepts/ideas + Dataview, Juggl v2](.scratch/research-assist/issues/00-prior.md): scaffold done.
- [Execution = campus server + git sync, size OK](.scratch/research-assist/issues/00-prior.md): 5-10KB/note, <200MB/yr.
- [LLM = Qwen-27B via llama.cpp + bge-m3, IEEE campus OK](.scratch/research-assist/issues/00-prior.md): stampPDF 2-step flow verified 200 application/pdf.

## Not yet specified

- Exact OpenAlex/S2 query shapes + rate-limit handling on server IP.
- Embedding choice final (bge-m3 vs Qwen-embedding) + 0.80 threshold validation.
- Extraction prompt quality from Qwen-27B — needs seen output.
- Publisher_fetch robustness (session renewal, Elsevier parity).
- Deployment shape (systemd timer + auto-push + secrets).

## Out of scope

- Embedding connectedpapers.com itself; we recreate view natively.
- Juggl typed edges (v2), paywall PDF parsing bulk, PubMed/ChemRxiv, paid LLM default.
