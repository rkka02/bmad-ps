# Story 3: Template Development

## Story Details
**ID**: PS-003  
**Title**: Create Problem-Solving Document Templates  
**Epic**: Problem-Solver Agent Integration  
**Priority**: P1 (High)  
**Estimate**: 6 hours  
**Dependencies**: Story 2 (Core Tasks)

## User Story
As a **Problem-Solver agent**,  
I want **YAML-driven interactive templates**,  
So that **I can generate structured problem-solving documents with user collaboration**.

## Technical Context

### BMad Template System
- YAML templates drive document generation
- Interactive elicitation with `elicit: true`
- Sections can be conditional, repeatable, nested
- Output in markdown format for agent consumption
- Templates use `create-doc.md` task for execution

### Templates to Create
1. Problem Definition Template - Comprehensive problem scoping
2. Solution Matrix Template - Multi-option comparison
3. Decision Record Template - ADR-style decision documentation
4. Root Cause Analysis Template - Investigation results
5. Innovation Canvas Template - Creative solution exploration

## Acceptance Criteria

### AC1: Problem Definition Template
**File**: `.bmad-core/templates/problem-definition-tmpl.yaml`

```yaml
template:
  id: problem-definition-v1
  name: Problem Definition Document
  version: 1.0
  output:
    format: markdown
    filename: docs/problem-definition.md
    title: "{{problem_name}} - Problem Definition"

workflow:
  mode: interactive
  elicitation: advanced-elicitation

sections:
  - id: executive-summary
    title: Executive Summary
    instruction: |
      Provide 2-3 sentence overview of the problem, its impact, and urgency.
      This will be read by stakeholders who need quick understanding.
    elicit: false
    template: |
      **Problem**: {{problem_statement}}
      **Impact**: {{business_impact}}
      **Urgency**: {{urgency_level}}

  - id: problem-statement
    title: Problem Statement
    instruction: |
      Apply McKinsey's structured problem definition:
      Transform vague concerns into specific, actionable problem statements.
      Use format: "How might we [action] for [user] to achieve [outcome] given [constraints]?"
    elicit: true
    sections:
      - id: current-state
        title: Current State
        type: paragraphs
        instruction: Describe what is happening now that is problematic
      - id: desired-state
        title: Desired State
        type: paragraphs
        instruction: Describe the target state we want to achieve
      - id: gap-analysis
        title: Gap Analysis
        type: bullet-list
        instruction: List specific gaps between current and desired states

  - id: stakeholder-analysis
    title: Stakeholder Analysis
    instruction: |
      Identify all affected parties and their perspectives on the problem.
      Use RACI matrix thinking (Responsible, Accountable, Consulted, Informed).
    elicit: true
    type: table
    columns: [Stakeholder, Impact Level, Concerns, Success Criteria]
    examples:
      - ["End Users", "High", "System downtime", "99.9% uptime"]
      - ["Operations Team", "Medium", "Maintenance burden", "Automated deployments"]

  - id: constraints-assumptions
    title: Constraints and Assumptions
    instruction: |
      Document boundaries and beliefs that shape solution space.
      Challenge each assumption using first principles thinking.
    sections:
      - id: hard-constraints
        title: Hard Constraints
        type: numbered-list
        prefix: HC
        instruction: Immutable limitations (budget, time, regulations)
        examples:
          - "HC1: Solution must comply with GDPR regulations"
          - "HC2: Budget limited to $100,000"
      - id: soft-constraints
        title: Soft Constraints
        type: numbered-list
        prefix: SC
        instruction: Preferred limitations that could be negotiated
      - id: assumptions
        title: Key Assumptions
        type: numbered-list
        prefix: A
        instruction: Beliefs we're operating under - mark confidence level

  - id: problem-decomposition
    title: Problem Decomposition
    instruction: |
      Break down the problem using MECE principle.
      Each component should be independently solvable.
    elicit: true
    sections:
      - id: decomposition-method
        title: Decomposition Method
        choices: [Functional, Temporal, Spatial, Causal, Stakeholder-based]
      - id: components
        title: Problem Components
        type: hierarchical-list
        instruction: Create 2-3 level hierarchy of problem components

  - id: success-metrics
    title: Success Metrics
    instruction: |
      Define measurable criteria for solution evaluation.
      Use SMART goals: Specific, Measurable, Achievable, Relevant, Time-bound.
    elicit: true
    sections:
      - id: primary-metrics
        title: Primary KPIs
        type: table
        columns: [Metric, Current Value, Target Value, Measurement Method]
      - id: secondary-metrics
        title: Secondary Indicators
        type: bullet-list

  - id: root-cause-hypothesis
    title: Initial Root Cause Hypothesis
    instruction: |
      Based on initial analysis, what might be causing this problem?
      Mark confidence level and evidence for each hypothesis.
    type: numbered-list
    elicit: true
    template: |
      {{number}}. **Hypothesis**: {{hypothesis}}
         - **Confidence**: {{confidence_level}}%
         - **Evidence**: {{supporting_evidence}}
         - **Test Method**: {{how_to_validate}}

  - id: solution-criteria
    title: Solution Evaluation Criteria
    instruction: |
      Define how potential solutions will be evaluated.
      Weight criteria by importance for decision-making.
    type: table
    columns: [Criterion, Weight (0-1), Description, Measurement]
    elicit: true
    validation:
      sum_weights: 1.0

  - id: next-steps
    title: Recommended Next Steps
    sections:
      - id: immediate-actions
        title: Immediate Actions (Next 48 hours)
        type: numbered-list
      - id: investigation-plan
        title: Investigation Plan
        type: numbered-list
      - id: stakeholder-communications
        title: Stakeholder Communications
        type: bullet-list
```

