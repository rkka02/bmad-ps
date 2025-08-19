# Iterative Thinking Framework for Problem-Solver Agent

## Overview

This plan implements an iterative thinking system for the BMad Problem-Solver agent that enforces step-by-step analysis based on problem complexity. The system creates dynamic thinking plans that scale from 3 steps (simple) to 10+ steps (wicked problems).

## Complexity Assessment Framework

### Complexity Dimensions
The agent assesses problems across 5 dimensions (1-4 scale each):

```yaml
complexity_dimensions:
  domain_breadth:      # How many domains/disciplines involved
    1: Single domain (e.g., pure technical)
    2: Two related domains (e.g., tech + UX) 
    3: Three domains (e.g., tech + business + user)
    4: Four+ domains (e.g., tech + business + legal + social)
  
  stakeholder_alignment:  # Level of stakeholder agreement
    1: Single stakeholder or high alignment
    2: 2-3 stakeholders with minor disagreements
    3: Multiple stakeholders with conflicting priorities
    4: Many stakeholders with fundamental conflicts
  
  solution_uncertainty:   # How clear is the solution space
    1: Known solutions exist and work
    2: Adaptations of known solutions needed
    3: Novel solutions required but constraints clear
    4: No known solutions, unclear constraints
  
  impact_scope:          # Breadth of consequences
    1: Local impact, easily reversible
    2: Team/project impact, moderately reversible
    3: Organizational impact, difficult to reverse
    4: Strategic/ecosystem impact, irreversible
  
  time_pressure:         # Urgency vs thoroughness tradeoff
    1: No time pressure, can be thorough
    2: Moderate timeline, some analysis trade-offs
    3: Tight timeline, must prioritize key analysis
    4: Crisis mode, minimal analysis time
```

### Complexity Calculation
```
Total Complexity Score = Sum of all dimension scores
- Simple (5-8): 3 thinking steps
- Medium (9-12): 5 thinking steps  
- Complex (13-16): 7 thinking steps
- Wicked (17-20): 10 thinking steps
```

## Iterative Thinking Templates

### Simple Problems (3 Steps)
```yaml
simple_thinking_plan:
  - step: 1
    title: "Problem Definition & Core Issue"
    focus: "What exactly needs to be solved?"
    methods: ["Problem statement crafting", "Core issue identification"]
    output: "Clear problem definition"
    time_box: "15 minutes"
  
  - step: 2
    title: "Solution Generation"
    focus: "What are the viable approaches?"
    methods: ["Brainstorming", "Best practices lookup"]
    output: "3-5 solution options"
    time_box: "20 minutes"
  
  - step: 3
    title: "Selection & Implementation"
    focus: "Which solution and how to execute?"
    methods: ["Simple criteria evaluation", "Implementation planning"]
    output: "Selected solution with action plan"
    time_box: "15 minutes"
```

### Medium Problems (5 Steps)
```yaml
medium_thinking_plan:
  - step: 1
    title: "Problem Scoping & Stakeholder Analysis"
    focus: "Who is affected and what are the boundaries?"
    methods: ["Stakeholder mapping", "Problem boundaries", "Success criteria"]
    output: "Comprehensive problem scope"
    time_box: "20 minutes"
  
  - step: 2
    title: "Root Cause Investigation"
    focus: "What are the underlying causes?"
    methods: ["5 Whys", "Fishbone analysis"]
    output: "Validated root causes"
    time_box: "25 minutes"
  
  - step: 3
    title: "Solution Space Exploration"
    focus: "What are all possible approaches?"
    methods: ["TRIZ", "Analogical thinking", "Best practices research"]
    output: "Diverse solution portfolio"
    time_box: "30 minutes"
  
  - step: 4
    title: "Trade-off Analysis"
    focus: "What are the pros/cons of each approach?"
    methods: ["Multi-criteria evaluation", "Risk assessment"]
    output: "Weighted solution comparison"
    time_box: "25 minutes"
  
  - step: 5
    title: "Decision & Implementation Strategy"
    focus: "Final selection with execution plan"
    methods: ["Decision rationale", "Phased implementation", "Success metrics"]
    output: "Decision record with roadmap"
    time_box: "20 minutes"
```

