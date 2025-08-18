# Story 5: Workflow Enhancement

## Story Details
**ID**: PS-005  
**Title**: Enhance Workflows with Problem-Solver Integration  
**Epic**: Problem-Solver Agent Integration  
**Priority**: P1 (High)  
**Estimate**: 6 hours  
**Dependencies**: Stories 1-4 (Agent and Integration Complete)

## User Story
As a **BMad user**,  
I want **problem-solver integrated into development workflows**,  
So that **complex problems are systematically analyzed before implementation**.

## Technical Context

### Workflow Integration Strategy
- Add problem-solver at key decision points
- Create new complex-problem-solving workflow
- Enhance existing workflows with optional problem analysis
- Define handoff protocols between agents

## Acceptance Criteria

### AC1: Create Complex Problem-Solving Workflow
**File**: `.bmad-core/workflows/complex-problem-solving.yaml`

```yaml
workflow:
  id: complex-problem-solving
  name: Complex Problem Resolution
  description: >-
    Systematic approach to analyzing and solving complex, cross-disciplinary problems
    using multiple analytical frameworks and innovation methodologies.
  type: analysis
  project_types:
    - research
    - innovation
    - troubleshooting
    - optimization
    - architecture-decisions

  sequence:
    - agent: problem-solver
      creates: problem-definition.md
      task: create-problem-def
      notes: |
        Define and decompose the problem using MECE principle.
        Identify stakeholders, constraints, and success criteria.
        SAVE OUTPUT: Copy problem-definition.md to docs/ folder.

    - agent: problem-solver
      creates: root-cause-analysis.md
      task: investigate-root-cause
      requires: problem-definition.md
      notes: |
        Apply 5 Whys, Fishbone, or Fault Tree Analysis.
        Identify true root causes with evidence.
        SAVE OUTPUT: Copy root-cause-analysis.md to docs/ folder.

    - agent: analyst
      creates: research-findings.md
      requires: root-cause-analysis.md
      optional: true
      condition: requires_domain_research
      notes: |
        OPTIONAL: Deep research into specific domain areas.
        Market analysis, competitor research, or technical investigation.

    - agent: problem-solver
      creates: solution-options.md
      task: generate-solutions
      requires:
        - problem-definition.md
        - root-cause-analysis.md
        - research-findings.md (if exists)
      notes: |
        Apply TRIZ, Design Thinking, Lateral Thinking, Biomimicry.
        Generate 3-7 solution options with different approaches.
        SAVE OUTPUT: Copy solution-options.md to docs/ folder.

    - agent: architect
      validates: technical-feasibility
      requires: solution-options.md
      condition: has_technical_solutions
      notes: |
        CONDITIONAL: Review technical solutions for feasibility.
        Provide implementation complexity estimates.
        May modify or add technical alternatives.

    - agent: pm
      validates: business-viability
      requires: solution-options.md
      condition: has_business_impact
      notes: |
        CONDITIONAL: Assess business value and ROI.
        Validate alignment with product strategy.
        May add business constraints or requirements.

    - agent: problem-solver
      creates: solution-matrix.md
      task: create-solution-matrix
      requires: all_validations
      notes: |
        Score all solutions against weighted criteria.
        Perform sensitivity analysis on decision factors.
        SAVE OUTPUT: Copy solution-matrix.md to docs/ folder.

    - agent: problem-solver
      creates: decision-record.md
      task: create-decision-record
      requires: solution-matrix.md
      notes: |
        Document final decision with full rationale.
        Create ADR (Architectural Decision Record).
        Include implementation roadmap.
        SAVE OUTPUT: Copy to docs/decisions/ folder.

    - agent: po
      validates: decision-alignment
      requires: all_documents
      notes: |
        Validate decision against original problem definition.
        Ensure all constraints are satisfied.
        Confirm stakeholder concerns addressed.

    - handoff_options:
      to_development:
        condition: requires_implementation
        next: Create implementation stories with SM agent
      to_monitoring:
        condition: requires_validation_only
        next: Set up monitoring and success metrics
      to_documentation:
        condition: knowledge_capture_only
        next: Archive in knowledge base

  flow_diagram: |
    ```mermaid
    graph TD
        A[Start: Complex Problem] --> B[problem-solver: Define Problem]
        B --> C[problem-solver: Root Cause Analysis]
        C --> D{Needs Research?}
        D -->|Yes| E[analyst: Domain Research]
        D -->|No| F[problem-solver: Generate Solutions]
        E --> F
        F --> G{Technical Solutions?}
        G -->|Yes| H[architect: Feasibility Review]
        G -->|No| I{Business Impact?}
        H --> I
        I -->|Yes| J[pm: Business Validation]
        I -->|No| K[problem-solver: Solution Matrix]
        J --> K
        K --> L[problem-solver: Decision Record]
        L --> M[po: Validate Alignment]
        M --> N{Next Steps?}
        N -->|Implement| O[To Development Workflow]
        N -->|Monitor| P[Set Up Metrics]
        N -->|Document| Q[Archive Knowledge]
        
        style B fill:#FFD700
        style C fill:#FFD700
        style F fill:#FFD700
        style K fill:#FFD700
        style L fill:#FFD700
    ```

  decision_guidance:
    when_to_use:
      - Problem spans multiple domains or systems
      - Root cause is unknown or disputed
      - Multiple solution approaches possible
      - High-stakes decisions with significant impact
      - Innovation or optimization needed
      - Troubleshooting complex failures
```

