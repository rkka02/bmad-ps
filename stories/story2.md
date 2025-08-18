# Story 2: Core Tasks Implementation

## Story Details
**ID**: PS-002  
**Title**: Implement Core Problem-Solving Tasks  
**Epic**: Problem-Solver Agent Integration  
**Priority**: P0 (Blocker)  
**Estimate**: 8 hours  
**Dependencies**: Story 1 (Agent Core Definition)

## User Story
As a **Problem-Solver agent**,  
I want **executable task files for problem-solving methodologies**,  
So that **I can systematically analyze problems and generate solutions using proven frameworks**.

## Technical Context

### Task Execution Pattern in BMad
- Tasks are markdown files with executable workflows
- Include CRITICAL EXECUTION NOTICE for mandatory steps
- Support interactive elicitation with 1-9 option format
- Output structured documents for agent handoffs

### Methodologies to Implement
1. First Principles Analysis (Feynman/Musk approach)
2. Root Cause Investigation (5 Whys, Fishbone, Fault Tree)
3. Problem Decomposition (MECE, Hierarchical Task Analysis)
4. Solution Synthesis (TRIZ, Lateral Thinking, Biomimicry)
5. Decision Analysis (MCDA, Decision Trees, Cost-Benefit)

## Acceptance Criteria

### AC1: First Principles Analysis Task
**File**: `.bmad-core/tasks/first-principles-analysis.md`

```markdown
# First Principles Analysis

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️
THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL
When invoked: MANDATORY STEP-BY-STEP EXECUTION with user interaction

## Method Overview
Break down complex problems to fundamental, irreducible elements following Feynman/Musk methodology.

## Execution Flow

### Phase 1: Problem Statement Clarification
1. Present current problem statement
2. Challenge every assumption
3. List what we think we know
4. Identify actual constraints vs perceived limitations

### Phase 2: Decomposition Process
1. Ask "What are we really trying to achieve?"
2. Strip away all implementation details
3. Identify fundamental physics/logic constraints
4. Find the core truth that cannot be reduced further

### Phase 3: Reconstruction
1. Build up from first principles
2. Question each addition: "Is this necessary?"
3. Look for novel combinations
4. Document reasoning chain

## Interactive Elicitation Points
When `elicit: true`:
1. Proceed to next phase
2. Challenge this assumption differently  
3. Add another fundamental constraint
4. Explore alternative decomposition
5. Consider physical laws application
6. Apply different domain principles
7. Question the problem itself
8. Validate with external data
9. Consult another agent perspective

## Output Format
```yaml
problem: Original problem statement
assumptions_challenged:
  - assumption: belief
    validity: true/false
    evidence: reasoning
fundamental_truths:
  - truth: statement
    domain: physics/logic/economics
    immutable: yes/no
reconstructed_solution:
  approach: description
  innovation: what's different
  validation: how to test
```
```

**Test Code**:
```python
# test_first_principles.py
def test_first_principles_output():
    output = """
problem: How to reduce software deployment time
assumptions_challenged:
  - assumption: Deployments must go through staging
    validity: false
    evidence: Can use feature flags for gradual rollout
fundamental_truths:
  - truth: Code must be tested before production
    domain: logic
    immutable: yes
reconstructed_solution:
  approach: Parallel testing with production deploy
  innovation: Test in production with 0.1% traffic
  validation: Measure error rates in canary
"""
    import yaml
    result = yaml.safe_load(output)
    assert 'problem' in result
    assert 'fundamental_truths' in result
    assert len(result['fundamental_truths']) > 0
    print("✅ First principles output valid")

test_first_principles_output()
```

### AC2: Root Cause Investigation Task
**File**: `.bmad-core/tasks/root-cause-investigation.md`

