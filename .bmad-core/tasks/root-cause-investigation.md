# Root Cause Investigation

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

Multi-method root cause analysis - SELECT appropriate method based on problem complexity and characteristics.

**CRITICAL RULE**: This task applies systematic investigation methods. User interaction is REQUIRED for method selection and validation at each step.

## Method Selection Matrix

Apply this decision tree to select optimal investigation approach:

```
Problem Characteristics → Method
├── Single Linear Cause → 5 Whys
├── Multiple Contributing Factors → Fishbone Diagram
├── Complex System Failure → Fault Tree Analysis
├── Unknown Failure Mode → Systematic Experimentation
└── Recurring Pattern → Historical Analysis + Multiple Methods
```

## Method 1: 5 Whys Analysis

**Best For**: Simple, linear causation chains
**Developed By**: Sakichi Toyoda (Toyota Production System)

### Execution Process

1. **Problem Statement Setup**
   - Define the specific problem/symptom
   - Ensure problem is observable and measurable
   - Document when/where/how the problem manifests

2. **Iterative Why Analysis**
   ```
   Problem: [State the problem]
   Why 1: [First level cause] → Ask next Why
   Why 2: [Deeper cause] → Ask next Why  
   Why 3: [Even deeper] → Ask next Why
   Why 4: [Root territory] → Ask next Why
   Why 5: [True root cause] → Validate
   ```

3. **Validation at Each Level**
   - Is this the real cause or another symptom?
   - Can we go deeper?
   - Do we have evidence for this causal link?
   - What would happen if we removed this cause?

### 5 Whys Interactive Flow

When `elicit: true`:
1. **Accept this cause and continue** - Move to next Why
2. **Challenge this causal link** - Question the connection
3. **Gather more evidence** - Need data to validate
4. **Try parallel cause** - Explore alternative at this level
5. **Go deeper on this cause** - More Whys needed here
6. **Test cause removal** - Validate through experiment
7. **Switch to different method** - 5 Whys not working
8. **Consult domain expert** - Need specialist knowledge
9. **Document assumption** - Mark for later validation

## Method 2: Fishbone Diagram (Ishikawa)

**Best For**: Multi-factorial problems with various contributing causes
**Categories**: 6M Framework

### Category Setup
1. **People (Manpower)**: Skills, training, motivation, communication
2. **Process (Method)**: Procedures, workflow, standards, sequence
3. **Technology (Machine)**: Tools, systems, software, infrastructure
4. **Environment (Mother Nature)**: Physical conditions, culture, regulations
5. **Materials**: Inputs, resources, information quality, availability
6. **Measurement**: Metrics, monitoring, feedback, detection systems

### Execution Process

1. **Diagram Construction**
   - Draw fish head (problem) on right
   - Draw main spine horizontally
   - Add category bones at angles
   - Populate with specific causes

2. **Systematic Category Investigation**
   - For each category, brainstorm all possible causes
   - Rate likelihood: High/Medium/Low
   - Assess evidence quality: Strong/Moderate/Weak/None
   - Identify interdependencies between causes

3. **Root Cause Prioritization**
   - Use data to validate most likely causes
   - Test: If we fix this, does problem disappear?
   - Rank causes by impact and feasibility

### Fishbone Interactive Elicitation

1. **Continue with current category** - Keep exploring this area
2. **Move to next category** - Shift focus to different type
3. **Combine causes across categories** - Look for interactions
4. **Validate with data** - Check evidence for this cause
5. **Rate cause likelihood** - Estimate probability
6. **Test cause hypothesis** - Design validation experiment
7. **Add new category** - Standard 6M insufficient
8. **Prioritize for action** - Focus on actionable causes
9. **Deep dive this branch** - More detail needed here

## Method 3: Fault Tree Analysis (FTA)

**Best For**: Complex systems, safety-critical analysis, multiple failure modes
**Approach**: Top-down deductive failure analysis

### Tree Construction Process

1. **Define Top Event**
   - Specific undesired system behavior
   - Must be observable and measurable
   - Example: "System crashes on startup"

2. **Identify Immediate Causes**
   - What directly causes top event?
   - Use logic gates: AND/OR/NOT
   - OR gate: Any one cause triggers event
   - AND gate: All causes must occur together

3. **Recursive Decomposition**
   - For each immediate cause, ask: "What causes this?"
   - Continue until basic events (cannot decompose further)
   - Basic events are hardware failures, human errors, etc.

4. **Probability Analysis** (if data available)
   - Assign failure probabilities to basic events
   - Calculate probability paths using Boolean algebra
   - Identify critical paths and common cause failures

### FTA Interactive Elicitation

1. **Continue decomposing this branch** - Go deeper on this path
2. **Switch to parallel branch** - Analyze different failure mode
3. **Add AND gate** - Multiple conditions must occur
4. **Add OR gate** - Any condition can cause failure
5. **Define basic event** - Cannot decompose further
6. **Assign probabilities** - Add quantitative analysis
7. **Identify common causes** - Same root affects multiple branches
8. **Calculate critical path** - Find most likely failure sequence
9. **Validate with testing** - Confirm failure modes exist