### AC2: Enhance Greenfield Full-Stack Workflow
**Modification**: `.bmad-core/workflows/greenfield-fullstack.yaml`

Add problem-solver insertion points:

```yaml
# INSERT after project-brief, before PRD
- agent: problem-solver
  creates: problem-analysis.md
  requires: project-brief.md
  optional: true
  condition: has_complex_challenges
  notes: |
    OPTIONAL: For complex or novel problems, perform deep analysis.
    Decompose problem, identify innovation opportunities.
    Output informs PRD creation with clearer requirements.

# INSERT before architecture
- agent: problem-solver
  creates: technical-decisions.md
  requires: prd.md
  optional: true
  condition: has_architectural_uncertainties
  notes: |
    OPTIONAL: For major technical decisions, use decision analysis.
    Evaluate architectural options systematically.
    Create ADRs for significant choices.
```

### AC3: Enhance Brownfield Workflows
**Modification**: `.bmad-core/workflows/brownfield-fullstack.yaml`

```yaml
# INSERT at beginning for legacy system analysis
- agent: problem-solver
  creates: legacy-analysis.md
  optional: true
  condition: dealing_with_legacy_complexity
  notes: |
    OPTIONAL: Analyze legacy system problems systematically.
    Identify refactoring opportunities and migration strategies.
    Use root cause analysis for persistent issues.

# INSERT before major refactoring
- agent: problem-solver
  creates: refactoring-strategy.md
  requires: code-analysis.md
  condition: major_refactoring_needed
  notes: |
    Systematically evaluate refactoring approaches.
    Use TRIZ for resolving technical contradictions.
    Create decision matrix for approach selection.
```

### AC4: Agent Handoff Protocols
**File**: `.bmad-core/utils/problem-solver-handoffs.md`

```markdown
# Problem-Solver Agent Handoff Protocols

## Incoming Handoffs (Other → Problem-Solver)

### From Analyst
**Trigger**: "This requires systematic problem decomposition"
**Provides**: market-research.md, competitive-analysis.md
**Expected Output**: problem-definition.md with market context

### From PM
**Trigger**: "Multiple product directions possible, need decision framework"
**Provides**: product-requirements.md, stakeholder-concerns.md
**Expected Output**: solution-matrix.md, decision-record.md

### From Architect
**Trigger**: "Technical contradiction needs resolution"
**Provides**: technical-constraints.md, architecture-options.md
**Expected Output**: TRIZ-based solution, decision-record.md

### From Developer
**Trigger**: "Complex bug requiring root cause analysis"
**Provides**: error-logs.md, system-behavior.md
**Expected Output**: root-cause-analysis.md, fix-recommendations.md

## Outgoing Handoffs (Problem-Solver → Other)

### To PM
**Output**: solution-matrix.md
**Message**: "Three viable solutions identified. Solution 2 scores highest on business value. See weighted analysis for trade-offs."

### To Architect
**Output**: technical-decisions.md
**Message**: "Recommended microservices approach based on MCDA. Key factors: scalability (0.4 weight) and maintainability (0.3 weight)."

### To Developer
**Output**: root-cause-analysis.md
**Message**: "Root cause identified: race condition in cache invalidation. See section 3.2 for specific code locations."

### To SM
**Output**: implementation-roadmap.md
**Message**: "Solution requires 5 implementation stories. Dependencies mapped in section 4. Recommend starting with data migration."
```

### AC5: Workflow Selection Matrix
Create decision matrix for when to use problem-solver:

```yaml
problem_complexity_matrix:
  simple:
    characteristics:
      - Single domain
      - Known solution patterns
      - Clear requirements
    recommended_workflow: standard-development
    problem_solver_role: none

  moderate:
    characteristics:
      - 2-3 domains involved
      - Some uncertainty
      - Multiple stakeholders
    recommended_workflow: standard-with-analysis
    problem_solver_role: optional-consultation

  complex:
    characteristics:
      - Cross-disciplinary
      - Unknown root causes
      - Conflicting requirements
      - Innovation needed
    recommended_workflow: complex-problem-solving
    problem_solver_role: primary-driver

  wicked:
    characteristics:
      - No clear problem definition
      - Solutions create new problems
      - Stakeholders disagree on problem
    recommended_workflow: iterative-problem-solving
    problem_solver_role: continuous-involvement
```

