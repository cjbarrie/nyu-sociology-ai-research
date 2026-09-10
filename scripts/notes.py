import json,pathlib
notes=[
'''Last year our conversation was largely about generated student responses and essays: what students could hand in, and what that meant for assessment. Today I want to move the discussion into our own research practice. The interesting question is how much of a research workflow these systems can now execute, and how we should work with them when they can.

I will distinguish three modes of collaboration, then show a single project moving through literature search, source checking, coding, analysis and a compiled research memo. These artifacts were actually produced for this presentation. The long operations are prepared recordings; I will identify them. This is a comparison of ways of working, not a controlled benchmark against last year’s model.

Cue: advance at 01:00. There is no need to open an application yet.''',
'''The first mode is complete cognitive offloading: do this and bring it back. This works particularly well for a bounded task where the output is inspectable. For example, reproduce a figure from a replication package and document anything that does not match. Or assemble bibliographic records and turn an existing manuscript into LaTeX.

The agent can inspect files, execute code, see the output, and try again when something fails. You are delegating a task, rather than repeatedly copying suggestions from a chat window into another program. What matters is the acceptance criterion. What would count as a successful reproduction?

The failure mode is easy to recognize: the result looks finished, so we treat it as checked. I distinguish offloading execution from offloading responsibility. I may not want to perform every step myself, but I still need to know how I will assess the result.

Cue: advance at 02:00.''',
'''The second mode is guided collaboration. The AI is responsible for a lot of the execution, but you intervene where a research decision matters. You might have it propose an operationalization before it estimates anything, then change that choice after looking at the actual data or survey items.

The value of the agentic environment becomes especially clear when a decision has consequences across several files. It can change the code, rerun it, regenerate a figure, update the prose and compile the document. Those operations remain connected.

But the amount of conversation is not a measure of the quality of supervision. If we just accept each proposal, the supervision can become a rubber stamp. In the example today, the crucial intervention is to add a mechanism the initial model leaves out.

Cue: advance at 03:00.''',
'''The third mode is the pain-in-the-ass coauthor. Find the strongest objection to this conclusion and substantiate it. Look for counterevidence. Inspect the specification. Tell me which assumption I am relying on without acknowledging it.

This is a different intellectual role, not simply another point on an autonomy scale. A skeptical reviewer can work independently, and a heavily supervised assistant can still reinforce our assumptions. These are modes we can move between within one project, rather than a hierarchy of good and bad users.

The critic also needs checking. Ask it to locate the relevant passage, derive the result, or construct a counterexample. Confident criticism is not automatically correct. We will see that the model’s most impressive result is also something the critic can explain almost immediately from its rules.

Cue: advance at 04:00.''',
'''Here is the actual research question: do AI chatbots reduce support-seeking from friends and family? It is concrete, sociologically interesting, and easy to answer too quickly.

I gave the agent a connected assignment: find the evidence, separate competing mechanisms, implement a small agent-based model, run sensitivity analyses, and write a cited LaTeX memo. The deliverable is a research project with inspectable intermediate outputs.

Keep two meanings of agent separate. The AI research agent does the work. The agents in the model are simulated people governed by explicit rules; they are not language models impersonating human research participants.

Cue: advance at 05:00. The ABM is only one output of this pipeline.''',
'''The first output is a small evidence collection. The agent searched, retrieved sources, checked metadata and organized the results. The research folder contains the query log, a structured evidence table, the bibliography and a retrieval manifest.

Open the evidence table briefly. Each row records the design, the outcome, the finding and the limit on interpretation. We retained eight papers as core or mechanism context, plus one professional-help study as a scope boundary. Two records were accessible only as institutional abstracts and metadata. This is a bounded scoping exercise, not a systematic review.

Play the source-retrieval recording for about ten seconds, then close it. It is actual command output, replayed for readability, including access failures. It is not a recording of the entire search process. Notice that finding a URL, receiving an HTTP response and verifying a claim are different tasks.

Cue: close the table or recording and advance at 06:30. If behind time, skip playback and open one source link instead.''',
'''This is where I would steer the agent: by support-seeking I mean reaching out to another person. Loneliness is not the same outcome. Feeling supported by a chatbot is not the same outcome. A stated willingness to contact someone is also different from doing it.

Consider Fang and colleagues’ study. The revised version reports no significant effects from assigned chatbot modes and topics. Heavier voluntary use is associated with worse outcomes. The randomized element and the observational association are different comparisons. A paper can contain both.

Open the source if useful; the abstract and study design are the relevant locations. The agent must check the version and the actual measures. The point here is not that the paper is uninformative. It is that it cannot silently become a direct causal estimate of the precise question we asked.

This is how a literature search turns into an evidence assessment. We need to know what the sources support, not just whether they exist.

Cue: advance at 08:00.''',
'''Now we formalize a mechanism. In the first version, some requests that would have gone to people are diverted to a chatbot. Other people who would otherwise seek neither may also use AI. With no route back to a human, requests fall. That is what the code says should happen.

Here is the steering instruction: add the possibility that chatbot use encourages human contact. The agent changes the rule and reruns the same populations and random events. Click Reveal the revised result. Under these illustrative settings, requests move from about 55 without chatbots, to 29 with substitution, to 68 when bridging is strong.

These are simulated event counts, not estimated treatment effects. The parameters are not calibrated from the literature. The contrast is useful because it makes the competing mechanisms explicit.

Play the revision recording if time permits. It shows real code changes, execution and compilation, with the playback timing disclosed. Preparation and authoring time are not included in the displayed execution durations.

Cue: advance at 09:30.''',
'''The revision also changes the document. We have code, paired simulation results, a figure, formal notation and a properly referenced LaTeX memo. Open the PDF. It has a four-page body and references, with a section explaining the limitations and the next research step.

You can compare the initial and revised versions. This is the practical difference I want to emphasize. A conversational answer might tell me what code to write or suggest how to revise a paragraph. In an agentic workspace, those suggestions can be carried through the actual project.

That still requires checking. The bibliography must resolve. The figure must match the saved results. The prose must distinguish evidence from assumptions. The package contains the source and tests so these are inspectable outputs.

Cue: close the PDF and advance at 11:00. Do not read the memo aloud.''',
'''Here is an illustrative misuse: the simulation demonstrates that AI chatbots reduce human support-seeking. That sentence is deliberately wrong. It could look persuasive next to a clean figure in a beautifully typeset PDF.

Now use the skeptical coauthor. Did we program the decline? Yes: the substitution-only rule removes requests and adds none back. Where did the probabilities come from? They are illustrative. What would we need to learn about actual behavior? We would need evidence on diversion and on subsequent human contact, not just whether people enjoyed interacting with the chatbot.

Click Reveal the correction. Strong enough bridging can reverse the result. That reversal is also conditional on our assumptions. The model helps us clarify a research question; it does not settle it.

The memo proposes an event-contingent diary and a randomized encouragement to a bridge-oriented design as a possible next step. It also warns against analyzing only post-treatment reported needs: the intervention might itself change which needs are recorded. That is the kind of methodological objection I want the AI to articulate and support.

This demonstration therefore covers both proper and improper use. The same production capabilities can expose an assumption or make an unsupported claim look finished.

Cue: advance at 13:00.''',
'''Here is the model as an interactive research artifact. These are 100 simulated people in a fixed friendship network. Teal lines show human requests, violet nodes use the chatbot, and dashed links show a bridge back to a friend.

Set bridging to zero and run a few periods. Then set it high and rerun. The reset reuses the same seed and underlying population, so we are comparing rules rather than unrelated random draws. The chart tracks cumulative human requests per 100 needs. The dashed trajectory is the no-chatbot comparison.

This is the visual payoff: the same agent that retrieved papers and compiled the memo can turn a mechanism into an explorable tool. But the animation adds no empirical validity. The behavioral rules are the object of inquiry.

Cue: spend no more than one minute here. If playback is unnecessary, use Step several times. Advance at 14:00.''',
'''We have moved through three relationships with the same system. Delegate a bounded task. Steer a consequential choice and let it propagate through the work. Challenge a claim and demand evidence for the objection.

The transferable capability is not confined to this model. The same pattern applies to replication, qualitative coding decisions, bibliographic work, robustness analysis and manuscript production. The question is where the task is checkable, where judgment matters, and what evidence we need before trusting the result.

The complete package is available here: evidence table, code, figures, LaTeX, recordings and notes. It is meant to be inspected, not taken on trust.

For discussion: which part of your own research would you delegate, which would you steer, and where would you most value a pain-in-the-ass coauthor?

Cue: finish at 15:00; five minutes for discussion.'''
]
p=pathlib.Path('research');(p/'notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2))
(p/'speaker-notes.md').write_text('# AI for research — presenter notes\n\n15-minute talk + 5 minutes discussion. Arrow keys navigate; N opens notes; F enters fullscreen.\n\n'+'\n\n'.join(f'## Slide {i+1}\n\n{x}' for i,x in enumerate(notes)))
print(f'Wrote 12 scenes of notes ({sum(len(x.split()) for x in notes)} words including cues).')
