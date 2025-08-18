# Problem-Solver Agent Handoff Protocols

## Overview

This document defines interaction protocols for seamless collaboration between the Problem-Solver agent and other BMad specialist agents. These protocols ensure smooth information flow, clear responsibilities, and effective problem-solving outcomes.

## Core Handoff Principles

1. **Clear Transition Points**: Each handoff has specific triggers and deliverables
2. **Contextual Information**: All relevant analysis is passed to receiving agent
3. **Bi-directional Communication**: Receiving agents can provide feedback to refine analysis
4. **Documentation Trail**: All handoffs are documented for traceability
5. **Quality Gates**: Receiving agents validate inputs before proceeding

## Incoming Handoffs (Other Agents → Problem-Solver)

### From Analyst → Problem-Solver
**Common Triggers:**
- "This requires systematic problem decomposition"
- "Need to explore multiple solution approaches"
- "Root cause analysis needed for complex issue"
- "Multiple stakeholders have conflicting views on the problem"

**Typical Handoff Message:**
> "Initial research complete. Market analysis shows 3 competing trends affecting user behavior. 
> Problem appears multi-factorial involving technology adoption, user training, and competitive pressure. 
> Requires systematic decomposition and root cause analysis. See market-research.md for context."

**What Analyst Provides:**
- Market research findings
- Competitive analysis
- User research data
- Industry trends and patterns
- Stakeholder interview results

**Problem-Solver Response:**
- Integrates research into problem definition
- Applies MECE decomposition to structure findings
- Identifies gaps requiring additional research
- Validates assumptions with data provided

**Expected Outputs:**
- problem-definition.md incorporating research context
- Structured analysis of research implications
- Additional research questions if needed

---

### From Product Manager → Problem-Solver
**Common Triggers:**
- "Multiple product directions possible, need decision framework"
- "Strategic decision requires systematic analysis"
- "Trade-offs unclear between competing priorities"
- "Business case needs analytical support"

**Typical Handoff Message:**
> "Product strategy at inflection point. Three potential directions identified but unclear which 
> maximizes business value. Stakeholder priorities conflict. Need systematic evaluation framework 
> and decision analysis. See product-requirements.md and stakeholder-analysis.md."

**What PM Provides:**
- Product requirements documentation
- Business objectives and success metrics
- Stakeholder priorities and concerns
- Resource constraints and timeline
- Competitive positioning requirements

**Problem-Solver Response:**
- Creates decision evaluation framework
- Develops criteria weighting based on business priorities
- Structures trade-off analysis
- Provides quantitative decision support

**Expected Outputs:**
- decision-analysis.md with MCDA framework
- solution-matrix.md comparing strategic options
- Recommendations with confidence levels and sensitivity analysis

---

### From Architect → Problem-Solver
**Common Triggers:**
- "Technical contradiction needs resolution"
- "Multiple architecture patterns possible, need selection criteria"
- "Innovation required to meet conflicting requirements"
- "System design decisions have broad implications"

**Typical Handoff Message:**
> "Architecture decision point reached. Need high performance AND low latency AND cost efficiency. 
> Standard patterns don't satisfy all constraints simultaneously. Requires systematic contradiction 
> resolution and creative alternatives. See technical-constraints.md and architecture-options.md."

**What Architect Provides:**
- Technical constraints and requirements
- Current architecture documentation
- Performance and scalability requirements
- Technology options analysis
- Infrastructure limitations

**Problem-Solver Response:**
- Applies TRIZ methodology for technical contradictions
- Generates innovative architecture alternatives
- Evaluates solutions against technical criteria
- Validates feasibility with architect

**Expected Outputs:**
- Technical decision record with TRIZ-based solutions
- Innovation alternatives with feasibility assessment
- Architecture recommendations with risk analysis

---

### From Developer → Problem-Solver
**Common Triggers:**
- "Complex bug requires systematic root cause analysis"
- "Performance issue spans multiple system components"
- "Solution approach unclear for complex technical challenge"
- "Multiple possible fixes, need systematic evaluation"

**Typical Handoff Message:**
> "System performance degraded 300% over 2 weeks. Multiple potential causes identified: database 
> queries, memory leaks, network latency, caching inefficiency. Need systematic investigation 
> to identify true root causes and optimal solution approach. See system-diagnostics.md."