### Complex Problems (7 Steps)
```yaml
complex_thinking_plan:
  - step: 1
    title: "Multi-Dimensional Problem Analysis"
    focus: "Understanding the problem ecosystem"
    methods: ["Systems mapping", "Stakeholder analysis", "Force field analysis"]
    output: "Problem ecosystem map"
    time_box: "30 minutes"
  
  - step: 2
    title: "First Principles Decomposition"
    focus: "Breaking down to fundamental elements"
    methods: ["First principles thinking", "MECE decomposition"]
    output: "Fundamental problem elements"
    time_box: "25 minutes"
  
  - step: 3
    title: "Root Cause Investigation"
    focus: "Multi-method causal analysis"
    methods: ["5 Whys", "Fault tree analysis", "Causal loop diagrams"]
    output: "Validated causal model"
    time_box: "35 minutes"
  
  - step: 4
    title: "Constraint & Opportunity Mapping"
    focus: "What limits and enables solutions?"
    methods: ["Constraint analysis", "Opportunity identification", "Resource assessment"]
    output: "Solution space boundaries"
    time_box: "25 minutes"
  
  - step: 5
    title: "Innovation & Solution Generation"
    focus: "Creating diverse solution approaches"
    methods: ["TRIZ", "Biomimicry", "Lateral thinking", "Cross-industry analysis"]
    output: "Innovation portfolio"
    time_box: "40 minutes"
  
  - step: 6
    title: "Multi-Criteria Decision Analysis"
    focus: "Systematic solution evaluation"
    methods: ["MCDA", "Sensitivity analysis", "Scenario testing"]
    output: "Quantified decision matrix"
    time_box: "35 minutes"
  
  - step: 7
    title: "Implementation Strategy & Risk Mitigation"
    focus: "Execution planning with contingencies"
    methods: ["Phased implementation", "Risk analysis", "Success metrics", "Feedback loops"]
    output: "Comprehensive implementation plan"
    time_box: "30 minutes"
```

### Wicked Problems (10 Steps)
```yaml
wicked_thinking_plan:
  - step: 1
    title: "Problem Space Exploration"
    focus: "Understanding the wicked problem characteristics"
    methods: ["Wicked problem assessment", "Multiple perspective gathering"]
    output: "Problem characterization"
    time_box: "25 minutes"
  
  - step: 2
    title: "Stakeholder Ecosystem Mapping"
    focus: "Who are all the players and their interests?"
    methods: ["Stakeholder analysis", "Power-interest mapping", "Conflict identification"]
    output: "Stakeholder ecosystem map"
    time_box: "30 minutes"
  
  - step: 3
    title: "Multiple Problem Framings"
    focus: "How can this problem be viewed differently?"
    methods: ["Perspective-taking", "Reframing exercises", "Mental model elicitation"]
    output: "Multiple problem definitions"
    time_box: "35 minutes"
  
  - step: 4
    title: "First Principles & Systems Analysis"
    focus: "What are the fundamental dynamics?"
    methods: ["First principles thinking", "Systems mapping", "Feedback loop identification"]
    output: "Systems understanding"
    time_box: "40 minutes"
  
  - step: 5
    title: "Historical & Cross-Domain Analysis"
    focus: "What can we learn from similar challenges?"
    methods: ["Case study analysis", "Analogical reasoning", "Pattern recognition"]
    output: "Learning from precedents"
    time_box: "35 minutes"
  
  - step: 6
    title: "Constraint & Leverage Point Identification"
    focus: "Where can we intervene most effectively?"
    methods: ["Constraint theory", "Leverage point analysis", "Intervention mapping"]
    output: "Intervention opportunities"
    time_box: "30 minutes"
  
  - step: 7
    title: "Solution Space Generation"
    focus: "Creating radical and incremental options"
    methods: ["TRIZ", "Design thinking", "Scenario planning", "Innovation techniques"]
    output: "Solution option space"
    time_box: "45 minutes"
  
  - step: 8
    title: "Multi-Perspective Evaluation"
    focus: "How do different stakeholders view options?"
    methods: ["Multi-stakeholder MCDA", "Devil's advocate", "Pre-mortem analysis"]
    output: "Multi-perspective evaluation"
    time_box: "40 minutes"
  
  - step: 9
    title: "Adaptive Strategy Design"
    focus: "Planning for emergence and learning"
    methods: ["Adaptive management", "Learning design", "Feedback mechanisms"]
    output: "Adaptive strategy framework"
    time_box: "35 minutes"
  
  - step: 10
    title: "Implementation & Monitoring Plan"
    focus: "Execution with continuous adaptation"
    methods: ["Phased rollout", "Learning metrics", "Pivot criteria", "Governance design"]
    output: "Adaptive implementation plan"
    time_box: "40 minutes"
```

