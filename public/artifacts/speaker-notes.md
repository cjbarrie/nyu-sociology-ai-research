# Presenter notes

15-minute walkthrough, followed by five minutes of discussion. Pre-open the opening readings, workshop index, evidence table and protocol PDF. The four opening slides take four minutes; each archetype then gets forty seconds. Links in the slides open the private hosted copies; offline users should use the local workshop index.

## Slide 1

0:00–0:30. Introduce the presenters and the topic briefly. Continue to the three opening images; the comparison with last year comes later in the presentation.

## Slide 2

0:30–0:45. Opening aside: Coxon. User-supplied image within the presentation frame, without added claims or captions.

## Slide 3

0:45–1:00. Opening aside: Amodei. User-supplied image within the presentation frame, without added claims or captions.

## Slide 4

1:00–1:15. Opening aside: Trump. User-supplied image within the presentation frame, without added claims or captions.

## Slide 5

1:15–2:20. Discuss the evidence by design. Lee measures reported effort; Bastani measures subsequent unaided mathematics performance. Neither is a longitudinal study of faculty cognitive decline. Risko and Gilbert provide the broader offloading framework. Sparrow and the EEG preprint are in the readings for discussion, rather than the core slide.

## Slide 6

2:20–3:25. These are different evaluations, not a head-to-head comparison. Co-Scientist includes expert selection and laboratory validation. The two CRUX cases show a gap between execution and research judgment; do not universalize two cases. METR reports benchmark task durations in human-time units, not autonomous scientific runtime. This evidence concerns what systems can do; the preceding slide concerns effects on people.

## Slide 7

3:25–4:00. Use this as a reminder of last year’s session, not a literal history of product capabilities. The exchange is illustrated. Chat can also be intellectually collaborative, and it remains useful. The new point is that execution can now happen inside the same research environment.

## Slide 8

4:00–4:45. In the browser, click the stages: assignment, parallel work, cross-checking, revision. Explain harness once as the software around the model that handles tools, state and execution. Saved project files allow continuation beyond one conversation window. This schematic combines common architectural patterns; it is not a faithful diagram of one vendor product. Agent agreement still needs source and substantive checks.

## Slide 9

4:45–5:25. Here the researcher specifies a task with a checkable result. Execution can be delegated, but responsibility for the result remains with us. An example is reproducing a figure: compare data, axes, values and exclusions, rather than just seeing that an image appeared. This is one working relationship, not the lowest rung of a hierarchy.

## Slide 10

5:25–6:05. The point is to put review at a consequential choice. Asking to see measures before analysis is useful; asking it to report every trivial step is usually not. We can give reasons for a change and have it follow the implications through code, tables and writing. We should inspect the revised result, not just the acknowledgement.

## Slide 11

6:05–6:45. This is a paired intellectual relationship, not outsourcing a referee report. You explain your interpretation; it raises a problem; you answer; the project changes through the exchange. The third mode describes an intellectual role, while the first two emphasize delegation. We can move among all three during the same project. AI objections can be wrong, and agreement is not a validation test.

## Slide 12

6:45–7:20. The headline is a cropped screenshot of the actual article. Use this question to introduce what an agent-assisted research workflow can do: find papers, compare findings, check citations and write a synthesis. We steer the search, question its interpretation and ask it to revise. This slide introduces the demonstration, not a full research design. Open the article briefly if useful, then move to the research folder.

## Slide 13

7:20–8:35. Open the how-to page. Click SKILL.md and show that it is a readable instruction file. Explain the project paths: .agents/skills in Codex, .claude/skills in Claude Code. Show the exact invocation and prompt. Click Run a script to explain the illustrative workflow: an agent calls Python, the script queries a literature API and saves records, then the agent reads and checks the returned material. The command is a teaching example; that script is not included or claimed to have run. The skill codifies the original workflow; do not imply the original review was produced by a recorded run of this skill. The local Claude login expired and the Codex CLI binary was unavailable, so no authentic skill-invocation clip is included. Official setup links are on the page. Keep this explanation practical.

## Slide 14

