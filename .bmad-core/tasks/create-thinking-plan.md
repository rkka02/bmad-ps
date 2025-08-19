# create-thinking-plan

## Execution Notice
You are about to execute the **Create Thinking Plan** task. This task generates a detailed iterative thinking plan based on the complexity assessment, creating a structured todo-list approach that enforces step-by-step analysis.

## Method Description
**Iterative Thinking Plan Generation**: Creates complexity-appropriate thinking plans that enforce systematic analysis through sequential steps with validation gates.

**Core Principle**: Structure thinking to match problem complexity while ensuring each step builds on previous insights and cannot be skipped without completion.

## Interactive Flow

### Step 1: Retrieve Complexity Assessment
**Check for Previous Assessment**: Look for `complexity-assessment.md` or prompt for complexity level if not available.

**If Assessment Missing**: 
"I need to understand problem complexity first. Should I:
1. Run complexity assessment now
2. You specify complexity level (Simple/Medium/Complex/Wicked)  
3. Use default Medium complexity"

### Step 2: Generate Appropriate Thinking Plan

**Based on Complexity Level, Generate Plan**:

#### Simple Problems (3 Steps)
```yaml
thinking_plan:
  complexity_level: "Simple"
  total_steps: 3
  plan_id: "simple-{timestamp}"
  
  steps:
    - step: 1
      title: "Problem Definition & Core Issue"
      status: "pending"
      focus_question: "What exactly needs to be solved and why?"
      methods: ["Problem statement crafting", "Core issue identification", "Success criteria"]
      deliverables:
        - type: "document"
          name: "problem-definition.md"
          template: "simple-problem-def-tmpl"
      validation_criteria:
        - "Problem statement is specific and actionable"
        - "Success criteria are clear and measurable"
        - "Core issue identified and validated"
      
    - step: 2
      title: "Solution Generation & Evaluation"
      status: "pending"
      focus_question: "What are the viable approaches and their trade-offs?"
      methods: ["Brainstorming", "Best practices lookup", "Quick pros/cons analysis"]
      prerequisites: ["step-1"]
      deliverables:
        - type: "analysis"
          name: "solution-options.md"
          template: "simple-solutions-tmpl"
      validation_criteria:
        - "At least 3 distinct solution approaches identified"
        - "Clear pros/cons for each approach"
        - "Initial feasibility assessment completed"
      
    - step: 3
      title: "Decision & Implementation Planning"
      status: "pending"
      focus_question: "Which solution and how to execute it?"
      methods: ["Simple criteria evaluation", "Implementation planning", "Next actions"]
      prerequisites: ["step-2"]
      deliverables:
        - type: "decision"
          name: "implementation-plan.md"
          template: "simple-implementation-tmpl"
      validation_criteria:
        - "Clear solution selection with rationale"
        - "Actionable implementation steps defined"
        - "Success metrics defined"
```

