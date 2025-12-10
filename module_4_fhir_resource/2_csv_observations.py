import csv
import os
from fhir.resources.observation import Observation
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.quantity import Quantity
#from fhir.resources.fhirreference import FHIRReference
from fhir.resources.reference import Reference

# Create list to store observations
observations = []

# Read CSV file
input_file = "input/observations.csv"
output_file = "output/observations.ndjson"
os.makedirs("output", exist_ok=True)

with open(input_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        obs = Observation(
            id=row["id"],
            status=row["status"],
            code=CodeableConcept(text=row["code_text"]),
            valueQuantity=Quantity(
                value=float(row["value"]),
                unit=row["unit"]
            ),
            subject=Reference(reference=row["subject"])
        )
        observations.append(obs)

# Write to NDJSON file
with open(output_file, "w") as f:
    for obs in observations:
        f.write(obs.json() + "\n")

print(f"Converted {len(observations)} observations to {output_file}")
