import os
import json

def fix_notebooks_metadata(base_dir):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".ipynb"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        nb = json.load(f)

                    if "widgets" in nb.get("metadata", {}):
                        # If 'state' is missing or malformed, fix it
                        if not isinstance(nb["metadata"]["widgets"].get("state", {}), dict):
                            nb["metadata"]["widgets"]["state"] = {}

                        # Optional: clean up unused fields (optional)
                        nb["metadata"]["widgets"] = {
                            "state": nb["metadata"]["widgets"]["state"]
                        }

                    with open(full_path, 'w', encoding='utf-8') as f:
                        json.dump(nb, f, indent=1, ensure_ascii=False)

                    print(f"✔ Fixed: {full_path}")
                except Exception as e:
                    print(f"✘ Error fixing {full_path}: {e}")

# Replace with your actual path (use raw string or double backslashes on Windows)
fix_notebooks_metadata(r"C:\Users\ADMIN\OneDrive - Nanyang Technological University\Sparsh Data\Year 4\Final Year Project (FYP)\GitHub")
