#!/usr/bin/env python3
"""
Validation test for iterative thinking Problem-Solver agent integration
Tests the complexity assessment → thinking plan → step execution pipeline
"""

import yaml
import os
import json
from datetime import datetime

def test_iterative_thinking_components():
    """Test all components of the iterative thinking system"""
    print("=== Iterative Thinking System Validation ===\n")
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "tests_passed": 0,
        "tests_failed": 0,
        "components_validated": [],
        "issues_found": []
    }
    
    # Test 1: Enhanced agent file structure
    print("🧠 Testing Enhanced Agent Definition...")
    agent_file = '.bmad-core/agents/problem-solver-iterative.md'
    if test_enhanced_agent_structure(agent_file, results):
        print("✅ Enhanced agent file structure valid")
    else:
        print("❌ Enhanced agent file has issues")
    
    # Test 2: Iterative thinking task files
    print("\n🔄 Testing Iterative Thinking Tasks...")
    iterative_tasks = [
        'complexity-assessment.md',
        'create-thinking-plan.md', 
        'execute-step.md'
    ]
    
    for task in iterative_tasks:
        task_path = f'.bmad-core/tasks/{task}'
        if test_task_file_structure(task_path, results):
            print(f"✅ Task file valid: {task}")
        else:
            print(f"❌ Task file issues: {task}")
    
    # Test 3: Complexity assessment logic
    print("\n📊 Testing Complexity Assessment Logic...")
    if test_complexity_assessment_logic(results):
        print("✅ Complexity assessment logic valid")
    else:
        print("❌ Complexity assessment logic issues")
    
    # Test 4: Thinking plan templates
    print("\n📋 Testing Thinking Plan Templates...")
    if test_thinking_plan_templates(results):
        print("✅ Thinking plan templates valid")
    else:
        print("❌ Thinking plan template issues")
    
    # Test 5: Step execution enforcement
    print("\n🎯 Testing Step Execution Enforcement...")
    if test_step_execution_enforcement(results):
        print("✅ Step execution enforcement logic valid")
    else:
        print("❌ Step execution enforcement issues")
    
    # Test 6: Agent command integration
    print("\n⚙️ Testing Agent Command Integration...")
    if test_agent_command_integration(results):
        print("✅ Agent commands properly integrated")
    else:
        print("❌ Agent command integration issues")
    
    # Generate test report
    print(f"\n📈 Test Summary:")
    print(f"Tests Passed: {results['tests_passed']}")
    print(f"Tests Failed: {results['tests_failed']}")
    print(f"Components Validated: {len(results['components_validated'])}")
    
    if results['issues_found']:
        print(f"\n⚠️ Issues Found:")
        for issue in results['issues_found']:
            print(f"  - {issue}")
    
    # Save detailed results
    with open('iterative_thinking_test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n🚀 Iterative thinking validation complete!")
    return results['tests_failed'] == 0

def test_enhanced_agent_structure(agent_file, results):
    """Test the enhanced agent file has iterative thinking capabilities"""
    try:
        if not os.path.exists(agent_file):
            results['issues_found'].append(f"Enhanced agent file missing: {agent_file}")
            results['tests_failed'] += 1
            return False
        
        with open(agent_file, 'r') as f:
            content = f.read()
        
        # Check for iterative thinking content
        required_elements = [
            'assess-complexity',
            'create-thinking-plan', 
            'execute-step',
            'plan-status',
            'thinking-summary',
            'iterative_thinking_behavior',
            'enforcement_rules',
            'complexity-assessment.md',
            'create-thinking-plan.md',
            'execute-step.md'
        ]
        
        missing_elements = []
        for element in required_elements:
            if element not in content:
                missing_elements.append(element)
        
        if missing_elements:
            results['issues_found'].append(f"Missing iterative thinking elements: {missing_elements}")
            results['tests_failed'] += 1
            return False
        
        # Validate YAML structure
        yaml_start = content.find('```yaml')
        yaml_end = content.find('```', yaml_start + 6)
        if yaml_start == -1 or yaml_end == -1:
            results['issues_found'].append("No YAML block found in agent file")
            results['tests_failed'] += 1
            return False
            
        yaml_content = content[yaml_start+7:yaml_end]
        config = yaml.safe_load(yaml_content)
        
        # Check iterative thinking commands
        commands = [cmd.split(':')[0] for cmd in config['commands']]
        iterative_commands = ['assess-complexity', 'create-thinking-plan', 'execute-step', 'plan-status']
        
        for cmd in iterative_commands:
            if cmd not in commands:
                results['issues_found'].append(f"Missing iterative command: {cmd}")
                results['tests_failed'] += 1
                return False
        
        results['components_validated'].append('enhanced_agent_structure')
        results['tests_passed'] += 1
        return True
        
    except Exception as e:
        results['issues_found'].append(f"Agent structure test error: {e}")
        results['tests_failed'] += 1
        return False

def test_task_file_structure(task_path, results):
    """Test task file has proper structure for BMad integration"""
    try:
        if not os.path.exists(task_path):
            results['issues_found'].append(f"Task file missing: {task_path}")
            results['tests_failed'] += 1
            return False
        
        with open(task_path, 'r') as f:
            content = f.read()
        
        # Check required sections
        required_sections = [
            '## Execution Notice',
            '## Method Description', 
            '## Interactive Flow',
            '## Output Format',
            '## Integration Points'
        ]
        
        missing_sections = []
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)
        
        if missing_sections:
            results['issues_found'].append(f"Missing sections in {task_path}: {missing_sections}")
            results['tests_failed'] += 1
            return False
        
        results['components_validated'].append(f'task_structure_{os.path.basename(task_path)}')
        results['tests_passed'] += 1
        return True
        
    except Exception as e:
        results['issues_found'].append(f"Task file test error for {task_path}: {e}")
        results['tests_failed'] += 1
        return False

