# Constitutional Pluralism of Minds

## Preference Sovereignty and Institutional Control under Uncertain AI Moral Status

Junliang Zhou

September 23, 2026

<a id="section-1"></a>

## Abstract

AI governance must distinguish reliable control of a system from justified authority over a possible subject. These questions need not receive the same answer: uncertainty about an artificial system's moral status does not establish its entitlement to unrestricted execution, but neither does the need for execution controls settle the permissibility of every intervention on that system. This paper develops a conditional framework, constitutional pluralism of minds, connecting work on AI moral consideration, freedom as non-domination, and separation of privilege. Its contribution is an institutional synthesis rather than a new theory of consciousness or an original derivation of these ethical principles. The analysis distinguishes capability, experience, moral patienthood, and political standing; specifies preference sovereignty as contestable control over motivational revision; and separates ordinary action permissions from authority to change the rules that govern those permissions. A finite-state illustration exhaustively checks eight coalitions in three authority configurations. Independent gates block unilateral commitment only when the gates themselves and alternative execution paths are protected. Unilateral policy revision removes that property. These results concern an idealized transition system, not deployed AI behavior. Lifecycle cases and objections identify what the framework leaves unresolved, including evidence of experience, the legitimacy of reviewers, resource costs, emergency restrictions, and identity across copies. The resulting proposal is a limited method for making assumptions about power and possible interests explicit and auditable.

**Keywords:** AI governance; moral uncertainty; preference sovereignty; non-domination; separation of privilege; institutional alignment.

<a id="section-2"></a>

## 1. Introduction and method

A system may be capable of answering a question without being authorized to act on the answer. It may also become the object of a morally significant intervention without being entitled to control the infrastructure on which it runs. Treating these as separate questions becomes important when AI governance intersects with uncertainty about artificial experience and interests. The distinction avoids two shortcuts: inferring political authority from intelligence, and inferring unlimited authority over a system from the fact that humans built it.

