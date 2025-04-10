import os
import json

# 👇 Replace with your exact folder path
folder = r"C:\Users\ADMIN\OneDrive - Nanyang Technological University\Sparsh Data\Year 4\Final Year Project (FYP)\GitHub"

for root, _, files in os.walk(folder):
    for file in files:
        if file.endswith(".ipynb"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                nb = json.load(f)

            # Fix widget metadata if needed
            widgets = nb.get("metadata", {}).get("widgets", None)
            if widgets is not None and "state" not in widgets:
                print(f"Fixing: {path}")
                nb["metadata"]["widgets"]["state"] = {}

                with open(path, "w", encoding="utf-8") as f:
                    json.dump(nb, f, indent=1, ensure_ascii=False)
