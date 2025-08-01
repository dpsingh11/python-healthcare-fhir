import requests
import time  

FHIR_BASE_URL = "https://server.fire.ly"
HEADERS = {"Accept": "application/fhir+json"}

def fetch_all_patients():
    url = f"{FHIR_BASE_URL}/Patient?_count=50"
    all_patients = []

    while url:
        response = requests.get(url, headers=HEADERS)
        print(url)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break

        bundle = response.json()
        entries = bundle.get("entry", [])
        print(len(entries))
        # extend --- to append a list to a list we use extend 
        all_patients.extend(entries)

        # Find 'next' link if available
        next_link = None
        for link in bundle.get("link", []):
            if link.get("relation") == "next":
                next_link = link.get("url")
                break

        url = next_link  # Move to next page

    return all_patients


start_time = time.time()  

patients = fetch_all_patients()

end_time = time.time()  
elapsed_time = end_time - start_time  

print(f"Total patients fetched: {len(patients)}")
print(f"Time taken: {elapsed_time:.2f} seconds")
