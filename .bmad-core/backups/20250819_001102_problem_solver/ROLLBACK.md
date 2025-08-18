# Problem-Solver Rollback Instructions

If you need to rollback this deployment:

```bash
# 1. Restore original files
cp .bmad-core/backups/20250819_001102_problem_solver/install-manifest.yaml .bmad-core/
cp .bmad-core/backups/20250819_001102_problem_solver/*.yaml .bmad-core/agent-teams/

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
```

**Rollback completed on**: #오후
**Backup restored from**: .bmad-core/backups/20250819_001102_problem_solver