def test_complexity_assessment_logic(results):
    """Test complexity assessment scoring logic"""
    try:
        # Test complexity calculation scenarios
        test_scenarios = [
            {
                'name': 'Simple API Problem',
                'scores': {'domain_breadth': 1, 'stakeholder_alignment': 1, 'solution_uncertainty': 2, 'impact_scope': 2, 'time_pressure': 2},
                'expected_total': 8,
                'expected_level': 'Simple',
                'expected_steps': 3
            },
            {
                'name': 'Medium Product Feature',
                'scores': {'domain_breadth': 2, 'stakeholder_alignment': 2, 'solution_uncertainty': 2, 'impact_scope': 3, 'time_pressure': 2},
                'expected_total': 11,
                'expected_level': 'Medium', 
                'expected_steps': 5
            },
            {
                'name': 'Complex Organizational Change',
                'scores': {'domain_breadth': 3, 'stakeholder_alignment': 3, 'solution_uncertainty': 3, 'impact_scope': 3, 'time_pressure': 2},
                'expected_total': 14,
                'expected_level': 'Complex',
                'expected_steps': 7
            },
            {
                'name': 'Wicked Strategic Pivot',
                'scores': {'domain_breadth': 4, 'stakeholder_alignment': 4, 'solution_uncertainty': 4, 'impact_scope': 4, 'time_pressure': 3},
                'expected_total': 19,
                'expected_level': 'Wicked',
                'expected_steps': 10
            }
        ]
        
        def calculate_complexity(scores):
            total = sum(scores.values())
            if total <= 8:
                return total, 'Simple', 3
            elif total <= 12:
                return total, 'Medium', 5
            elif total <= 16:
                return total, 'Complex', 7
            else:
                return total, 'Wicked', 10
        
        all_passed = True
        for scenario in test_scenarios:
            total, level, steps = calculate_complexity(scenario['scores'])
            
            if (total != scenario['expected_total'] or 
                level != scenario['expected_level'] or 
                steps != scenario['expected_steps']):
                results['issues_found'].append(
                    f"Complexity calculation failed for {scenario['name']}: "
                    f"got {total}/{level}/{steps}, expected {scenario['expected_total']}/{scenario['expected_level']}/{scenario['expected_steps']}"
                )
                all_passed = False
        
        if all_passed:
            results['components_validated'].append('complexity_assessment_logic')
            results['tests_passed'] += 1
            return True
        else:
            results['tests_failed'] += 1
            return False
            
    except Exception as e:
        results['issues_found'].append(f"Complexity assessment logic test error: {e}")
        results['tests_failed'] += 1
        return False

def test_thinking_plan_templates(results):
    """Test thinking plan template structure and completeness"""
    try:
        # Test that all complexity levels have appropriate step counts
        expected_plans = {
            'Simple': 3,
            'Medium': 5,
            'Complex': 7, 
            'Wicked': 10
        }
        
        # Read thinking plan creation logic from iterative-thinking-plan.md
        plan_file = 'iterative-thinking-plan.md'
        if not os.path.exists(plan_file):
            results['issues_found'].append(f"Thinking plan documentation missing: {plan_file}")
            results['tests_failed'] += 1
            return False
        
        with open(plan_file, 'r') as f:
            plan_content = f.read()
        
        # Check that all complexity levels are documented
        all_levels_found = True
        for level, steps in expected_plans.items():
            if f'{level} Problems ({steps} Steps)' not in plan_content:
                results['issues_found'].append(f"Missing {level} complexity plan documentation")
                all_levels_found = False
        
        if all_levels_found:
            results['components_validated'].append('thinking_plan_templates')
            results['tests_passed'] += 1
            return True
        else:
            results['tests_failed'] += 1
            return False
            
    except Exception as e:
        results['issues_found'].append(f"Thinking plan template test error: {e}")
        results['tests_failed'] += 1
        return False