8:35–9:55. Show the products of the 8 September search: nine evidence records, retrieval log and bibliography. Each table record links to its primary source and names the source version and access limits. Fang v2 remains accessible through its record, rather than a disconnected slide-level link. The later source review shows what was checked and corrected. These outputs fed the proposal compiled on 9 September; the reusable skill codifies this earlier workflow.

## Slide 15

9:55–10:50. Open the scripted exchange. Read two or three turns, not the entire page. The researcher first proposes a mechanism, then clarifies requests rather than harm, then proposes a denominator. The AI raises selection and the researcher chooses a narrower protocol. The AI does not win an argument or dictate a specification. Explain the denominator issue in ordinary language: the set of situations being counted could itself change with treatment. Make clear that researcher turns are illustrative.

## Slide 16

10:50–12:30. Open the actual reports. Show the source locators and the methods reviewer’s questions. Then show each cross-check at the end of its report. These are actual separate Codex agents used during revision. Multiple agents can share a mistake, so the source and substantive question remain the test. Point to one open researcher decision: who is the target population? Do not answer it on Christopher’s behalf.

## Slide 17

12:30–14:00. Open the compiled proposal and show the evidence assessment, proposed study and draft instrument. The production details remain available in the PDF and supporting files, rather than on this slide.

## Slide 18

14:00–15:00. Introduce these as open questions, not demonstrated harms or agreed norms. Influence: useful suggestions can become starting assumptions; consider noting the original question and consequential changes. Reproducibility: distinguish rerunning final code, auditing decisions, and rerunning the agent. Reading: ask which central sources researchers must consult themselves. Leave this slide up for five minutes of discussion. Ask for one practice colleagues would expect of a student or coauthor and whether they would follow it themselves. Full suggested talking points: /artifacts/discussion-notes.md.

---

# Closing discussion: suggested talking points

Use the last minute of the talk to introduce the three questions. Leave the slide visible for the five-minute discussion. These are open questions and possible norms to debate, not findings established by this demonstration.

## 1. Influence on the researcher

Even a critical, collaborative exchange can shape what seems worth asking. The issue is not only accepting a wrong answer: an agent might supply the initial categories, comparisons or explanations, and those may become the project’s defaults. Human coauthors also influence one another; what would make this influence different, and how would we notice it?

Ask: “Can you think of a case where a useful AI suggestion changed the question you were trying to answer?” Then: “How would we distinguish productive intellectual influence from narrowing the possibilities too early?”

Possible norms to discuss: write down the question and your initial reasoning before consulting an agent; request plausible alternative framings; keep a short record of consequential changes and why you accepted them. An agent’s disagreement is useful input, not proof that a decision has been independently checked.

## 2. Reproducing an agent-assisted pipeline

Distinguish three goals: rerunning the saved analysis code; inspecting how the agent arrived at it; and rerunning the agent itself to see whether it follows the same path. Those are different standards. A transcript is not an executable analysis, and the same final answer is not necessarily the same research process.

Ask: “What would you need in a replication package to evaluate this project?” Discuss source snapshots or stable identifiers, search dates and queries, the exact skill and prompt, model/version information where available, tool and dependency versions, returned tool data, final code, and records of researcher interventions. Respect source-access and confidentiality restrictions when sharing records.

Possible norm: preserve the final analysis as ordinary runnable code and retain enough of the agent’s search and decisions to audit consequential choices. Which parts need exact repetition, and which require an independently defensible result? What should a reviewer require when the original model or service is no longer available?

## 3. Deep reading and source consultation

A summary may help identify what to read, but what happens when it becomes the main encounter with a paper, interview or archival source? Which insights depend on reading an argument’s development, noticing qualifications, or encountering something outside the original query?

Ask: “Which sources would you insist on reading yourself before putting your name on the paper?” Include qualitative and theoretical work, not just methods sections and numerical claims.

Possible norms to discuss: personally read sources central to the argument; distinguish first-hand reading from a summary or abstract; protect time for reading without an agent’s framing; return to source passages when a synthesis becomes consequential. Avoid treating a checked citation as evidence that the surrounding argument has been understood.

## Closing invitation

“What is one practice we would want a student or coauthor to follow—and would we follow it ourselves?”

If discussion stalls, ask colleagues to choose one candidate norm from the three areas and say what would make it workable. The aim is to surface disagreements about standards, rather than to adopt a departmental policy in five minutes.
