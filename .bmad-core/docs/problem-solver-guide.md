# BMad Problem-Solver Agent (Sage) - User Guide

## 🧠 Meet Sage: Your Problem-Solving Specialist

The Problem-Solver agent embodies the methodologies of exceptional problem solvers like Richard Feynman, Charlie Munger, and Elon Musk. Sage applies 15+ systematic frameworks to analyze complex problems, generate innovative solutions, and support high-stakes decision-making.

## When to Use Problem-Solver

### ✅ Ideal Scenarios
- **Complex Multi-Domain Problems**: Issues spanning technical, business, and user experience
- **Unknown Root Causes**: Problems where the source isn't immediately apparent  
- **Innovation Required**: Situations needing creative, non-obvious solutions
- **High-Stakes Decisions**: Choices with significant impact requiring systematic analysis
- **Technical Contradictions**: Requirements that seem mutually exclusive
- **Cross-Functional Challenges**: Problems affecting multiple teams or systems

### ❌ When NOT to Use
- Simple, well-understood problems with obvious solutions
- Time-critical urgent fixes where speed matters more than analysis depth
- Problems with single clear solution already identified
- Purely operational issues without strategic implications

### 🎯 Problem Complexity Assessment

| Level | Characteristics | Approach |
|-------|----------------|----------|
| **Simple** | Single domain, known patterns, clear requirements | Use standard agents |
| **Moderate** | 2-3 domains, some uncertainty, multiple stakeholders | Optional problem-solver consultation |
| **Complex** | Cross-disciplinary, unknown causes, conflicting requirements | Full problem-solver engagement |
| **Wicked** | No clear definition, solutions create new problems | Iterative problem-solver cycles |

## 🚀 Getting Started

### Activation
```bash
# From BMad Orchestrator
*agent problem-solver

# Will activate as "Sage, Problem-Solving Specialist"
```

### Core Commands
```bash
*help                     # Show all available commands
*analyze-problem          # First principles analysis (break to fundamentals)
*investigate-root-cause   # 5 Whys, Fishbone, Fault Tree analysis
*decompose               # MECE problem breakdown
*generate-solutions      # TRIZ, Lateral Thinking, Biomimicry innovation
*evaluate-decisions      # Multi-criteria decision analysis (MCDA)
*create-problem-def      # Comprehensive problem definition document
*create-solution-matrix  # Systematic solution comparison
*create-decision-record  # ADR-style decision documentation
```

## 🧪 Core Methodologies

### 1. First Principles Analysis
**Method**: Break problems to fundamental, irreducible truths
**Best For**: Challenging assumptions, breakthrough innovation
**Approach**: Feynman/Musk systematic doubt methodology

```bash
*analyze-problem
# Systematically challenges assumptions
# Identifies fundamental constraints vs. conventional thinking  
# Reconstructs solutions from basic truths
# Output: fundamental_truths, reconstructed_solution
```

**Example**: SpaceX rocket costs - Instead of accepting industry pricing, analyzed material costs (aluminum, titanium) reaching 10x cost reduction.

### 2. Root Cause Investigation
**Method**: Multiple systematic approaches to find true causes
**Best For**: Complex failures, recurring problems
**Auto-selects**: 5 Whys (linear), Fishbone (multi-factor), Fault Tree (complex systems)

```bash
*investigate-root-cause
# Automatically chooses best method based on problem characteristics
# Validates causes with evidence requirements
# Maps cause-and-effect relationships
# Output: verified root causes with confidence levels
```

### 3. MECE Problem Decomposition
**Method**: Mutually Exclusive, Collectively Exhaustive breakdown
**Best For**: Complex systems, unclear scope
**Ensures**: No overlaps, complete coverage, same abstraction levels

```bash
*decompose
# Creates hierarchical problem structure
# Validates MECE principle compliance
# Identifies leverage points and critical dependencies
# Output: structured problem hierarchy
```

### 4. Solution Synthesis (Innovation Portfolio)
**Method**: Multiple creative frameworks applied systematically
**Frameworks**: TRIZ, Lateral Thinking, Biomimicry, Design Thinking, Combinatory Play
**Best For**: Need multiple solution alternatives, innovation required

```bash
*generate-solutions
# Applies 3-5 innovation methods automatically
# Generates 3-7 diverse solution approaches
# Scores solutions on feasibility, innovation, impact
# Output: solution portfolio with implementation approaches
```

**TRIZ Example**: Technical contradiction "faster processing requires more energy" → Apply Principle #15 (Segmentation) → Distributed processing solution.