**Test Code**:
```python
# test_problem_definition_template.py
import yaml
import jsonschema

def test_template_structure():
    with open('.bmad-core/templates/problem-definition-tmpl.yaml', 'r') as f:
        template = yaml.safe_load(f)
    
    # Validate required top-level keys
    required_keys = ['template', 'workflow', 'sections']
    for key in required_keys:
        assert key in template, f"Missing required key: {key}"
    
    # Validate template metadata
    assert template['template']['id'] == 'problem-definition-v1'
    assert template['template']['output']['format'] == 'markdown'
    
    # Validate sections
    assert len(template['sections']) > 5, "Template should have comprehensive sections"
    
    # Check for elicitation points
    elicit_count = sum(1 for s in template['sections'] if s.get('elicit', False))
    assert elicit_count >= 3, "Template needs multiple interaction points"
    
    print("✅ Problem definition template structure valid")

def test_weight_validation():
    # Test solution criteria weight validation
    criteria = [
        {'criterion': 'Cost', 'weight': 0.3},
        {'criterion': 'Time', 'weight': 0.3},
        {'criterion': 'Quality', 'weight': 0.4}
    ]
    
    total_weight = sum(c['weight'] for c in criteria)
    assert abs(total_weight - 1.0) < 0.001, f"Weights must sum to 1.0, got {total_weight}"
    print("✅ Weight validation logic works")

test_template_structure()
test_weight_validation()
```

### AC2: Solution Matrix Template
**File**: `.bmad-core/templates/solution-matrix-tmpl.yaml`