**What Developer Provides:**
- System diagnostic data
- Error logs and stack traces
- Performance metrics and trends
- Code analysis results
- Debugging attempts made

**Problem-Solver Response:**
- Applies systematic root cause analysis (5 Whys, Fishbone, Fault Tree)
- Prioritizes investigation approaches based on evidence
- Generates solution alternatives with feasibility assessment
- Creates implementation approach recommendations

**Expected Outputs:**
- root-cause-analysis.md with validated causes
- Solution alternatives with technical risk assessment
- Implementation recommendations prioritized by impact

---

### From UX Expert → Problem-Solver
**Common Triggers:**
- "User needs conflict with technical constraints"
- "Multiple user experience approaches possible"
- "Design decisions require systematic evaluation"
- "Innovation needed to satisfy user requirements"

**Typical Handoff Message:**
> "User research reveals conflicting needs across segments. Power users want complexity and control, 
> new users need simplicity and guidance. Current design patterns don't serve both. Need systematic 
> approach to resolve design contradictions. See user-research.md and design-constraints.md."

**What UX Expert Provides:**
- User research findings
- Persona analysis and journey maps
- Design constraints and requirements
- Usability testing results
- Interface design principles

**Problem-Solver Response:**
- Applies design thinking methodology
- Uses lateral thinking for creative UX solutions
- Develops user-centered evaluation criteria
- Integrates behavioral economics insights

**Expected Outputs:**
- Design solution alternatives with user impact analysis
- Innovation approaches using design thinking methods
- User experience evaluation framework

## Outgoing Handoffs (Problem-Solver → Other Agents)

### Problem-Solver → Analyst
**When to Handoff:**
- Domain expertise needed for solution validation
- Market research required for decision confirmation
- Competitive analysis needed for solution positioning
- User validation required for proposed solutions

**Typical Handoff Message:**
> "Problem analysis complete. Three solution approaches identified, with Solution 2 scoring highest 
> on technical criteria. However, need market validation for commercial viability and competitive 
> positioning analysis. Specifically need research on: [specific areas]. See solution-matrix.md 
> sections 3.2 and 4.1 for research questions."

**What Problem-Solver Provides:**
- Structured research questions
- Solution alternatives needing validation
- Success criteria for market acceptance
- Competitive positioning requirements
- Timeline and resource constraints for research

**Expected Analyst Response:**
- Market validation of solution approaches
- Competitive landscape analysis
- Customer acceptance likelihood assessment
- Business model implications

---

### Problem-Solver → Product Manager
**When to Handoff:**
- Business case development needed
- Product strategy alignment required
- Resource allocation decisions needed
- Stakeholder communication required

**Typical Handoff Message:**
> "Decision analysis complete. Recommended Solution A based on MCDA scoring (8.4/10 confidence). 
> Requires $150K investment over 6 months with 200% ROI projected. Need business case development 
> and stakeholder alignment on resource allocation. See decision-record.md ADR-015 for full rationale."

**What Problem-Solver Provides:**
- Quantified solution recommendation
- Resource requirements and timeline
- Risk assessment and mitigation strategies
- Success metrics and measurement approach
- Stakeholder impact analysis

**Expected PM Response:**
- Business case formalization
- Budget approval and resource allocation
- Stakeholder communication plan
- Implementation timeline integration with product roadmap

---

### Problem-Solver → Architect
**When to Handoff:**
- Technical implementation planning needed
- Architecture integration required
- Performance validation needed
- Technology selection decisions required

**Typical Handoff Message:**
> "Solution analysis identifies microservices architecture as optimal approach using TRIZ Principle #15 
> (Segmentation). Addresses performance contradictions while maintaining maintainability. Need detailed 
> technical architecture and implementation planning. Key technical decisions in decision-record.md 
> sections 4.3-4.5."

**What Problem-Solver Provides:**
- Technical solution approach and rationale
- Architecture decisions with trade-off analysis
- Performance requirements and constraints
- Integration points and dependencies
- Implementation risk assessment

**Expected Architect Response:**
- Detailed technical architecture design
- Implementation approach and phases
- Technology stack recommendations
- Performance validation plan

