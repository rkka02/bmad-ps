# Decision Analysis Framework

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

**THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

Systematic decision support using quantitative Multi-Criteria Decision Analysis (MCDA) with sensitivity testing. This task requires user interaction for criteria definition and weighting.

**CRITICAL RULE**: All significant decisions must be supported by systematic analysis, not intuition alone.

## Method Selection Guide

Choose decision analysis approach based on problem characteristics:

```
Decision Context → Recommended Method
├── 2-4 options, simple criteria → Simple Weighted Matrix
├── Many options, complex criteria → Analytic Hierarchy Process (AHP)
├── Uncertainty/Risk present → Decision Tree with Expected Value
├── Multiple stakeholders → Multi-Stakeholder MCDA
├── Cost-focused decisions → Cost-Benefit Analysis with NPV
└── Sequential decisions → Dynamic Programming / Decision Tree
```

## Multi-Criteria Decision Analysis (MCDA)

**Best For**: Most complex decisions with multiple competing objectives
**Approach**: Systematic evaluation using weighted criteria

### MCDA Execution Process

#### Step 1: Define Decision Criteria

**Criteria Quality Requirements**:
- **Measurable**: Can be quantified or assessed consistently
- **Independent**: Minimal overlap between criteria  
- **Complete**: Cover all important decision factors
- **Operational**: Data available or can be reasonably estimated

**Common Criteria Categories**:
```
Financial: Cost, ROI, Revenue potential, Budget fit
Technical: Feasibility, Complexity, Reliability, Performance
Strategic: Alignment, Competitive advantage, Market position
Operational: Implementation ease, Resource requirements, Timeline
Risk: Technical risk, Market risk, Regulatory risk
Stakeholder: User satisfaction, Team capability, Leadership support
```

#### Step 2: Criteria Weighting Methods

**Method A: Direct Rating (0-100)**
- Assign importance scores to each criterion
- Normalize so total = 100%
- Simple but may not capture trade-offs well

**Method B: Pairwise Comparison (AHP Method)**
- Compare each criterion pair: "How much more important is A than B?"
- Use 1-9 scale: 1=Equal, 3=Moderate, 5=Strong, 7=Very Strong, 9=Extreme
- Calculate eigenvalues for consistency
- More accurate but more complex

**Method C: Swing Weights**
- Imagine all criteria at worst level
- Which would you most want to improve to best level?
- Rank criteria by improvement value
- Assign relative weights based on rankings

**Method D: Trade-off Analysis**  
- Present trade-off scenarios
- "Would you accept 20% higher cost for 30% better performance?"
- Infer weights from trade-off preferences
- Most accurate but time-intensive

#### Step 3: Alternative Scoring

For each criterion, score each alternative:

**Scoring Approaches**:
- **Direct Rating**: 1-10 or 1-100 scale
- **Relative Comparison**: Compare alternatives pairwise for each criterion
- **Objective Measures**: Use actual data where available
- **Conversion Scales**: Transform raw data to common scale

**Score Normalization Methods**:
```python
# Linear normalization (0-1 scale)
normalized_score = (raw_score - min_score) / (max_score - min_score)

# For "minimize" criteria (like cost), reverse the scale
normalized_score = (max_score - raw_score) / (max_score - min_score)
```

#### Step 4: Calculate Weighted Scores

**Formula**: 
```
Total_Score = Σ(Weight_i × Score_i) for all criteria i
```

**Implementation**:
```python
def calculate_weighted_score(weights, scores):
    """
    weights: list of criterion weights (sum = 1.0)
    scores: list of normalized scores (0-1 scale)
    """
    return sum(w * s for w, s in zip(weights, scores))
```

#### Step 5: Sensitivity Analysis

**Critical for Decision Confidence**: Test how robust the decision is

**Weight Sensitivity**:
- Vary each weight by ±20%
- Renormalize remaining weights
- Check if ranking changes
- Identify "critical criteria" where small changes alter decision