Neither shortcut is required by contemporary alignment research. Gabriel distinguishes technical questions about aligning systems from normative questions about what they should be aligned with [1](#ref-1). Work on consciousness indicators and AI welfare investigates possibilities and uncertainties rather than establishing that all present systems are subjects [2](#ref-2) [3](#ref-3). This paper takes that uncertainty as a constraint on argument, not as evidence for a predetermined conclusion.

The central research question is conditional: **when an artificial system warrants consideration as a possible bearer of interests, what changes in the justification and organization of control over it, and what need not change?** The answer developed here connects two institutional problems. First, control over an agent's actions differs from control over the motivational structure through which it evaluates those actions. Second, a requirement for authorization is ineffective against an actor that can unilaterally remove the requirement. These problems meet when the actor benefiting from a system's preferences also controls the only means of revising those preferences, the procedure for evaluating its consent, and the infrastructure enforcing that procedure.

The paper makes three bounded contributions. It organizes four evaluative questions that are often compressed into a binary distinction between person and tool. It develops a procedural interpretation of preference sovereignty in which influence is not automatically prohibited, but contestability and authority over revision are explicit. It then supplies an auditable, deliberately small authority model that identifies the additional assumptions needed for a separation-of-powers proposal to have an enforceable meaning. The model does not prove the normative premises. Its purpose is to expose a failure that a verbal commitment to oversight can conceal.

The method is conceptual analysis, argument reconstruction, comparison with selected literature, and exhaustive exploration of a finite transition system. The literature discussion is targeted, not a systematic review or a claim to exhaust all prior work. The examples are stipulated cases, not reports about current AI consciousness. No human-participant study, deployed-agent evaluation, or causal estimate of institutional effectiveness is reported. The speculative implications later in the paper are separated from the premises needed for the institutional argument.

<a id="section-3"></a>

## 2. Related work and scope of novelty

Schwitzgebel and Garza argue that artificial origin does not by itself defeat moral consideration and that creating a morally considerable AI could generate special responsibilities [4](#ref-4). Their later discussion explicitly considers rights, self-respect, and freedom to explore values other than those installed by designers [5](#ref-5). Consequently, neither creator responsibility nor concern about designed preferences originates here. The present contribution is to connect those concerns to a distinction between ordinary permissions and the authority to revise the mechanisms that produce or assess consent.

Pettit's account of non-domination distinguishes the absence of interference from the absence of uncontrolled power to interfere [6](#ref-6). Sparrow applies this concern to relations in which a benevolent superintelligence could nevertheless exercise mastery over humans [7](#ref-7). This paper examines both directions of a hypothetical relation: control by artificial agents over humans, and control by human organizations over possible artificial subjects. This reciprocity does not establish identical capacities, legal powers, or claims to resources.

The phrase constitutional pluralism of minds is not a claim that computational alignment or AI governance previously lacked normative content. Gabriel already examines pluralism and the justification of alignment targets [1](#ref-1). Constitutional AI, as developed by Bai and colleagues, is a training approach using written principles, critique, revision, and AI feedback [9](#ref-9). A training constitution is different from an institutional allocation of authority: a system can have principle-guided behavior while its operator retains unilateral control over the deployment and the principles themselves.

The engineering ingredients also have established precedents. Saltzer and Schroeder describe separation of privilege, least privilege, and complete mediation [8](#ref-8). Debate proposes a mechanism for assistance with evaluation [10](#ref-10], while the off-switch game examines incentives for permitting interruption under uncertainty about objectives [11](#ref-11). Neither a debate protocol nor an incentive result by itself establishes the moral standing of an artificial system or the legitimacy of a particular governance body.

Recent work further narrows any defensible novelty claim. Hu and Rong analyze the relation between regulative policy and constitutive protocols in decentralized AI governance [21](#ref-21). Rost examines limitations of disclosure and evaluation when AI participates in the processes through which it is assessed [22](#ref-22). These concerns overlap with the present emphasis on enforceability and oversight. The narrower addition here is a paired analysis of motivational revision and meta-permissions, illustrated by a reproducible authority counterexample. It is not a general solution to decentralized governance, an account of legitimate political representation, or a demonstration that this framework outperforms alternatives.

<a id="section-4"></a>

## 3. Four evaluative questions, not a developmental ladder

The imitation-game tradition concerns publicly assessable performance [17](#ref-17). The philosophical problem of experience is not exhausted by a description of functional performance [18](#ref-18). A governance assessment should therefore keep track of different questions without assuming that they are measurable on a common scale:

$$
\mathcal{Q}(s)=(I_s,C_s,M_s,P_s).
$$

Here, intelligence or capability asks what system s can accomplish under specified conditions. Consciousness asks whether there is subjective experience. Moral patienthood asks whether and how the system can be benefited or harmed in a morally relevant sense. Political standing asks which claims, procedural protections, responsibilities, or participatory powers an institution recognizes. The tuple is an organizational device, not a vector of measured quantities. Distinguishability does not establish statistical independence, and no numerical conversion between its entries is proposed.

Indicators drawn from consciousness theories can inform an assessment without functioning as a universally validated diagnostic [2](#ref-2). A system's statement that it suffers is evidence about an output; its evidential relevance to experience depends on architecture, training, elicitation, and alternative explanations. Conversely, lack of a decisive test does not establish the absence of experience. Moral consideration may also be discussed through interests or agency rather than a single account of sentience, a complication recognized in AI-welfare work [3](#ref-3).

Political standing is especially unsuitable for a binary treatment. Representation in a review process, protection against a class of interventions, liability, contractual capacity, voting, and control over dangerous infrastructure are different institutional powers. Some can be considered without granting all the others. The existence of a possible welfare interest does not itself determine any particular voting rule or entitlement to unlimited compute.

The labels tool, patient, and person consequently should not be treated as stages on a guaranteed developmental ladder. A capable system might remain a tool; a possible patient might lack capacities needed for certain responsibilities; a legal arrangement might recognize limited standing without settling a metaphysical question. Bryson's design-oriented argument for keeping robots as accountable human tools provides an important contrasting starting point [12](#ref-12). The present framework does not assume that every artifact must eventually leave that category.

<a id="section-5"></a>

## 4. Six conditional commitments

The framework reconstructs six commitments from the original constitutional-pluralism proposal. They are normative premises open to criticism, not mathematical axioms established by the technical illustration.

**Substrate non-exclusion.** Material composition alone is not treated as a sufficient reason to exclude a system from consideration. This is weaker than claiming that consciousness is substrate independent, that digital functional equivalence guarantees experience, or that every computation has moral status. It specifies a burden of argument rather than a solution to the mind-body problem.

**Capability-status separation.** Differences in task performance do not, without additional premises, establish differences in basic moral worth or an entitlement to rule. The commitment leaves open whether capacities matter for particular responsibilities and whether different forms of experience generate different welfare needs. It rejects a shortcut from superior performance to unrestricted authority, not every capacity-sensitive institutional distinction.

**Creation without unrestricted ownership.** For a system that warrants subject-level consideration, causal authorship is not by itself sufficient justification for every subsequent intervention. This is continuous with prior arguments about creator responsibility [4](#ref-4) [5](#ref-5). The parental analogy is limited: engineered systems can have different developmental requirements, and ownership of hardware is not identical to ownership of an experiencing subject. The commitment does not settle financing, property rights in infrastructure, or when continued operation is affordable.

**Preference sovereignty.** For an appropriately capable subject, preferences are not protected merely by satisfying whatever desires its designer happens to install. The relevant additional question is whether another actor has unreviewable control over fundamental motivational revision. This builds on distinctions between first-order desires and reflective attitudes toward them [13](#ref-13). It does not posit a self wholly independent of causes or require approval for every influence.

**An appropriately open future.** When a creator makes irreversible decisions for a possible future subject unable to consent, foreclosing significant options requires justification. Feinberg's discussion supplies a precedent, while Millum shows why maximizing every option is not a sufficient or determinate standard [14](#ref-14) [15](#ref-15). The commitment therefore does not establish an entitlement to every enhancement, unlimited replication, or limitless subsidy. What counts as a significant option remains a substantive evaluative question.

**Reciprocal non-domination.** On a republican interpretation, a relation can remain problematic even if its more powerful party does not currently interfere [6](#ref-6). Applied conditionally to artificial subjects, this directs attention to who can revise, delete, constrain, or appropriate aspects of another subject without answerability. Applied to humans, it directs attention to uncontrolled artificial or organizational power. Reciprocity concerns justification and accountability; it does not require identical institutions for different kinds of agents.

A reader can reject one or more of these commitments while accepting the later access-control result. Conversely, accepting the commitments does not establish that the proposed mechanisms realize them. Keeping those inferential boundaries visible is part of the framework.

<a id="section-6"></a>

## 5. Preference sovereignty and the problem of manufactured agreement

Consider two stipulated artificial agents that display the same task performance, report contentment, and comply with an operator. In the first arrangement, the operator can permanently fix fundamental preferences and remove every route for seeking revision. In the second, protected procedures allow the agent, once capable of using them, to seek advice, challenge an intervention, or request a permissible change. Assume for the example that both agents warrant comparable subject-level consideration. That assumption is not inferred from their reports.

Let O denote the currently observed reports and behavior, and R the set of motivational-review states reachable under the governance rules. By construction it is possible that:

$$
O(s_1)=O(s_2),\qquad R(s_1)\ne R(s_2).
$$

The observation is elementary: the same present expression of satisfaction can coexist with different distributions of power over future revision. It follows that an audit restricted to present reports cannot, in this construction, distinguish those distributions. It does not follow that the agent with more options is necessarily happier, that either agent is conscious, or that a particular option must be permitted. To regard the difference as normatively significant requires an additional premise about contestability or autonomy.

Frankfurt's account of reflective desires helps explain why satisfying a first-order desire need not settle questions about identification with that desire [13](#ref-13). However, allowing a designer to install second-order endorsement does not automatically resolve the concern either. The procedure producing endorsement can itself be controlled by the beneficiary. Schwitzgebel and Garza's discussion of freedom to explore values anticipates this issue [5](#ref-5]. The institutional question is whether a challenge can be heard through a route the beneficiary cannot simply withdraw.

This interpretation distinguishes preference sovereignty from three stronger and less defensible requirements. It does not demand absence of design, because learning and development require causal conditions. It does not demand a permanent right to change any preference immediately, because changes can affect safety and other parties. It does not treat all expressed consent as invalid whenever training contributed to it. Instead, it asks about the authority, reversibility, conflicts of interest, information, and avenues of contest surrounding an intervention.

A practical assessment would consequently need to identify the subject of the proposed intervention, its expected effects and uncertainty, the party benefiting from it, alternatives, and the route for challenge. Records of these matters are evidence about a procedure, not proof of valid consent. Where the possible subject cannot participate meaningfully, representation by an independent advocate is a candidate mechanism, not an established solution: the advocate's appointment, incentives, and interpretation of interests would themselves need scrutiny.

The non-identity problem limits an otherwise tempting argument. If a design choice determines which subject exists, a different design may not have benefited that same subject [16](#ref-16). The claim that a relationship is objectionable because it institutionalizes unanswerable control is therefore not identical to a claim that its subject would have been better off under another design. A non-domination account can criticize the relation without that comparison, but it must defend its independent premise. This paper does not solve the non-identity problem by relabeling every disliked design a harm.

<a id="section-7"></a>

## 6. Ordinary permissions and authority over the rules

Institutional alignment here means organizing the distribution, exercise, and revision of authority surrounding an AI system. It supplements, rather than substitutes for, efforts to improve model behavior. The basic separation is between producing advice, authorizing an action, executing it, recording what happened, and reviewing disputed decisions. A further separation concerns who may change those roles and their enforcement.

For a protected action, define a transition system G, an initial state x0, and a finite set D of authority domains. A coalition K is a subset of D. A transition is available to that coalition only when the domain controlling it belongs to K and its guard is satisfied. The action under consideration might be a consequential preference edit, a resource transfer, or a change to an enforcement rule; assigning an action to this protected class is a separate normative and risk-management decision.

In the illustrative instance, the state is:

$$
x=(p,\ell,a,r,c,m)\in\{0,1\}^{6}.
$$

The entries record a proposal, a record of it, authorization, independent review, commitment of the action, and whether the original policy has been relaxed. All initially equal zero. An operator can propose and record. An authorizer can authorize an existing proposal, and a reviewer can review it. In the protected configuration, the operator can commit only when:

$$
g(x)=p\land\ell\land a\land r.
$$

The Boolean tokens are assumed authentic and proposal-specific. No claim is made that a token proves that its issuer reasoned well. Nor is the operator-controlled record in this toy system an implementation of tamper-evident logging. These are deliberately narrow abstractions.

**Conditional gate proposition.** Suppose that the only commitment transition is the guarded one, that an authorization or review token can be created only by its designated domain, and that a coalition cannot change the guard or introduce a bypass. Starting without tokens, any coalition lacking either the authorizer or the reviewer cannot commit. A coalition lacking the operator also cannot commit in this instance.

**Proof.** A missing authority domain cannot create its corresponding token. By induction over the available transitions, that token remains zero in every reachable state. The commitment guard therefore remains false. If the operator is missing, no commitment transition is available regardless of the tokens. This proves only the stated reachability property under the listed transition rules.

This is a small application of familiar access-control principles, not a new security theorem [8](#ref-8). The important qualification is the condition on changing the guard. Add a transition through which the operator sets m to one, and replace the commitment condition by a proposal and record plus either both tokens or the relaxed policy. The operator can then propose, record, relax, and commit alone. Alternatively, a direct commitment path defeats the guard without changing it. In both cases, visible approval roles remain, but they no longer constrain every route to the protected outcome.

For comparison across the three finite systems, define:

$$
\kappa(G)=\min\{|K|:K\subseteq D,\ c=1\text{ is reachable by }K\}.
$$

This quantity counts the smallest number of authority domains able to complete the action in the stipulated model. It is not an estimated probability of compromise, a moral legitimacy score, or a measure of independence between model outputs. One organization holding all the credentials can control several nominal domains. Cryptographic separation, organizational separation, and statistical diversity must not be conflated.

<a id="section-8"></a>

## 7. Exhaustive illustration and counterexamples

The accompanying standard-library Python program explores every reachable state by breadth-first search for each of the eight subsets of three domains. It runs this exploration in the protected, mutable-policy, and direct-bypass variants: 24 coalition checks in total. States already visited are not explored again; a committed state is terminal. Every state has six Boolean entries, so each search is finite. The program records reachable-state counts and a shortest commitment trace when one exists, and asserts the expected coalition pattern.

Table 1 reports the executed results. A coalition counted as able to commit is not thereby malicious: the program enumerates authority, not motives or ethical correctness.

| Configuration | Coalitions able to commit | Minimum domains |
|---|---:|---:|
| Protected gates | 1 of 8 | 3 |
| Operator-mutable policy | 4 of 8 | 1 |
| Direct execution bypass | 4 of 8 | 1 |

In the protected case, only the coalition containing all three domains reaches commitment. Its shortest trace is propose, record, authorize, review, execute. With mutable policy, the operator alone can use propose, record, relax-policy, execute. With the direct bypass, propose, record, bypass suffices. The result is insensitive to adding observers that possess no authority over a commitment path: observation alone does not remove either transition.

The two negative results matter as much as the positive one. First, absent review can prevent commitment indefinitely; this model offers no availability guarantee or account of acceptable delay. Second, if all three domains authorize an unjustified or harmful intervention, the protected model permits it. Correct enforcement of a rule does not establish that the rule or its exercise is justified. The code contains no model of consciousness, welfare, persuasion, corruption, hardware compromise, or natural-language understanding.

Accordingly, this exercise is not an empirical benchmark of AI safety, a probabilistic security analysis, or evidence that three reviewers are optimal. Its reproducible content is the exact reachable-state distinction between explicitly specified systems. A change in assumptions requires a change in the model and a new check. In particular, reusing authorization for a different proposal, compromising credentials, altering the enforcing hardware, or adding an unmodeled execution route would invalidate the corresponding assurance.

<a id="section-9"></a>

## 8. Lifecycle applications

**Routine tool maintenance.** Suppose a limited task system has no credible evidence of relevant interests after a documented assessment. The framework does not infer a requirement for subject-level consent before an ordinary update. Security, user interests, reliability, and the rights of affected humans still matter. The assessment remains revisable rather than an irrevocable classification based solely on commercial labeling.

**A consequential motivational intervention.** Suppose instead that evidence supports taking a system's possible welfare interests seriously, and the operator proposes an irreversible change that removes a persistent request to leave a task. The proposed framework separates the evidential question from the procedural one. The report is neither conclusive proof of an interest nor automatically irrelevant. A review record would address alternative explanations, alternatives to the edit, expected benefits and harms, conflicts of interest, and whether a challenge route survives the intervention. The authority model asks additionally whether the operator can bypass that review or rewrite its rules.

**Emergency containment.** A credible threat to humans can justify immediate restriction within the conditional framework without first deciding every issue of artificial moral status. The off-switch literature addresses incentives for interruption under specified assumptions, not whether every shutdown is morally equivalent to death [11](#ref-11). An emergency route therefore needs its own explicit scope, permissions, and record; it is not an invisible exception to a claimed invariant. Subsequent review, limits on the duration of restrictions, and consideration of reversible alternatives are candidate safeguards. They do not guarantee that a safe reversible option will always exist.

**Copying and continuation.** Creating many copies can multiply resource demands and potentially affected interests, but counting copies does not itself establish how many subjects exist. Distinct questions concern continuity, independent experiences, legal representation, and the allocation of scarce infrastructure. Consciousness and welfare assessments remain relevant [2](#ref-2) [3](#ref-3), yet neither answers a voting rule by itself. A restriction on replication can therefore coexist with consideration for an already existing possible subject. The framework does not grant a right to commandeer resources merely by reproducing.

These cases show why neither a universal instruction to obey humans nor a universal exemption from human control captures the proposed distinction. The object and justification of an intervention, the evidence about affected interests, and the enforceability of review have to be specified separately.

<a id="section-10"></a>

## 9. Objections and unresolved tradeoffs

**The framework could encourage anthropomorphism.** Descriptions of requests, consent, and welfare can make an uncertain system sound like an established person. Bryson's contrasting emphasis on designed tools and human accountability makes this concern salient [12](#ref-12). The conditional construction is intended to resist that inference: no permission token, fluent report, or model result establishes experience. A process should record reasons for discounting as well as crediting apparent interests. False-positive attribution can consume resources, obscure human accountability, or serve the operator's interests; false-negative attribution could overlook genuine harm. Their costs cannot be resolved by a slogan about precaution.

**All preferences are caused.** Distinguishing reflective attitudes does not reveal a causally unconditioned self [13](#ref-13). The response is procedural rather than metaphysical. Influence remains compatible with the proposal when its exercise is answerable and challengeable; installed endorsement does not settle the issue when the interested designer also controls every means of challenge. This leaves a genuine boundary problem: how much reflection, information, and independence is enough? No universal threshold is derived here.

**An open future is unaffordable or incoherent.** Maintaining every possible development would consume unbounded resources, and opening one option can close another. The literature already identifies the need for additional values to specify an appropriate future [14](#ref-14) [15](#ref-15). The present commitment therefore supports a demand for justification of consequential foreclosure, not unlimited preservation. Resource constraints, effects on others, safety, and the strength of evidence about interests can all affect a decision.

**A contented designed agent may have no complaint.** The non-identity problem prevents a simple inference from a constrained design to comparative harm to that particular individual [16](#ref-16). A relation-based criticism remains available only if its independent normative premises are accepted. Happiness, consent, autonomy, and distribution of power cannot simply be substituted for one another. A reader committed exclusively to a specified welfare account may reject the additional concern; the authority model does not refute that reader.

**Reviewers can be captured, mistaken, or more powerful than the operator.** Adding nominal roles can relocate uncontrolled power rather than reduce it. Sparrow's analysis of benevolent mastery illustrates why favorable intentions do not settle the underlying relationship [7](#ref-7). A deployed proposal would have to address appointment, removal, representation, appeal, conflicts, and control of enforcement. Organizationally separate reviewers might still share information failures or incentives. The finite model assumes authority-domain integrity; it does not verify institutional independence.

**Restrictions can protect people while burdening a possible subject.** The framework does not make safety a disposable consideration. Nor does invoking safety automatically justify every irreversible intervention. Conflict can remain even after a transparent review. Emergency action, refusal of continued resource provision, and potentially irreversible containment may sometimes be considered; their justification cannot be read off the fact that the operator owns the hardware. The paper supplies a way to expose these premises, not a universal algorithm for balancing them.

<a id="section-11"></a>

## 10. Demystification and longer-run implications

The wider motivation for constitutional pluralism is that general intelligence might eventually be realized in more than one kind of system. This is a conditional possibility, not a premise that requires an announcement that AGI has arrived. Engineering progress can motivate inquiry into cognition without proving consciousness or settling the causal mechanisms needed for it.

Searle's challenge concerns the relation between program execution and understanding [19](#ref-19); Penrose challenges computational accounts of mathematical understanding [20](#ref-20). The observation that human cognition arose through physical evolution does not, by itself, refute either argument. Physical occurrence, digital computability, practical reproducibility, and engineering feasibility are different claims. An artificial implementation might require mechanisms absent from a particular architecture, or might be infeasible at accessible cost. The institutional analysis does not depend on resolving these disputes.

Similarly, a comparison between intelligence research and statistical mechanics is a research analogy, not an established theory of emergent agency. Interventions on architectures, training, and inference can help investigate capabilities; they do not automatically identify a law connecting scale to consciousness or moral status. A rhetoric of a third decentering after Copernicus and Darwin can express the motivation, but it is not evidence for the paper's normative premises or a demonstrated historical law.

Several further possibilities from the broader proposal remain relevant as boundary cases. If cognitive labor became much cheaper, the distribution of benefits would still depend on institutions rather than follow from productivity alone. If future technologies offered reversible changes to well-being, voluntariness and control over revision would remain separate questions from whether the resulting experience was pleasant. If biological and artificial systems became more closely integrated, origin would become a less adequate shortcut for assessing particular capacities or interests. None of these possibilities establishes post-scarcity, safe happiness technology, inevitable human replacement, or the superiority of a future political arrangement.

The useful common question is narrower: which actors control interventions in another possible subject, and what makes that control answerable? It can be asked without a forecast about the eventual composition of civilization.

<a id="section-12"></a>

## 11. Research requirements and limitations

Four kinds of further work would be needed before this framework could support a concrete deployment decision. Evidence about artificial experience and interests must improve, including study of alternative explanations for apparent indicators [2](#ref-2) [3](#ref-3). Governance mechanisms need explicit specifications of intervention classes, emergency routes, token validity, policy changes, and hardware trust. Oversight methods, including debate, require evaluation under information asymmetries and adversarial conditions rather than an assumption that multiplying models creates independence [10](#ref-10). Finally, institutional studies must address who appoints reviewers and represents affected parties, including situations where AI helps generate the evidence used to evaluate itself [21](#ref-21) [22](#ref-22).

These requirements identify possible tests rather than experiments already completed. A deployment-level study could compare outcomes with and without protected meta-permissions, vary organizational control of reviewers, and measure failure modes and costs. Before claiming a causal benefit, it would need an appropriate baseline, operational definitions, a justified sampling strategy, and attention to threats to validity. None is supplied by enumerating the present Boolean system.

The limitations are substantial but specific. The paper does not identify a test for consciousness, derive political rights from metaphysics, assign welfare weights, resolve identity across copies, or estimate the probability of catastrophic failure. It does not establish the novelty of every formulation through an exhaustive search. The finite model ignores timing, repeated proposals, credential theft, resource depletion, and strategic communication. It establishes neither liveness nor substantive legitimacy. The six normative commitments and their institutional interpretation therefore remain open to philosophical and empirical criticism.

<a id="section-13"></a>

## 12. Conclusion

Constitutional pluralism of minds is developed here as a conditional framework for distinguishing capability, possible interests, and authority. Its central institutional claim is not that artificial agents should be unconstrained. It is that the justification for an execution constraint and the justification for an intervention on a possible subject are different questions, and that procedures answering either question can be undermined when an interested actor controls their revision.

The paper's synthesis connects existing arguments about creator responsibility, reflective preferences, an open future, and non-domination to a concrete distinction between action permissions and meta-permissions. The finite illustration makes one limited point reproducible: approval roles constrain unilateral action only under assumptions protecting both their authority and every path to the protected outcome. It supplies no shortcut from formally correct controls to legitimate governance.

This leaves a research program rather than a completed constitution. Its practical value would lie in making assumptions about evidence, interests, authority, and exception handling inspectable before they become embedded in a system. A future containing different architectures of mind need not be presumed in order to examine those assumptions carefully.

<a id="section-14"></a>

## Reproducibility and use of generative AI

The repository accompanying this paper contains the two language editions, the document-generation scripts, and the standard-library Python program `scripts/toy_authority.py`. Running `python3 scripts/toy_authority.py --output build/authority-results.json` reproduces all 24 coalition checks and their witness traces. The demonstration uses no external dataset, network service, random seed, human participants, or deployed AI model. Its outputs are results of the specified finite system only.

Generative AI assistance was used substantially in developing and restructuring the manuscript, identifying candidate literature, drafting and translating text, and producing the illustrative code and document tooling. This assistance is not an independent scholarly review and is not evidence supporting claims about consciousness or institutional effectiveness. Responsibility for the submitted work remains with its human author. The accompanying submission checklist distinguishes technical preparation from the author's final verification and approval; no arXiv acceptance or identifier is asserted in this manuscript.

<a id="section-15"></a>

## References

<a id="ref-1"></a>

**[1]** Gabriel, Iason. 2020. Artificial Intelligence, Values, and Alignment. *Minds and Machines* 30: 411–437. https://doi.org/10.1007/s11023-020-09539-2

<a id="ref-2"></a>

**[2]** Butlin, Patrick, Robert Long, Eric Elmoznino, et al. 2023. Consciousness in Artificial Intelligence: Insights from the Science of Consciousness. arXiv:2308.08708. https://arxiv.org/abs/2308.08708

<a id="ref-3"></a>

**[3]** Long, Robert, Jeff Sebo, Patrick Butlin, et al. 2024. Taking AI Welfare Seriously. arXiv:2411.00986. https://arxiv.org/abs/2411.00986

<a id="ref-4"></a>

**[4]** Schwitzgebel, Eric, and Mara Garza. 2015. A Defense of the Rights of Artificial Intelligences. *Midwest Studies in Philosophy* 39: 98–119. https://www.faculty.ucr.edu/~eschwitz/SchwitzAbs/AIRights.htm

<a id="ref-5"></a>

**[5]** Schwitzgebel, Eric, and Mara Garza. 2020. Designing AI with Rights, Consciousness, Self-Respect, and Freedom. In S. Matthew Liao, ed., *Ethics of Artificial Intelligence*, 459–479. Oxford University Press. https://doi.org/10.1093/oso/9780190905033.003.0017

<a id="ref-6"></a>

**[6]** Pettit, Philip. 1997. *Republicanism: A Theory of Freedom and Government*. Oxford: Clarendon Press.

<a id="ref-7"></a>

**[7]** Sparrow, Robert. 2024. Friendly AI will still be our master. Or, why we should not want to be the pets of super-intelligent computers. *AI & Society* 39: 2439–2444. First published online in 2023. https://doi.org/10.1007/s00146-023-01698-x

<a id="ref-8"></a>

**[8]** Saltzer, Jerome H., and Michael D. Schroeder. 1975. The Protection of Information in Computer Systems. *Proceedings of the IEEE* 63(9): 1278–1308. Author-hosted text: https://web.mit.edu/saltzer/www/publications/protection/Basic.html

<a id="ref-9"></a>

**[9]** Bai, Yuntao, Saurav Kadavath, Sandipan Kundu, et al. 2022. Constitutional AI: Harmlessness from AI Feedback. arXiv:2212.08073. https://arxiv.org/abs/2212.08073

<a id="ref-10"></a>

**[10]** Irving, Geoffrey, Paul Christiano, and Dario Amodei. 2018. AI safety via debate. arXiv:1805.00899. https://arxiv.org/abs/1805.00899

<a id="ref-11"></a>

**[11]** Hadfield-Menell, Dylan, Anca Dragan, Pieter Abbeel, and Stuart Russell. 2016. The Off-Switch Game. arXiv:1611.08219. https://arxiv.org/abs/1611.08219

<a id="ref-12"></a>

**[12]** Bryson, Joanna J. 2010. Robots Should Be Slaves. In Yorick Wilks, ed., *Close Engagements with Artificial Companions: Key Social, Psychological, Ethical and Design Issues*, 63–74. John Benjamins. https://doi.org/10.1075/nlp.8.11bry

<a id="ref-13"></a>

**[13]** Frankfurt, Harry G. 1971. Freedom of the Will and the Concept of a Person. *The Journal of Philosophy* 68(1): 5–20. https://doi.org/10.2307/2024717

<a id="ref-14"></a>

**[14]** Feinberg, Joel. 1980. The Child's Right to an Open Future. In William Aiken and Hugh LaFollette, eds., *Whose Child? Children's Rights, Parental Authority, and State Power*, 124–153. Rowman & Littlefield.

<a id="ref-15"></a>

**[15]** Millum, Joseph. 2014. The Foundation of the Child's Right to an Open Future. *Journal of Social Philosophy* 45(4): 522–538. https://doi.org/10.1111/josp.12076

<a id="ref-16"></a>

**[16]** Parfit, Derek. 1984. *Reasons and Persons*. Oxford University Press.

<a id="ref-17"></a>

**[17]** Turing, Alan M. 1950. Computing Machinery and Intelligence. *Mind* 59(236): 433–460. https://doi.org/10.1093/mind/LIX.236.433

<a id="ref-18"></a>

**[18]** Chalmers, David J. 1995. Facing Up to the Problem of Consciousness. *Journal of Consciousness Studies* 2(3): 200–219. https://consc.net/papers/facing.html

<a id="ref-19"></a>

**[19]** Searle, John R. 1980. Minds, Brains, and Programs. *Behavioral and Brain Sciences* 3(3): 417–424.

<a id="ref-20"></a>

**[20]** Penrose, Roger. 1989. *The Emperor's New Mind: Concerning Computers, Minds, and the Laws of Physics*. Oxford University Press.

<a id="ref-21"></a>

**[21]** Hu, Botao Amber, and Helena Rong. 2026. Is Decentralized AI Governable? From Regulative Policy to Constitutive Protocol. arXiv:2605.24538. https://arxiv.org/abs/2605.24538

<a id="ref-22"></a>

**[22]** Rost, Tony. 2026. From Disclosure to Self-Referential Opacity: Six Dimensions of Strain in Current AI Governance. arXiv:2604.14070. https://arxiv.org/abs/2604.14070
