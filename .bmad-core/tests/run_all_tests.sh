#!/bin/bash
# BMad Problem-Solver Test Suite

set -e  # Exit on error

echo "=== BMad Problem-Solver Test Suite ==="
echo "$(date)"
echo

# Test 1: File existence
echo "Test 1: File Existence..."
files=(
    ".bmad-core/agents/problem-solver.md"
    ".bmad-core/tasks/first-principles-analysis.md"
    ".bmad-core/tasks/root-cause-investigation.md"
    ".bmad-core/tasks/problem-decomposition.md" 
    ".bmad-core/tasks/solution-synthesis.md"
    ".bmad-core/tasks/decision-analysis.md"
    ".bmad-core/templates/problem-definition-tmpl.yaml"
    ".bmad-core/templates/solution-matrix-tmpl.yaml"
    ".bmad-core/templates/decision-record-tmpl.yaml"
    ".bmad-core/workflows/complex-problem-solving.yaml"
    ".bmad-core/utils/problem-solver-handoffs.md"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        size=$(wc -c < "$file")
        echo "✅ $file ($size bytes)"
    else
        echo "❌ $file: NOT FOUND"
        exit 1
    fi
done

# Test 2: YAML validity
echo -e "\nTest 2: YAML Validity..."
yaml_files=(
    ".bmad-core/agents/problem-solver.md"
    ".bmad-core/templates/problem-definition-tmpl.yaml"
    ".bmad-core/templates/solution-matrix-tmpl.yaml"
    ".bmad-core/templates/decision-record-tmpl.yaml"
    ".bmad-core/workflows/complex-problem-solving.yaml"
    ".bmad-core/install-manifest.yaml"
)

for file in "${yaml_files[@]}"; do
    if [[ "$file" == *.md ]]; then
        # Extract YAML from markdown
        if grep -q '```yaml' "$file"; then
            echo "✅ $file: Contains YAML block"
        else
            echo "❌ $file: No YAML block found"
            exit 1
        fi
    else
        # Validate YAML file directly
        python3 -c "import yaml; yaml.safe_load(open('$file'))" 2>/dev/null
        if [ $? -eq 0 ]; then
            echo "✅ $file: Valid YAML"
        else
            echo "❌ $file: Invalid YAML"
            exit 1
        fi
    fi
done

# Test 3: Agent team integration
echo -e "\nTest 3: Agent Team Integration..."
for team in team-fullstack.yaml team-no-ui.yaml; do
    team_file=".bmad-core/agent-teams/$team"
    if grep -q "problem-solver" "$team_file" || grep -q "\*" "$team_file"; then
        echo "✅ $team: Contains problem-solver or wildcard"
    else
        echo "❌ $team: Missing problem-solver"
        exit 1
    fi
done

# Test 4: Install manifest validation
echo -e "\nTest 4: Install Manifest..."
if grep -q "problem-solver" .bmad-core/install-manifest.yaml; then
    echo "✅ Install manifest includes problem-solver files"
else
    echo "❌ Install manifest not updated"
    exit 1
fi

# Test 5: Content validation
echo -e "\nTest 5: Content Validation..."

# Check agent has required concepts
agent_content=$(cat .bmad-core/agents/problem-solver.md | tr '[:upper:]' '[:lower:]')
concepts=("first principles" "triz" "mece" "root cause" "decision analysis")

for concept in "${concepts[@]}"; do
    if echo "$agent_content" | grep -q "$concept"; then
        echo "✅ Agent contains: $concept"
    else
        echo "⚠️  Agent missing concept: $concept"
    fi
done

# Check tasks have execution notices
for task in .bmad-core/tasks/*-analysis.md .bmad-core/tasks/problem-decomposition.md .bmad-core/tasks/solution-synthesis.md; do
    if grep -q "CRITICAL EXECUTION NOTICE" "$task"; then
        task_name=$(basename "$task")
        echo "✅ $task_name: Has execution notice"
    else
        echo "❌ $task: Missing execution notice"
        exit 1
    fi
done

# Test 6: Integration test
echo -e "\nTest 6: Integration Test..."

# Simulate workflow execution
python3 << 'EOF'
import yaml

# Load workflow
with open('.bmad-core/workflows/complex-problem-solving.yaml', 'r') as f:
    workflow = yaml.safe_load(f)

sequence = workflow['workflow']['sequence']
created = set()

print("Simulating workflow execution:")
for i, step in enumerate(sequence, 1):
    if isinstance(step, dict) and 'agent' in step:
        agent = step['agent']
        creates = step.get('creates', 'output')
        requires = step.get('requires', [])
        
        if isinstance(requires, str):
            requires = [requires]
        
        # Check dependencies
        missing = [r for r in requires if r not in created and r not in ['all_validations', 'all_documents']]
        if missing and not step.get('optional', False):
            print(f"❌ Step {i}: {agent} missing required: {missing}")
            exit(1)
        
        print(f"✅ Step {i}: {agent} -> {creates}")
        if creates != 'output':
            created.add(creates)

print(f"Workflow complete: {len(created)} artifacts created")
EOF

if [ $? -eq 0 ]; then
    echo "✅ Workflow simulation passed"
else
    echo "❌ Workflow simulation failed"
    exit 1
fi

# Final summary
echo -e "\n=== Test Summary ==="
echo "✅ All core tests passed!"
echo "🎉 Problem-Solver integration is ready!"
echo "🚀 To use: *agent problem-solver"
echo

echo "Files created:"
echo "- Agent: .bmad-core/agents/problem-solver.md"
echo "- Tasks: 5 problem-solving task files"
echo "- Templates: 3 interactive document templates"
echo "- Workflow: complex-problem-solving.yaml"
echo "- Utils: problem-solver-handoffs.md"
echo

echo "=== Tests Complete ==="