**Score Sensitivity**:  
- Vary uncertain scores by ±1-2 points
- Recalculate rankings
- Identify decisions sensitive to scoring assumptions

**Threshold Analysis**:
- Find minimum weight/score changes needed to alter decision
- "Option B would win if Cost weight drops below 25%"

## Decision Tree Analysis

**Best For**: Sequential decisions under uncertainty
**Elements**: Decision nodes (□), Chance nodes (○), Terminal nodes (△)

### Decision Tree Construction

#### Step 1: Structure the Decision
```
Decision Node → Alternatives → Chance Node → Outcomes → Value
     □             ↓             ○           ↓        △
   Choice A    → Uncertain    → Good (0.6) → $1000
               → Event       → Bad (0.4)  → -$200
   Choice B    → Different   → Success (0.8) → $600  
               → Uncertainty → Failure (0.2) → $0
```

#### Step 2: Assign Probabilities
- Based on historical data, expert judgment, or models
- Must sum to 1.0 for each chance node
- Use confidence intervals if uncertain

#### Step 3: Calculate Expected Values
**Backward Induction**: Start from outcomes, work backward

```python
def expected_value(outcomes_probs):
    """
    outcomes_probs: list of (value, probability) tuples
    """
    return sum(value * prob for value, prob in outcomes_probs)

# Example:
choice_a_ev = 1000 * 0.6 + (-200) * 0.4 = 600 - 80 = $520
choice_b_ev = 600 * 0.8 + 0 * 0.2 = 480 + 0 = $480
# Choose A: Higher expected value
```

#### Step 4: Sensitivity Analysis for Probabilities
- How much would probability need to change to alter decision?
- "Choice B becomes better if success probability > 87%"

## Advanced Decision Methods

### Multi-Stakeholder MCDA
When different groups have different priorities:

1. **Stakeholder Weighting**: Different weights for each stakeholder group
2. **Consensus Building**: Facilitate agreement on criteria and weights  
3. **Compromise Solutions**: Find alternatives acceptable to all groups
4. **Voting Methods**: Combine individual preferences systematically

### Dynamic Programming
For sequential decision problems:
- Optimize sequence of interconnected decisions
- Each decision affects future options
- Work backward from final decision point

### Real Options Analysis  
When decisions create future opportunities:
- Value of flexibility and future choices
- Option to expand, abandon, or defer
- Accounts for uncertainty resolution over time

## Interactive Elicitation Process

When `elicit: true`, present these options:

1. **Proceed with analysis** - Continue with current settings
2. **Add new criterion** - Include additional decision factor
3. **Modify criterion weight** - Adjust importance of existing criterion
4. **Re-score alternatives** - Update alternative ratings
5. **Run sensitivity analysis** - Test robustness of decision
6. **Add uncertainty analysis** - Include risk/probability considerations
7. **Consider stakeholder differences** - Account for different perspectives
8. **Examine trade-off scenarios** - Explore specific trade-offs
9. **Get expert input** - Consult domain specialist for validation

## Output Format

