# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the implementation of a **Problem-Solver Agent** for the BMad framework. BMad is an AI agent orchestration system where specialized agents (like Product Manager, Architect, Developer) collaborate on software projects. This project adds a new "Sage" agent that applies systematic problem-solving methodologies from experts like Feynman, Charlie Munger, and Elon Musk.

## Architecture

### Core Components
- **Agent Definition**: `.bmad-core/agents/problem-solver.md` - Main agent configuration file
- **Tasks**: `.bmad-core/tasks/` - Individual problem-solving methodologies (5 Whys, TRIZ, etc.)
- **Templates**: `.bmad-core/templates/` - Interactive document templates for problem analysis
- **Validation**: `quick_test.py` - Integration testing script

### Agent System Integration
The Problem-Solver agent integrates with BMad's orchestrator pattern:
1. **Activation**: `*agent problem-solver` transforms orchestrator into Sage persona
2. **Collaboration**: Works with existing agents (PM, Architect, Analyst) on complex problems
3. **Workflows**: Can be inserted into standard BMad workflows or run standalone

### Problem-Solving Methodologies
The agent applies 15+ systematic frameworks:
- **Analysis**: First principles thinking, 5 Whys, Fishbone diagrams, Fault Tree Analysis
- **Innovation**: TRIZ, Lateral thinking, Biomimicry, Design thinking
- **Decision Making**: Multi-Criteria Decision Analysis (MCDA), Decision trees
- **Documentation**: Architectural Decision Records (ADR), Problem definition templates

### Iterative Thinking System (NEW)
The enhanced agent enforces complexity-adaptive iterative thinking:
- **Complexity Assessment**: 5-dimension scoring determines thinking depth
- **Adaptive Planning**: 3 steps (Simple) → 5 steps (Medium) → 7 steps (Complex) → 10 steps (Wicked)
- **Sequential Enforcement**: Cannot skip ahead without completing prerequisites
- **Validation Gates**: Each step requires completion criteria before progression
- **Progressive Learning**: Insights accumulate and inform subsequent steps
- **Pure Iteration Focus**: No time constraints - emphasis on systematic thinking progression

## Development Commands

### Testing
```bash
# Run basic validation tests
python quick_test.py

# Run iterative thinking system validation  
python iterative_thinking_test.py

# Test agent loading (if BMad environment available)
echo "*agent problem-solver" | bmad-orchestrator
```

### Project Structure Validation
The implementation follows a specific file structure that must be maintained:
```
.bmad-core/
├── agents/
│   ├── problem-solver.md             # Original agent definition
│   └── problem-solver-iterative.md   # Enhanced agent with iterative thinking
├── tasks/
│   ├── complexity-assessment.md      # NEW: Problem complexity evaluation
│   ├── create-thinking-plan.md       # NEW: Generate adaptive thinking plans
│   ├── execute-step.md               # NEW: Enforce step-by-step execution
│   └── [existing task files]         # Original problem-solving methodologies
├── templates/                        # Interactive document templates
├── workflows/complex-problem-solving.yaml
└── install-manifest.yaml            # File registry
```

### Key New Files
- `iterative-thinking-plan.md`: Complete framework design and templates
- `iterative_thinking_test.py`: Validation testing for the new system
- `problem-solver-iterative.md`: Enhanced agent with enforced thinking discipline

## Key Implementation Guidelines

### Agent File Format
- Agent files use specific BMad YAML-in-Markdown format
- Must include ACTIVATION-NOTICE header
- YAML block contains persona, commands, dependencies
- Exact formatting is critical for BMad parser

### Problem-Solving Philosophy
The agent embodies philosophical principles from exceptional problem solvers:
- **First principles thinking**: Break problems to fundamental truths
- **Systems thinking**: Identify leverage points and feedback loops
- **Bayesian reasoning**: Embrace uncertainty, update beliefs with evidence
- **Aesthetic elegance**: Seek beautiful, sophisticated solutions

### Collaboration Patterns
- **Advisory Mode**: Provides frameworks, others execute
- **Leading Mode**: Drives analysis, others provide domain expertise
- **Support Mode**: Assists when other agents encounter blockers
- **Review Mode**: Validates solutions using multiple frameworks

## Documentation Structure

### Core Files
- `implementation_plan.md`: Comprehensive implementation strategy with PDCA methodology
- `problem_solver_core.md`: Philosophical foundations and methodologies from research
- `problem-solver-korean-guide.md`: Complete user guide in Korean
- `stories/`: User stories for implementation phases

### Story-Driven Development
Implementation follows agile story structure:
- Story 1: Agent core definition
- Story 2: Task implementations  
- Story 3: Template development
- Story 4: Orchestrator integration
- Story 5: Workflow enhancements

## Important Notes

### BMad Framework Dependencies
- This is a plugin/extension for the BMad agent orchestration system
- Requires understanding of BMad's agent transformation mechanism
- Agent interactions follow specific handoff protocols
- YAML syntax must be precise for BMad compatibility

### Validation Requirements
- All agent files must pass YAML validation
- Integration tests verify orchestrator compatibility
- Problem-solving methodologies must produce expected document formats
- Agent persona must be evident in responses

### No Package Management
This is a documentation and configuration project - no package.json, requirements.txt, or build tools. Testing is done via Python scripts and BMad orchestrator integration.