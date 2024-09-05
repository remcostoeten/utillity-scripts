import argparse
import os
import re
from typing import List, Set

def extract_classes_from_scss(file_path: str) -> Set[str]:
    with open(file_path, 'r') as f:
        content = f.read()
    
    # This regex pattern attempts to match class definitions in SCSS
    class_pattern = r'\.([a-zA-Z0-9_-]+)'
    return set(re.findall(class_pattern, content))

def extract_classes_from_tsx(file_path: str) -> Set[str]:
    with open(file_path, 'r') as f:
        content = f.read()
    
    # This regex pattern attempts to match class usage in TSX files
    class_pattern = r'className="([^"]*)"'
    class_strings = re.findall(class_pattern, content)
    
    classes = set()
    for class_string in class_strings:
        classes.update(class_string.split())
    
    return classes

def find_tsx_files(directory: str) -> List[str]:
    tsx_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.tsx'):
                tsx_files.append(os.path.join(root, file))
    return tsx_files

def check_unused_classes(scss_file: str, tsx_files: List[str]) -> Set[str]:
    scss_classes = extract_classes_from_scss(scss_file)
    used_classes = set()
    
    for tsx_file in tsx_files:
        used_classes.update(extract_classes_from_tsx(tsx_file))
    
    return scss_classes - used_classes

def main():
    parser = argparse.ArgumentParser(description="Check for unused SCSS/CSS classes in TSX files")
    parser.add_argument("--app", action="store_true", help="Check only src/app directory")
    parser.add_argument("--components", action="store_true", help="Check only src/components directory")
    parser.add_argument("--checkSingle", type=str, help="Check a single SCSS file")
    args = parser.parse_args()

    if args.checkSingle:
        scss_file = args.checkSingle
        tsx_files = find_tsx_files("src")
    elif args.app:
        scss_file = "app.scss"  # Assuming app.scss is in the root directory
        tsx_files = find_tsx_files("src/app")
    elif args.components:
        scss_file = "app.scss"  # Assuming app.scss is in the root directory
        tsx_files = find_tsx_files("src/components")
    else:
        scss_file = "app.scss"  # Assuming app.scss is in the root directory
        tsx_files = find_tsx_files("src")

    unused_classes = check_unused_classes(scss_file, tsx_files)

    if unused_classes:
        print(f"Unused classes found in {scss_file}:")
        for cls in unused_classes:
            print(f"- {cls}")
    else:
        print(f"No unused classes found in {scss_file}")

if __name__ == "__main__":
    main()
