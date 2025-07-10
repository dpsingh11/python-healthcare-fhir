# Use parse_obj() to load and safely interact with any FHIR resource from a FHIR server or test JSON.
from fhir.resources.patient import Patient
import json
import requests
base_url = "http://hapi.fhir.org/baseR5"

url = f"{base_url}/Patient?_count=10&_total=accurate"
# Load FHIR response
res = requests.get(url, headers={"Accept": "application/fhir+json"})
print(type(res))
if res.status_code == 200:
    bundle = res.json()
    if "entry" in bundle:
        print(f"\n🔎 Total Matches (accurate): {bundle.get('total')}")
        print(f"🔢 Showing {len(bundle['entry'])} patients:\n")

        for i, entry in enumerate(bundle["entry"], start=1):
            try:
                # Get only the resource (Patient) from Bundle.entry
                patient_data = entry["resource"]
                # ✅ Use model_validate (Pydantic v2+)
                patient = Patient.model_validate(patient_data)

                print(f"👤 Patient {i}:")
                if 'name' in patient:
                    name = patient.name[0]
                    print(f"  • Name   : {' '.join(name.given)} {name.family}")
                print(f"  • Gender : {patient.gender}")
                print(f"  • DOB    : {patient.birthDate}")

                print(f"  • id    : {patient.id}")

            except ValidationError as e:
                print(f"❌ Failed to validate patient {i}:")
                print(e)
            except Exception as e:
                print(str(e))
    else:
        print("⚠️ No patient entries found in bundle.")
else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")

# print(type(data))
# # print(data)
# # print(res.data)


# # with open("input/sample_patient_response.json") as f:
# #     data = json.load(f)

# # Parse and validate
# try:
#     patients = data['entry']
#     for patient in patients:
#         patient = Patient.parse_obj(patient)
#         print("✅ Valid Patient resource")
#         print(f"Name: {patient.name[0].given[0]} {patient.name[0].family}")
#         print(f"DOB: {patient.birthDate}")
# except Exception as e:
#     print("❌ Invalid FHIR Patient:", str(e))
