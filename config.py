# config.py
import os


FHIR_BASE_URL = 'https://server.fire.ly'
HEADERS = {
    "Content-Type": "application/fhir+json"
}


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

INPUT_DIR = os.path.join(BASE_DIR, "..", "input")
os.makedirs(INPUT_DIR, exist_ok=True)