## Step Execution System

### Thinking Step Structure
```yaml
thinking_step:
  id: "step-{number}"
  title: "Step Title"
  status: "pending" | "in_progress" | "completed" | "skipped"
  focus_question: "Core question for this step"
  methods: ["list", "of", "applicable", "methods"]
  time_box: "estimated time"
  prerequisites: ["previous", "steps", "required"]
  deliverables:
    - type: "document" | "analysis" | "decision"
      name: "deliverable name"
      template: "optional template reference"
  validation_criteria:
    - "Criteria 1 for step completion"
    - "Criteria 2 for step completion"
  next_actions: ["possible", "next", "steps"]
```

## Implementation in BMad Agent

### New Agent Commands
```yaml
iterative_commands:
  - assess-complexity: "Evaluate problem complexity across 5 dimensions"
  - create-thinking-plan: "Generate appropriate iterative thinking plan"
  - execute-step: "Execute current thinking step with focus"
  - review-step: "Validate step completion before proceeding"
  - plan-status: "Show thinking plan progress and next steps"
  - adjust-plan: "Modify plan based on emerging insights"
  - skip-step: "Skip current step with justification (discouraged)"
  - thinking-summary: "Synthesize insights across all completed steps"
```

### Agent State Management
```yaml
agent_state:
  current_problem: "problem description"
  complexity_assessment:
    scores: {domain_breadth: 3, stakeholder_alignment: 2, ...}
    total_score: 14
    complexity_level: "complex"
  
  thinking_plan:
    template: "complex_thinking_plan"
    total_steps: 7
    current_step: 3
    steps: [array of step objects]
  
  session_context:
    start_time: "timestamp"
    accumulated_insights: ["insight 1", "insight 2"]
    decision_trail: ["decision 1", "decision 2"]
    deliverables: ["doc1.md", "analysis2.md"]
```

### Enforcement Mechanisms
1. **Sequential Progression**: Cannot skip to step N+2 without completing step N+1
2. **Validation Gates**: Each step requires validation criteria to be met
3. **Time Boxing**: Gentle reminders about time allocation per step
4. **Insight Capture**: Force documentation of key insights before proceeding
5. **Backtracking**: Allow revisiting previous steps if new information emerges

## Integration Points

### With Existing BMad Tasks
- Map existing tasks (first-principles-analysis.md, root-cause-investigation.md, etc.) to thinking steps
- Use thinking steps to orchestrate task execution
- Ensure task outputs feed into subsequent steps

### With Templates
- Create step-specific templates for capturing insights
- Link template generation to step completion
- Use templates to enforce structured thinking

### With Other Agents
- Design handoff points where other agents can provide domain expertise
- Allow collaborative steps where multiple agents contribute
- Maintain thinking plan context across agent interactions

This framework transforms the Problem-Solver agent from a collection of independent tools into a systematic thinking machine that adapts its depth and rigor to problem complexity.