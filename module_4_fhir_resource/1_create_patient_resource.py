# Import the Patient model and required classes from fhir.resources
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName

from fhir.resources.meta import Meta


# Step 1: Create a HumanName object for the patient
name = HumanName.model_construct()
name.given = ["John"]
name.family = "Doe"

# Step 2: Create the Patient resource
patient = Patient.model_construct()

# Add a Meta tag (optional but useful for profiles or tags)
patient.meta = Meta.model_construct()
patient.meta.versionId = "1"
patient.meta.profile = [
    "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"]

# Assign basic fields
patient.id = "12345"

patient.name = [name]  # FHIR allows multiple names
patient.gender = "male"
patient.birthDate = "1980-01-28"

print(type(patient))
print(patient)
# Step 3: Print the Python object (as dict)
print("Patient resource as Python dict:")
print(patient.model_dump())

# Step 4: Convert to FHIR JSON and print
patient_json = patient.model_dump_json(indent=2)
print("\n Patient resource as JSON:")
print(patient_json)

# Optional: Save to file
with open("output/fhir_patient.json", "w") as f:
    f.write(patient_json)

print("\n Patient resource written to output/fhir_patient.json")