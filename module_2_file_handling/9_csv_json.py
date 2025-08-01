import json
import csv

patients = []

with open("input/patients.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        patients.append(row)

# Serialize to JSON
with open("output/patients.json", "w") as f:
    json.dump(patients, f, indent=2)

print("Converted CSV → JSON")

# bundle = {
#     "resourceType": "Bundle",
#     "type": "collection",
#     "entry": patients  # placing the list inside an object
# }

# with open("output/patients.json", "w") as f:
#     json.dump(bundle, f, indent=2)
