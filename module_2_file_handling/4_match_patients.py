import csv
import json


def load_csv_ids(file_path):
    # set is unordered collection of unique items
    ids = set()
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids.add(row['id'])
    return ids


def find_matching_patients(json_path, patient_ids):
    with open(json_path) as f:
        bundle = json.load(f)

    print("Matching Patients:")
    for entry in bundle.get('entry', []):
        resource = entry.get('resource', {})
        if resource.get('resourceType') == 'Patient' and resource.get('id') in patient_ids:
            name = resource.get('name', [{}])[0]
            given = name.get('given', [''])[0]
            family = name.get('family', '')
            print(f"Matched: {given} {family} (ID: {resource.get('id')})")


if __name__ == "__main__":
    patient_ids = load_csv_ids('input/patients.csv')
    find_matching_patients('input/fhir_bundle.json', patient_ids)

# next instead of id match with patiet do demographic match - name,dob,gender
