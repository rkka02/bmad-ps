# Story 6: Testing & Validation

## Story Details
**ID**: PS-006  
**Title**: Comprehensive Testing and Validation Suite  
**Epic**: Problem-Solver Agent Integration  
**Priority**: P1 (High)  
**Estimate**: 6 hours  
**Dependencies**: Stories 1-5 (All components implemented)

## User Story
As a **BMad developer**,  
I want **comprehensive tests for the problem-solver integration**,  
So that **all components work reliably and can be maintained confidently**.

## Technical Context

### Testing Levels Required
1. **Unit Tests**: Individual component functionality
2. **Integration Tests**: Agent interactions and handoffs
3. **End-to-End Tests**: Complete workflow execution
4. **Regression Tests**: Existing functionality preserved
5. **Performance Tests**: Response time and resource usage

## Acceptance Criteria

### AC1: Unit Test Suite
**File**: `.bmad-core/tests/test_problem_solver_unit.py`

```python
#!/usr/bin/env python3
"""
Unit tests for Problem-Solver agent components
"""

import unittest
import yaml
import os
import sys
import hashlib
from pathlib import Path

class TestAgentDefinition(unittest.TestCase):
    """Test the agent definition file structure and content"""
    
    def setUp(self):
        self.agent_file = '.bmad-core/agents/problem-solver.md'
        
    def test_agent_file_exists(self):
        """Agent file should exist"""
        self.assertTrue(os.path.exists(self.agent_file), 
                       f"Agent file not found: {self.agent_file}")
    
    def test_agent_yaml_structure(self):
        """Agent YAML should have required sections"""
        with open(self.agent_file, 'r') as f:
            content = f.read()
        
        # Extract YAML block
        yaml_start = content.find('```yaml')
        yaml_end = content.find('```', yaml_start + 6)
        yaml_content = content[yaml_start+7:yaml_end]
        
        config = yaml.safe_load(yaml_content)
        
        # Required sections
        required_sections = [
            'agent', 'persona', 'commands', 
            'dependencies', 'activation-instructions'
        ]
        
        for section in required_sections:
            self.assertIn(section, config, 
                         f"Missing required section: {section}")
    
    def test_agent_id_correct(self):
        """Agent ID should be 'problem-solver'"""
        with open(self.agent_file, 'r') as f:
            content = f.read()
        
        self.assertIn("id: problem-solver", content,
                     "Agent ID should be 'problem-solver'")
    
    def test_agent_commands_complete(self):
        """All required commands should be defined"""
        required_commands = [
            'help', 'analyze-problem', 'investigate-root-cause',
            'decompose', 'generate-solutions', 'evaluate-decisions'
        ]
        
        with open(self.agent_file, 'r') as f:
            content = f.read()
        
        for command in required_commands:
            self.assertIn(f"- {command}:", content,
                         f"Missing command: {command}")

class TestCoreTasks(unittest.TestCase):
    """Test the problem-solving task files"""
    
    def setUp(self):
        self.task_dir = '.bmad-core/tasks'
        self.required_tasks = [
            'first-principles-analysis.md',
            'root-cause-investigation.md',
            'problem-decomposition.md',
            'solution-synthesis.md',
            'decision-analysis.md'
        ]
    
    def test_all_tasks_exist(self):
        """All required task files should exist"""
        for task in self.required_tasks:
            task_path = os.path.join(self.task_dir, task)
            self.assertTrue(os.path.exists(task_path),
                           f"Task file not found: {task}")
    
    def test_task_structure(self):
        """Tasks should have required sections"""
        required_patterns = [
            '## ⚠️ CRITICAL EXECUTION NOTICE',
            '## Method',
            '## Output'
        ]
        
        for task in self.required_tasks:
            task_path = os.path.join(self.task_dir, task)
            with open(task_path, 'r') as f:
                content = f.read()
            
            for pattern in required_patterns:
                self.assertIn(pattern, content,
                             f"{task} missing: {pattern}")
    
    def test_task_output_yaml_valid(self):
        """Task output examples should be valid YAML"""
        for task in self.required_tasks:
            task_path = os.path.join(self.task_dir, task)
            with open(task_path, 'r') as f:
                content = f.read()
            
            # Extract YAML output examples
            if '```yaml' in content:
                yaml_start = content.find('```yaml')
                yaml_end = content.find('```', yaml_start + 6)
                yaml_content = content[yaml_start+7:yaml_end]
                
                try:
                    yaml.safe_load(yaml_content)
                except yaml.YAMLError as e:
                    self.fail(f"{task} has invalid YAML: {e}")

