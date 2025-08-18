#!/bin/bash
# BMad Problem-Solver Agent Deployment Script

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
print_header() {
    echo -e "${BLUE}=== $1 ===${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

main() {
    print_header "BMad Problem-Solver Agent Deployment"
    echo "Version: 1.0.0"
    echo "Date: $(date)"
    echo

    # Check BMad installation
    if [ ! -d ".bmad-core" ]; then
        print_error "Error: .bmad-core directory not found"
        print_info "Please run from BMad project root directory"
        exit 1
    fi
    
    print_success "BMad installation detected"

    # Create backup
    print_header "Creating Backup"
    BACKUP_DIR=".bmad-core/backups/$(date +%Y%m%d_%H%M%S)_problem_solver"
    mkdir -p "$BACKUP_DIR"

    # Backup critical files that will be modified
    if [ -f ".bmad-core/install-manifest.yaml" ]; then
        cp ".bmad-core/install-manifest.yaml" "$BACKUP_DIR/"
        print_success "Backed up install-manifest.yaml"
    fi

    for team_file in .bmad-core/agent-teams/*.yaml; do
        if [ -f "$team_file" ]; then
            cp "$team_file" "$BACKUP_DIR/"
            filename=$(basename "$team_file")
            print_success "Backed up $filename"
        fi
    done

    print_info "Backup created at: $BACKUP_DIR"

    # Validate all components exist
    print_header "Validating Components"
    
    required_files=(
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

    missing_files=()
    for file in "${required_files[@]}"; do
        if [ -f "$file" ]; then
            size=$(wc -c < "$file")
            print_success "$(basename "$file") (${size} bytes)"
        else
            missing_files+=("$file")
            print_error "Missing: $file"
        fi
    done

    if [ ${#missing_files[@]} -gt 0 ]; then
        print_error "Deployment cannot proceed - missing required files"
        exit 1
    fi

    # Validate YAML files
    print_header "Validating YAML Structure"
    
    yaml_files=(
        ".bmad-core/templates/problem-definition-tmpl.yaml"
        ".bmad-core/templates/solution-matrix-tmpl.yaml"
        ".bmad-core/templates/decision-record-tmpl.yaml"
        ".bmad-core/workflows/complex-problem-solving.yaml"
    )

    for file in "${yaml_files[@]}"; do
        if python3 -c "import yaml; yaml.safe_load(open('$file'))" 2>/dev/null; then
            print_success "$(basename "$file"): Valid YAML"
        else
            print_error "$(basename "$file"): Invalid YAML structure"
            exit 1
        fi
    done

    # Run comprehensive tests
    print_header "Running Test Suite"
    
    if [ -f ".bmad-core/tests/run_all_tests.sh" ]; then
        bash .bmad-core/tests/run_all_tests.sh
        if [ $? -eq 0 ]; then
            print_success "All tests passed"
        else
            print_warning "Some tests failed - check test output above"
            echo "Continue anyway? (y/N)"
            read -r response
            if [[ ! "$response" =~ ^[Yy]$ ]]; then
                exit 1
            fi
        fi
    else
        print_warning "Test suite not found - skipping tests"
    fi

    # Verify agent team configurations
    print_header "Verifying Agent Team Integration"
    
    for team in team-fullstack.yaml team-no-ui.yaml; do
        team_file=".bmad-core/agent-teams/$team"
        if [ -f "$team_file" ]; then
            if grep -q "problem-solver" "$team_file" || grep -q "\*" "$team_file"; then
                print_success "$team: Problem-solver integrated"
            else
                print_warning "$team: Problem-solver not found (may need manual addition)"
            fi
        fi
    done

    # Verify install manifest
    print_header "Verifying Install Manifest"
    
    if grep -q "problem-solver" .bmad-core/install-manifest.yaml; then
        version=$(grep "version:" .bmad-core/install-manifest.yaml | head -1 | cut -d' ' -f2)
        print_success "Install manifest updated (version: $version)"
    else
        print_error "Install manifest not properly updated"
        exit 1
    fi

    # Create deployment summary
    print_header "Deployment Summary"
    
    echo "📦 Problem-Solver Agent Successfully Deployed!"
    echo
    echo "🎯 New Capabilities:"
    echo "   • Systematic problem analysis with 15+ methodologies"
    echo "   • Creative solution generation using innovation frameworks"
    echo "   • Quantitative decision support with sensitivity analysis"
    echo "   • Comprehensive documentation of analysis and decisions"
    echo
    echo "🚀 How to Use:"
    echo "   1. *agent problem-solver     (activate Sage)"
    echo "   2. *help                     (see all commands)"
    echo "   3. *create-problem-def       (start with problem definition)"
    echo "   4. *workflow complex-problem-solving (full analysis)"
    echo
    echo "📚 Documentation:"
    echo "   • User Guide: .bmad-core/docs/problem-solver-guide.md"
    echo "   • Handoff Protocols: .bmad-core/utils/problem-solver-handoffs.md"
    echo "   • Release Notes: .bmad-core/RELEASE_NOTES.md"
    echo
    echo "🛡️  Backup Location: $BACKUP_DIR"
    
    # Create rollback instructions
    cat > "$BACKUP_DIR/ROLLBACK.md" << EOF
# Problem-Solver Rollback Instructions

If you need to rollback this deployment:

\`\`\`bash
# 1. Restore original files
cp $BACKUP_DIR/install-manifest.yaml .bmad-core/
cp $BACKUP_DIR/*.yaml .bmad-core/agent-teams/

# 2. Remove problem-solver files
rm -f .bmad-core/agents/problem-solver.md
rm -f .bmad-core/tasks/first-principles-analysis.md
rm -f .bmad-core/tasks/root-cause-investigation.md
rm -f .bmad-core/tasks/problem-decomposition.md
rm -f .bmad-core/tasks/solution-synthesis.md
rm -f .bmad-core/tasks/decision-analysis.md
rm -f .bmad-core/templates/problem-definition-tmpl.yaml
rm -f .bmad-core/templates/solution-matrix-tmpl.yaml
rm -f .bmad-core/templates/decision-record-tmpl.yaml
rm -f .bmad-core/workflows/complex-problem-solving.yaml
rm -f .bmad-core/utils/problem-solver-handoffs.md
rm -f .bmad-core/docs/problem-solver-guide.md
rm -f .bmad-core/RELEASE_NOTES.md

# 3. Verify rollback
ls -la .bmad-core/agents/problem-solver.md  # Should show "No such file"
\`\`\`

**Rollback completed on**: $(date)
**Backup restored from**: $BACKUP_DIR
EOF

    print_info "Rollback instructions saved to: $BACKUP_DIR/ROLLBACK.md"
    
    # Final success message
    print_header "Deployment Complete"
    print_success "BMad Problem-Solver Agent is now ready for use!"
    print_info "Try: *agent problem-solver to get started"
    
    echo
    echo "🧠 Sage is ready to help you solve complex problems systematically!"
    echo "🎯 Apply first principles thinking, TRIZ innovation, and MCDA decision analysis"
    echo "🚀 From root cause investigation to creative solution synthesis"
    
    return 0
}

# Execute main function
main "$@"