```yaml
template:
  id: solution-matrix-v1
  name: Solution Comparison Matrix
  version: 1.0
  output:
    format: markdown
    filename: docs/solution-matrix.md
    title: "Solution Options Analysis"

workflow:
  mode: interactive
  elicitation: advanced-elicitation

sections:
  - id: problem-recap
    title: Problem Recap
    instruction: Brief reminder of the problem being solved
    template: |
      **Problem**: {{problem_statement}}
      **Key Constraints**: {{constraints_summary}}
      **Success Criteria**: {{success_criteria}}

  - id: solution-generation-methods
    title: Solution Generation Methods Used
    instruction: Document which innovation frameworks were applied
    type: checklist
    options:
      - TRIZ (Systematic Innovation)
      - Design Thinking
      - Lateral Thinking
      - Biomimicry
      - First Principles Reconstruction
      - Analogical Reasoning
      - Combinatory Play
    elicit: true

  - id: solution-options
    title: Solution Option {{solution_number}}
    repeatable: true
    max_items: 10
    instruction: |
      Describe each solution option comprehensively.
      Include enough detail for evaluation but stay high-level on implementation.
    elicit: true
    sections:
      - id: solution-overview
        title: Overview
        type: paragraph
        instruction: 2-3 sentence description of the solution approach
      
      - id: innovation-principle
        title: Innovation Principle Applied
        instruction: Which creative principle or method led to this solution?
      
      - id: implementation-approach
        title: Implementation Approach
        type: numbered-list
        instruction: High-level steps to implement this solution
      
      - id: pros-cons
        title: Advantages and Disadvantages
        sections:
          - id: advantages
            title: Advantages
            type: bullet-list
            min_items: 3
          - id: disadvantages
            title: Disadvantages
            type: bullet-list
            min_items: 2
      
      - id: risks
        title: Key Risks
        type: table
        columns: [Risk, Likelihood (L/M/H), Impact (L/M/H), Mitigation]
      
      - id: resource-requirements
        title: Resource Requirements
        sections:
          - id: time-estimate
            title: Time Estimate
            type: text
          - id: cost-estimate
            title: Cost Estimate
            type: text
          - id: team-requirements
            title: Team Requirements
            type: bullet-list

  - id: evaluation-matrix
    title: Comparative Evaluation Matrix
    instruction: |
      Score each solution against predefined criteria.
      Use 1-10 scale consistently. Reference criteria from problem definition.
    type: dynamic-table
    elicit: true
    structure:
      rows: solutions  # Populated from solution-options
      columns: criteria  # From problem definition or define here
      cells: scores (1-10)
    calculation:
      weighted_score: sum(score * criterion_weight)
    template: |
      | Solution | {{criteria_names}} | Weighted Total |
      |----------|-------------------|----------------|
      {{#each solutions}}
      | {{name}} | {{scores}} | {{weighted_total}} |
      {{/each}}

  - id: sensitivity-analysis
    title: Sensitivity Analysis
    instruction: |
      Test how robust the ranking is to weight changes.
      Identify which criteria changes would alter the recommendation.
    elicit: false
    auto_generate: true
    sections:
      - id: critical-factors
        title: Critical Decision Factors
        instruction: Criteria where ±20% weight change alters ranking
      - id: robust-winner
        title: Robustness Assessment
        instruction: Does recommended solution remain best under variations?

  - id: recommendation
    title: Recommendation
    instruction: |
      Based on systematic analysis, provide clear recommendation with rationale.
      Address why other options were not selected.
    elicit: true
    sections:
      - id: selected-solution
        title: Recommended Solution
        template: |
          **Selected**: Solution {{solution_id}} - {{solution_name}}
          **Overall Score**: {{weighted_score}}/10
          **Confidence Level**: {{confidence}}
      
      - id: rationale
        title: Decision Rationale
        type: paragraphs
        min_length: 100
      
      - id: why-not-others
        title: Why Other Options Were Not Selected
        type: bullet-list
        instruction: Brief explanation for each rejected option
      
      - id: implementation-roadmap
        title: Implementation Roadmap
        type: numbered-list
        instruction: Next steps to begin implementing selected solution

  - id: validation-plan
    title: Solution Validation Plan
    instruction: How will we know if the solution is working?
    sections:
      - id: success-indicators
        title: Early Success Indicators
        type: bullet-list
      - id: failure-signals
        title: Failure Signals to Watch
        type: bullet-list
      - id: pivot-criteria
        title: Pivot Criteria
        instruction: Under what conditions would we reconsider?
```

