import json
import csv
from scrape.extractor import scrape_ctf_writeups
from scrape.config import BASE_URL, NUM_PAGES, OUTPUT_JSON, OUTPUT_CSV

def save_dataset(dataset, json_path, csv_path):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=4)

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["title", "tags", "year", "url", "content"])
        writer.writeheader()
        writer.writerows(dataset)

if __name__ == "__main__":
    data = scrape_ctf_writeups(BASE_URL, NUM_PAGES)
    save_dataset(data, OUTPUT_JSON, OUTPUT_CSV)
    print("✅ Dataset saved to /data directory.")
