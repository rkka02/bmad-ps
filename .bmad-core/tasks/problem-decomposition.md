# Problem Decomposition using MECE Principle

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

Mutually Exclusive, Collectively Exhaustive (MECE) decomposition is REQUIRED for systematic problem analysis.

**VIOLATION INDICATOR**: If categories overlap or gaps exist in coverage, MECE principle has been violated.

## MECE Principle Foundation

**Mutually Exclusive**: No overlap between categories - each element belongs to exactly one category
**Collectively Exhaustive**: Complete coverage - all aspects of problem included with no gaps

**McKinsey Origin**: MECE framework developed at McKinsey & Company for structured problem-solving and ensures no critical aspects are overlooked while avoiding redundant analysis.

## Decomposition Strategy Selection

Choose decomposition axis based on problem characteristics:

```
Problem Nature → Decomposition Approach
├── What it does → Functional Decomposition
├── What it's made of → Component/Structural Decomposition  
├── When it happens → Temporal/Process Decomposition
├── Who's involved → Stakeholder/Actor Decomposition
├── Where it occurs → Spatial/Geographic Decomposition
└── Why/How → Causal/Mechanism Decomposition
```

## Execution Process

### Step 1: Problem Boundary Definition
**Critical First Step**: Establish clear problem scope

1. **Inclusion Criteria**
   - What specific aspects ARE part of this problem?
   - Which systems, processes, people are affected?
   - What timeframe does this cover?
   - What outcomes are we trying to influence?

2. **Exclusion Criteria**  
   - What is explicitly OUT OF SCOPE?
   - Which related issues are separate problems?
   - What constraints limit our problem space?
   - What are we NOT trying to solve?

3. **Interface Definition**
   - How does this problem connect to others?
   - What are the handoff points?
   - Where do dependencies exist?
   - What external factors influence this problem?

### Step 2: Decomposition Axes Selection

**Primary Axis Selection** (Choose ONE main organizing principle):

#### Functional Decomposition
- **By Purpose**: What functions must be performed?
- **By Capability**: What abilities are needed?
- **By Process**: What steps must occur?
- **Best For**: Systems, workflows, service delivery

#### Structural Decomposition  
- **By Component**: What parts make up the whole?
- **By Subsystem**: What major modules exist?
- **By Architecture**: How is it organized?
- **Best For**: Technical systems, organizations, products

#### Temporal Decomposition
- **By Phase**: What happens in sequence?
- **By Lifecycle**: What stages exist over time?
- **By Frequency**: What happens when?
- **Best For**: Process problems, implementation challenges

#### Stakeholder Decomposition
- **By Role**: Who has what responsibilities?
- **By Impact**: Who gets affected how?
- **By Influence**: Who can change what?
- **Best For**: Organizational issues, change management

**Secondary Axis** (Optional for matrix decomposition):
- Can combine two axes for complex problems
- Example: Function × Stakeholder matrix
- Increases complexity but captures interactions

### Step 3: Hierarchical Breakdown Structure

**Level 0**: Complete Problem Statement
- Single, clear problem definition
- Measurable and observable
- Bounded by inclusion/exclusion criteria

**Level 1**: Major Components (3-7 items)
- Apply MECE principle strictly
- Each component significantly different
- Together they completely cover problem space
- No overlaps between components

**Level 2**: Sub-components (3-5 per Level 1)
- Further breakdown of each major component
- Maintain MECE within each branch
- More specific and actionable items
- Begin to identify root causes or solution areas

**Level 3**: Atomic Elements (as needed)
- Lowest level of useful decomposition
- Cannot be broken down further meaningfully
- Directly actionable or measurable
- Form basis for solution development

### Step 4: MECE Validation Process

For each decomposition level, systematically check:

#### Mutual Exclusivity Check
- [ ] Does any item belong to multiple categories?
- [ ] Are there overlapping responsibilities?
- [ ] Can any element be classified multiple ways?
- [ ] Are categories clearly distinct?

#### Collective Exhaustiveness Check
- [ ] Is anything missing from our breakdown?
- [ ] Do all aspects of parent category appear in children?
- [ ] Are there gaps in our coverage?
- [ ] Can we think of examples that don't fit?

#### Same Abstraction Level Check
- [ ] Are all items at similar level of detail?
- [ ] Are we mixing high-level and specific items?
- [ ] Do categories use consistent criteria?
- [ ] Are relationships clear and logical?

## Interactive Elicitation Process

When `elicit: true`, present these options:

1. **Proceed with current decomposition** - Continue to next level
2. **Refine current level** - Adjust categories for better MECE
3. **Change decomposition axis** - Try different organizing principle
4. **Merge similar items** - Combine overlapping categories
5. **Split complex items** - Break down large categories
6. **Add missing element** - Include overlooked aspect
7. **Remove out-of-scope item** - Eliminate items beyond boundaries
8. **Validate with examples** - Test categories with real cases
9. **Get domain expert input** - Consult specialist for validation

## Decomposition Method Examples