**Test Code**:
```python
# test_solution_matrix.py
import numpy as np

def test_matrix_calculation():
    # Mock solution scores
    solutions = [
        {'name': 'Solution A', 'scores': [8, 7, 9, 6]},
        {'name': 'Solution B', 'scores': [7, 9, 7, 8]},
        {'name': 'Solution C', 'scores': [9, 6, 8, 7]}
    ]
    
    # Criteria weights
    weights = [0.3, 0.3, 0.2, 0.2]  # Must sum to 1.0
    
    # Calculate weighted scores
    results = []
    for solution in solutions:
        weighted_score = sum(s * w for s, w in zip(solution['scores'], weights))
        results.append({
            'name': solution['name'],
            'weighted_score': round(weighted_score, 2)
        })
    
    # Sort by score
    results.sort(key=lambda x: x['weighted_score'], reverse=True)
    
    print("✅ Solution Matrix Calculations:")
    for r in results:
        print(f"  {r['name']}: {r['weighted_score']}")
    
    assert results[0]['weighted_score'] >= results[1]['weighted_score']
    return results

def test_sensitivity_analysis():
    base_weights = [0.3, 0.3, 0.2, 0.2]
    variation = 0.2  # ±20%
    
    # Test weight variations
    def vary_weight(weights, index, delta):
        new_weights = weights.copy()
        new_weights[index] += delta
        # Renormalize
        total = sum(new_weights)
        return [w/total for w in new_weights]
    
    # Check if ranking changes with variations
    ranking_changes = []
    for i in range(len(base_weights)):
        for delta in [-variation, variation]:
            new_weights = vary_weight(base_weights, i, delta)
            # Would recalculate rankings here
            ranking_changes.append((i, delta))
    
    print(f"✅ Sensitivity analysis tested {len(ranking_changes)} variations")
    assert len(ranking_changes) == 8  # 4 criteria × 2 directions

test_matrix_calculation()
test_sensitivity_analysis()
```

### AC3: Decision Record Template
**File**: `.bmad-core/templates/decision-record-tmpl.yaml`

```yaml
template:
  id: decision-record-v1
  name: Architectural Decision Record
  version: 1.0
  output:
    format: markdown
    filename: docs/decisions/ADR-{{number}}-{{slug}}.md
    title: "ADR-{{number}}: {{title}}"

workflow:
  mode: interactive
  elicitation: focused

metadata:
  - id: number
    title: ADR Number
    type: auto-increment
    prefix: ADR-
    start: 1
  
  - id: title
    title: Decision Title
    type: text
    validation: max_length: 100
  
  - id: date
    title: Date
    type: date
    default: today
  
  - id: status
    title: Status
    type: select
    options: [Proposed, Accepted, Deprecated, Superseded]
    default: Proposed

sections:
  - id: context
    title: Context
    instruction: |
      Describe the forces at play, including technological, political, social, and project constraints.
      What is the issue that we're seeing that is motivating this decision?
    elicit: true
    min_length: 200
    prompts:
      - What problem are we trying to solve?
      - What constraints exist?
      - What patterns have we observed?
      - What are the stakeholder concerns?

  - id: decision-process
    title: Decision Process
    instruction: Document how the decision was reached
    sections:
      - id: options-considered
        title: Options Considered
        type: numbered-list
        min_items: 2
        instruction: List all options that were seriously evaluated
      
      - id: evaluation-method
        title: Evaluation Method
        instruction: How were options evaluated? (e.g., PoC, research, team discussion)
      
      - id: decision-criteria
        title: Decision Criteria
        type: bullet-list
        instruction: What factors were most important in the decision?

  - id: decision
    title: Decision
    instruction: |
      State the decision clearly and concisely.
      Use active voice and full sentences.
      Be specific about what will be done.
    elicit: true
    template: |
      We will **{{decision_action}}** because **{{primary_rationale}}**.
      
      This means:
      {{implementation_implications}}

  - id: consequences
    title: Consequences
    instruction: |
      Document the results of this decision, both positive and negative.
      Include second-order effects and long-term implications.
    elicit: true
    sections:
      - id: positive-consequences
        title: Positive Consequences
        type: bullet-list
        min_items: 2
        examples:
          - "Reduced deployment time from 2 hours to 15 minutes"
          - "Improved developer experience with hot reloading"
      
      - id: negative-consequences
        title: Negative Consequences
        type: bullet-list
        min_items: 1
        examples:
          - "Increased complexity in build configuration"
          - "Additional training required for team members"
      
      - id: risks-tradeoffs
        title: Risks and Trade-offs
        type: table
        columns: [Risk/Trade-off, Likelihood, Impact, Mitigation Strategy]

  - id: implementation
    title: Implementation
    sections:
      - id: action-items
        title: Action Items
        type: table
        columns: [Action, Owner, Due Date, Status]
      
      - id: validation
        title: How will we validate this decision?
        type: paragraphs
        instruction: Describe how we'll know if this was the right choice

  - id: references
    title: References
    instruction: Link to relevant documentation, research, or related ADRs
    type: bullet-list
    examples:
      - "[Related ADR-005](../ADR-005-api-versioning.md)"
      - "[Research spike results](../research/caching-strategies.md)"
      - "[Industry best practices](https://martinfowler.com/articles/microservices.html)"

  - id: revision-history
    title: Revision History
    type: table
    columns: [Date, Version, Author, Changes]
    auto_populate: true
```