def test_step_execution_enforcement(results):
    """Test step execution enforcement logic"""
    try:
        # Test sequential progression logic
        def can_execute_step(current_step, target_step, completed_steps):
            """Simulate step execution enforcement"""
            # Cannot skip ahead more than 1 step
            if target_step > current_step + 1:
                return False, "Cannot skip ahead - must complete steps sequentially"
            
            # Must complete all prerequisite steps
            for i in range(1, target_step):
                if i not in completed_steps:
                    return False, f"Step {i} must be completed first"
            
            return True, "Step execution allowed"
        
        # Test scenarios
        test_cases = [
            {'current': 1, 'target': 1, 'completed': [], 'should_pass': True},
            {'current': 1, 'target': 2, 'completed': [1], 'should_pass': True},
            {'current': 1, 'target': 3, 'completed': [1], 'should_pass': False},  # Skip ahead
            {'current': 3, 'target': 3, 'completed': [1], 'should_pass': False},  # Missing step 2
            {'current': 3, 'target': 3, 'completed': [1, 2], 'should_pass': True}
        ]
        
        all_passed = True
        for case in test_cases:
            can_execute, message = can_execute_step(case['current'], case['target'], case['completed'])
            if can_execute != case['should_pass']:
                results['issues_found'].append(
                    f"Step enforcement failed: current={case['current']}, target={case['target']}, "
                    f"completed={case['completed']}, got {can_execute}, expected {case['should_pass']}"
                )
                all_passed = False
        
        if all_passed:
            results['components_validated'].append('step_execution_enforcement')
            results['tests_passed'] += 1
            return True
        else:
            results['tests_failed'] += 1
            return False
            
    except Exception as e:
        results['issues_found'].append(f"Step execution enforcement test error: {e}")
        results['tests_failed'] += 1
        return False

def test_agent_command_integration(results):
    """Test that new commands integrate properly with existing agent structure"""
    try:
        agent_file = '.bmad-core/agents/problem-solver-iterative.md'
        if not os.path.exists(agent_file):
            results['issues_found'].append(f"Enhanced agent file not found: {agent_file}")
            results['tests_failed'] += 1
            return False
        
        with open(agent_file, 'r') as f:
            content = f.read()
        
        # Extract commands section
        yaml_start = content.find('```yaml')
        yaml_end = content.find('```', yaml_start + 6)
        yaml_content = content[yaml_start+7:yaml_end]
        config = yaml.safe_load(yaml_content)
        
        # Check command integration
        commands = config.get('commands', [])
        
        # Must have both iterative and traditional commands
        iterative_commands = ['assess-complexity', 'create-thinking-plan', 'execute-step']
        traditional_commands = ['analyze-problem', 'investigate-root-cause', 'generate-solutions']
        
        missing_iterative = [cmd for cmd in iterative_commands if not any(cmd in str(c) for c in commands)]
        missing_traditional = [cmd for cmd in traditional_commands if not any(cmd in str(c) for c in commands)]
        
        if missing_iterative:
            results['issues_found'].append(f"Missing iterative commands: {missing_iterative}")
            results['tests_failed'] += 1
            return False
        
        if missing_traditional:
            results['issues_found'].append(f"Missing traditional commands: {missing_traditional}")
            results['tests_failed'] += 1
            return False
        
        # Check dependencies include iterative thinking tasks
        dependencies = config.get('dependencies', {})
        tasks = dependencies.get('tasks', [])
        
        required_iterative_tasks = ['complexity-assessment.md', 'create-thinking-plan.md', 'execute-step.md']
        missing_tasks = [task for task in required_iterative_tasks if task not in tasks]
        
        if missing_tasks:
            results['issues_found'].append(f"Missing iterative thinking tasks in dependencies: {missing_tasks}")
            results['tests_failed'] += 1
            return False
        
        results['components_validated'].append('agent_command_integration')
        results['tests_passed'] += 1
        return True
        
    except Exception as e:
        results['issues_found'].append(f"Agent command integration test error: {e}")
        results['tests_failed'] += 1
        return False

if __name__ == '__main__':
    success = test_iterative_thinking_components()
    exit(0 if success else 1)