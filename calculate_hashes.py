#!/usr/bin/env python3
"""
Calculate hashes for new Problem-Solver files to update install-manifest.yaml
"""

import hashlib
import yaml
import os
from datetime import datetime

def calculate_file_hash(filepath):
    """Calculate hash for BMad manifest (matches existing format)"""
    try:
        with open(filepath, 'rb') as f:
            content = f.read()
        return hashlib.md5(content).hexdigest()[:16]
    except FileNotFoundError:
        return None

def main():
    """Calculate hashes for all new problem-solver files"""
    
    new_files = [
        '.bmad-core/agents/problem-solver.md',
        '.bmad-core/tasks/first-principles-analysis.md',
        '.bmad-core/tasks/root-cause-investigation.md', 
        '.bmad-core/tasks/problem-decomposition.md',
        '.bmad-core/tasks/solution-synthesis.md',
        '.bmad-core/tasks/decision-analysis.md',
        '.bmad-core/templates/problem-definition-tmpl.yaml',
        '.bmad-core/templates/solution-matrix-tmpl.yaml',
        '.bmad-core/templates/decision-record-tmpl.yaml',
    ]
    
    print("=== BMad Problem-Solver File Hashes ===\n")
    
    manifest_entries = []
    
    for filepath in new_files:
        hash_value = calculate_file_hash(filepath)
        if hash_value:
            manifest_entries.append({
                'path': filepath,
                'hash': hash_value,
                'modified': False
            })
            print(f"✅ {filepath}")
            print(f"   Hash: {hash_value}")
        else:
            print(f"❌ {filepath}: File not found")
    
    # Also check modified files
    modified_files = [
        '.bmad-core/agent-teams/team-fullstack.yaml',
        '.bmad-core/agent-teams/team-no-ui.yaml'
    ]
    
    print(f"\n=== Modified Files ===\n")
    
    for filepath in modified_files:
        hash_value = calculate_file_hash(filepath)
        if hash_value:
            manifest_entries.append({
                'path': filepath,
                'hash': hash_value,
                'modified': True  # These were modified
            })
            print(f"✅ {filepath}")
            print(f"   Hash: {hash_value} (updated)")
        else:
            print(f"❌ {filepath}: File not found")
    
    # Generate YAML entries to add to manifest
    print(f"\n=== Add to install-manifest.yaml ===\n")
    
    # Read current manifest
    manifest_path = '.bmad-core/install-manifest.yaml'
    try:
        with open(manifest_path, 'r') as f:
            manifest = yaml.safe_load(f)
    except FileNotFoundError:
        print("❌ install-manifest.yaml not found!")
        return 1
    
    # Update or add entries
    current_files = {entry['path']: entry for entry in manifest.get('files', [])}
    
    for entry in manifest_entries:
        path = entry['path']
        if path in current_files:
            # Update existing entry
            current_files[path]['hash'] = entry['hash']
            current_files[path]['modified'] = entry['modified']
            print(f"📝 Updated: {path}")
        else:
            # Add new entry
            manifest['files'].append(entry)
            print(f"➕ Added: {path}")
    
    # Update manifest metadata
    manifest['version'] = '4.39.2-problem-solver'
    manifest['installed_at'] = datetime.now().isoformat() + 'Z'
    
    # Write updated manifest
    with open(manifest_path, 'w') as f:
        yaml.dump(manifest, f, default_flow_style=False, sort_keys=False)
    
    print(f"\n✅ Updated {manifest_path}")
    print(f"📊 Total files in manifest: {len(manifest['files'])}")
    print(f"🆕 New files added: {len([e for e in manifest_entries if not e['modified']])}")
    print(f"📝 Modified files updated: {len([e for e in manifest_entries if e['modified']])}")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())