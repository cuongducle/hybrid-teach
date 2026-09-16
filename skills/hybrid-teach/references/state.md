# Durable learning state

All paths are relative to the user-approved workspace, not the installed skill.
Prefer a directory outside source repositories. Inside Git, check tracked paths: ignore rules do not
protect already tracked files. Publishing, changing ignore rules and untracking need separate consent.
Local storage does not prevent cloud sync or transmission of read content to a hosted model provider.

## Checkpoint and recovery

Create files lazily. Read before editing and preserve unrelated content. Checkpoint meaningful evidence
after an independent attempt, diagnosed/corrected misconception, or approved mission change.
Write the learning record first, then update the index and review queue referencing its ID.
Use sequential IDs after inspecting filenames; never overwrite a colliding record.
Report failed writes. On return, reconcile records with the index/queue without duplicating review items.
Re-read before edits; reconcile concurrent changes or ask rather than overwriting another session.
This is a manual recovery protocol, not transactional storage.

## MISSION.md

```markdown
# Mission
- Outcome: observable task
- Success criteria: how we will check it
- Prior experience: self-reported unless tested
- Constraints: time, budget, tools, accessibility
- Exclusions: adjacent topics not pursued
- Preferences: language, pace, output medium
```

Confirm substantive mission changes and record why.

## LEARNER.md

```markdown
# Learner map
| Concept / task scope | Assistance | Checked on / delay | Transfer | Verification | Record | Next check |
|---|---|---|---|---|---|---|
| Explain a definition | not assessed | — | untested | introduced | — | fresh explanation |
```

- Scope: recall, explanation, calculation, debugging, application, etc.
- Assistance: not assessed / independent / hints / worked solution / self-report.
- Delay: immediate or actual time since relevant learning/practice; unknown stays unknown.
- Transfer: untested / attempted / demonstrated, with specified changed conditions.
- Verification: introduced / checked / disputed / unverified.

Do not collapse these into a permanent mastery score. Delayed recall does not establish transfer.
A dependency map is optional and does not replace evidence.

Migration: preserve old records with Evidence level. Map only supported facts; missing scope, delay
and transfer remain unknown. The old label retained alone must not imply application competence.

## learning-records/0001-topic.md

```markdown
# Concept or meaningful change
- Date: YYYY-MM-DD
- Status: active (or superseded by 000N-topic.md)
- Task/scope: question or reproducible task
- Evidence: what the learner actually did
- Assistance: none / hints / worked solution / self-report; specify
- Delay: immediate / elapsed time / unknown
- Transfer: untested / attempted / demonstrated; specify changed conditions
- Verification: checked / disputed / unverified; method or unresolved issue
- Interpretation: what this supports and what it does NOT establish
- Next check: fresh application or delayed recall
```

Avoid unnecessary personal data or whole transcripts. Exposure can update the index as introduced,
not as understanding. An unresolved grading dispute is not a learner misconception. Supersede erroneous
records without deleting history. Do not label an attempted correction successful without new evidence.

## RESOURCES.md

```markdown
# Sources
| Source / URL / section | Used for | Verification status / limits |
|---|---|---|
```

Include relevant edition/version, supported claims, and explicit gaps. Optional trusted communities.

## REVIEW.md

```markdown
# Recall queue
| ID | Concept / scope / record | Prompt (no answer) | Due date | Last checked | Last result / evidence ID | Stage | Interval override |
|---|---|---|---|---|---|---|---|
```

Keep checked solutions/rubrics separate from prompts. Stage 0 is for new items only. Follow the
transition table in assessment.md; closing a session never resets existing schedules.
Use separate tasks for different scopes, and avoid duplicate items on resume. Keep disputed items on
hold; preserve their last due date/stage until adjudication. Log attempts as evidence records, including
assisted, failed or disputed attempts. No background reminders are provided.

## reference/ and optional lessons/

Reference notes contain reusable definitions, examples, caveats and citations. Optional HTML lessons
may share assets/ and link to references. These artifacts are not evidence that their contents were learned.
