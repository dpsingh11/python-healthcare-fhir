from fhir.resources.bundle import Bundle
from fhir.resources.patient import Patient
from fhir.resources.coverage import Coverage
from fhir.resources.explanationofbenefit import ExplanationOfBenefit
from fhir.resources.meta import Meta
from fhir.resources.humanname import HumanName
from fhir.resources.reference import Reference
import uuid
import json
import os
import datetime


def generate_id():
    return str(uuid.uuid4())


# Create Patient
patient_id = generate_id()
patient = Patient(
    id=patient_id,
    name=[HumanName(given=["Alice"], family="Smith")],
    gender="female",
    birthDate="1985-05-05",
    meta=Meta(
        profile=["http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"])
)

# Create Coverage
coverage_id = generate_id()
coverage = Coverage(
    id=coverage_id,
    status="active",
    kind="insurance",
    type={"coding": [{"code": "plan"}]},
    beneficiary=Reference(reference=f"Patient/{patient_id}")
)

# Create ExplanationOfBenefit
eob_id = generate_id()
eob = ExplanationOfBenefit(
    id=eob_id,
    status="active",
    use="claim",
    type={"coding": [{"code": "professional"}]},
    patient=Reference(reference=f"Patient/{patient_id}"),
    created=datetime.date.today(),
    outcome="completed",
    insurance=[{
        "coverage": Reference(reference=f"Coverage/{coverage_id}"),
        "focal": True
    }]
)

# Create Transaction Bundle
bundle = Bundle(
    type="transaction",
    entry=[
        {"resource": patient, "request": {"method": "POST", "url": "Patient"}},
        {"resource": coverage, "request": {"method": "POST", "url": "Coverage"}},
        {"resource": eob, "request": {"method": "POST", "url": "ExplanationOfBenefit"}}
    ]
)

# Output
os.makedirs("output", exist_ok=True)
with open("output/linked_bundle.json", "w") as f:
    f.write(bundle.json(indent=2))

print("✅ Bundle written to output/linked_bundle.json")