#### Medium Problems (5 Steps)  
```yaml
thinking_plan:
  complexity_level: "Medium"
  total_steps: 5
  plan_id: "medium-{timestamp}"
  
  steps:
    - step: 1
      title: "Problem Scoping & Stakeholder Analysis"
      status: "pending"
      focus_question: "Who is affected and what are the true boundaries?"
      methods: ["Stakeholder mapping", "Problem boundaries", "Success criteria", "Constraint identification"]
 "20 minutes"
      deliverables:
        - type: "document"
          name: "problem-scope.md"
          template: "medium-problem-scope-tmpl"
      validation_criteria:
        - "All key stakeholders identified with interests mapped"
        - "Problem boundaries clearly defined"
        - "Success criteria agreed upon by stakeholders"
        
    - step: 2
      title: "Root Cause Investigation"
      status: "pending"
      focus_question: "What are the underlying causes driving this problem?"
      methods: ["5 Whys", "Fishbone analysis", "Evidence gathering"]
 "25 minutes"
      prerequisites: ["step-1"]
      deliverables:
        - type: "analysis"
          name: "root-cause-analysis.md"
          template: "root-cause-tmpl"
      validation_criteria:
        - "Root causes identified with supporting evidence"
        - "Cause-effect relationships validated"
        - "Addressed symptoms vs causes distinction"
        
    - step: 3
      title: "Solution Space Exploration"
      status: "pending"
      focus_question: "What are all possible approaches to address root causes?"
      methods: ["TRIZ principles", "Analogical thinking", "Best practices research", "Creative techniques"]
 "30 minutes"
      prerequisites: ["step-2"]
      deliverables:
        - type: "analysis"
          name: "solution-portfolio.md"
          template: "solution-portfolio-tmpl"
      validation_criteria:
        - "Diverse solution approaches generated (5-7 options)"
        - "Solutions address root causes, not just symptoms"
        - "Both incremental and breakthrough options considered"
        
    - step: 4
      title: "Trade-off Analysis & Evaluation"
      status: "pending"
      focus_question: "What are the pros, cons, and trade-offs of each approach?"
      methods: ["Multi-criteria evaluation", "Risk assessment", "Resource analysis"]
 "25 minutes"
      prerequisites: ["step-3"]
      deliverables:
        - type: "analysis"
          name: "solution-evaluation.md"
          template: "solution-matrix-tmpl"
      validation_criteria:
        - "Each solution evaluated against consistent criteria"
        - "Risks and mitigation strategies identified"
        - "Resource requirements estimated"
        
    - step: 5
      title: "Decision & Implementation Strategy"
      status: "pending"
      focus_question: "Final selection with comprehensive execution plan"
      methods: ["Decision rationale", "Phased implementation", "Success metrics", "Monitoring plan"]
 "20 minutes"
      prerequisites: ["step-4"]
      deliverables:
        - type: "decision"
          name: "decision-record.md"
          template: "decision-record-tmpl"
      validation_criteria:
        - "Clear decision with compelling rationale"
        - "Phased implementation plan with milestones"
        - "Success metrics and monitoring approach defined"
```

#### Complex Problems (7 Steps)
```yaml
thinking_plan:
  complexity_level: "Complex"
  total_steps: 7
  plan_id: "complex-{timestamp}"
  
  steps:
    - step: 1
      title: "Multi-Dimensional Problem Analysis"
      status: "pending"
      focus_question: "How does this problem manifest across different dimensions?"
      methods: ["Systems mapping", "Stakeholder analysis", "Force field analysis", "Problem ecosystem"]
 "30 minutes"
      
    - step: 2
      title: "First Principles Decomposition"
      status: "pending"
      focus_question: "What are the fundamental elements and assumptions?"
      methods: ["First principles thinking", "MECE decomposition", "Assumption challenging"]
 "25 minutes"
      prerequisites: ["step-1"]
      
    - step: 3
      title: "Comprehensive Root Cause Investigation"
      status: "pending"
      focus_question: "What are all the causal factors and their interactions?"
      methods: ["5 Whys", "Fault tree analysis", "Causal loop diagrams", "Systems thinking"]
 "35 minutes"
      prerequisites: ["step-2"]
      
    - step: 4
      title: "Constraint & Opportunity Mapping"
      status: "pending"
      focus_question: "What limits our solutions and what enables breakthrough?"
      methods: ["Constraint analysis", "Opportunity identification", "Resource assessment", "Leverage points"]
 "25 minutes"
      prerequisites: ["step-3"]
      
    - step: 5
      title: "Innovation & Solution Generation"
      status: "pending"
      focus_question: "How can we create breakthrough solutions?"
      methods: ["TRIZ", "Biomimicry", "Lateral thinking", "Cross-industry analysis", "Design thinking"]
 "40 minutes"
      prerequisites: ["step-4"]
      
    - step: 6
      title: "Multi-Criteria Decision Analysis"
      status: "pending"
      focus_question: "How do solutions perform across all important criteria?"
      methods: ["MCDA", "Sensitivity analysis", "Scenario testing", "Risk modeling"]
 "35 minutes"
      prerequisites: ["step-5"]
      
    - step: 7
      title: "Implementation Strategy & Risk Mitigation"
      status: "pending"
      focus_question: "How do we execute with contingencies for uncertainty?"
      methods: ["Phased implementation", "Risk analysis", "Success metrics", "Feedback loops", "Adaptive planning"]
 "30 minutes"
      prerequisites: ["step-6"]
```

