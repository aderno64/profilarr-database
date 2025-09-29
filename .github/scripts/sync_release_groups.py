import sys
import json
import yaml
import os

# --- Configuration ---
FLAT_PATTERN_KEY = 'pattern'
SOURCE_CONDITIONS_KEY = 'conditions'
RELEASE_GROUP_TYPE = 'release_group'
REGEX_DELIMITER = '|'
REGEX_PREFIX = r'(?<=^|[\s.-])('
REGEX_SUFFIX = r')\b'

def load_yaml(filepath):
    """Loads a YAML file and handles non-existent files gracefully."""
    if not os.path.exists(filepath):
        return {
            'name': os.path.basename(filepath).replace('.yml', '').replace('Dictionarry ', ''),
            FLAT_PATTERN_KEY: '',
            'description': '',
            'tags': ['- Release Group Tier'],
            'tests': []
        }
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def save_yaml(filepath, data):
    """Saves data back to a YAML file with consistent formatting."""
    with open(filepath, 'w') as f:
        yaml.safe_dump(data, f, sort_keys=False)

def collect_groups_from_flat_pattern(pattern_string):
    """Extracts groups from a single regex pattern (used for comparison)."""
    if not pattern_string or REGEX_PREFIX not in pattern_string or REGEX_SUFFIX not in pattern_string:
        return set()
    
    start = pattern_string.find(REGEX_PREFIX) + len(REGEX_PREFIX)
    end = pattern_string.find(REGEX_SUFFIX, start)
    
    if start != -1 and end != -1:
        group_string = pattern_string[start:end]
        return set(group for group in group_string.split(REGEX_DELIMITER) if group)
    
    return set()

def collect_groups_from_conditions(data):
    """
    Extracts group names from the conditions list in the source files.
    Returns a set of groups.
    """
    groups = set()
    conditions = data.get(SOURCE_CONDITIONS_KEY, [])
    
    for item in conditions:
        if isinstance(item, dict) and item.get('type') == RELEASE_GROUP_TYPE:
            group_name = item.get('pattern')
            if group_name:
                groups.add(group_name)
                
    return groups

def process_and_mirror_groups(source_data, target_data):
    """
    Performs a Pure Mirror Sync: ONLY uses groups collected from the source file.
    Any group in the target but not the source will be removed.
    """
    
    # 1. Collect ONLY the groups from the SOURCE file (The single source of truth)
    all_groups = collect_groups_from_conditions(source_data)
    
    # 2. Sort the unique groups alphabetically
    final_groups_list = [group for group in all_groups if group]
    final_groups_list.sort(key=str.lower)

    # 3. Construct the new, sorted regex pattern
    new_group_string = REGEX_DELIMITER.join(final_groups_list)
    new_pattern = REGEX_PREFIX + new_group_string + REGEX_SUFFIX

    # 4. Get the current pattern string from the target for comparison
    target_pattern = target_data.get(FLAT_PATTERN_KEY, '')

    # --- Check for Change ---
    # The script saves only if the new, desired pattern differs from the existing one.
    changed = new_pattern != target_pattern

    # 5. Update the target data structure's single pattern key
    target_data[FLAT_PATTERN_KEY] = new_pattern

    return target_data, changed

def main(file_map_path):
    """Main function to orchestrate the synchronization process."""
    if not os.path.exists(file_map_path):
        print(f"Error: File map not found at {file_map_path}")
        sys.exit(1)

    with open(file_map_path, 'r') as f:
        file_map = json.load(f)

    source_dir = 'source_files'
    total_changes = 0

    for source_file_name, target_file_path in file_map.items():
        source_file_path = os.path.join(source_dir, os.path.basename(source_file_name))
        
        if not os.path.exists(source_file_path):
            print(f"Warning: Source file not found: {source_file_path}. Skipping.")
            continue

        print(f"Processing: {os.path.basename(source_file_path)} -> {target_file_path}")

        source_data = load_yaml(source_file_path)
        target_data = load_yaml(target_file_path)
        
        try:
            updated_target_data, changed = process_and_mirror_groups(source_data, target_data)
        except Exception as e:
            print(f"Error processing groups for {target_file_path}: {e}")
            continue

        if changed:
            save_yaml(target_file_path, updated_target_data)
            print("=> SUCCESSFULLY MIRRORED AND SORTED (Changes written).")
            total_changes += 1
        else:
            print("=> No changes detected. Skipping file write.")

    print(f"\n--- Synchronization Complete: {total_changes} file(s) were modified. ---")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sync_release_groups.py <file_map.json>")
        sys.exit(1)
    
    main(sys.argv[1])
