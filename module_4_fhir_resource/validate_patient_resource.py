import os
from fhir.resources.patient import Patient

# Step 1: Define patient data as a dictionary
patient_data = {
    "resourceType": "Patient",
    "id": "12345",
    "name": [{
        "given": ["John"],
        "family": "Doe"
    }],
    "birthDate": "1980-07-31",  # try with Invalid date format
    "meta": {
        "versionId": "1",
        "profile": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"]
    }
}

# Step 2: Create a Patient object with validation
try:
    patient = Patient(**patient_data)
except ValueError as e:
    print(str(e))

# Step 3: Print as Python dict
print("Patient as Python dict:")
print(patient.model_dump())

# Step 4: Print as JSON
print("\n Patient as JSON:")
print(patient.model_dump_json(indent=2))

# Step 5: Write to file
os.makedirs("output", exist_ok=True)
with open("output/fhir_patient.json", "w") as f:
    f.write(patient.model_dump_json(indent=2))

print("\n Patient resource written to output/fhir_patient.json")
