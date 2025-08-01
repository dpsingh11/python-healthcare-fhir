'''
1. Read CSV file
2. Create individual FHIR Patient resources
3. Wrap them in a FHIR Bundle of type batch
4. POST the bundle to the FHIR server
'''
import csv
import json
import requests

#FHIR_BASE_URL = "https://server.fire.ly" 
FHIR_BASE_URL = "http://hapi.fhir.org/baseR4" 
HEADERS = {"Content-Type": "application/fhir+json"}

def build_patient_resource(row):
    print(f"converting the individiual patient row {row} in fhir json format")
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

def build_bundle_from_csv(csv_path):
    print("okay i have reacher here inside build_bundle_from_csv")
    bundle = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": []
    }

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"iterating over the csv row individually : {row}")
            patient_id = row["id"]
            patient_resource = build_patient_resource(row)
            bundle["entry"].append({
                "resource": patient_resource,
                "request": {
                    "method": "PUT",
                    "url": f"Patient/{patient_id}"
                }
            })
    
    return bundle

def post_bundle_to_fhir(bundle):
    response = requests.post(FHIR_BASE_URL, headers=HEADERS, data=json.dumps(bundle))
    print(f"Status: {response.status_code}")
    if response.ok:
        print("Bundle uploaded successfully.")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Error uploading bundle:")
        print(response.text)

# starting point 
csv_file_path = "input/patients.csv"
print("starting ......")
bundle = build_bundle_from_csv(csv_file_path)
post_bundle_to_fhir(bundle)

'''
batch vs transaction 

batch processing should continue processing all entries independently and 
return individual success/failure results.

transaction processing is atomic — all-or-nothing — and should fail the entire bundle 
if any entry fails.

'''