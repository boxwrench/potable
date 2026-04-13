# Roadmap

## Phase 0: Public setup — COMPLETE

- GitHub repo, Hugging Face dataset card, Hugging Face model card
- Repository structure, naming conventions, reference docs

## Phase 1: Seed dataset — IN PROGRESS

Infrastructure complete. Content authoring is the remaining work.

Done:
- System prompt, style guide, taxonomy, schema docs
- Toolchain: validate, export, stats, eval, scaffolding (interactive and batch)
- CI validation on push/PR
- 16-category municipal taxonomy
- Golden eval set (8 cases across 8 categories)
- Seed topic planning (26 topics across all 16 categories)

Remaining:
- Author first batch of seed examples
- Review and approve initial records

## Phase 2: Minimum viable dataset

- Grow dataset toward first fine-tune
- Run first municipal fine-tune
- Expand golden eval set

## Phase 3: Public release and tooling

- Release community dataset tier on Hugging Face
- Publish model evaluation notes
- Eval harness
- Agentic layer (potable-agent)
- Plugins and skills for IDE and CLI integration

## Phase 4: Developing regions track

- Develop WASH taxonomy
- Create seed WASH examples
- Evaluate small-model performance on offline hardware targets
- Philanthropic funding and partnerships
