#!/usr/bin/env python3
"""
Comprehensive Test Suite for BMad Problem-Solver Agent Integration
"""

import unittest
import yaml
import os
import sys
import hashlib
import json
import re
from pathlib import Path
from datetime import datetime

class TestProblemSolverIntegration(unittest.TestCase):
    """Master test class for Problem-Solver integration"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.base_path = Path('.bmad-core')
        cls.test_results = {
            'timestamp': datetime.now().isoformat(),
            'tests_run': [],
            'failures': [],
            'successes': []
        }
        
    def setUp(self):
        """Set up for each test"""
        self.test_name = self._testMethodName
        self.start_time = datetime.now()
        
    def tearDown(self):
        """Clean up after each test"""
        duration = (datetime.now() - self.start_time).total_seconds()
        test_info = {
            'name': self.test_name,
            'duration': duration,
            'status': 'passed'
        }
        self.test_results['tests_run'].append(test_info)
        

class TestAgentDefinition(TestProblemSolverIntegration):
    """Test the Problem-Solver agent definition"""
    
    def test_agent_file_exists(self):
        """Agent file should exist and be readable"""
        agent_file = self.base_path / 'agents' / 'problem-solver.md'
        self.assertTrue(agent_file.exists(), f"Agent file not found: {agent_file}")
        
        with open(agent_file, 'r') as f:
            content = f.read()
            
        self.assertGreater(len(content), 1000, "Agent file seems too small")
        self.assertIn('ACTIVATION-NOTICE', content, "Missing activation notice")
        
    def test_agent_yaml_structure(self):
        """Agent YAML should have all required sections"""
        agent_file = self.base_path / 'agents' / 'problem-solver.md'
        
        with open(agent_file, 'r') as f:
            content = f.read()
        
        # Extract YAML block
        yaml_start = content.find('```yaml')
        yaml_end = content.find('```', yaml_start + 6)
        self.assertNotEqual(yaml_start, -1, "No YAML block found")
        self.assertNotEqual(yaml_end, -1, "YAML block not properly closed")
        
        yaml_content = content[yaml_start+7:yaml_end]
        config = yaml.safe_load(yaml_content)
        
        # Test required sections
        required_sections = [
            'agent', 'persona', 'commands', 
            'dependencies', 'activation-instructions'
        ]
        
        for section in required_sections:
            self.assertIn(section, config, f"Missing required section: {section}")
        
        # Test agent metadata
        agent_meta = config['agent']
        self.assertEqual(agent_meta['id'], 'problem-solver')
        self.assertEqual(agent_meta['name'], 'Sage') 
        self.assertEqual(agent_meta['icon'], '🧠')
        
    def test_agent_commands_complete(self):
        """All expected commands should be defined"""
        agent_file = self.base_path / 'agents' / 'problem-solver.md'
        
        with open(agent_file, 'r') as f:
            content = f.read()
        
        required_commands = [
            'help', 'analyze-problem', 'investigate-root-cause',
            'decompose', 'generate-solutions', 'evaluate-decisions',
            'create-problem-def', 'create-solution-matrix', 'create-decision-record'
        ]
        
        for command in required_commands:
            self.assertIn(command, content, f"Missing command: {command}")
    
    def test_problem_solving_concepts(self):
        """Agent should reference key problem-solving concepts"""
        agent_file = self.base_path / 'agents' / 'problem-solver.md'
        
        with open(agent_file, 'r') as f:
            content = f.read().lower()
        
        required_concepts = [
            'first principles', 'triz', 'mece', 'mcda',
            'root cause', 'systematic', 'decision analysis'
        ]
        
        for concept in required_concepts:
            self.assertIn(concept, content, f"Missing concept: {concept}")


class TestCoreTasks(TestProblemSolverIntegration):
    """Test the problem-solving task files"""
    
    def setUp(self):
        super().setUp()
        self.task_dir = self.base_path / 'tasks'
        self.required_tasks = [
            'first-principles-analysis.md',
            'root-cause-investigation.md', 
            'problem-decomposition.md',
            'solution-synthesis.md',
            'decision-analysis.md'
        ]
    
    def test_all_task_files_exist(self):
        """All required task files should exist"""
        for task_file in self.required_tasks:
            task_path = self.task_dir / task_file
            self.assertTrue(task_path.exists(), f"Task file missing: {task_file}")
            
            # Check file size
            size = task_path.stat().st_size
            self.assertGreater(size, 1000, f"Task file {task_file} seems too small ({size} bytes)")
    
    def test_task_structure_compliance(self):
        """Tasks should follow BMad task structure patterns"""
        required_patterns = [
            r'## ⚠️ CRITICAL EXECUTION NOTICE',
            r'## (Method|Execution|Process|Flow)',
            r'## (Output|Result)',
            r'(elicit|Interactive)'
        ]
        
        for task_file in self.required_tasks:
            task_path = self.task_dir / task_file
            with open(task_path, 'r') as f:
                content = f.read()
            
            for pattern in required_patterns:
                self.assertRegex(content, pattern, 
                               f"{task_file} missing pattern: {pattern}")
    
    def test_task_methodology_content(self):
        """Tasks should contain appropriate methodology content"""
        methodology_tests = {
            'first-principles-analysis.md': ['feynman', 'fundamental', 'assumption'],
            'root-cause-investigation.md': ['5 whys', 'fishbone', 'fault tree'],
            'problem-decomposition.md': ['mece', 'mutually exclusive', 'collectively exhaustive'],
            'solution-synthesis.md': ['triz', 'lateral thinking', 'biomimicry'],
            'decision-analysis.md': ['mcda', 'criteria', 'weighted']
        }
        
        for task_file, concepts in methodology_tests.items():
            task_path = self.task_dir / task_file
            with open(task_path, 'r') as f:
                content = f.read().lower()
            
            for concept in concepts:
                self.assertIn(concept, content, 
                             f"{task_file} missing methodology concept: {concept}")
    
    def test_output_format_yaml(self):
        """Tasks should specify valid YAML output formats"""
        for task_file in self.required_tasks:
            task_path = self.task_dir / task_file
            with open(task_path, 'r') as f:
                content = f.read()
            
            # Find YAML output examples
            yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
            
            self.assertGreater(len(yaml_blocks), 0, 
                             f"{task_file} should have YAML output examples")
            
            # Test that at least one YAML block is valid
            valid_yaml_found = False
            for yaml_block in yaml_blocks:
                try:
                    yaml.safe_load(yaml_block)
                    valid_yaml_found = True
                    break
                except yaml.YAMLError:
                    continue
            
            self.assertTrue(valid_yaml_found, 
                          f"{task_file} has no valid YAML output examples")


class TestTemplates(TestProblemSolverIntegration):
    """Test the document templates"""
    
    def setUp(self):
        super().setUp()
        self.template_dir = self.base_path / 'templates'
        self.required_templates = [
            'problem-definition-tmpl.yaml',
            'solution-matrix-tmpl.yaml',
            'decision-record-tmpl.yaml'
        ]
    
    def test_template_files_exist(self):
        """All required template files should exist"""
        for template_file in self.required_templates:
            template_path = self.template_dir / template_file
            self.assertTrue(template_path.exists(), f"Template missing: {template_file}")
            
            size = template_path.stat().st_size
            self.assertGreater(size, 2000, f"Template {template_file} seems too small")
    
    def test_template_yaml_validity(self):
        """All templates should be valid YAML"""
        for template_file in self.required_templates:
            template_path = self.template_dir / template_file
            
            with open(template_path, 'r') as f:
                try:
                    template_data = yaml.safe_load(f)
                except yaml.YAMLError as e:
                    self.fail(f"{template_file} has invalid YAML: {e}")
            
            # Check basic structure
            self.assertIn('template', template_data, f"{template_file} missing 'template' section")
            self.assertIn('sections', template_data, f"{template_file} missing 'sections' section")
    
    def test_template_metadata_complete(self):
        """Templates should have complete metadata"""
        for template_file in self.required_templates:
            template_path = self.template_dir / template_file
            
            with open(template_path, 'r') as f:
                template_data = yaml.safe_load(f)
            
            template_meta = template_data['template']
            
            required_fields = ['id', 'name', 'version', 'output']
            for field in required_fields:
                self.assertIn(field, template_meta, 
                             f"{template_file} missing template field: {field}")
    
    def test_template_elicitation_points(self):
        """Templates should have appropriate elicitation points"""
        for template_file in self.required_templates:
            template_path = self.template_dir / template_file
            
            with open(template_path, 'r') as f:
                template_data = yaml.safe_load(f)
            
            # Recursively check for elicit: true
            elicit_found = self._check_elicit_recursive(template_data['sections'])
            self.assertTrue(elicit_found, f"{template_file} has no elicitation points")
    
    def _check_elicit_recursive(self, sections):
        """Recursively check for elicit: true in sections"""
        for section in sections:
            if section.get('elicit', False):
                return True
            if 'sections' in section:
                if self._check_elicit_recursive(section['sections']):
                    return True
        return False
    
    def test_template_workflow_integration(self):
        """Templates should specify workflow integration"""
        for template_file in self.required_templates:
            template_path = self.template_dir / template_file
            
            with open(template_path, 'r') as f:
                template_data = yaml.safe_load(f)
            
            # Should have workflow section
            self.assertIn('workflow', template_data, 
                         f"{template_file} missing workflow section")
            
            workflow = template_data['workflow']
            self.assertIn('mode', workflow, f"{template_file} missing workflow mode")


class TestWorkflowIntegration(TestProblemSolverIntegration):
    """Test workflow integration and configuration"""
    
    def test_complex_problem_solving_workflow_exists(self):
        """Complex problem-solving workflow should exist"""
        workflow_path = self.base_path / 'workflows' / 'complex-problem-solving.yaml'
        self.assertTrue(workflow_path.exists(), "Complex problem-solving workflow not found")
        
        with open(workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)
        
        self.assertIn('workflow', workflow, "Workflow structure missing")
        self.assertEqual(workflow['workflow']['id'], 'complex-problem-solving')
    
    def test_workflow_sequence_valid(self):
        """Workflow sequence should have valid dependencies"""
        workflow_path = self.base_path / 'workflows' / 'complex-problem-solving.yaml'
        
        with open(workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)
        
        sequence = workflow['workflow']['sequence']
        created_artifacts = set()
        
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
                                        f"Workflow step requires {req} but it's not created yet")
                
                # Add created artifact
                creates = step.get('creates')
                if creates:
                    created_artifacts.add(creates)
    
    def test_problem_solver_prominence_in_workflow(self):
        """Problem-solver should be primary agent in complex workflow"""
        workflow_path = self.base_path / 'workflows' / 'complex-problem-solving.yaml'
        
        with open(workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)
        
        sequence = workflow['workflow']['sequence']
        ps_count = sum(1 for step in sequence 
                      if isinstance(step, dict) and step.get('agent') == 'problem-solver')
        
        self.assertGreaterEqual(ps_count, 4, 
                               f"Problem-solver should appear at least 4 times, found {ps_count}")
    
    def test_agent_team_integration(self):
        """Problem-solver should be in appropriate agent teams"""
        teams_to_check = ['team-fullstack.yaml', 'team-no-ui.yaml']
        
        for team_file in teams_to_check:
            team_path = self.base_path / 'agent-teams' / team_file
            self.assertTrue(team_path.exists(), f"Team file not found: {team_file}")
            
            with open(team_path, 'r') as f:
                team_config = yaml.safe_load(f)
            
            agents = team_config.get('agents', [])
            self.assertTrue(
                'problem-solver' in agents or '*' in agents,
                f"problem-solver not in {team_file}"
            )


class TestInstallManifest(TestProblemSolverIntegration):
    """Test install manifest integration"""
    
    def test_manifest_updated(self):
        """Install manifest should include all problem-solver files"""
        manifest_path = self.base_path / 'install-manifest.yaml'
        self.assertTrue(manifest_path.exists(), "Install manifest not found")
        
        with open(manifest_path, 'r') as f:
            manifest = yaml.safe_load(f)
        
        # Check version updated
        version = manifest.get('version', '')
        self.assertIn('problem-solver', version, "Version not updated for problem-solver")
        
        # Check files included
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
        
        for file_path in required_files:
            self.assertIn(file_path, files, f"File not in manifest: {file_path}")
            
            # Check hash exists
            entry = files[file_path]
            self.assertIn('hash', entry, f"No hash for {file_path}")
            self.assertEqual(len(entry['hash']), 16, f"Invalid hash length for {file_path}")
    
    def test_file_integrity(self):
        """File hashes should match actual files"""
        manifest_path = self.base_path / 'install-manifest.yaml'
        
        with open(manifest_path, 'r') as f:
            manifest = yaml.safe_load(f)
        
        files = {entry['path']: entry for entry in manifest.get('files', [])}
        
        problem_solver_files = [
            '.bmad-core/agents/problem-solver.md',
            '.bmad-core/tasks/first-principles-analysis.md',
            '.bmad-core/templates/problem-definition-tmpl.yaml'
        ]
        
        for file_path in problem_solver_files:
            if file_path in files:
                expected_hash = files[file_path]['hash']
                
                # Calculate actual hash
                try:
                    with open(file_path, 'rb') as f:
                        content = f.read()
                    actual_hash = hashlib.md5(content).hexdigest()[:16]
                    
                    self.assertEqual(actual_hash, expected_hash,
                                   f"Hash mismatch for {file_path}")
                except FileNotFoundError:
                    self.fail(f"File in manifest but not found: {file_path}")


class TestEndToEndWorkflow(TestProblemSolverIntegration):
    """End-to-end workflow simulation tests"""
    
    def test_workflow_simulation(self):
        """Simulate execution of complex problem-solving workflow"""
        workflow_path = self.base_path / 'workflows' / 'complex-problem-solving.yaml'
        
        with open(workflow_path, 'r') as f:
            workflow = yaml.safe_load(f)
        
        sequence = workflow['workflow']['sequence']
        artifacts = set()
        
        print(f"\nSimulating workflow: {workflow['workflow']['name']}")
        
        for i, step in enumerate(sequence, 1):
            if isinstance(step, dict) and 'agent' in step:
                agent = step['agent']
                creates = step.get('creates', 'output')
                task = step.get('task', 'default')
                
                print(f"Step {i}: {agent} -> {creates}")
                
                # Check dependencies available
                requires = step.get('requires', [])
                if isinstance(requires, str):
                    requires = [requires]
                
                for req in requires:
                    if req not in ['all_validations', 'all_documents']:
                        if not step.get('optional', False):
                            self.assertIn(req, artifacts,
                                        f"Step {i} requires {req} but not available")
                
                # Add created artifact
                if creates != 'output':
                    artifacts.add(creates)
        
        # Check that key artifacts were created
        expected_artifacts = {
            'problem-definition.md',
            'root-cause-analysis.md', 
            'solution-options.md',
            'solution-matrix.md',
            'decision-record.md'
        }
        
        for artifact in expected_artifacts:
            self.assertIn(artifact, artifacts, f"Expected artifact not created: {artifact}")
        
        print("✅ Workflow simulation successful")


class TestPerformance(TestProblemSolverIntegration):
    """Performance and quality tests"""
    
    def test_file_sizes_reasonable(self):
        """Files should be appropriately sized"""
        size_expectations = {
            'problem-solver.md': (3000, 10000),  # Agent file
            'first-principles-analysis.md': (5000, 15000),  # Task file
            'problem-definition-tmpl.yaml': (10000, 25000),  # Template file
            'complex-problem-solving.yaml': (8000, 20000)  # Workflow file
        }
        
        for filename, (min_size, max_size) in size_expectations.items():
            # Find file in appropriate directory
            for subdir in ['agents', 'tasks', 'templates', 'workflows']:
                file_path = self.base_path / subdir / filename
                if file_path.exists():
                    size = file_path.stat().st_size
                    self.assertGreaterEqual(size, min_size,
                                          f"{filename} too small: {size} < {min_size}")
                    self.assertLessEqual(size, max_size,
                                       f"{filename} too large: {size} > {max_size}")
                    break
    
    def test_content_quality_indicators(self):
        """Test qualitative content indicators"""
        agent_file = self.base_path / 'agents' / 'problem-solver.md'
        
        with open(agent_file, 'r') as f:
            content = f.read()
        
        # Count methodology references
        methodologies = [
            'TRIZ', 'MECE', 'MCDA', '5 Whys', 'Fishbone',
            'Design Thinking', 'First Principles', 'Lateral Thinking'
        ]
        
        found_methodologies = sum(1 for m in methodologies if m in content)
        self.assertGreaterEqual(found_methodologies, 6,
                               f"Only found {found_methodologies} methodologies, expected at least 6")
        
        # Check for problem-solving vocabulary
        vocab_indicators = [
            'systematic', 'analysis', 'root cause', 'solution',
            'decision', 'criteria', 'evaluation', 'validation'
        ]
        
        found_vocab = sum(1 for v in vocab_indicators if v.lower() in content.lower())
        self.assertGreaterEqual(found_vocab, 6,
                               f"Limited problem-solving vocabulary: {found_vocab}/8")


def run_test_suite():
    """Run the complete test suite"""
    print("=" * 60)
    print("BMad Problem-Solver Integration Test Suite")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestAgentDefinition,
        TestCoreTasks, 
        TestTemplates,
        TestWorkflowIntegration,
        TestInstallManifest,
        TestEndToEndWorkflow,
        TestPerformance
    ]
    
    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(
        verbosity=2,
        stream=sys.stdout,
        buffer=True
    )
    
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print(f"Test Summary: {result.testsRun} tests run")
    print(f"✅ Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Failed: {len(result.failures)}")
    print(f"💥 Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback.split('AssertionError: ')[-1].split('\\n')[0]}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback.split('\\n')[-2]}")
    
    success = len(result.failures) == 0 and len(result.errors) == 0
    
    if success:
        print("\n🎉 ALL TESTS PASSED! Problem-Solver integration is ready!")
    else:
        print("\n💥 Some tests failed. Check output above for details.")
    
    print("=" * 60)
    return 0 if success else 1


if __name__ == '__main__':
    import sys
    sys.exit(run_test_suite())