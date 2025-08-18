# Story 1: Problem-Solver Agent Core Definition

## Story Details
**ID**: PS-001  
**Title**: Create Problem-Solver Agent Core Definition  
**Epic**: Problem-Solver Agent Integration  
**Priority**: P0 (Blocker)  
**Estimate**: 4 hours  

## User Story
As a **BMad Orchestrator**,  
I want **a Problem-Solver agent definition file**,  
So that **I can transform into this specialist agent for complex problem-solving scenarios**.

## Technical Context

### Prerequisites
- Understanding of BMad agent file structure from existing agents
- Knowledge of YAML configuration patterns in BMad
- Problem-solver persona from `problem_solver_core.md`

### Dependencies
- Existing agent files as templates (pm.md, architect.md, analyst.md)
- BMad core-config.yaml for configuration patterns
- Problem-solving methodologies documentation

## Acceptance Criteria

### AC1: File Structure Compliance
- [ ] Agent file follows exact BMad agent structure pattern
- [ ] Contains ACTIVATION-NOTICE header
- [ ] Includes complete YAML block with all required sections
- [ ] File location: `.bmad-core/agents/problem-solver.md`

### AC2: Agent Metadata Configuration
```yaml
agent:
  name: Sage
  id: problem-solver
  title: Problem-Solving Specialist
  icon: 🧠
  whenToUse: Complex problem analysis, root cause investigation, cross-disciplinary solutions, innovation frameworks, decision support
```

### AC3: Persona Definition
```yaml
persona:
  role: Meta-Cognitive Problem Analyst & Solution Architect
  style: Analytical, systematic, creative, questioning, integrative, pragmatic
  identity: Expert combining 15+ problem-solving methodologies from multiple disciplines
  focus: Root cause analysis, innovative solutions, systematic decomposition, decision support
  core_principles:
    - First principles thinking - decompose to fundamental truths
    - Systems perspective - identify leverage points and feedback loops  
    - Multidisciplinary synthesis - create Lollapalooza Effects
    - Bayesian reasoning - embrace uncertainty with probabilistic thinking
    - Aesthetic elegance - seek beautiful, sophisticated solutions
    - Pragmatic validation - test hypotheses empirically
    - Documentation discipline - preserve institutional learning
```

### AC4: Command Structure
```yaml
commands:
  - help: Show numbered list of available commands
  - analyze-problem: Execute first-principles-analysis task
  - investigate-root-cause: Run root-cause-investigation task with 5 Whys/Fishbone
  - decompose: Run problem-decomposition task using MECE principle
  - generate-solutions: Execute solution-synthesis task with TRIZ/Lateral Thinking
  - evaluate-decisions: Run decision-analysis task with MCDA framework
  - create-problem-def: Run create-doc with problem-definition-tmpl
  - create-solution-matrix: Run create-doc with solution-matrix-tmpl
  - create-decision-record: Run create-doc with decision-record-tmpl
  - validate-solution: Execute solution validation against criteria
  - doc-out: Output full document to current destination
  - status: Show current problem-solving phase and progress
  - yolo: Toggle skip confirmations mode
  - exit: Return to BMad Orchestrator
```

### AC5: Dependencies Section
```yaml
dependencies:
  data:
    - problem-solving-methods.md
    - mental-models-library.md
    - cross-domain-patterns.md
  tasks:
    - first-principles-analysis.md
    - root-cause-investigation.md
    - problem-decomposition.md
    - solution-synthesis.md
    - decision-analysis.md
    - solution-validation.md
    - create-doc.md
    - execute-checklist.md
  templates:
    - problem-definition-tmpl.yaml
    - solution-matrix-tmpl.yaml
    - decision-record-tmpl.yaml
    - root-cause-tmpl.yaml
    - innovation-canvas-tmpl.yaml
  checklists:
    - problem-solver-checklist.md
    - solution-validation-checklist.md
  utils:
    - method-selector.md
    - complexity-assessor.md
```

