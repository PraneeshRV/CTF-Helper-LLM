import os
import json
import pandas as pd
import markdown2
from tqdm import tqdm

# Set your root folder here (repo directory)
ROOT_DIR = "."

# Output paths
CSV_PATH = "compiled_dataset.csv"
JSON_PATH = "compiled_dataset.json"

# Dataset list
dataset = []

# Loop through the structure
for category in tqdm(os.listdir(ROOT_DIR)):
    cat_path = os.path.join(ROOT_DIR, category)
    if not os.path.isdir(cat_path):
        continue

    for challenge in os.listdir(cat_path):
        chal_path = os.path.join(cat_path, challenge)
        if not os.path.isdir(chal_path):
            continue

        writeup_path = os.path.join(chal_path, "writeup.md")
        image_folder = os.path.join(chal_path, "images")
        image_files = []

        # Collect images
        if os.path.isdir(image_folder):
            image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

        # Read markdown content
        writeup_text = ""
        if os.path.exists(writeup_path):
            with open(writeup_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
                writeup_text = markdown2.markdown(markdown_content)
                writeup_text = markdown2.markdown(writeup_text)

        # Add to dataset
        dataset.append({
            "category": category,
            "challenge": challenge,
            "text": writeup_text,
            "images": image_files
        })

# Save JSON
with open(JSON_PATH, 'w', encoding='utf-8') as jf:
    json.dump(dataset, jf, indent=2, ensure_ascii=False)

# Save CSV
df = pd.DataFrame(dataset)
df.to_csv(CSV_PATH, index=False)