---

### Problem-Solver → Developer
**When to Handoff:**
- Implementation ready for development
- Complex debugging approach defined
- Performance optimization approach specified
- Technical solution needs coding

**Typical Handoff Message:**
> "Root cause analysis complete. Primary cause identified: database query inefficiency in user service 
> (confidence: 85%). Recommended approach: implement query optimization with connection pooling. 
> Expected 60% performance improvement. Implementation plan in root-cause-analysis.md section 5.2."

**What Problem-Solver Provides:**
- Specific technical solution approach
- Implementation steps and priority order
- Expected outcomes and success metrics
- Risk mitigation strategies
- Testing and validation approach

**Expected Developer Response:**
- Technical implementation plan
- Code changes and testing approach
- Timeline and milestone estimates
- Success measurement implementation

---

### Problem-Solver → Scrum Master
**When to Handoff:**
- Implementation requires story creation
- Work breakdown and planning needed
- Team coordination required
- Agile process integration needed

**Typical Handoff Message:**
> "Complex solution requires 3-phase implementation over 12 weeks. Dependencies mapped between 
> 5 major components. Need story creation and sprint planning to coordinate 3 development teams. 
> Implementation roadmap in decision-record.md section 6.0 with dependency matrix."

**What Problem-Solver Provides:**
- Implementation phases and dependencies
- Work breakdown structure
- Team coordination requirements
- Success criteria for each phase
- Risk factors requiring monitoring

**Expected SM Response:**
- Epic and story creation
- Sprint planning and team coordination
- Dependency management approach
- Progress tracking and reporting plan

## Collaborative Modes

### Advisory Mode
**When Applied:** Problem-solver provides frameworks and guidance while other agents execute
**Agent Relationship:** Consultant → Executor
**Communication Pattern:** 
- Other agent requests specific analytical support
- Problem-solver provides methodology and frameworks
- Other agent applies methods with problem-solver guidance
- Results validated through problem-solver review

**Example:**
> PM: "Need to evaluate 3 product feature options systematically"
> Problem-Solver: "Apply MCDA framework. Here are weighted criteria based on your objectives: [criteria]. Use this scoring method: [method]. I'll validate your analysis."
> PM: [Applies framework and returns analysis]
> Problem-Solver: "Analysis looks sound. Recommend sensitivity test on criteria X and Y."

### Leading Mode
**When Applied:** Problem-solver drives comprehensive analysis with other agents providing domain expertise
**Agent Relationship:** Lead Analyst → Domain Expert
**Communication Pattern:**
- Problem-solver defines analytical approach and timeline
- Other agents provide specialized knowledge and validation
- Problem-solver integrates inputs and drives to decision
- Other agents support implementation of resulting decisions

**Example:**
> Problem-Solver: "Leading comprehensive analysis of platform architecture decision. Need your technical validation at 3 decision points over next 2 weeks. First input needed: current system performance baseline."
> Architect: [Provides technical baseline]
> Problem-Solver: [Integrates into overall analysis, continues analytical process]

### Support Mode
**When Applied:** Other agents lead while problem-solver assists when analytical bottlenecks occur
**Agent Relationship:** Domain Expert → Analytical Support
**Communication Pattern:**
- Other agent drives overall work with clear objectives
- Problem-solver called in when analytical challenges arise
- Focused problem-solving support provided
- Control returns to other agent for implementation

**Example:**
> Architect: "Architecture design progressing but stuck on storage strategy decision. Multiple trade-offs unclear."
> Problem-Solver: "Let me apply decision analysis framework to your storage options. Need 2 hours for evaluation."
> Problem-Solver: [Provides focused analysis and recommendation]
> Architect: [Continues with architecture design using recommendation]

### Review Mode
**When Applied:** Problem-solver validates other agents' work using systematic analytical frameworks
**Agent Relationship:** Validator → Solution Provider
**Communication Pattern:**
- Other agent completes work and requests validation
- Problem-solver applies appropriate analytical frameworks
- Validation results with recommendations provided
- Other agent refines work based on validation feedback

**Example:**
> PM: "Product strategy complete. Need validation of decision rationale and stakeholder alignment."
> Problem-Solver: "Reviewing using stakeholder analysis and business case evaluation frameworks."
> Problem-Solver: "Strategy sound. Recommend strengthening stakeholder concerns section and adding risk mitigation for assumption #3."

