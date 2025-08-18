# Story 4: Orchestrator Integration

## Story Details
**ID**: PS-004  
**Title**: Integrate Problem-Solver with BMad Orchestrator  
**Epic**: Problem-Solver Agent Integration  
**Priority**: P0 (Blocker)  
**Estimate**: 4 hours  
**Dependencies**: Story 1 (Agent Definition)

## User Story
As a **BMad user**,  
I want **the Orchestrator to recognize and transform into Problem-Solver agent**,  
So that **I can access problem-solving capabilities through the standard BMad interface**.

## Technical Context

### Orchestrator Integration Points
- Agent registry in orchestrator configuration
- Transform command recognition (`*agent problem-solver`)
- Agent team bundle updates
- Command routing and help display

## Acceptance Criteria

### AC1: Update Orchestrator Configuration
**File**: `.bmad-core/agents/bmad-orchestrator.md`

Add problem-solver to available agents list in YAML configuration:

```yaml
available-agents:
  - id: problem-solver
    title: Problem-Solving Specialist
    whenToUse: Complex problem analysis, root cause investigation, innovation
    file: problem-solver.md
```

### AC2: Modify Agent Team Configurations

**Update**: `.bmad-core/agent-teams/team-all.yaml`
```yaml
agents:
  - bmad-orchestrator
  - analyst
  - pm
  - ux-expert
  - architect
  - po
  - problem-solver  # ADD THIS LINE
  - dev
  - sm
  - qa
```

**Update**: `.bmad-core/agent-teams/team-fullstack.yaml`
```yaml
agents:
  - bmad-orchestrator
  - analyst
  - pm
  - ux-expert
  - architect
  - po
  - problem-solver  # ADD THIS LINE
```

### AC3: Command Recognition Test
```bash
# test_orchestrator_integration.sh
#!/bin/bash

# Test agent listing
echo "*agent" | bmad-orchestrator | grep -q "problem-solver"
if [ $? -eq 0 ]; then
    echo "✅ Problem-solver listed in available agents"
else
    echo "❌ Problem-solver not found in agent list"
    exit 1
fi

# Test transformation
echo "*agent problem-solver" | bmad-orchestrator | grep -q "Sage"
if [ $? -eq 0 ]; then
    echo "✅ Transformation to problem-solver works"
else
    echo "❌ Transformation failed"
    exit 1
fi

# Test fuzzy matching
echo "*agent problem solver" | bmad-orchestrator | grep -q "problem-solver"
echo "*agent sage" | bmad-orchestrator | grep -q "problem-solver"
```

### AC4: Help System Integration
When `*help` is called, problem-solver should appear:

```markdown
=== Available Specialist Agents ===
*agent problem-solver: Problem-Solving Specialist
  When to use: Complex problem analysis, root cause investigation, 
               cross-disciplinary solutions, innovation frameworks
  Key deliverables: problem-definition.md, solution-matrix.md, 
                   decision-record.md
```

### AC5: Install Manifest Update
**File**: `.bmad-core/install-manifest.yaml`

Add entries for all new files:
```yaml
files:
  - path: .bmad-core/agents/problem-solver.md
    hash: [calculate-hash]
    modified: false
  - path: .bmad-core/tasks/first-principles-analysis.md
    hash: [calculate-hash]
    modified: false
  # ... all other new files
```

**Hash Calculation Script**:
```python
# calculate_hashes.py
import hashlib
import yaml

def calculate_file_hash(filepath):
    """Calculate hash for BMad manifest"""
    with open(filepath, 'rb') as f:
        content = f.read()
    return hashlib.md5(content).hexdigest()[:16]

new_files = [
    '.bmad-core/agents/problem-solver.md',
    '.bmad-core/tasks/first-principles-analysis.md',
    '.bmad-core/tasks/root-cause-investigation.md',
    '.bmad-core/tasks/problem-decomposition.md',
    '.bmad-core/tasks/solution-synthesis.md',
    '.bmad-core/tasks/decision-analysis.md',
    '.bmad-core/templates/problem-definition-tmpl.yaml',
    '.bmad-core/templates/solution-matrix-tmpl.yaml',
    '.bmad-core/templates/decision-record-tmpl.yaml',
]

manifest_entries = []
for filepath in new_files:
    try:
        hash_value = calculate_file_hash(filepath)
        manifest_entries.append({
            'path': filepath,
            'hash': hash_value,
            'modified': False
        })
        print(f"✅ {filepath}: {hash_value}")
    except FileNotFoundError:
        print(f"❌ {filepath}: File not found")

# Output YAML format
print("\n# Add to install-manifest.yaml:")
print(yaml.dump({'files': manifest_entries}, default_flow_style=False))
```

## Implementation Tasks

### Task 1: Update Orchestrator Files
```bash
#!/bin/bash
# update_orchestrator.sh

# Backup original files
cp .bmad-core/agents/bmad-orchestrator.md .bmad-core/agents/bmad-orchestrator.md.bak
cp .bmad-core/agent-teams/team-all.yaml .bmad-core/agent-teams/team-all.yaml.bak

echo "✅ Backups created"

# Apply updates (would be done via proper edit commands)
echo "📝 Update bmad-orchestrator.md to include problem-solver"
echo "📝 Update team configurations"
```

### Task 2: Validate Integration
```python
# validate_integration.py
import yaml
import os

def check_agent_in_team(team_file, agent_id):
    """Check if agent is in team configuration"""
    with open(team_file, 'r') as f:
        team_config = yaml.safe_load(f)
    
    agents = team_config.get('agents', [])
    return agent_id in agents

def check_orchestrator_knows_agent(orchestrator_file, agent_id):
    """Check if orchestrator can list agent"""
    # Parse orchestrator YAML block
    with open(orchestrator_file, 'r') as f:
        content = f.read()
    
    # Check for agent reference
    return f"id: {agent_id}" in content or f"*agent {agent_id}" in content

# Run checks
teams = ['team-all.yaml', 'team-fullstack.yaml']
for team in teams:
    path = f'.bmad-core/agent-teams/{team}'
    if os.path.exists(path):
        if check_agent_in_team(path, 'problem-solver'):
            print(f"✅ {team}: Contains problem-solver")
        else:
            print(f"❌ {team}: Missing problem-solver")

if check_orchestrator_knows_agent('.bmad-core/agents/bmad-orchestrator.md', 'problem-solver'):
    print("✅ Orchestrator recognizes problem-solver")
else:
    print("❌ Orchestrator doesn't recognize problem-solver")
```

## Testing Checklist

### Unit Tests
- [ ] Orchestrator lists problem-solver
- [ ] Transform command works
- [ ] Fuzzy matching works
- [ ] Help displays correctly

### Integration Tests
- [ ] Can transform to problem-solver
- [ ] Problem-solver commands accessible
- [ ] Can return to orchestrator
- [ ] Team configurations include agent

### Validation Tests
- [ ] Install manifest updated
- [ ] File hashes correct
- [ ] No conflicts with existing agents

## Definition of Done
- [ ] Orchestrator configuration updated
- [ ] Team configurations updated
- [ ] Install manifest includes new files
- [ ] All integration tests passing
- [ ] Help system shows problem-solver

## File List
```
Modified:
- .bmad-core/agents/bmad-orchestrator.md
- .bmad-core/agent-teams/team-all.yaml
- .bmad-core/agent-teams/team-fullstack.yaml
- .bmad-core/agent-teams/team-no-ui.yaml (optional)
- .bmad-core/install-manifest.yaml
```