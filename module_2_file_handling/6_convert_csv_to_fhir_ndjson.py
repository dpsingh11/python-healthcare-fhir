import csv
import json


def csv_to_fhir_patient(row):
    name = row['name']
    first_name, last_name = name.split(' ')
    return {
        "resourceType": "Patient",
        "id": row['id'],
        "name": [{
            "given": [first_name],
            "family": last_name
        }],
        "gender": row['gender'],
        "birthDate": row['birthDate']
    }


def convert_and_write_ndjson(csv_path, ndjson_path):
    with open(csv_path) as f_in, open(ndjson_path, 'w') as f_out:
        reader = csv.DictReader(f_in)
        for row in reader:
            patient = csv_to_fhir_patient(row)
            f_out.write(json.dumps(patient) + '\n')


if __name__ == "__main__":
    convert_and_write_ndjson(
        'input/patients.csv', 'output/converted_patients.ndjson')