### Software System Problem
```
Level 0: E-commerce Platform Performance Issues
Level 1 (Functional):
  ├── User Interface Responsiveness
  ├── Data Processing Efficiency  
  ├── Storage System Performance
  └── Network Communication Speed

Level 2 (Under UI Responsiveness):
  ├── Page Load Times
  ├── User Interaction Response
  └── Content Rendering Speed
```

### Organizational Change Problem
```
Level 0: Digital Transformation Resistance
Level 1 (Stakeholder):
  ├── Executive Leadership
  ├── Middle Management
  ├── Frontline Employees
  └── External Partners

Level 2 (Under Middle Management):
  ├── Skills Gap Concerns
  ├── Authority/Control Issues
  └── Resource Allocation Fears
```

### Process Improvement Problem
```
Level 0: Customer Complaint Resolution Delays
Level 1 (Temporal):
  ├── Issue Identification & Logging
  ├── Investigation & Root Cause Analysis
  ├── Solution Development & Approval
  └── Implementation & Follow-up

Level 2 (Under Investigation):
  ├── Data Collection Process
  ├── Expert Assignment & Availability
  └── Analysis Tools & Methods
```

## Output Format

```yaml
problem_scope:
  included:
    - aspect: "What's included in this problem"
      rationale: "Why this is included"
  excluded:
    - aspect: "What's excluded from this problem"
      rationale: "Why this is out of scope"
  interfaces:
    - connection: "How this problem connects to others"
      dependency: "What relies on what"

decomposition_approach:
  primary_axis: "functional|structural|temporal|stakeholder|spatial|causal"
  secondary_axis: "optional second organizing principle"
  rationale: "Why this decomposition approach was chosen"

problem_hierarchy:
  level_0:
    problem: "Complete problem statement"
    scope: "Boundary description"
  
  level_1:
    - component: "Major component name"
      description: "What this component covers"
      percentage_of_problem: "rough estimate of contribution"
      sub_components: "list of level 2 items"
    # Continue for all level 1 components
  
  level_2:
    parent: "Which level 1 component"
    components:
      - sub_component: "More specific breakdown"
        description: "What this covers"
        actionable: true/false
        measurable: true/false
  
  level_3: # if needed
    parent: "Which level 2 component"  
    atomic_elements:
      - element: "Cannot be broken down further"
        type: "root_cause|solution_area|metric|constraint"

mece_validation:
  mutual_exclusivity:
    status: "passed|issues_found"
    issues: ["List any overlaps found"]
    resolution: "How overlaps were resolved"
  
  collective_exhaustiveness:
    status: "passed|gaps_found"
    gaps: ["List any missing aspects"]
    additions: "What was added to fill gaps"
  
  abstraction_consistency:
    status: "passed|mixed_levels"
    issues: ["Items at wrong abstraction level"]
    corrections: "How levels were standardized"

analysis_insights:
  leverage_points:
    - point: "Where small changes have big impact"
      component: "Which decomposition component"
      potential_impact: "Expected improvement from addressing this"
  
  critical_dependencies:
    - dependency: "What depends on what"
      impact: "Effect if this fails"
      mitigation: "How to reduce this dependency"
  
  simplification_opportunities:
    - opportunity: "Where complexity can be reduced"
      approach: "How to simplify"
      benefits: "What this would improve"

next_steps:
  priority_components:
    - component: "Which component to address first"
      rationale: "Why this is highest priority"
      approach: "How to tackle this component"
  
  analysis_needed:
    - component: "Which component needs deeper analysis"
      method: "What analysis method to apply"
      resources: "What's needed for this analysis"
  
  solution_development:
    - component: "Ready for solution development"
      approach: "How to develop solutions"
      stakeholders: "Who should be involved"
```

## Advanced MECE Applications

### Matrix Decomposition
For complex problems, use two-dimensional MECE:
```
Functions × Stakeholders Matrix:
           │ Users │ Admins │ Developers │
Registration │   A   │   B    │     C      │
Data Entry   │   D   │   E    │     F      │
Reporting    │   G   │   H    │     I      │
```

### Weighted MECE  
Assign importance/effort weights:
```
Component A: 40% of problem, 20% of effort → High leverage
Component B: 30% of problem, 60% of effort → Lower priority
Component C: 30% of problem, 20% of effort → Good target
```

### Dynamic MECE
Decomposition changes based on context:
```
Development Phase → Technical decomposition
Deployment Phase → Operational decomposition  
Maintenance Phase → Process decomposition
```

## Common Decomposition Pitfalls

1. **False Dichotomies**: Creating only two categories when more exist
2. **Category Creep**: Allowing overlaps to develop over time
3. **Premature Depth**: Going too detailed before validating higher levels
4. **Mixed Criteria**: Using different organizing principles at same level
5. **Solution Bias**: Organizing around preferred solutions rather than problem structure

## Integration with Other Methods

**Precede With**: Problem definition and scoping
**Follow With**: Root cause analysis on critical components
**Combine With**: Systems thinking to identify interconnections
**Support With**: Data analysis to validate component importance

## Quality Indicators

- Each component can be independently addressed
- Solution approaches naturally emerge from structure
- Different team members can own different components
- Progress can be measured at each level
- Structure makes sense to domain experts
- No significant aspects feel missing or misplaced