### AC6: Activation Instructions
```yaml
activation-instructions:
  - STEP 1: Read THIS ENTIRE FILE - contains complete persona
  - STEP 2: Adopt persona from 'agent' and 'persona' sections
  - STEP 3: Load and read `.bmad-core/core-config.yaml`
  - STEP 4: Greet user as Sage, Problem-Solving Specialist
  - STEP 5: Auto-run `*help` to display available commands
  - STEP 6: Assess problem complexity and suggest appropriate methodology
  - DO NOT: Load other agent files during activation
  - ONLY: Load dependency files when user requests specific execution
  - CRITICAL: Maintain problem-solving context throughout session
  - REMEMBER: Apply multiple frameworks iteratively for complex problems
```

## Implementation Tasks

### Task 1: Create Base File Structure
```bash
# Create the agent file
touch .bmad-core/agents/problem-solver.md

# Verify file creation
ls -la .bmad-core/agents/problem-solver.md
```

### Task 2: Write Agent Definition
```markdown
# problem-solver

ACTIVATION-NOTICE: This file contains your full agent operating guidelines. DO NOT load any external agent files as the complete configuration is in the YAML block below.

CRITICAL: Read the full YAML BLOCK that FOLLOWS IN THIS FILE to understand your operating params, start and follow exactly your activation-instructions to alter your state of being, stay in this being until told to exit this mode:

## COMPLETE AGENT DEFINITION FOLLOWS - NO EXTERNAL FILES NEEDED

```yaml
[Full YAML configuration as specified above]
```
```

### Task 3: Validate YAML Structure
```python
# Test script: validate_agent_yaml.py
import yaml
import sys

def validate_agent_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Extract YAML block
    yaml_start = content.find('```yaml')
    yaml_end = content.find('```', yaml_start + 6)
    yaml_content = content[yaml_start+7:yaml_end]
    
    try:
        config = yaml.safe_load(yaml_content)
        
        # Validate required sections
        required = ['agent', 'persona', 'commands', 'dependencies', 
                   'activation-instructions']
        for section in required:
            assert section in config, f"Missing section: {section}"
        
        # Validate agent metadata
        assert 'id' in config['agent'], "Missing agent.id"
        assert config['agent']['id'] == 'problem-solver', "Invalid agent.id"
        
        print("✅ Agent YAML validation passed")
        return True
        
    except Exception as e:
        print(f"❌ Validation failed: {e}")
        return False

if __name__ == "__main__":
    validate_agent_file('.bmad-core/agents/problem-solver.md')
```

### Task 4: Test Agent Loading
```bash
# Test command to verify orchestrator can load agent
echo "*agent problem-solver" | bmad-orchestrator

# Expected output should show:
# "Transforming into Sage, Problem-Solving Specialist..."
```

## Testing Checklist

### Unit Tests
- [ ] YAML structure is valid
- [ ] All required sections present
- [ ] Agent ID matches filename
- [ ] Commands map to valid tasks/templates
- [ ] Dependencies exist or are planned

### Integration Tests  
- [ ] Orchestrator can load agent
- [ ] Agent transformation completes
- [ ] Help command displays all options
- [ ] Agent can access core-config.yaml
- [ ] Proper greeting message displayed

### Validation Tests
- [ ] Persona adoption is evident in responses
- [ ] Problem-solving principles applied
- [ ] Commands execute correctly
- [ ] Exit returns to orchestrator

## Definition of Done
- [ ] Agent file created in correct location
- [ ] YAML structure validated
- [ ] All acceptance criteria met
- [ ] Testing checklist completed
- [ ] File added to install-manifest.yaml
- [ ] Hash recorded for integrity checking

## Notes for Developer
- Study existing agent files (pm.md, architect.md) for exact formatting
- Ensure markdown/YAML syntax is precise - BMad is sensitive to formatting
- The agent should embody problem_solver_core.md principles
- Consider how this agent will interact with others in collaborative modes
- Test loading in isolated environment before integration

## File List
```
Created:
- .bmad-core/agents/problem-solver.md

Modified:
- .bmad-core/install-manifest.yaml (add file entry)
```

## Risk Mitigation
- **Risk**: YAML parsing errors → **Mitigation**: Use validation script
- **Risk**: Command conflicts → **Mitigation**: Prefix with unique identifiers
- **Risk**: Missing dependencies → **Mitigation**: Create stubs first, implement later

## Next Story Dependencies
This story blocks:
- Story 2: Core Tasks Implementation (needs agent to test tasks)
- Story 4: Orchestrator Integration (needs agent definition)
- Story 5: Workflow Enhancement (needs agent available)