## Quality Gates and Validation

### Pre-Handoff Quality Checks
Before any handoff, verify:
- [ ] Clear problem/objective statement provided
- [ ] All relevant context and constraints documented
- [ ] Success criteria and timeline specified
- [ ] Resources and authority boundaries defined
- [ ] Expected deliverables explicitly stated

### Post-Handoff Validation
After receiving handoff, validate:
- [ ] All required information provided
- [ ] Problem scope and constraints understood
- [ ] Success criteria achievable with given resources
- [ ] Timeline realistic for quality outcomes
- [ ] Dependencies and interfaces clear

### Feedback Loops
**Regular Check-ins:** Schedule periodic updates for complex analysis
**Issue Escalation:** Clear process when handoffs encounter problems
**Learning Capture:** Document what works well for future handoffs
**Process Improvement:** Regular retrospectives on handoff effectiveness

## Common Handoff Challenges and Solutions

### Challenge: Incomplete Context Transfer
**Symptoms:** Receiving agent asks many clarifying questions, analysis goes in wrong direction
**Solution:** Use structured handoff templates with required information checklist
**Prevention:** Problem-solver creates comprehensive context documents before handoff

### Challenge: Misaligned Expectations
**Symptoms:** Deliverables don't match what was expected, timeline disputes
**Solution:** Explicit success criteria and timeline agreement before starting work
**Prevention:** Written confirmation of handoff scope and deliverables

### Challenge: Quality vs. Speed Trade-offs
**Symptoms:** Pressure to rush analysis, skipping important validation steps
**Solution:** Clear discussion of trade-offs and explicit agreement on analysis depth
**Prevention:** Upfront agreement on analysis rigor appropriate to decision importance

### Challenge: Domain Knowledge Gaps
**Symptoms:** Problem-solver lacks context for domain-specific validation
**Solution:** Extended collaboration phase with domain expert teaching
**Prevention:** Problem-solver maintains learning log of domain knowledge gaps

## Success Metrics for Handoffs

### Quantitative Metrics
- **Handoff Completion Rate:** % of handoffs completed without requiring rework
- **Cycle Time:** Average time from handoff initiation to completion
- **Quality Score:** % of handoffs meeting all success criteria on first attempt
- **Clarification Frequency:** Average number of questions required per handoff

### Qualitative Indicators
- **Agent Satisfaction:** Feedback scores from both giving and receiving agents  
- **Process Smoothness:** Subjective assessment of handoff friction
- **Value Addition:** Assessment of problem-solver contribution quality
- **Learning Transfer:** Knowledge gained by other agents from problem-solver methods

### Improvement Indicators
- **Repeat Collaboration:** Frequency of agents returning for problem-solver support
- **Method Adoption:** Other agents adopting problem-solving methods independently
- **Decision Quality:** Long-term success of decisions supported by problem-solver analysis
- **Process Innovation:** New handoff patterns and improvements identified

## Templates and Standard Operating Procedures

### Handoff Request Template
```
Agent: [Requesting Agent]
Problem/Objective: [Clear statement of what needs to be solved/analyzed]
Context: [Background information and constraints]
Deliverables: [Specific outputs expected]
Timeline: [When results are needed]
Resources: [Budget, tools, access available]
Success Criteria: [How to measure successful completion]
Priority: [High/Medium/Low with justification]
```

### Handoff Response Template
```
Acceptance: [Yes/No with reasoning]
Approach: [Analytical methods and frameworks to be applied]
Timeline: [Realistic timeline with milestones]
Assumptions: [Key assumptions being made]
Dependencies: [What is needed from other agents/sources]
Deliverables: [Confirmation of specific outputs]
Check-in Schedule: [When and how to provide updates]
```

### Completion Handback Template
```
Deliverables: [Links to all completed documents/analysis]
Key Findings: [Summary of most important results]
Recommendations: [Specific actions recommended]
Confidence Level: [High/Medium/Low with reasoning]
Limitations: [What the analysis doesn't cover]
Next Steps: [Recommended follow-up actions]
Questions: [Any outstanding issues requiring clarification]
```