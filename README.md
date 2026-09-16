# Hybrid Teach

A portable tutoring skill combining **adaptive in-session teaching** with **durable, evidence-backed learning state**. Written for Vietnamese or English dialogue; no specific model, extensions, subagents, or Obsidian required.

> Diagnose briefly → agree on a grounded plan → teach one motivated step → practice independently → record evidence → revisit later.

## Install in pi

```bash
git clone https://github.com/cuongducle/hybrid-teach.git ~/.local/share/hybrid-teach
mkdir -p ~/.pi/agent/skills
ln -s ~/.local/share/hybrid-teach/skills/hybrid-teach ~/.pi/agent/skills/hybrid-teach
```

If either destination already exists, inspect it first; do not overwrite an existing skill. Start a new pi session (or reload skills), then:

```text
/skill:hybrid-teach Tôi muốn học Rust để viết một CLI xử lý CSV. Tôi biết Python, có 30 phút mỗi ngày.
```

Other file-capable agents can load `skills/hybrid-teach/SKILL.md` and its relative references. Their skill installation mechanisms differ; this repo does not claim tested compatibility with every harness.

## What it does

- Clarifies an observable mission and offers orientation to absolute beginners.
- Caps initial diagnosis (default 5 questions or 5 minutes), then checks gaps as needed.
- Separates definitions, assumptions, evidence and uncertain claims.
- Uses motivated reasoning steps, optional dependency diagrams, and adaptive hints.
- Prioritizes free-response, fresh problems and transfer over multiple-choice recognition.
- Records evidence and assistance, not just topics covered.
- Maintains a recall queue with a simple 1/3/7/14-day starting heuristic.
- Reads prior records on return; no full re-probe required every session.

## Private learning workspace

The agent asks where to store your data, separately from the installed skill:

```text
~/learning/<topic>/
  MISSION.md
  LEARNER.md
  RESOURCES.md
  REVIEW.md
  learning-records/0001-topic.md
  reference/
  lessons/    # optional HTML
```

Prefer a directory outside source repositories. Ignore rules do **not** protect files already tracked by Git; inspect tracked paths before writing. This skill must not change ignore rules, untrack or publish personal records without separate consent. Local files can still be cloud-synced, and a hosted model provider may receive content the agent reads.

## Example session

1. Agree a goal: parse a CSV and report malformed rows.
2. Ask a short prerequisite task, not an entire exam.
3. Offer a 3-node plan and wait for approval.
4. Explain one concept, ask for a prediction, then offer a small exercise.
5. Give a fresh independent task; note any hints honestly.
6. Checkpoint meaningful evidence during the session; schedule new review items without resetting existing ones. On return, reconcile state and check the queue before new material.

Evidence tracks scope, assistance, delay, transfer and verification separately. Disputed grading is put on hold, not treated as a learner misconception.

## Limitations

This is an instruction package, not an enforced state machine, validated diagnostic test, scheduler service, or standalone app. A model may fail to follow it. Review dates do not produce notifications. Sources and generated answers can be wrong; another model or visual inspection cannot guarantee correctness. No empirical learning-effectiveness claim is made.

Spacing is requested by the protocol; it is not an automatic spaced-repetition engine. Optional HTML, diagrams and external tools depend on the agent's capabilities.

## Validation

```bash
python3 scripts/check.py
python3 -O scripts/check.py
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

Static checks cover metadata, bundled reference links and required files. Regression tests include invalid metadata under Python optimization; checks never rely on removable `assert` statements. Manual behavioral evaluation scenarios live in `skills/hybrid-teach/references/assessment.md`; they have not been run as model benchmarks.

## Inspiration and differences

Original implementation inspired by:

- [Eero Alvar — learn](https://github.com/amosblomqvist/learn): adaptive diagnosis, motivated derivations, small-step feedback.
- [Matt Pocock — skills](https://github.com/mattpocock/skills): mission-centered workspaces, durable learning records, sources and long-term practice.

No upstream source files or extensions are bundled. Unlike either exact workflow, this skill deliberately bounds diagnosis, supports beginners and free-response assessment, avoids unconditional-truth overclaims, and separates evidence levels. See [DESIGN.md](DESIGN.md).

MIT licensed; see [LICENSE](LICENSE).