```markdown
# Root Cause Investigation

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️
Multi-method root cause analysis - SELECT appropriate method based on problem complexity

## Method Selection
```
Simple Linear → 5 Whys
Multi-factor → Fishbone Diagram  
Complex Systems → Fault Tree Analysis
Unknown Factors → Systematic Experimentation
```

## Method 1: 5 Whys Execution
### Interactive Flow
Present symptom → Ask Why₁ → Answer → Ask Why₂ → ... → Root Cause

### Validation Check
After each "Why":
- Is this the real cause or just another symptom?
- Can we go deeper?
- Are we assuming or do we have evidence?

## Method 2: Fishbone Diagram
### Categories Setup
- People: Skills, training, motivation
- Process: Procedures, workflow, standards
- Technology: Tools, systems, infrastructure  
- Environment: Physical, cultural, organizational
- Materials: Inputs, resources, information
- Measurement: Metrics, monitoring, feedback

### Systematic Investigation
For each category:
1. Brainstorm potential causes
2. Rate likelihood (High/Medium/Low)
3. Check for evidence
4. Test if removing cause eliminates problem

## Method 3: Fault Tree Analysis
### Tree Construction
1. Define TOP undesired event
2. Identify immediate causes (OR/AND gates)
3. Decompose each cause recursively
4. Calculate probability paths
5. Identify critical failure points

## Output Structure
```yaml
investigation_method: [5-whys|fishbone|fault-tree]
problem_statement: description
symptoms:
  - symptom: observation
    frequency: often/sometimes/rare
    impact: high/medium/low
root_causes:
  - cause: description
    evidence: data/observation
    confidence: percentage
    remediation: proposed fix
contributing_factors:
  - factor: description
    influence: direct/indirect
validation_plan:
  - test: description
    expected_result: outcome
```
```

**Test Code**:
```bash
# test_root_cause.sh
#!/bin/bash

# Test 5 Whys logic
cat << EOF > test_5whys.yaml
problem: System crashes every Monday morning
why1:
  question: Why does system crash Monday morning?
  answer: Memory usage spikes at 9am
why2:
  question: Why does memory spike at 9am?
  answer: All users log in simultaneously
why3:
  question: Why do all users log in simultaneously?
  answer: Company policy requires 9am standup
why4:
  question: Why does simultaneous login cause crash?
  answer: Session cache not distributed
why5:
  question: Why is session cache not distributed?
  answer: Original design for 50 users, now 500
root_cause: System architecture not scaled for 10x growth
EOF

# Validate structure
python3 -c "
import yaml
with open('test_5whys.yaml') as f:
    data = yaml.safe_load(f)
    assert 'root_cause' in data
    assert 'why5' in data
    print('✅ 5 Whys structure valid')
"
```

### AC3: Problem Decomposition Task
**File**: `.bmad-core/tasks/problem-decomposition.md`

```markdown
# Problem Decomposition using MECE Principle

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️
Mutually Exclusive, Collectively Exhaustive decomposition required

## Decomposition Strategy Selection
Based on problem type:
- Functional → Function-Class Decomposition
- Process → Workflow Decomposition
- System → Component Decomposition
- Decision → Option Tree Analysis

## MECE Validation Rules
1. **Mutually Exclusive**: No overlap between categories
2. **Collectively Exhaustive**: Covers 100% of problem space
3. **Same Level**: All items at same abstraction level

## Execution Process

### Step 1: Problem Boundary Definition
- What's included?
- What's explicitly excluded?
- What are the interfaces?

### Step 2: Decomposition Axes Selection
Choose 1-2 primary axes:
- By Function (what it does)
- By Component (what it's made of)
- By Phase (when it happens)
- By Actor (who's involved)
- By Location (where it occurs)

### Step 3: Hierarchical Breakdown
```
Level 0: Complete Problem
Level 1: 3-7 Major Components (MECE)
Level 2: 3-5 Sub-components each
Level 3: Atomic tasks/elements
```

### Step 4: Validation Checklist
For each decomposition level:
- [ ] No overlaps between items?
- [ ] Nothing missing?
- [ ] Items comparable in scope?
- [ ] Clear parent-child relationships?

## Interactive Elicitation
At each level, options:
1. Proceed with decomposition
2. Refine current level
3. Change decomposition axis
4. Merge similar items
5. Split complex items
6. Add missing element
7. Remove out-of-scope item
8. Validate with examples
9. Get expert input

## Output Format
```yaml
problem_scope:
  included: [list]
  excluded: [list]
  interfaces: [list]
decomposition_axis: function|component|phase|actor|location
hierarchy:
  level_0: problem_statement
  level_1:
    - component: name
      description: what
      sub_components: [list]
mece_validation:
  mutually_exclusive: true/false
  collectively_exhaustive: true/false
  issues_found: [list]
```
```