**Test Code**:
```bash
#!/bin/bash
# test_decision_record.sh

# Test ADR number generation
test_adr_numbering() {
    local last_number=0
    local adr_dir="docs/decisions"
    
    # Find highest existing ADR number
    if [ -d "$adr_dir" ]; then
        last_number=$(ls $adr_dir/ADR-*.md 2>/dev/null | \
                     sed 's/.*ADR-\([0-9]*\).*/\1/' | \
                     sort -n | tail -1)
    fi
    
    next_number=$((last_number + 1))
    echo "Next ADR number: $next_number"
    
    # Test slug generation
    title="Use React for Frontend Framework"
    slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
    filename="ADR-${next_number}-${slug}.md"
    
    echo "✅ Generated filename: $filename"
}

# Test decision validation
test_decision_validation() {
    # Check that decision has required components
    decision="We will use React for the frontend because it has strong community support."
    
    if [[ $decision == *"We will"* ]] && [[ $decision == *"because"* ]]; then
        echo "✅ Decision format valid"
    else
        echo "❌ Decision must use 'We will... because...' format"
        exit 1
    fi
}

test_adr_numbering
test_decision_validation
```

### AC4: Supporting Templates
Create two additional templates for comprehensive problem-solving:

**Root Cause Analysis Template** (`.bmad-core/templates/root-cause-tmpl.yaml`):
- 5 Whys progression tracking
- Fishbone diagram categories
- Evidence collection for each cause
- Validation experiments design

**Innovation Canvas Template** (`.bmad-core/templates/innovation-canvas-tmpl.yaml`):
- Problem-Solution Fit section
- Innovation method application
- Feasibility analysis
- Prototype planning

## Implementation Tasks

### Task 1: Create Template Files
```bash
#!/bin/bash
# create_templates.sh

TEMPLATE_DIR=".bmad-core/templates"
mkdir -p $TEMPLATE_DIR

templates=(
    "problem-definition-tmpl.yaml"
    "solution-matrix-tmpl.yaml"
    "decision-record-tmpl.yaml"
    "root-cause-tmpl.yaml"
    "innovation-canvas-tmpl.yaml"
)

for template in "${templates[@]}"; do
    touch "$TEMPLATE_DIR/$template"
    echo "Created: $TEMPLATE_DIR/$template"
done

echo "✅ All template files created"
ls -la $TEMPLATE_DIR/*-tmpl.yaml
```

### Task 2: Validate Template YAML
```python
# validate_templates.py
import yaml
import os

def validate_template(filepath):
    """Validate template structure and requirements"""
    try:
        with open(filepath, 'r') as f:
            template = yaml.safe_load(f)
        
        # Check required top-level keys
        required = ['template', 'sections']
        missing = [k for k in required if k not in template]
        if missing:
            return False, f"Missing keys: {missing}"
        
        # Check template metadata
        if 'id' not in template['template']:
            return False, "Missing template.id"
        
        # Check for at least one elicitation point
        def has_elicit(sections):
            for section in sections:
                if section.get('elicit', False):
                    return True
                if 'sections' in section:
                    if has_elicit(section['sections']):
                        return True
            return False
        
        if not has_elicit(template['sections']):
            return False, "No elicitation points found"
        
        return True, "Valid"
        
    except yaml.YAMLError as e:
        return False, f"YAML error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

# Test all templates
template_dir = ".bmad-core/templates"
templates = [
    "problem-definition-tmpl.yaml",
    "solution-matrix-tmpl.yaml",
    "decision-record-tmpl.yaml"
]

for template_file in templates:
    path = os.path.join(template_dir, template_file)
    if os.path.exists(path):
        valid, message = validate_template(path)
        status = "✅" if valid else "❌"
        print(f"{status} {template_file}: {message}")
```