### 5. Decision Analysis (MCDA)
**Method**: Multi-Criteria Decision Analysis with sensitivity testing
**Best For**: Multiple options with trade-offs, high-stakes choices
**Features**: Weighted scoring, sensitivity analysis, scenario testing

```bash
*evaluate-decisions
# Systematically scores alternatives against criteria
# Provides weighted recommendations with confidence levels
# Tests decision robustness through sensitivity analysis
# Output: quantified decision with rationale
```

## 📋 Document Templates

### Problem Definition Template
Comprehensive problem scoping with stakeholder analysis:
```bash
*create-problem-def
# Interactive template covering:
# - Structured problem statements (McKinsey method)
# - Stakeholder analysis with impact assessment
# - Success metrics and evaluation criteria
# - Constraints vs. assumptions analysis
# - Initial root cause hypotheses
```

### Solution Matrix Template  
Systematic solution comparison and evaluation:
```bash
*create-solution-matrix
# Features:
# - Multi-option scoring against weighted criteria
# - Sensitivity analysis for decision robustness
# - Scenario analysis (optimistic/pessimistic/disruptive)
# - Risk assessment and mitigation strategies
# - Implementation roadmap for recommended solution
```

### Decision Record Template
ADR-style decision documentation:
```bash
*create-decision-record
# Captures:
# - Decision context and driving forces
# - All alternatives considered with rationale
# - Decision outcome and implementation plan
# - Expected consequences and trade-offs
# - Success measurement and review plan
```

## 🔄 Workflow Integration

### Complex Problem-Solving Workflow
Complete end-to-end problem analysis:
```bash
*workflow complex-problem-solving
```

**Flow**: Problem Definition → Root Cause Analysis → Solution Generation → Technical/Business Validation → Decision Matrix → Decision Record → Implementation Handoff

**Timeline**: 1-2 weeks for thorough analysis
**Outputs**: 5-6 comprehensive documents with full analysis trail

### Integration with Standard Workflows
Problem-solver can be inserted at key decision points:
- **After Project Brief**: Deep problem analysis for complex requirements
- **Before Architecture**: Technical decision support with MCDA
- **During Development**: Complex debugging with systematic root cause analysis
- **Legacy Systems**: Systematic refactoring strategy development

## 🤝 Agent Collaboration Patterns

### Working with Analyst
```
Analyst → Problem-Solver: "Market research shows conflicting trends. Need systematic analysis."
Problem-Solver → Analyst: "Problem decomposed into 4 research areas. Focus on segments 2 and 4."
```

### Working with Architect
```
Architect → Problem-Solver: "Technical contradiction: need high performance AND low cost."
Problem-Solver → Architect: "TRIZ Principle #15: Segmentation. Distribute load processing."
```

### Working with Product Manager  
```
PM → Problem-Solver: "Three product directions possible, unclear which maximizes value."
Problem-Solver → PM: "MCDA analysis complete. Option B scores 8.4/10. See decision-matrix.md."
```

## 💡 Real-World Examples

### Example 1: System Performance Crisis
```bash
# Problem: E-commerce site crashes during peak traffic
*create-problem-def
# → Structured problem: "How to handle 10x traffic spikes..."

*investigate-root-cause  
# → Method: Fault Tree Analysis
# → Found: Database connection pool + Cache invalidation + Load balancer config

*generate-solutions
# → TRIZ contradiction resolution
# → Biomimicry: Ant colony load distribution
# → Generated: 5 solution approaches

*create-solution-matrix
# → Recommendation: Adaptive load balancing + Connection pooling
# → Score: 8.7/10, High confidence

*create-decision-record
# → ADR-023: Implement adaptive infrastructure scaling
```

### Example 2: Feature Innovation Challenge
```bash
# Problem: Need 90% faster deployment process
*analyze-problem
# → First principles: What fundamentally limits deployment speed?
# → Insight: Sequential steps not parallelizable  

*generate-solutions
# → Lateral thinking with "pizza delivery" random input
# → Insight: Hot-swap deployments like fresh pizza rotation
# → Solution: Blue-green deployment with feature flags

*evaluate-decisions
# → Winner: Parallel deployment pipeline with instant rollback
```

### Example 3: Cross-Team Conflict Resolution
```bash
# Problem: Engineering vs. Product priorities constantly conflict
*decompose
# → MECE breakdown: Resources, Process, Communication, Incentives
# → Leverage point identified: Misaligned success metrics

*create-solution-matrix
# → Multiple organizational solutions evaluated
# → Recommendation: Shared OKRs with joint success metrics
```

## 🛠️ Advanced Usage

### Method Selection Guidance
```bash
*method-select
# Helps choose optimal problem-solving approach based on:
# - Problem characteristics
# - Available time and resources
# - Stakeholder preferences
# - Desired outcome type
```

