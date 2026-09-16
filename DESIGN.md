# Design decisions

## Live adaptation plus persistent evidence

Use prior records as hypotheses, then update through current performance. Transcripts are not learning
records, and old success does not imply retention. A dependency diagram is a teaching aid, not an
implemented knowledge-tracing model.

## Bound the probe

Exhaustively bracketing every prerequisite can exhaust a learner before teaching begins. Default to
five questions or five minutes and make uncertainty visible. Beginners need orientation, not a test
whose every answer is wrong.

## Motivate without claiming certainty

Build explanations from definitions, assumptions and evidence. Do not replace qualified statements
with attractive but false universals. A fact-checking agent may repeat the same mistake as a teacher.

## Recognition is not production

Multiple choice is optional diagnostic support, not the only assessment channel. Independent fresh tasks,
delayed checks, explicit assistance and transfer provide stronger evidence. Store the distinction.

## Memory is a protocol, not magic

Local Markdown makes state inspectable and portable. Retention practices need the user to return;
this package does not implement automatic reminders or a validated scheduling algorithm.

## Keep dependencies optional

A file-capable agent can run the core dialogue. Browser widgets, quiz extensions, researchers, images,
Obsidian, and HTML artifacts can improve delivery, but should not gate access to learning.

## Claims corrected from the initial comparison

A skill recommending spacing is not the same as a scheduling implementation. Conversely, a session log
can be reread even if a repository does not define a structured learner-state protocol. These distinctions
are why this package supplies explicit record formats and a transparent, manual review rule rather than
claiming either upstream design proves learning effectiveness.