**Test Code**:
```python
# test_decomposition.py
def validate_mece_decomposition():
    test_data = {
        'problem_scope': {
            'included': ['user authentication', 'authorization'],
            'excluded': ['payment processing'],
            'interfaces': ['user database', 'session store']
        },
        'decomposition_axis': 'function',
        'hierarchy': {
            'level_0': 'Access Control System',
            'level_1': [
                {
                    'component': 'Authentication',
                    'description': 'Verify user identity',
                    'sub_components': ['login', 'MFA', 'SSO']
                },
                {
                    'component': 'Authorization', 
                    'description': 'Verify user permissions',
                    'sub_components': ['role check', 'resource access', 'audit']
                },
                {
                    'component': 'Session Management',
                    'description': 'Maintain user state',
                    'sub_components': ['create', 'validate', 'expire']
                }
            ]
        },
        'mece_validation': {
            'mutually_exclusive': True,
            'collectively_exhaustive': True,
            'issues_found': []
        }
    }
    
    # Check MECE properties
    components = [c['component'] for c in test_data['hierarchy']['level_1']]
    
    # Check mutual exclusion (no duplicates)
    assert len(components) == len(set(components)), "Components not mutually exclusive"
    
    # Check exhaustive (all aspects covered)
    required_aspects = {'Authentication', 'Authorization', 'Session Management'}
    assert required_aspects.issubset(set(components)), "Not collectively exhaustive"
    
    print("✅ MECE decomposition valid")
    return True

validate_mece_decomposition()
```

### AC4: Solution Synthesis Task
**File**: `.bmad-core/tasks/solution-synthesis.md`

```markdown
# Solution Synthesis - Multi-Method Innovation

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️
Apply multiple innovation frameworks iteratively

## Method Portfolio
1. **TRIZ** - Systematic innovation through contradiction resolution
2. **Lateral Thinking** - Break patterns with provocative operations
3. **Biomimicry** - Nature-inspired solutions
4. **Design Thinking** - Human-centered innovation
5. **Combinatory Play** - Cross-domain synthesis

## TRIZ Execution Flow

### Step 1: Identify Contradiction
- Technical: Same parameter needs opposite states
- Physical: Object needs contradictory properties

### Step 2: Abstract to TRIZ Parameters
Map specific problem to 39 engineering parameters

### Step 3: Apply Inventive Principles
Use contradiction matrix → Get 3-4 relevant principles from 40

### Step 4: Adapt to Specific Context
Translate generic principle to domain-specific solution

## Lateral Thinking Techniques

### Random Input Method
1. Generate random word/concept
2. Force connection to problem
3. Extract unexpected insight

### Provocative Operation (PO)
1. Make impossible statement: "PO: Cars have square wheels"
2. Extract useful concept: "Controlled friction points"
3. Develop practical application

### Concept Extraction
1. Identify successful solution in different domain
2. Extract core principle
3. Apply to current problem

## Biomimicry Process

### Challenge → Biology
1. Define function needed
2. Ask: "How does nature do this?"
3. Find organisms/systems with this function
4. Abstract design principles
5. Apply with available technology

## Solution Scoring Matrix
```yaml
evaluation_criteria:
  - feasibility: 1-10
  - innovation: 1-10  
  - cost: 1-10
  - time_to_implement: 1-10
  - risk: 1-10
  - scalability: 1-10
```

## Output Format
```yaml
synthesis_methods_used: [list]
solutions:
  - id: SOL-001
    method: TRIZ
    description: solution
    principle_applied: which principle/concept
    feasibility_score: 1-10
    innovation_score: 1-10
    implementation_notes: how to build
    risks: [list]
    validation_approach: how to test
recommended_solution:
  id: SOL-XXX
  rationale: why this one
  next_steps: [list]
```
```

**Test Code**:
```python
# test_solution_synthesis.py
import json

def test_triz_contradiction_matrix():
    # Simplified TRIZ matrix for testing
    triz_matrix = {
        ("weight", "strength"): [1, 35, 40],  # Segmentation, Parameter changes, Composite
        ("speed", "accuracy"): [2, 10, 35],   # Taking out, Preliminary action, Parameter changes
    }
    
    problem = ("weight", "strength")
    principles = triz_matrix.get(problem, [])
    
    assert len(principles) > 0, "No TRIZ principles found"
    assert 35 in principles, "Parameter changes should be suggested"
    print(f"✅ TRIZ matrix returns principles: {principles}")

def test_solution_scoring():
    solution = {
        'id': 'SOL-001',
        'method': 'TRIZ',
        'description': 'Segmented structure for weight reduction',
        'scores': {
            'feasibility': 8,
            'innovation': 7,
            'cost': 6,
            'time_to_implement': 7,
            'risk': 4,
            'scalability': 9
        }
    }
    
    # Calculate weighted score
    weights = {'feasibility': 0.3, 'innovation': 0.2, 'cost': 0.2, 
               'time_to_implement': 0.1, 'risk': 0.1, 'scalability': 0.1}
    
    total_score = sum(solution['scores'][k] * weights[k] for k in weights)
    
    assert 0 <= total_score <= 10, "Score out of range"
    print(f"✅ Solution scored: {total_score:.2f}/10")

test_triz_contradiction_matrix()
test_solution_scoring()
```

