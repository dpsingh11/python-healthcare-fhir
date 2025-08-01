import csv
import json
import requests

FHIR_BASE_URL = "https://server.fire.ly"  
HEADERS = {"Content-Type": "application/fhir+json"}

def build_patient_resource(row):
    first_name, last_name = row["name"].split(' ')
    return {
        "resourceType": "Patient",
        "id": row["id"],
        "name": [{
            "use": "official",
            "family": last_name,
            "given": [first_name]
        }],
        "gender": row["gender"],
        "birthDate": row["birthDate"]
    }

def upload_patients_individually(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            patient = build_patient_resource(row)
            patient_id = patient["id"]
            url = f"{FHIR_BASE_URL}/Patient/{patient_id}"
            response = requests.put(url, headers=HEADERS, data=json.dumps(patient))

            print(f"Uploading Patient/{patient_id} - Status: {response.status_code}")
            if response.ok:
                print("Success")
            else:
                print("Failed:", response.text)


csv_file_path = "input/patients.csv"
upload_patients_individually(csv_file_path)