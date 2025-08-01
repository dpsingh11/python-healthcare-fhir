import csv
import json
import uuid
# pip install requests
import requests

FHIR_SERVER = "https://hapi.fhir.org/baseR4"  # Public test server


def generate_id():
    return str(uuid.uuid4())


def validate_row(row):
    errors = []
    if not row.get('first_name'):
        errors.append('Missing first_name')
    if not row.get('last_name'):
        errors.append('Missing last_name')
    if not row.get('gender'):
        errors.append('Missing gender')
    if not row.get('birthDate'):
        errors.append('Missing birthDate')
    if not row.get('eob_status'):
        errors.append('Missing eob_status')
    if not row.get('eob_type'):
        errors.append('Missing eob_type')
    if not row.get('coverage_type'):
        errors.append('Missing coverage_type')
    return errors


def row_to_fhir_resources(row):
    patient_id = generate_id()
    coverage_id = generate_id()
    eob_id = generate_id()

    patient = {
        "resourceType": "Patient",
        "id": patient_id,
        "name": [{
            "given": [row['first_name']],
            "family": row['last_name']
        }],
        "gender": row['gender'],
        "birthDate": row['birthDate']
    }

    coverage = {
        "resourceType": "Coverage",
        "id": coverage_id,
        "status": "active",
        "type": {
            "coding": [{
                "code": row['coverage_type']
            }]
        },
        "beneficiary": {
            "reference": f"Patient/{patient_id}"
        }
    }

    eob = {
        "resourceType": "ExplanationOfBenefit",
        "id": eob_id,
        "status": row['eob_status'],
        "type": {
            "coding": [{
                "code": row['eob_type']
            }]
        },
        "patient": {
            "reference": f"Patient/{patient_id}"
        },
        "insurance": [{
            "coverage": {
                "reference": f"Coverage/{coverage_id}"
            }
        }]
    }

    return patient, coverage, eob


def build_transaction_bundle(resources):
    return {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": [{
            "resource": res,
            "request": {
                "method": "POST",
                "url": res['resourceType']
            }
        } for res in resources]
    }


def post_to_fhir_server(bundle):
    headers = {"Content-Type": "application/fhir+json"}
    response = requests.post(FHIR_SERVER, headers=headers, json=bundle)
    print(f"Server Response: {response.status_code}")
    if response.status_code >= 400:
        print(response.text)


def main(csv_file):
    valid_resources = []
    error_log = []

    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):
            errors = validate_row(row)
            if errors:
                error_log.append({
                    "row_number": idx,
                    "errors": errors,
                    "data": row
                })
                continue
            patient, coverage, eob = row_to_fhir_resources(row)
            valid_resources.extend([patient, coverage, eob])

    if valid_resources:
        bundle = build_transaction_bundle(valid_resources)

        with open('../output/valid_bundle.json', 'w') as out:
            json.dump(bundle, out, indent=2)
        print("Written valid_bundle.json")

        print("Sending bundle to FHIR server...")
        post_to_fhir_server(bundle)
    else:
        print("No valid resources found to send.")

    if error_log:
        with open('../output/error_log.json', 'w') as out:
            json.dump(error_log, out, indent=2)
        print("Written error_log.json")


if __name__ == "__main__":
    main('../input/raw_data.csv')