## Method 4: Systematic Experimentation

**Best For**: Unknown failure modes, complex interactions, hypothesis testing

### Experimental Design

1. **Hypothesis Formation**
   - Based on initial investigation
   - Must be testable and falsifiable
   - Define expected results if hypothesis true

2. **Variable Control**
   - Independent variables (what we change)
   - Dependent variables (what we measure)
   - Controlled variables (kept constant)
   - Confounding variables (could affect results)

3. **Test Execution**
   - Run controlled experiments
   - Document all conditions
   - Measure results systematically
   - Repeat for statistical significance

## Output Structure

```yaml
investigation_method: "5-whys|fishbone|fault-tree|experimental"
problem_statement:
  description: "Clear description of the problem"
  symptoms: ["Observable manifestations"]
  frequency: "How often it occurs"
  impact: "Severity and scope of impact"
  context: "When/where/how it happens"

# For 5 Whys Method
five_whys_analysis:
  why_1:
    question: "Why does [problem] occur?"
    answer: "First level cause"
    evidence: "Supporting evidence"
    confidence: "percentage confidence"
  why_2:
    question: "Why does [why_1_answer] occur?"
    answer: "Second level cause"
    evidence: "Supporting evidence"
    confidence: "percentage confidence"
  # ... continue through why_5
  root_cause: "Final identified root cause"
  validation_test: "How to verify this is true root cause"

# For Fishbone Method  
fishbone_analysis:
  categories:
    people:
      causes: ["Specific people-related causes"]
      likelihood: ["High|Medium|Low for each cause"]
      evidence: ["Evidence supporting each cause"]
    process:
      causes: ["Process-related causes"]
      likelihood: ["ratings"]
      evidence: ["evidence"]
    # ... continue for all categories
  priority_causes:
    - cause: "Most likely root cause"
      category: "Which category"
      likelihood: "High|Medium|Low"
      evidence: "Why we think this is it"
      action_required: "What to do about it"

# For Fault Tree Method
fault_tree_analysis:
  top_event: "System failure being analyzed"
  failure_paths:
    - path_id: "PATH-001"
      description: "Sequence of events leading to failure"
      probability: "calculated or estimated probability"
      basic_events: ["List of basic failures in this path"]
      critical: true/false
  common_causes:
    - cause: "Failure that affects multiple paths"
      impact_paths: ["Which paths this affects"]
      mitigation: "How to address this common cause"

# Common fields for all methods
root_causes:
  - cause: "Identified root cause"
    method: "How identified"
    confidence: "percentage confidence in this cause"
    evidence: "Supporting evidence"
    validation_approach: "How to test this"
    remediation: "Proposed fix"

contributing_factors:
  - factor: "Contributing but not root cause"
    influence: "direct|indirect"
    importance: "high|medium|low"

validation_plan:
  - test: "Validation test description"
    expected_result: "What should happen if root cause correct"
    timeline: "When to conduct test"
    resources_needed: "What's required for test"

prevention_strategy:
  immediate_actions: ["Quick fixes to stop problem"]
  systemic_changes: ["Deeper changes to prevent recurrence"]
  monitoring: ["How to detect if problem returns"]

lessons_learned:
  - insight: "What we learned from investigation"
    application: "How to apply this elsewhere"
```

## Method Selection Guidance

### Choose 5 Whys When:
- Problem has clear single symptom
- Causation appears linear
- Quick investigation needed
- Team familiar with problem domain

### Choose Fishbone When:
- Multiple factors likely involved
- Cross-functional problem
- Need systematic category coverage
- Brainstorming session format useful

### Choose Fault Tree When:
- System safety critical
- Multiple failure modes possible
- Quantitative analysis needed
- Complex interdependencies exist

### Choose Experimentation When:
- Unknown failure mechanism
- Theories need testing
- Statistical validation required
- Resources available for testing

## Common Investigation Pitfalls

1. **Stopping at Symptoms**: Accepting surface causes as root
2. **Single Method Bias**: Using one method for all problems
3. **Confirmation Bias**: Looking for evidence supporting preconceptions
4. **Anchoring**: First hypothesis becomes fixed assumption
5. **Complexity Avoidance**: Choosing simple causes over complex reality

## Integration with Other Problem-Solving Methods

**Precede With**: Problem definition to scope investigation
**Follow With**: Solution synthesis targeting identified root causes
**Combine With**: First principles thinking to challenge "root" causes
**Support With**: Data analysis and statistical validation

## Success Metrics

- Root cause removal eliminates problem occurrence
- Multiple investigation methods converge on same cause
- Remediation addresses systemic not just symptomatic issues
- Prevention strategy stops problem recurrence
- Investigation insights transfer to other problems