### AC5: Decision Analysis Task
**File**: `.bmad-core/tasks/decision-analysis.md`

```markdown
# Decision Analysis Framework

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️
Systematic decision support using multiple quantitative methods

## Method Selection Guide
```
2-3 options, 3-5 criteria → Simple Matrix
Many options, complex criteria → AHP
Uncertainty/Risk → Decision Tree
Multiple stakeholders → MCDA
Cost-focused → Cost-Benefit Analysis
```

## Multi-Criteria Decision Analysis (MCDA)

### Step 1: Define Criteria
- Must be measurable
- Independent (non-overlapping)
- Complete (cover all important aspects)
- Operational (data available)

### Step 2: Weight Criteria
Techniques:
1. Direct Rating (0-100)
2. Pairwise Comparison (AHP)
3. Swing Weights
4. Trade-off Analysis

### Step 3: Score Alternatives
For each criterion:
- Define measurement scale
- Normalize scores (0-1 or 0-100)
- Apply scoring function

### Step 4: Calculate Results
```
Total Score = Σ(Weight_i × Score_i)
```

### Step 5: Sensitivity Analysis
- Vary weights ±20%
- Check if ranking changes
- Identify critical criteria

## Decision Tree Construction

### Node Types
- **Decision Node** (□): Choice point
- **Chance Node** (○): Uncertain outcome
- **Terminal Node** (△): Final value

### Calculation Process
1. Assign probabilities to chance nodes
2. Assign values to terminal nodes
3. Calculate expected values backward
4. Choose path with highest expected value

## Output Format
```yaml
decision_context:
  problem: statement
  constraints: [list]
  stakeholders: [list]
criteria:
  - name: criterion
    weight: 0.0-1.0
    measurement: how measured
    direction: maximize|minimize
alternatives:
  - id: ALT-001
    name: option name
    scores:
      criterion1: score
      criterion2: score
    weighted_total: calculated
    rank: position
sensitivity_analysis:
  critical_criteria: [list]
  robust: true|false
  breaking_points: [weight changes that alter decision]
recommendation:
  selected: ALT-XXX
  confidence: high|medium|low
  rationale: explanation
  risks: [list]
```
```

**Test Code**:
```python
# test_decision_analysis.py
import numpy as np

def test_mcda_calculation():
    # Define criteria and weights
    criteria = {
        'cost': {'weight': 0.3, 'direction': 'minimize'},
        'performance': {'weight': 0.4, 'direction': 'maximize'},
        'reliability': {'weight': 0.3, 'direction': 'maximize'}
    }
    
    # Alternative scores (raw)
    alternatives = {
        'Option A': {'cost': 100000, 'performance': 85, 'reliability': 0.95},
        'Option B': {'cost': 80000, 'performance': 90, 'reliability': 0.92},
        'Option C': {'cost': 120000, 'performance': 95, 'reliability': 0.98}
    }
    
    # Normalize scores
    def normalize(values, direction='maximize'):
        if direction == 'maximize':
            return [(v - min(values)) / (max(values) - min(values)) for v in values]
        else:  # minimize
            return [(max(values) - v) / (max(values) - min(values)) for v in values]
    
    # Calculate weighted scores
    results = {}
    for alt_name, alt_scores in alternatives.items():
        weighted_sum = 0
        for crit_name, crit_info in criteria.items():
            # Get all values for this criterion for normalization
            all_values = [alt[crit_name] for alt in alternatives.values()]
            normalized = normalize(all_values, crit_info['direction'])
            
            # Find this alternative's normalized score
            alt_index = list(alternatives.keys()).index(alt_name)
            norm_score = normalized[alt_index]
            
            weighted_sum += norm_score * crit_info['weight']
        
        results[alt_name] = round(weighted_sum, 3)
    
    # Rank alternatives
    ranked = sorted(results.items(), key=lambda x: x[1], reverse=True)
    
    print("✅ MCDA Calculation Results:")
    for rank, (name, score) in enumerate(ranked, 1):
        print(f"  {rank}. {name}: {score}")
    
    assert len(ranked) == 3
    assert all(0 <= score <= 1 for _, score in ranked)
    return ranked

def test_decision_tree():
    # Simple decision tree example
    class DecisionNode:
        def __init__(self, name, children=None):
            self.name = name
            self.children = children or []
            self.expected_value = 0
    
    class ChanceNode:
        def __init__(self, name, outcomes):
            self.name = name
            self.outcomes = outcomes  # [(probability, value, child)]
            self.expected_value = 0
        
        def calculate_ev(self):
            self.expected_value = sum(p * v for p, v, _ in self.outcomes)
            return self.expected_value
    
    # Build tree
    chance = ChanceNode("Market Response", [
        (0.6, 1000000, None),  # Good response
        (0.3, 500000, None),   # Moderate response  
        (0.1, -200000, None)   # Poor response
    ])
    
    ev = chance.calculate_ev()
    print(f"✅ Decision Tree EV: ${ev:,.0f}")
    assert ev == 680000

test_mcda_calculation()
test_decision_tree()
```

