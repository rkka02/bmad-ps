# complexity-assessment

## Execution Notice
You are about to execute the **Complexity Assessment** task. This task evaluates problems across 5 dimensions to determine the appropriate level of iterative thinking depth (3, 5, 7, or 10+ steps).

## Method Description
**Complexity Assessment Framework**: Systematic evaluation of problem characteristics to determine thinking plan depth.

**Core Principle**: Match analytical rigor to problem complexity - simple problems get focused analysis, wicked problems get comprehensive systematic thinking.

**Assessment Dimensions**:
1. **Domain Breadth**: How many disciplines/domains are involved?
2. **Stakeholder Alignment**: Level of agreement among affected parties
3. **Solution Uncertainty**: How clear is the path to resolution?
4. **Impact Scope**: Breadth and reversibility of consequences
5. **Time Pressure**: Urgency vs thoroughness trade-offs

## Interactive Flow

### Step 1: Problem Context Gathering
**Question**: "Describe the problem you're trying to solve in 2-3 sentences."

*Wait for user response, then proceed to dimensional assessment*

### Step 2: Dimensional Assessment

**Domain Breadth Assessment**:
"How many different domains or disciplines does this problem span?"
- 1 = Single domain (e.g., purely technical, purely business)
- 2 = Two related domains (e.g., technical + UX, business + legal)  
- 3 = Three domains (e.g., technical + business + user experience)
- 4 = Four or more domains (e.g., technical + business + legal + social impact)

*Record score, continue*

**Stakeholder Alignment Assessment**:
"What's the level of agreement among people affected by this problem?"
- 1 = Single stakeholder or high alignment among all parties
- 2 = 2-3 stakeholders with minor disagreements on approach
- 3 = Multiple stakeholders with conflicting priorities
- 4 = Many stakeholders with fundamental conflicts in values/goals

*Record score, continue*

**Solution Uncertainty Assessment**:
"How clear is the path to solving this problem?"
- 1 = Known solutions exist and have been proven to work
- 2 = Adaptations of known solutions are needed
- 3 = Novel solutions required but constraints are clear
- 4 = No known solutions exist, unclear what constraints apply

*Record score, continue*

**Impact Scope Assessment**:
"What's the breadth of consequences if this problem is solved incorrectly?"
- 1 = Local impact, easily reversible if wrong
- 2 = Team/project impact, moderately reversible
- 3 = Organizational impact, difficult to reverse
- 4 = Strategic/ecosystem impact, largely irreversible

*Record score, continue*

**Time Pressure Assessment**:
"What's the timeline pressure for solving this problem?"
- 1 = No time pressure, can be thoroughly analytical
- 2 = Moderate timeline, some analysis trade-offs acceptable
- 3 = Tight timeline, must prioritize key analysis only
- 4 = Crisis mode, minimal analysis time available

*Record score, calculate total*

### Step 3: Complexity Calculation & Recommendation

**Calculate Total Score**: Sum all dimension scores (5-20 range)

**Determine Complexity Level**:
- **Simple (5-8)**: 3-step thinking plan
- **Medium (9-12)**: 5-step thinking plan  
- **Complex (13-16)**: 7-step thinking plan
- **Wicked (17-20)**: 10-step thinking plan

**Present Assessment Results**:
```
COMPLEXITY ASSESSMENT RESULTS
================================

Problem: [user's problem statement]

Dimensional Scores:
- Domain Breadth: [score]/4
- Stakeholder Alignment: [score]/4  
- Solution Uncertainty: [score]/4
- Impact Scope: [score]/4
- Time Pressure: [score]/4

Total Complexity Score: [total]/20
Complexity Level: [Simple/Medium/Complex/Wicked]

Recommended Thinking Plan: [X]-step iterative analysis

Reasoning: [1-2 sentences explaining why this complexity level fits]
```

### Step 4: Thinking Plan Preview

**Show Recommended Plan Structure**:
For the determined complexity level, show:
- Number of thinking steps
- High-level step titles
- Key deliverables

**Confirmation**: "Does this thinking plan depth feel appropriate for your problem? (yes/adjust/explain)"

## Output Format

### Primary Output: complexity-assessment.md
```yaml
problem_statement: "[user's description]"
assessment_date: "[timestamp]"

dimensional_scores:
  domain_breadth: [1-4]
  stakeholder_alignment: [1-4]  
  solution_uncertainty: [1-4]
  impact_scope: [1-4]
  time_pressure: [1-4]

complexity_summary:
  total_score: [5-20]
  complexity_level: "[Simple/Medium/Complex/Wicked]"
  thinking_steps: [3/5/7/10]
  
recommended_plan:
  template: "[simple/medium/complex/wicked]_thinking_plan"
  focus_areas: ["key", "analysis", "areas"]
  
assessment_reasoning: "[explanation of complexity level choice]"

next_action: "Execute 'create-thinking-plan' command to generate detailed step-by-step plan"
```

## Integration Points

**With Other Tasks**:
- Feeds into `create-thinking-plan` task
- Can be revisited during `adjust-plan` if complexity changes
- Results used by `execute-step` for step selection

**With Templates**:  
- Generates complexity-assessment.md using assessment template
- Informs selection of appropriate thinking plan template

**With Agent Commands**:
- Triggered by `*assess-complexity` command
- Results stored in agent state for session context
- Can be re-run if problem scope changes significantly

## Validation Criteria

**Assessment Quality**:
- Each dimension scored based on clear evidence from problem description
- Total score logically reflects individual dimension scores  
- Reasoning provided connects scores to complexity recommendation
- Time estimates realistic for recommended depth

**User Alignment**:
- User confirms complexity assessment feels appropriate
- Any adjustments explained and rescored
- Final recommendation accepted before proceeding

## Notes for Sage

**Calibration Guidelines**:
- Err toward slightly higher complexity when uncertain
- Consider that users often underestimate stakeholder complexity
- Document any manual adjustments with reasoning

**Common Patterns**:
- Technical problems often underestimate stakeholder dimension
- Business problems often underestimate solution uncertainty  
- Innovation challenges typically score high on solution uncertainty
- Organizational changes typically score high on impact scope and stakeholder alignment