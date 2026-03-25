#update the resource 
import requests
import json

base_url = "https://hapi.fhir.org/baseR4/Patient"
headers = {"Content-Type": "application/fhir+json"}
patient_id = "P001"
updated_patient_resource = {
    "resourceType": "Patient",
    "id": patient_id,
    "name": [{
        "use": "official",
        "family": "Saksham",
        "given": ["Pandey"] 
    }],
    "gender": "male",
    "birthDate": "1999-07-29"
}

print("Before serialisation:", updated_patient_resource)

serialised_resource = json.dumps(updated_patient_resource)
print("After serialisation:", serialised_resource)
response = requests.put(f"{base_url}/{patient_id}", headers=headers, data=serialised_resource)
print(f"Status code: {response.status_code}")
if response.status_code == 200:
    print(response.json()) 