#!/usr/bin/env python3
"""
Test problem-solver integration with BMad system
"""

import yaml
import os

def test_agent_in_teams():
    """Test that problem-solver is included in team configurations"""
    print("=== Testing Agent Team Integration ===\n")
    
    teams_to_check = [
        'team-fullstack.yaml',
        'team-no-ui.yaml'
    ]
    
    for team_file in teams_to_check:
        path = f'.bmad-core/agent-teams/{team_file}'
        try:
            with open(path, 'r') as f:
                team_config = yaml.safe_load(f)
            
            agents = team_config.get('agents', [])
            
            if 'problem-solver' in agents:
                print(f"✅ {team_file}: problem-solver included")
            elif '*' in agents:
                print(f"✅ {team_file}: uses wildcard (includes all agents)")
            else:
                print(f"❌ {team_file}: problem-solver NOT found")
                return False
                
        except Exception as e:
            print(f"❌ {team_file}: Error reading file - {e}")
            return False
    
    return True

def test_install_manifest():
    """Test that all problem-solver files are in install manifest"""
    print("\n=== Testing Install Manifest ===\n")
    
    try:
        with open('.bmad-core/install-manifest.yaml', 'r') as f:
            manifest = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error reading install-manifest.yaml: {e}")
        return False
    
    # Check version updated
    version = manifest.get('version', '')
    if 'problem-solver' in version:
        print(f"✅ Version updated: {version}")
    else:
        print(f"⚠️  Version may not be updated: {version}")
    
    # Check files are included
    files = {entry['path']: entry for entry in manifest.get('files', [])}
    
    required_files = [
        '.bmad-core/agents/problem-solver.md',
        '.bmad-core/tasks/first-principles-analysis.md',
        '.bmad-core/tasks/root-cause-investigation.md',
        '.bmad-core/tasks/problem-decomposition.md',
        '.bmad-core/tasks/solution-synthesis.md',
        '.bmad-core/tasks/decision-analysis.md',
        '.bmad-core/templates/problem-definition-tmpl.yaml',
        '.bmad-core/templates/solution-matrix-tmpl.yaml',
        '.bmad-core/templates/decision-record-tmpl.yaml'
    ]
    
    missing_files = []
    for file_path in required_files:
        if file_path in files:
            entry = files[file_path]
            print(f"✅ {file_path} (hash: {entry['hash']})")
        else:
            missing_files.append(file_path)
            print(f"❌ {file_path}: NOT FOUND in manifest")
    
    if missing_files:
        return False
    
    return True

def test_file_existence():
    """Test that all files actually exist on disk"""
    print("\n=== Testing File Existence ===\n")
    
    all_files = [
        '.bmad-core/agents/problem-solver.md',
        '.bmad-core/tasks/first-principles-analysis.md',
        '.bmad-core/tasks/root-cause-investigation.md',
        '.bmad-core/tasks/problem-decomposition.md', 
        '.bmad-core/tasks/solution-synthesis.md',
        '.bmad-core/tasks/decision-analysis.md',
        '.bmad-core/templates/problem-definition-tmpl.yaml',
        '.bmad-core/templates/solution-matrix-tmpl.yaml',
        '.bmad-core/templates/decision-record-tmpl.yaml'
    ]
    
    missing_files = []
    for file_path in all_files:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"✅ {file_path} ({size:,} bytes)")
        else:
            missing_files.append(file_path)
            print(f"❌ {file_path}: FILE NOT FOUND")
    
    if missing_files:
        return False
        
    return True

def test_agent_structure():
    """Test that the agent file has correct structure"""
    print("\n=== Testing Agent Structure ===\n")
    
    agent_file = '.bmad-core/agents/problem-solver.md'
    
    try:
        with open(agent_file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading agent file: {e}")
        return False
    
    # Check for required content
    required_content = [
        'ACTIVATION-NOTICE',
        'problem-solver',
        'Sage',
        'Problem-Solving Specialist',
        'first-principles-analysis',
        'root-cause-investigation',
        'decision-analysis',
        'TRIZ',
        'MECE'
    ]
    
    missing_content = []
    for item in required_content:
        if item in content:
            print(f"✅ Contains: {item}")
        else:
            missing_content.append(item)
            print(f"❌ Missing: {item}")
    
    if missing_content:
        return False
    
    return True

def main():
    """Run all integration tests"""
    print("=== BMad Problem-Solver Integration Test ===\n")
    
    tests = [
        ("Agent Team Configuration", test_agent_in_teams),
        ("Install Manifest", test_install_manifest),
        ("File Existence", test_file_existence),
        ("Agent Structure", test_agent_structure)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print(f"\n=== Test Results Summary ===\n")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL INTEGRATION TESTS PASSED!")
        print("🚀 Problem-Solver is ready for use!")
        return 0
    else:
        print("💥 Some tests failed - check logs above")
        return 1

if __name__ == '__main__':
    import sys
    sys.exit(main())