class TestTemplates(unittest.TestCase):
    """Test the document templates"""
    
    def setUp(self):
        self.template_dir = '.bmad-core/templates'
        self.required_templates = [
            'problem-definition-tmpl.yaml',
            'solution-matrix-tmpl.yaml',
            'decision-record-tmpl.yaml'
        ]
    
    def test_templates_exist(self):
        """All required templates should exist"""
        for template in self.required_templates:
            template_path = os.path.join(self.template_dir, template)
            self.assertTrue(os.path.exists(template_path),
                           f"Template not found: {template}")
    
    def test_template_yaml_valid(self):
        """Templates should be valid YAML"""
        for template in self.required_templates:
            template_path = os.path.join(self.template_dir, template)
            
            try:
                with open(template_path, 'r') as f:
                    yaml.safe_load(f)
            except yaml.YAMLError as e:
                self.fail(f"{template} has invalid YAML: {e}")
    
    def test_template_has_elicitation(self):
        """Templates should have elicitation points"""
        for template in self.required_templates:
            template_path = os.path.join(self.template_dir, template)
            with open(template_path, 'r') as f:
                template_data = yaml.safe_load(f)
            
            # Check for at least one elicitation point
            has_elicit = self._check_elicit(template_data['sections'])
            self.assertTrue(has_elicit,
                           f"{template} has no elicitation points")
    
    def _check_elicit(self, sections):
        """Recursively check for elicit: true"""
        for section in sections:
            if section.get('elicit', False):
                return True
            if 'sections' in section:
                if self._check_elicit(section['sections']):
                    return True
        return False

class TestWorkflowIntegration(unittest.TestCase):
    """Test workflow integration"""
    
    def setUp(self):
        self.workflow_dir = '.bmad-core/workflows'
        self.new_workflow = 'complex-problem-solving.yaml'
    
    def test_new_workflow_exists(self):
        """Complex problem-solving workflow should exist"""
        workflow_path = os.path.join(self.workflow_dir, self.new_workflow)
        self.assertTrue(os.path.exists(workflow_path),
                       f"Workflow not found: {self.new_workflow}")
    
    def test_workflow_sequence_valid(self):
        """Workflow sequence should have valid dependencies"""
        workflow_path = os.path.join(self.workflow_dir, self.new_workflow)
        with open(workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)
        
        sequence = workflow['workflow']['sequence']
        created_artifacts = []
        
        for step in sequence:
            if isinstance(step, dict) and 'agent' in step:
                # Check dependencies
                requires = step.get('requires', [])
                if isinstance(requires, str):
                    requires = [requires]
                
                for req in requires:
                    if req not in ['all_validations', 'all_documents']:
                        if not step.get('optional', False):
                            self.assertIn(req, created_artifacts,
                                        f"Missing dependency: {req}")
                
                # Add created artifact
                creates = step.get('creates')
                if creates:
                    created_artifacts.append(creates)

