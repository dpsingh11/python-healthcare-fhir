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
input_csv = "input/patients.csv"
template_dir = "templates"
template_file = "patient_template.txt"
output_json = "output/patient_transaction_bundle.json"
os.makedirs("output", exist_ok=True)

# Jinja2 Environment
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template(template_file)

entries = []

# Read and transform each CSV row
with open(input_csv, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
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
with open(output_json, "w") as f:
    json.dump(bundle, f, indent=2)

print(f"Transaction bundle written to: {output_json}")