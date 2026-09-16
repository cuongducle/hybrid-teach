# Durable learning state

All paths below are relative to the user-approved learning workspace, not this skill.
Create files lazily. Inspect existing content and preserve unrelated notes. Use sequential record IDs
by inspecting existing filenames. File writes are local; publishing needs separate consent.

## MISSION.md

```markdown
# Mission
- Outcome: observable task the learner wants to perform
- Success criteria: how we will check it
- Prior experience: self-reported, not yet verified
- Constraints: time, budget, tools, accessibility
- Exclusions: adjacent topics we will not chase
- Preferences: language, pace, output medium
```

Confirm substantive mission changes with the user and record why.

## LEARNER.md

A compact, revisable index, not a numerical intelligence score.

```markdown
# Learner map
| Concept | Evidence level | Evidence record | Uncertainty / next check |
|---|---|---|---|
| Example concept | introduced | — | independent task needed |
```

Levels: self-reported / introduced / assisted / independent / retained.
“Retained” requires a successful delayed check. None means permanent mastery.
A dependency map may be included; uncertainty is better than invented precision.

## learning-records/0001-topic.md

```markdown
# Concept or meaningful change
- Date: YYYY-MM-DD
- Status: active (or superseded by 000N-topic.md)
- Task: question or independently reproducible task
- Evidence: concise description of what the learner actually did
- Assistance: none / hints / worked solution; specify what
- Interpretation: what this supports and what it does NOT establish
- Next check: fresh application or delayed recall
```

Do not retain unnecessary personal information. Do not copy entire conversations as evidence.
Log corrected misconceptions, independently demonstrated skills, prior-knowledge disclosures, or mission
changes. Exposure alone may update “introduced” in LEARNER.md but is not evidence of understanding.

## RESOURCES.md

```markdown
# Sources
| Source / URL / section | Used for | Verification status / limits |
|---|---|---|
```

Include edition/version where relevant. A citation supports only the claim it actually covers.
Keep gaps visible. Optional separate section for trusted communities or practitioners.

## REVIEW.md

```markdown
# Recall queue
| ID | Concept / record | Prompt (no answer) | Due date | Last result | Success stage |
|---|---|---|---|---|---|
```

Store solutions separately from prompts and do not reveal them before an attempt.
Success stage starts at 0; advance only after independent recall. A hint-assisted answer does not advance.
On a miss, repair the misconception and schedule a fresh check sooner. Preserve the last result.
Do not promise notifications: review happens when the user returns.

## reference/ and optional lessons/

Reference notes contain concise reusable definitions, examples, caveats and citations.
Optional numbered HTML lessons may share assets/ and link to reference material.
These artifacts do not prove the learner has learned their contents.