if __name__ == '__main__':
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestAgentDefinition))
    suite.addTests(loader.loadTestsFromTestCase(TestCoreTasks))
    suite.addTests(loader.loadTestsFromTestCase(TestTemplates))
    suite.addTests(loader.loadTestsFromTestCase(TestWorkflowIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
```

### AC2: Integration Test Suite
**File**: `.bmad-core/tests/test_problem_solver_integration.sh`

```bash
#!/bin/bash
# Integration tests for Problem-Solver agent

set -e  # Exit on error

echo "=== Problem-Solver Integration Tests ==="
echo

# Test 1: Agent Loading
echo "Test 1: Agent Loading..."
if grep -q "problem-solver" .bmad-core/agent-teams/team-all.yaml; then
    echo "✅ Problem-solver in team-all"
else
    echo "❌ Problem-solver not in team-all"
    exit 1
fi

# Test 2: Task Execution Simulation
echo "Test 2: Task Execution..."
for task in first-principles-analysis root-cause-investigation problem-decomposition; do
    if [ -f ".bmad-core/tasks/${task}.md" ]; then
        echo "✅ Task exists: $task"
        
        # Check for execution notice
        if grep -q "CRITICAL EXECUTION NOTICE" ".bmad-core/tasks/${task}.md"; then
            echo "  ✓ Has execution notice"
        else
            echo "  ✗ Missing execution notice"
            exit 1
        fi
    else
        echo "❌ Task missing: $task"
        exit 1
    fi
done

# Test 3: Template Processing
echo "Test 3: Template Processing..."
python3 << 'EOF'
import yaml
import sys

templates = [
    'problem-definition-tmpl.yaml',
    'solution-matrix-tmpl.yaml',
    'decision-record-tmpl.yaml'
]

for template_name in templates:
    path = f'.bmad-core/templates/{template_name}'
    try:
        with open(path, 'r') as f:
            template = yaml.safe_load(f)
        
        # Check basic structure
        if 'template' in template and 'sections' in template:
            print(f"✅ {template_name}: Valid structure")
        else:
            print(f"❌ {template_name}: Invalid structure")
            sys.exit(1)
    except Exception as e:
        print(f"❌ {template_name}: {e}")
        sys.exit(1)
EOF

# Test 4: Workflow Dependencies
echo "Test 4: Workflow Dependencies..."
python3 << 'EOF'
import yaml

workflow_file = '.bmad-core/workflows/complex-problem-solving.yaml'
try:
    with open(workflow_file, 'r') as f:
        workflow = yaml.safe_load(f)
    
    # Verify problem-solver is primary agent
    sequence = workflow['workflow']['sequence']
    ps_count = sum(1 for s in sequence 
                   if isinstance(s, dict) and s.get('agent') == 'problem-solver')
    
    if ps_count >= 4:
        print(f"✅ Problem-solver appears {ps_count} times in workflow")
    else:
        print(f"❌ Problem-solver only appears {ps_count} times")
        exit(1)
except Exception as e:
    print(f"❌ Workflow error: {e}")
    exit(1)
EOF

echo
echo "=== All Integration Tests Passed ==="
```

### AC3: End-to-End Test
**File**: `.bmad-core/tests/test_e2e_problem_solving.py`

```python
#!/usr/bin/env python3
"""
End-to-end test simulating complete problem-solving workflow
"""

import os
import yaml
import json
from datetime import datetime

class WorkflowSimulator:
    """Simulate complete workflow execution"""
    
    def __init__(self):
        self.artifacts = {}
        self.current_agent = None
        self.log = []
    
    def load_workflow(self, workflow_file):
        """Load workflow definition"""
        with open(workflow_file, 'r') as f:
            self.workflow = yaml.safe_load(f)
        return self.workflow['workflow']['name']
    
    def execute_step(self, step):
        """Execute a workflow step"""
        if not isinstance(step, dict) or 'agent' not in step:
            return True
        
        agent = step['agent']
        creates = step.get('creates', 'output')
        task = step.get('task', 'default')
        
        # Log step
        self.log.append({
            'timestamp': datetime.now().isoformat(),
            'agent': agent,
            'task': task,
            'creates': creates
        })
        
        # Simulate agent transformation
        self.current_agent = agent
        print(f"\n[{agent}] Executing: {task}")
        
        # Check dependencies
        requires = step.get('requires', [])
        if isinstance(requires, str):
            requires = [requires]
        
        for req in requires:
            if req not in self.artifacts and req not in ['all_validations', 'all_documents']:
                if not step.get('optional', False):
                    print(f"  ❌ Missing required: {req}")
                    return False
        
        # Simulate task execution
        if agent == 'problem-solver':
            output = self.simulate_problem_solver_task(task)
        else:
            output = self.simulate_other_agent(agent, task)
        
        # Store artifact
        self.artifacts[creates] = output
        print(f"  ✅ Created: {creates}")
        
        return True
    
    def simulate_problem_solver_task(self, task):
        """Simulate problem-solver task execution"""
        task_outputs = {
            'create-problem-def': {
                'problem': 'System performance degradation',
                'stakeholders': ['users', 'ops', 'business'],
                'constraints': ['budget: $50k', 'time: 2 months'],
                'success_metrics': ['response time < 200ms', 'uptime > 99.9%']
            },
            'investigate-root-cause': {
                'method': '5-whys',
                'root_causes': [
                    {'cause': 'Database query inefficiency', 'confidence': 0.85},
                    {'cause': 'Memory leaks in service', 'confidence': 0.65}
                ]
            },
            'generate-solutions': {
                'solutions': [
                    {'id': 'SOL-001', 'approach': 'Query optimization', 'score': 8.5},
                    {'id': 'SOL-002', 'approach': 'Caching layer', 'score': 7.8},
                    {'id': 'SOL-003', 'approach': 'Service rewrite', 'score': 6.2}
                ]
            },
            'create-solution-matrix': {
                'recommended': 'SOL-001',
                'rationale': 'Highest ROI with minimal risk'
            }
        }
        return task_outputs.get(task, {'status': 'completed'})
    
    def simulate_other_agent(self, agent, task):
        """Simulate other agent tasks"""
        return {
            'agent': agent,
            'task': task,
            'status': 'completed',
            'timestamp': datetime.now().isoformat()
        }
    
    def run_workflow(self):
        """Execute complete workflow"""
        print(f"Starting workflow: {self.workflow['workflow']['name']}")
        print("=" * 60)
        
        sequence = self.workflow['workflow']['sequence']
        
        for i, step in enumerate(sequence, 1):
            if isinstance(step, dict) and 'agent' in step:
                print(f"\nStep {i}/{len(sequence)}")
                if not self.execute_step(step):
                    print("\n❌ Workflow failed")
                    return False
        
        print("\n" + "=" * 60)
        print("✅ Workflow completed successfully")
        print(f"Created artifacts: {list(self.artifacts.keys())}")
        return True
    
    def save_execution_log(self, filepath):
        """Save execution log for analysis"""
        with open(filepath, 'w') as f:
            json.dump({
                'workflow': self.workflow['workflow']['id'],
                'execution_time': datetime.now().isoformat(),
                'steps': self.log,
                'artifacts': list(self.artifacts.keys()),
                'success': True
            }, f, indent=2)

def main():
    """Run end-to-end test"""
    simulator = WorkflowSimulator()
    
    # Test complex problem-solving workflow
    workflow_file = '.bmad-core/workflows/complex-problem-solving.yaml'
    
    if not os.path.exists(workflow_file):
        print(f"❌ Workflow file not found: {workflow_file}")
        return False
    
    workflow_name = simulator.load_workflow(workflow_file)
    success = simulator.run_workflow()
    
    if success:
        # Save execution log
        log_file = 'test_execution_log.json'
        simulator.save_execution_log(log_file)
        print(f"\nExecution log saved to: {log_file}")
    
    return success

if __name__ == '__main__':
    import sys
    sys.exit(0 if main() else 1)
```

### AC4: Regression Test Suite
**File**: `.bmad-core/tests/test_regression.sh`

```bash
#!/bin/bash
# Regression tests to ensure existing functionality preserved

echo "=== Regression Test Suite ==="

# Test existing agents still work
echo "Testing existing agents..."
for agent in analyst pm architect po dev sm qa ux-expert; do
    if grep -q "id: $agent" .bmad-core/agents/${agent}.md 2>/dev/null; then
        echo "✅ $agent agent intact"
    else
        echo "⚠️  $agent agent may be affected"
    fi
done

# Test existing workflows unchanged
echo "Testing existing workflows..."
for workflow in greenfield-fullstack brownfield-fullstack; do
    if [ -f ".bmad-core/workflows/${workflow}.yaml" ]; then
        # Check if core structure intact
        if grep -q "sequence:" ".bmad-core/workflows/${workflow}.yaml"; then
            echo "✅ $workflow structure intact"
        else
            echo "❌ $workflow structure damaged"
            exit 1
        fi
    fi
done

# Test orchestrator still functions
echo "Testing orchestrator..."
if grep -q "available-agents:" .bmad-core/agents/bmad-orchestrator.md; then
    echo "✅ Orchestrator configuration intact"
else
    echo "❌ Orchestrator configuration damaged"
    exit 1
fi

echo
echo "=== Regression Tests Passed ==="
```

### AC5: Performance Test
**File**: `.bmad-core/tests/test_performance.py`

```python
#!/usr/bin/env python3
"""
Performance tests for problem-solver integration
"""

import time
import yaml
import os
from statistics import mean, stdev

def measure_file_load_time(filepath, iterations=10):
    """Measure file loading performance"""
    times = []
    
    for _ in range(iterations):
        start = time.perf_counter()
        with open(filepath, 'r') as f:
            content = f.read()
            if filepath.endswith('.yaml'):
                yaml.safe_load(content)
        end = time.perf_counter()
        times.append(end - start)
    
    return {
        'mean': mean(times),
        'stdev': stdev(times) if len(times) > 1 else 0,
        'max': max(times),
        'min': min(times)
    }

def test_agent_load_performance():
    """Test agent file loading performance"""
    print("Testing agent load performance...")
    
    agent_file = '.bmad-core/agents/problem-solver.md'
    if not os.path.exists(agent_file):
        print(f"❌ Agent file not found: {agent_file}")
        return False
    
    stats = measure_file_load_time(agent_file)
    
    # Performance criteria: Load in < 100ms average
    if stats['mean'] < 0.1:
        print(f"✅ Agent loads in {stats['mean']*1000:.2f}ms average")
        return True
    else:
        print(f"❌ Agent load too slow: {stats['mean']*1000:.2f}ms")
        return False

def test_workflow_parsing_performance():
    """Test workflow parsing performance"""
    print("Testing workflow parsing performance...")
    
    workflow_file = '.bmad-core/workflows/complex-problem-solving.yaml'
    if not os.path.exists(workflow_file):
        print(f"❌ Workflow file not found: {workflow_file}")
        return False
    
    stats = measure_file_load_time(workflow_file)
    
    # Performance criteria: Parse in < 50ms average
    if stats['mean'] < 0.05:
        print(f"✅ Workflow parses in {stats['mean']*1000:.2f}ms average")
        return True
    else:
        print(f"❌ Workflow parsing too slow: {stats['mean']*1000:.2f}ms")
        return False

def test_template_processing_performance():
    """Test template processing performance"""
    print("Testing template processing performance...")
    
    templates = [
        'problem-definition-tmpl.yaml',
        'solution-matrix-tmpl.yaml',
        'decision-record-tmpl.yaml'
    ]
    
    total_time = 0
    for template in templates:
        template_path = f'.bmad-core/templates/{template}'
        if os.path.exists(template_path):
            stats = measure_file_load_time(template_path, iterations=5)
            total_time += stats['mean']
            print(f"  {template}: {stats['mean']*1000:.2f}ms")
    
    # All templates should load in < 200ms total
    if total_time < 0.2:
        print(f"✅ All templates load in {total_time*1000:.2f}ms total")
        return True
    else:
        print(f"❌ Template loading too slow: {total_time*1000:.2f}ms")
        return False

def main():
    """Run all performance tests"""
    print("=== Performance Test Suite ===\n")
    
    tests = [
        test_agent_load_performance,
        test_workflow_parsing_performance,
        test_template_processing_performance
    ]
    
    results = []
    for test in tests:
        results.append(test())
        print()
    
    if all(results):
        print("=== All Performance Tests Passed ===")
        return True
    else:
        print("=== Some Performance Tests Failed ===")
        return False

if __name__ == '__main__':
    import sys
    sys.exit(0 if main() else 1)
```

## Implementation Tasks

### Task 1: Create Test Directory
```bash
#!/bin/bash
# setup_tests.sh

# Create test directory
mkdir -p .bmad-core/tests

# Create test files
touch .bmad-core/tests/test_problem_solver_unit.py
touch .bmad-core/tests/test_problem_solver_integration.sh
touch .bmad-core/tests/test_e2e_problem_solving.py
touch .bmad-core/tests/test_regression.sh
touch .bmad-core/tests/test_performance.py

# Make shell scripts executable
chmod +x .bmad-core/tests/*.sh

echo "✅ Test directory and files created"
```

### Task 2: Run Test Suite
```bash
#!/bin/bash
# run_all_tests.sh

echo "=== BMad Problem-Solver Test Suite ==="
echo

# Unit tests
echo "Running unit tests..."
python3 .bmad-core/tests/test_problem_solver_unit.py
UNIT_RESULT=$?

# Integration tests
echo -e "\nRunning integration tests..."
bash .bmad-core/tests/test_problem_solver_integration.sh
INTEGRATION_RESULT=$?

# E2E tests
echo -e "\nRunning end-to-end tests..."
python3 .bmad-core/tests/test_e2e_problem_solving.py
E2E_RESULT=$?

# Regression tests
echo -e "\nRunning regression tests..."
bash .bmad-core/tests/test_regression.sh
REGRESSION_RESULT=$?

# Performance tests
echo -e "\nRunning performance tests..."
python3 .bmad-core/tests/test_performance.py
PERFORMANCE_RESULT=$?

# Summary
echo -e "\n=== Test Results Summary ==="
[ $UNIT_RESULT -eq 0 ] && echo "✅ Unit tests: PASSED" || echo "❌ Unit tests: FAILED"
[ $INTEGRATION_RESULT -eq 0 ] && echo "✅ Integration tests: PASSED" || echo "❌ Integration tests: FAILED"
[ $E2E_RESULT -eq 0 ] && echo "✅ E2E tests: PASSED" || echo "❌ E2E tests: FAILED"
[ $REGRESSION_RESULT -eq 0 ] && echo "✅ Regression tests: PASSED" || echo "❌ Regression tests: FAILED"
[ $PERFORMANCE_RESULT -eq 0 ] && echo "✅ Performance tests: PASSED" || echo "❌ Performance tests: FAILED"

# Exit with failure if any test failed
if [ $UNIT_RESULT -ne 0 ] || [ $INTEGRATION_RESULT -ne 0 ] || \
   [ $E2E_RESULT -ne 0 ] || [ $REGRESSION_RESULT -ne 0 ] || \
   [ $PERFORMANCE_RESULT -ne 0 ]; then
    exit 1
fi

echo -e "\n🎉 All tests passed successfully!"
```

## Testing Checklist

### Test Coverage
- [ ] Agent definition validated
- [ ] All tasks tested
- [ ] All templates tested
- [ ] Workflow execution validated
- [ ] Integration points tested
- [ ] Performance benchmarks met

### Test Types
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] E2E tests passing
- [ ] Regression tests passing
- [ ] Performance tests passing

## Definition of Done
- [ ] All test files created
- [ ] Test suite executable
- [ ] All tests passing
- [ ] Performance criteria met
- [ ] No regression in existing functionality
- [ ] Test documentation complete

## File List
```
Created:
- .bmad-core/tests/
- .bmad-core/tests/test_problem_solver_unit.py
- .bmad-core/tests/test_problem_solver_integration.sh
- .bmad-core/tests/test_e2e_problem_solving.py
- .bmad-core/tests/test_regression.sh
- .bmad-core/tests/test_performance.py
- .bmad-core/tests/run_all_tests.sh
```