```yaml
decision_context:
  problem: "Clear statement of decision to be made"
  alternatives: ["List of options being evaluated"]
  constraints: ["Limitations or requirements"]
  stakeholders: ["Who is affected by this decision"]
  timeline: "When decision must be made"

criteria_definition:
  - name: "Criterion name"
    description: "What this measures"
    weight: 0.0-1.0
    measurement_approach: "How to assess this"
    direction: "maximize|minimize"
    data_source: "Where scores come from"

alternatives_analysis:
  - alternative: "Option name/ID"
    scores:
      criterion_1: score (0-1 normalized)
      criterion_2: score
      # ... for all criteria
    raw_scores:
      criterion_1: "original measurement"
      criterion_2: "original measurement"  
    weighted_total: calculated_score
    rank: final_ranking_position
    
    strengths:
      - strength: "Major advantage of this option"
        criterion: "Which criterion this relates to"
    
    weaknesses:
      - weakness: "Major limitation"
        criterion: "Which criterion this relates to"
        severity: "How significant this limitation is"

sensitivity_analysis:
  weight_sensitivity:
    - criterion: "Criterion name"
      current_weight: 0.XX
      threshold_weight: "Weight at which decision would change"
      robust: true/false
      notes: "How sensitive decision is to this weight"
  
  score_sensitivity:
    - alternative: "Option name"
      criterion: "Score being tested"
      threshold_change: "Score change needed to alter decision"
      robust: true/false
  
  overall_robustness: "high|medium|low"
  critical_assumptions: ["Assumptions most important to decision"]

decision_recommendation:
  selected_alternative: "Recommended option"
  confidence_level: "high|medium|low"
  
  rationale:
    primary_reasons:
      - reason: "Main factor supporting this choice"
        evidence: "Supporting analysis"
    
    risk_factors:
      - risk: "What could make this wrong choice"
        likelihood: "low|medium|high"
        mitigation: "How to address this risk"
  
  implementation_considerations:
    - consideration: "Important factor for implementation"
      impact: "How this affects success"
      approach: "How to handle this"

alternative_recommendations:
  - condition: "Under what circumstances would you choose different option"
    alternative: "Which option would be better"
    rationale: "Why this would be better under these conditions"

validation_approach:
  - test: "How to validate this decision was correct"
    timeline: "When to assess this"
    metrics: "What to measure"
    success_criteria: "What would indicate good decision"

decision_tree_analysis: # If applicable
  structure:
    - node_type: "decision|chance|terminal"
      description: "What happens at this node"
      options: ["Available choices at this point"]
      probabilities: ["If chance node, probability of each outcome"]
      values: ["If terminal node, final value"]
  
  expected_values:
    - path: "Decision sequence"
      probability: "Overall probability of this path"  
      value: "Final value if this path occurs"
      expected_contribution: "probability × value"
  
  optimal_strategy: "Which choices to make at each decision point"

lessons_learned:
  - insight: "What this analysis revealed"
    implication: "How this affects future decisions"
    generalization: "How this applies to other situations"

next_steps:
  immediate_actions:
    - action: "What to do right away"
      timeline: "When to complete this"
      owner: "Who is responsible"
  
  monitoring_plan:
    - metric: "What to track after implementation"
      frequency: "How often to measure"
      trigger: "What would indicate need to reconsider"
  
  review_schedule:
    - milestone: "When to formally review decision"
      focus: "What aspects to evaluate"
      criteria: "How to judge if decision was good"
```

## Quality Validation Checklist

Before finalizing decision analysis:
- [ ] Are all important criteria included?
- [ ] Do weights properly reflect stakeholder values?
- [ ] Are scores based on reliable information?
- [ ] Is the decision robust to reasonable assumption changes?
- [ ] Have we considered implementation challenges?
- [ ] Do results pass "gut check" for reasonableness?
- [ ] Can we explain the recommendation clearly to stakeholders?

## Common Decision Analysis Pitfalls

1. **Criteria Overlap**: Double-counting similar factors
2. **Weight Anchoring**: First weight assignments become fixed
3. **Scoring Bias**: Unconsciously favoring preferred alternatives  
4. **False Precision**: Over-confident in uncertain scores
5. **Analysis Paralysis**: Endless refinement instead of deciding
6. **Context Ignorance**: Ignoring implementation realities

## Integration with Other Methods

**Precede With**: Problem definition and solution generation
**Follow With**: Implementation planning and risk management
**Combine With**: Stakeholder analysis and change management
**Support With**: Data analysis and expert consultation

## Success Indicators

- Decision can be clearly explained and defended
- Stakeholders understand and accept the reasoning
- Implementation proceeds smoothly without major surprises
- Post-decision review validates the choice was sound
- Decision process becomes template for future similar choices