import os
import json

def fix_colab_widgets(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".ipynb"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        nb = json.load(f)

                    modified = False

                    widgets = nb.get("metadata", {}).get("widgets", {})
                    # Detect Colab-style widget metadata
                    if "application/vnd.jupyter.widget-state+json" in widgets:
                        print(f"🔧 Fixing widgets in: {full_path}")
                        nb["metadata"]["widgets"] = {
                            "state": {}
                        }
                        modified = True

                    if modified:
                        with open(full_path, "w", encoding="utf-8") as f:
                            json.dump(nb, f, indent=1, ensure_ascii=False)

                except Exception as e:
                    print(f"❌ Failed to process {full_path}: {e}")

# 👇 Replace this with your actual local notebook directory
fix_colab_widgets(r"C:\Users\ADMIN\OneDrive - Nanyang Technological University\Sparsh Data\Year 4\Final Year Project (FYP)\GitHub")