#### Wicked Problems (10 Steps)
```yaml
thinking_plan:
  complexity_level: "Wicked"
  total_steps: 10
  plan_id: "wicked-{timestamp}"
  
  steps:
    - step: 1
      title: "Problem Space Exploration"
      focus_question: "What makes this problem 'wicked' and how do we approach it?"
 "25 minutes"
      
    - step: 2
      title: "Stakeholder Ecosystem Mapping"
      focus_question: "Who are all the players and what are their conflicting interests?"
 "30 minutes"
      
    - step: 3
      title: "Multiple Problem Framings"
      focus_question: "How can this problem be viewed from different perspectives?"
 "35 minutes"
      
    - step: 4
      title: "First Principles & Systems Analysis"
      focus_question: "What are the fundamental dynamics and system behaviors?"
 "40 minutes"
      
    - step: 5
      title: "Historical & Cross-Domain Analysis"
      focus_question: "What can we learn from similar challenges elsewhere?"
 "35 minutes"
      
    - step: 6
      title: "Constraint & Leverage Point Identification"
      focus_question: "Where can we intervene most effectively in this system?"
 "30 minutes"
      
    - step: 7
      title: "Solution Space Generation"
      focus_question: "What radical and incremental interventions are possible?"
 "45 minutes"
      
    - step: 8
      title: "Multi-Perspective Evaluation"
      focus_question: "How do different stakeholders view each option?"
 "40 minutes"
      
    - step: 9
      title: "Adaptive Strategy Design"
      focus_question: "How do we plan for emergence and continuous learning?"
 "35 minutes"
      
    - step: 10
      title: "Implementation & Monitoring Plan"
      focus_question: "How do we execute with continuous adaptation capability?"
 "40 minutes"
```

### Step 3: Simplified Plan Confirmation

**Present Plan for Approval**:
```
ITERATIVE THINKING PLAN GENERATED
==================================

Problem: [from complexity assessment]
Complexity Level: [Simple/Medium/Complex/Wicked] 
Proposed Steps: [3/5/7/10]

THINKING STEPS:
[For each step, show: Step N: Title - Focus Question]

Do you want to proceed with this {N}-step thinking plan?

Options:
1. ✅ Yes, execute all steps automatically
2. 🔢 Adjust - Change number of steps ([3/5/7/10])
3. ❌ Cancel - Return without creating plan

[If option 2 selected: "How many steps? (3=Simple, 5=Medium, 7=Complex, 10=Wicked)"]

**When Option 1 Selected (Yes, execute automatically)**:
- Save thinking plan
- Immediately trigger execute-step task in auto mode
- Begin sequential execution of all steps
```

## Output Format

### Primary Output: thinking-plan.md
```yaml
plan_metadata:
  plan_id: "[complexity]-[timestamp]"
  created: "[timestamp]"
  complexity_level: "[Simple/Medium/Complex/Wicked]"
  total_steps: [number]
  
problem_context:
  statement: "[problem description]"
  complexity_scores: "[from assessment]"
  
execution_state:
  current_step: 1
  status: "ready_to_start"
  start_time: null
  step_completions: []
  
thinking_steps: [detailed step array as generated above]

session_tracking:
  insights_captured: []
  decisions_made: []
  deliverables_created: []
```

## Integration Points

**With Complexity Assessment**: 
- Reads complexity-assessment.md for plan generation
- Uses complexity scores to select appropriate template

**With Step Execution**:
- Provides structured plan for execute-step task
- Maintains state across thinking sessions
- Enforces sequential progression

**With Agent State**:
- Updates agent context with active thinking plan
- Tracks progress and maintains session continuity

## Validation Criteria

**Plan Quality**:
- Steps logically build on each other
- Appropriate depth for complexity level
- Clear focus questions for each step

**Enforceability**:
- Prerequisites clearly defined
- Validation criteria are specific and checkable
- Cannot advance without meeting completion criteria

## Notes for Sage

**Plan Adaptation**:
- Plans can be adjusted mid-execution if complexity changes
- Emergency skip procedures available but discouraged
- Focus on insight quality and systematic progression