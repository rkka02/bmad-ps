#!/usr/bin/env python3
"""Quick validation test for problem-solver integration"""

import yaml
import os

def quick_test():
    print("=== Quick Problem-Solver Validation ===\n")
    
    # Test 1: Agent file exists and has basic structure
    agent_file = '.bmad-core/agents/problem-solver.md'
    if os.path.exists(agent_file):
        print("✅ Agent file exists")
        with open(agent_file, 'r') as f:
            content = f.read()
        if 'problem-solver' in content and 'Sage' in content:
            print("✅ Agent identity correct")
        else:
            print("❌ Agent identity issues")
    else:
        print("❌ Agent file missing")
        return False
    
    # Test 2: Core tasks exist
    tasks = [
        'first-principles-analysis.md',
        'root-cause-investigation.md',
        'problem-decomposition.md',
        'solution-synthesis.md',
        'decision-analysis.md'
    ]
    
    missing_tasks = []
    for task in tasks:
        task_path = f'.bmad-core/tasks/{task}'
        if os.path.exists(task_path):
            print(f"✅ Task exists: {task}")
        else:
            missing_tasks.append(task)
            print(f"❌ Task missing: {task}")
    
    # Test 3: Templates exist and are valid YAML
    templates = [
        'problem-definition-tmpl.yaml',
        'solution-matrix-tmpl.yaml', 
        'decision-record-tmpl.yaml'
    ]
    
    for template in templates:
        template_path = f'.bmad-core/templates/{template}'
        if os.path.exists(template_path):
            try:
                with open(template_path, 'r') as f:
                    yaml.safe_load(f)
                print(f"✅ Template valid: {template}")
            except Exception as e:
                print(f"❌ Template invalid: {template} - {e}")
        else:
            print(f"❌ Template missing: {template}")
    
    # Test 4: Workflow exists
    workflow_path = '.bmad-core/workflows/complex-problem-solving.yaml'
    if os.path.exists(workflow_path):
        try:
            with open(workflow_path, 'r') as f:
                yaml.safe_load(f)
            print("✅ Workflow exists and valid")
        except Exception as e:
            print(f"❌ Workflow invalid: {e}")
    else:
        print("❌ Workflow missing")
    
    # Test 5: Install manifest updated
    manifest_path = '.bmad-core/install-manifest.yaml'
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            manifest = yaml.safe_load(f)
        
        files = {entry['path']: entry for entry in manifest.get('files', [])}
        
        if '.bmad-core/agents/problem-solver.md' in files:
            print("✅ Install manifest updated")
        else:
            print("❌ Install manifest not updated")
    
    print("\n🚀 Quick validation complete!")
    return True

if __name__ == '__main__':
    quick_test()