### Complexity Assessment
```bash
*complexity-assess
# Evaluates problem across 5 dimensions:
# - Domain breadth (how many areas affected)
# - Stakeholder disagreement level
# - Solution uncertainty
# - Impact significance  
# - Time sensitivity
```

### Status Tracking
```bash
*status
# Shows current analysis phase
# Active methodologies being applied
# Progress toward solution
# Next recommended steps
```

## 🔧 Best Practices

### 1. Start with Problem Definition
Always begin with comprehensive problem scoping before jumping to solutions.

### 2. Apply Multiple Methods
Complex problems benefit from multiple analytical approaches for validation.

### 3. Document Decision Rationale
Use decision records for important choices to preserve institutional learning.

### 4. Iterate and Refine
First analysis is rarely complete - use feedback loops for improvement.

### 5. Collaborate with Domain Experts
Leverage other agents for specialized knowledge and validation.

### 6. Validate with Data
Test hypotheses empirically rather than relying on theoretical analysis alone.

## 🚨 Troubleshooting

| Issue | Diagnosis | Solution |
|-------|-----------|----------|
| "This seems like overkill" | Problem too simple for systematic analysis | Use standard agents instead |
| "Too many solution options" | Need stricter evaluation criteria | Apply more selective scoring |
| "Root cause still unclear" | Insufficient data or wrong method | Try different investigation approach |
| "Solutions seem obvious" | May need more creative methods | Apply lateral thinking or biomimicry |
| "Decision keeps changing" | Inadequate sensitivity analysis | Run robustness testing |

### Debug Commands
```bash
*yolo          # Skip confirmations for rapid iteration
*status        # Check current analysis phase and progress
*method-select # Get guidance on appropriate methodology
```

## 📚 Methodology Reference

### Innovation Methods
- **TRIZ**: Systematic contradiction resolution (40 inventive principles)
- **Lateral Thinking**: Pattern-breaking with provocative operations
- **Biomimicry**: Nature-inspired solutions for efficiency
- **Design Thinking**: Human-centered 5-stage innovation process
- **Combinatory Play**: Cross-domain synthesis (Einstein's method)

### Analysis Methods
- **First Principles**: Fundamental truth decomposition (Feynman/Musk)
- **5 Whys**: Linear root cause analysis (Toyota method)
- **Fishbone**: Multi-factor cause analysis (Ishikawa)
- **Fault Tree**: Complex system failure analysis
- **MECE**: Structured problem decomposition (McKinsey)

### Decision Methods
- **MCDA**: Multi-criteria decision analysis with weighting
- **Decision Trees**: Sequential decision under uncertainty
- **Cost-Benefit**: Quantitative option comparison
- **Scenario Analysis**: Robustness under different futures
- **Sensitivity Analysis**: Testing decision stability

## 🎓 Learning Resources

### Problem-Solving Principles
- First Principles Thinking: Question everything, build from fundamentals
- Systems Thinking: See wholes, identify leverage points
- Bayesian Reasoning: Embrace uncertainty, update beliefs with evidence
- Multidisciplinary Synthesis: Combine frameworks for Lollapalooza Effects

### Cognitive Biases to Avoid
- **Confirmation Bias**: Seeking only supporting evidence
- **Anchoring**: Over-relying on first information received
- **Availability Heuristic**: Overweighting recent or memorable examples
- **Sunk Cost Fallacy**: Continuing because of past investment
- **Expert Bias**: Assuming domain knowledge always helps creativity

## 🏆 Success Indicators

You'll know problem-solver is working well when:
- Problems are clearly defined before solution development starts
- Multiple innovative solution approaches are generated consistently
- Decisions can be clearly explained and defended to stakeholders
- Root causes are validated with evidence rather than assumed
- Solutions address structural issues rather than just symptoms
- Decision quality improves over time with institutional learning

## 📞 Getting Help

- **Within Session**: Use `*help` for command guidance
- **Methodology Questions**: Reference `.bmad-core/data/problem-solving-methods.md`
- **Integration Issues**: See `.bmad-core/docs/problem-solver-integration.md`
- **Workflow Guidance**: Use `*workflow-guidance` from orchestrator

## 🎯 Next Steps

Ready to solve complex problems systematically? Start with:
1. `*agent problem-solver` to activate Sage
2. `*help` to see all available commands
3. `*create-problem-def` for comprehensive problem scoping
4. Follow the systematic methodology step-by-step
5. Document your decision with `*create-decision-record`

**Remember**: Great problem-solving is systematic, creative, and humble. Question assumptions, apply multiple frameworks, and validate empirically.