## Implementation Tasks

### Task 1: Create Task Files
```bash
#!/bin/bash
# create_task_files.sh

TASK_DIR=".bmad-core/tasks"
mkdir -p $TASK_DIR

# Create all task files
touch $TASK_DIR/first-principles-analysis.md
touch $TASK_DIR/root-cause-investigation.md
touch $TASK_DIR/problem-decomposition.md
touch $TASK_DIR/solution-synthesis.md
touch $TASK_DIR/decision-analysis.md

echo "✅ Task files created"
ls -la $TASK_DIR/*.md
```

### Task 2: Validate Task Execution Flow
```python
# validate_tasks.py
import os
import re

def validate_task_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check for required sections
    required_patterns = [
        r'## ⚠️ CRITICAL EXECUTION NOTICE',
        r'## Method|## Execution Flow',
        r'## Output Format|## Output Structure',
        r'elicit:|## Interactive'
    ]
    
    missing = []
    for pattern in required_patterns:
        if not re.search(pattern, content):
            missing.append(pattern)
    
    if missing:
        print(f"❌ {filepath}: Missing {missing}")
        return False
    
    print(f"✅ {filepath}: Valid structure")
    return True

# Test all task files
task_files = [
    'first-principles-analysis.md',
    'root-cause-investigation.md',
    'problem-decomposition.md',
    'solution-synthesis.md',
    'decision-analysis.md'
]

for task_file in task_files:
    path = f'.bmad-core/tasks/{task_file}'
    if os.path.exists(path):
        validate_task_file(path)
```

## Testing Checklist

### Unit Tests
- [ ] Each task produces valid YAML output
- [ ] Interactive elicitation points defined
- [ ] Method selection logic works
- [ ] Output formats consistent

### Integration Tests
- [ ] Tasks callable from problem-solver agent
- [ ] Output consumable by other agents
- [ ] Elicitation flow works correctly
- [ ] Documents saved to correct locations

### Validation Tests
- [ ] First principles reaches fundamentals
- [ ] Root cause identifies true causes
- [ ] MECE decomposition validated
- [ ] Solutions scored consistently
- [ ] Decisions traceable

## Definition of Done
- [ ] All 5 core task files created
- [ ] Task execution flows documented
- [ ] Output formats specified
- [ ] Test scripts passing
- [ ] Interactive elicitation implemented
- [ ] Integration with agent verified

## Notes for Developer
- Tasks must be self-contained executable workflows
- Follow exact BMad task patterns from existing tasks
- Ensure YAML output is valid and parseable
- Test each methodology independently
- Consider edge cases (no solution found, multiple root causes)

## File List
```
Created:
- .bmad-core/tasks/first-principles-analysis.md
- .bmad-core/tasks/root-cause-investigation.md  
- .bmad-core/tasks/problem-decomposition.md
- .bmad-core/tasks/solution-synthesis.md
- .bmad-core/tasks/decision-analysis.md

Test Files:
- test_first_principles.py
- test_root_cause.sh
- test_decomposition.py
- test_solution_synthesis.py
- test_decision_analysis.py
```

## Next Story Dependencies
This story enables:
- Story 3: Templates can reference these tasks
- Story 6: Testing can validate task execution
- Story 7: Documentation can show task examples