## Implementation Tasks

### Task 1: Create New Workflow File
```bash
#!/bin/bash
# create_workflow.sh

WORKFLOW_DIR=".bmad-core/workflows"
NEW_WORKFLOW="complex-problem-solving.yaml"

# Create workflow file
cat > "$WORKFLOW_DIR/$NEW_WORKFLOW" << 'EOF'
workflow:
  id: complex-problem-solving
  name: Complex Problem Resolution
  # ... rest of workflow
EOF

echo "✅ Created $NEW_WORKFLOW"

# Validate YAML
python3 -c "import yaml; yaml.safe_load(open('$WORKFLOW_DIR/$NEW_WORKFLOW'))" && \
  echo "✅ YAML valid" || echo "❌ YAML invalid"
```

### Task 2: Test Workflow Execution
```python
# test_workflow_execution.py
import yaml

def simulate_workflow_execution(workflow_file):
    """Simulate workflow execution to verify sequence"""
    with open(workflow_file, 'r') as f:
        workflow = yaml.safe_load(f)
    
    sequence = workflow['workflow']['sequence']
    created_artifacts = []
    
    print(f"Executing workflow: {workflow['workflow']['name']}")
    print("=" * 50)
    
    for step in sequence:
        if isinstance(step, dict) and 'agent' in step:
            agent = step['agent']
            creates = step.get('creates', 'N/A')
            requires = step.get('requires', [])
            
            # Check dependencies
            if isinstance(requires, str):
                requires = [requires]
            
            missing = [r for r in requires if r not in created_artifacts and r != 'all_validations']
            
            if missing and not step.get('optional', False):
                print(f"❌ {agent}: Missing required artifacts: {missing}")
                return False
            
            print(f"✅ {agent}: Creates {creates}")
            if creates != 'N/A':
                created_artifacts.append(creates)
    
    print("=" * 50)
    print(f"Workflow complete. Created: {created_artifacts}")
    return True

# Test the workflow
workflow_path = '.bmad-core/workflows/complex-problem-solving.yaml'
simulate_workflow_execution(workflow_path)
```

### Task 3: Update Existing Workflows
```python
# update_workflows.py
import yaml
import copy

def insert_problem_solver_steps(workflow_file, insertions):
    """Insert problem-solver steps into existing workflow"""
    
    with open(workflow_file, 'r') as f:
        workflow = yaml.safe_load(f)
    
    original = copy.deepcopy(workflow)
    sequence = workflow['workflow']['sequence']
    
    # Add insertions at specified points
    for insertion in insertions:
        position = insertion['position']
        step = insertion['step']
        
        # Find insertion point
        for i, existing_step in enumerate(sequence):
            if existing_step.get('agent') == position['after']:
                sequence.insert(i + 1, step)
                print(f"✅ Inserted problem-solver after {position['after']}")
                break
    
    # Backup and save
    with open(f"{workflow_file}.bak", 'w') as f:
        yaml.dump(original, f)
    
    with open(workflow_file, 'w') as f:
        yaml.dump(workflow, f)
    
    return True

# Define insertions for greenfield workflow
greenfield_insertions = [
    {
        'position': {'after': 'analyst'},
        'step': {
            'agent': 'problem-solver',
            'creates': 'problem-analysis.md',
            'optional': True,
            'condition': 'has_complex_challenges'
        }
    }
]

# Apply updates
# update_workflows('greenfield-fullstack.yaml', greenfield_insertions)
```

## Testing Checklist

### Unit Tests
- [ ] Workflow YAML valid
- [ ] Sequence dependencies correct
- [ ] Conditional logic works
- [ ] Handoff messages clear

### Integration Tests
- [ ] Workflow executable end-to-end
- [ ] Agent transitions smooth
- [ ] Documents created in correct order
- [ ] Optional steps skip appropriately

### Validation Tests
- [ ] Problem-solver adds value at insertion points
- [ ] No disruption to existing workflows
- [ ] Handoff protocols followed
- [ ] Decision points clear

## Definition of Done
- [ ] Complex problem-solving workflow created
- [ ] Existing workflows enhanced
- [ ] Handoff protocols documented
- [ ] Workflow selection matrix defined
- [ ] All tests passing
- [ ] Documentation updated

## File List
```
Created:
- .bmad-core/workflows/complex-problem-solving.yaml
- .bmad-core/utils/problem-solver-handoffs.md

Modified:
- .bmad-core/workflows/greenfield-fullstack.yaml
- .bmad-core/workflows/brownfield-fullstack.yaml
- .bmad-core/workflows/greenfield-service.yaml (optional)
- .bmad-core/workflows/brownfield-service.yaml (optional)
```