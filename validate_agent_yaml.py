#!/usr/bin/env python3
"""
Validate problem-solver agent YAML structure and requirements
"""

import yaml
import sys
import re
import os

def validate_agent_file(filepath):
    """Validate agent file structure and content"""
    print(f"Validating agent file: {filepath}")
    
    if not os.path.exists(filepath):
        print(f"❌ Agent file not found: {filepath}")
        return False
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Extract YAML block
    yaml_start = content.find('```yaml')
    yaml_end = content.find('```', yaml_start + 6)
    
    if yaml_start == -1 or yaml_end == -1:
        print("❌ No YAML block found in agent file")
        return False
        
    yaml_content = content[yaml_start+7:yaml_end]
    
    try:
        config = yaml.safe_load(yaml_content)
        print("✅ YAML syntax is valid")
        
        # Validate required sections
        required_sections = [
            'agent', 'persona', 'commands', 
            'dependencies', 'activation-instructions'
        ]
        
        missing_sections = []
        for section in required_sections:
            if section not in config:
                missing_sections.append(section)
        
        if missing_sections:
            print(f"❌ Missing required sections: {missing_sections}")
            return False
        
        print("✅ All required sections present")
        
        # Validate agent metadata
        agent_meta = config['agent']
        required_agent_fields = ['name', 'id', 'title', 'icon', 'whenToUse']
        
        for field in required_agent_fields:
            if field not in agent_meta:
                print(f"❌ Missing agent field: {field}")
                return False
        
        if agent_meta['id'] != 'problem-solver':
            print(f"❌ Agent ID should be 'problem-solver', got: {agent_meta['id']}")
            return False
            
        if agent_meta['name'] != 'Sage':
            print(f"❌ Agent name should be 'Sage', got: {agent_meta['name']}")
            return False
            
        print("✅ Agent metadata valid")
        
        # Validate persona
        persona = config['persona']
        required_persona_fields = ['role', 'style', 'identity', 'focus', 'core_principles']
        
        for field in required_persona_fields:
            if field not in persona:
                print(f"❌ Missing persona field: {field}")
                return False
        
        # Check core principles count
        principles = persona['core_principles']
        if len(principles) < 5:
            print(f"❌ Need at least 5 core principles, got: {len(principles)}")
            return False
            
        print("✅ Persona configuration valid")
        
        # Validate commands
        commands = config['commands']
        required_commands = [
            'help', 'analyze-problem', 'investigate-root-cause',
            'decompose', 'generate-solutions', 'evaluate-decisions'
        ]
        
        # Extract command names (remove descriptions)
        command_names = []
        for cmd in commands:
            if isinstance(cmd, dict):
                command_names.extend(cmd.keys())
            elif isinstance(cmd, str):
                # Handle "command: description" format
                cmd_name = cmd.split(':')[0].strip()
                command_names.append(cmd_name)
        
        missing_commands = [cmd for cmd in required_commands if cmd not in command_names]
        if missing_commands:
            print(f"❌ Missing required commands: {missing_commands}")
            return False
        
        print("✅ Commands structure valid")
        
        # Validate dependencies
        deps = config['dependencies']
        required_dep_types = ['data', 'tasks', 'templates', 'checklists']
        
        for dep_type in required_dep_types:
            if dep_type not in deps:
                print(f"❌ Missing dependency type: {dep_type}")
                return False
            
            if not isinstance(deps[dep_type], list):
                print(f"❌ Dependency {dep_type} should be a list")
                return False
        
        print("✅ Dependencies structure valid")
        
        # Validate activation instructions
        activation = config['activation-instructions']
        if not isinstance(activation, list):
            print("❌ Activation instructions should be a list")
            return False
            
        if len(activation) < 4:
            print(f"❌ Need at least 4 activation steps, got: {len(activation)}")
            return False
        
        print("✅ Activation instructions valid")
        
        # Check for problem-solver specific content
        content_lower = content.lower()
        required_concepts = [
            'first principles', 'triz', 'systematic', 'root cause',
            'problem-solving', 'mcda', 'mece'
        ]
        
        missing_concepts = []
        for concept in required_concepts:
            if concept not in content_lower:
                missing_concepts.append(concept)
        
        if missing_concepts:
            print(f"⚠️  Missing problem-solving concepts: {missing_concepts}")
        else:
            print("✅ Problem-solving concepts present")
        
        print("\n🎉 Agent YAML validation PASSED!")
        return True
        
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error: {e}")
        return False
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return False

def main():
    """Run validation"""
    agent_file = '.bmad-core/agents/problem-solver.md'
    
    print("=== BMad Problem-Solver Agent Validation ===\n")
    
    success = validate_agent_file(agent_file)
    
    if success:
        print("\n✅ ALL VALIDATIONS PASSED - Agent ready for integration!")
        return 0
    else:
        print("\n❌ VALIDATION FAILED - Please fix issues above")
        return 1

if __name__ == '__main__':
    sys.exit(main())