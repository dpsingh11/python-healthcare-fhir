import requests
import json

FHIR_BASE_URL = "https://server.fire.ly"
HEADERS = {"Accept": "application/fhir+json"}

def fetch_filtered_patients(gender=None, last_updated_after=None):
    query_params = []

    if gender:
        query_params.append(f"gender={gender}")
    if last_updated_after:
        query_params.append(f"_lastUpdated=ge{last_updated_after}")

    query_params.append("_count=10")
    query_string = "&".join(query_params)
    url = f"{FHIR_BASE_URL}/Patient?{query_string}"

    print(url)

    all_patients = []

    while url:
        response = requests.get(url, headers=HEADERS)
        print(response.status_code)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break

        bundle = response.json()
        entries = bundle.get("entry", [])
        print(len(entries))
        all_patients.extend(entries)

        # Get the 'next' page link
        next_link = None
        for link in bundle.get("link", []):
            if link.get("relation") == "next":
                next_link = link.get("url")
                break

        url = next_link

    return all_patients


patients = fetch_filtered_patients(gender="male", last_updated_after="2025-07-28")


with open('output/filtered_bundle.json', 'w') as f:
    json.dump(patients, f, indent=2)
    print("written successfully")

print(f"Total matching patients: {len(patients)}")




#print the name details of the patients which got filterd out with above requirements 
def print_patient_names(patients):
    print(f"\nTotal matching patients: {len(patients)}\n")
    for i, entry in enumerate(patients, 1):
        patient = entry.get("resource", {})
        names = patient.get("name", [])

        if names:
            human_name = names[0]
            given = " ".join(human_name.get("given", []))
            family = human_name.get("family", "")
            full_name = f"{given} {family}".strip()
        else:
            full_name = "(No name available)"

        print(f"{i}. {full_name}")

print_patient_names(patients)

