import csv
import json
import os
from jinja2 import Environment, FileSystemLoader
'''
Jinja2 is a templating engine for Python, 
used to create dynamic text files (like HTML, JSON, or FHIR resources) 
by mixing static text with dynamic values (placeholders).
pip install jinja2
'''
# Paths
# Base directory (project root assumed to be one level above this script)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_CSV = os.path.join(BASE_DIR, "input", "patients.csv")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATE_FILE = "patient_template.txt"
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_JSON = os.path.join(OUTPUT_DIR, "patient_transaction_bundle.json")

# Create output directory if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ----------- JINJA2 TEMPLATE -------------
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

entries = []

# Read and transform each CSV row
with open(INPUT_CSV, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name_parts = row["name"].strip().split(" ", 1)
        row["given"] = name_parts[0]
        row["family"] = name_parts[1] if len(name_parts) > 1 else ""
        resource_str = template.render(**row)
        patient_resource = json.loads(resource_str)
        
        entry = {
            "resource": patient_resource,
            "request": {
                "method": "PUT",
                "url": f"Patient/{row['id']}"
            }
        }
        entries.append(entry)

# Wrap as transaction bundle
bundle = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": entries
}

# Write to file
with open(OUTPUT_JSON, "w") as f:
    json.dump(bundle, f, indent=2)

print(f"Transaction bundle written to: {OUTPUT_JSON}")