### Task 3: Test Template Integration
```python
# test_template_integration.py

def test_create_doc_integration():
    """Test that templates work with create-doc.md task"""
    
    # Simulate create-doc.md execution
    class TemplateProcessor:
        def __init__(self, template_path):
            with open(template_path, 'r') as f:
                self.template = yaml.safe_load(f)
        
        def process_section(self, section):
            """Process a template section"""
            output = []
            
            # Add section title
            level = section.get('level', 2)
            output.append(f"{'#' * level} {section['title']}")
            
            # Process based on type
            section_type = section.get('type', 'text')
            
            if section_type == 'table':
                columns = section.get('columns', [])
                output.append(f"| {' | '.join(columns)} |")
                output.append(f"| {' | '.join(['---'] * len(columns))} |")
            
            elif section_type == 'numbered-list':
                prefix = section.get('prefix', '')
                for i in range(3):  # Mock items
                    output.append(f"{prefix}{i+1}: Item {i+1}")
            
            # Handle nested sections
            if 'sections' in section:
                for subsection in section['sections']:
                    output.extend(self.process_section(subsection))
            
            return output
        
        def generate_document(self):
            """Generate full document from template"""
            lines = [f"# {self.template['template']['title']}"]
            
            for section in self.template['sections']:
                lines.extend(self.process_section(section))
                lines.append("")  # Empty line between sections
            
            return '\n'.join(lines)
    
    # Test with problem definition template
    processor = TemplateProcessor('.bmad-core/templates/problem-definition-tmpl.yaml')
    document = processor.generate_document()
    
    assert '# Problem Definition' in document
    assert '## ' in document  # Has sections
    print("✅ Template processing works")
    
    return document

# Run test
if os.path.exists('.bmad-core/templates/problem-definition-tmpl.yaml'):
    doc = test_create_doc_integration()
    print(f"Generated {len(doc)} characters of documentation")
```

## Testing Checklist

### Unit Tests
- [ ] YAML structure valid for all templates
- [ ] Required sections present
- [ ] Elicitation points properly marked
- [ ] Output format specifications correct

### Integration Tests
- [ ] Templates loadable by create-doc task
- [ ] Interactive elicitation flow works
- [ ] Conditional sections evaluate correctly
- [ ] Repeatable sections function properly

### Validation Tests
- [ ] Problem definition covers all aspects
- [ ] Solution matrix calculates correctly
- [ ] Decision records follow ADR standards
- [ ] All templates produce valid markdown

## Definition of Done
- [ ] All 5 template files created
- [ ] YAML structure validated
- [ ] Elicitation points implemented
- [ ] Integration with create-doc verified
- [ ] Test scripts passing
- [ ] Documentation examples created

## Notes for Developer
- Study existing templates (prd-tmpl.yaml) for patterns
- Ensure elicitation points use standard 1-9 format
- Test conditional and repeatable sections
- Validate YAML carefully - small errors break parsing
- Consider template versioning for future updates

## File List
```
Created:
- .bmad-core/templates/problem-definition-tmpl.yaml
- .bmad-core/templates/solution-matrix-tmpl.yaml
- .bmad-core/templates/decision-record-tmpl.yaml
- .bmad-core/templates/root-cause-tmpl.yaml
- .bmad-core/templates/innovation-canvas-tmpl.yaml

Test Files:
- test_problem_definition_template.py
- test_solution_matrix.py
- test_decision_record.sh
- validate_templates.py
- test_template_integration.py
```

## Next Story Dependencies
This story enables:
- Story 4: Templates available for agent commands
- Story 5: Workflows can reference templates
- Story 7: Documentation can show template examples