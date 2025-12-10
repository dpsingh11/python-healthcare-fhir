'''
fhir.resources
-->build, parse, and validate FHIR resources using Python classes (auto-generated from FHIR schema)
-->strongly typed FHIR resource classes
-->pip install fhir.resources
-->
'''

#create with validation
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName

name = HumanName.model_construct()
name.family = "Doe"
name.given = ["John"]

patient = Patient.model_construct()
patient.id = "patient-001"
patient.name = [name]
patient.gender = "male"

print(patient.model_dump_json(indent=2))

#validate and create

patient_json = {
  "resourceType": "Patient",
  "id": "test",
  "name": [{"family": "Doe", "given": ["Jane"]}],
  "gender": "female"
}

patient = Patient(**patient_json)  # Auto-validates on init
print(patient.name[0].given)


# reading from a json file 

import json
from fhir.resources.observation import Observation

with open("input/observation.json") as f:
    data = json.load(f)

obs = Observation(**data)
print(obs.status, obs.code.text)

#reading multiple observations
import json
from fhir.resources.observation import Observation

with open("input/observations.json") as f:
    data = json.load(f)
print(type(data))
for obs_data in data:
    obs = Observation(**obs_data)
    print(obs.id, obs.status, obs.code.text)