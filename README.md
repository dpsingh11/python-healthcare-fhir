# 🩺 Healthcare IT Python Training – FHIR-Centric File Handling

This training module demonstrates how to use Python to handle healthcare data files (`CSV`, `JSON`, `NDJSON`), validate them, and convert raw data into **FHIR-compliant JSON resources**. It also shows how to bundle and post those resources to a **FHIR server** (like HAPI).

## 📦 Modules

- **File Handling**: Read/write CSV, JSON, NDJSON
- **FHIR Transformation**: Convert raw files into FHIR-compliant Patient, Coverage, EOB
- **FHIR Server Interaction**: Search and post to a FHIR server
- **FHIR Python Library**: Use `fhir.resources` to create and validate resource objects

## 📁 Project Structure

PYTHON-HEALTHCARE/
│
├── input/                            # 🔹 Input files (raw data in CSV/JSON/NDJSON)
│   ├── fhir_bundle.json
│   ├── patients.csv
│   ├── patients.ndjson
│   ├── raw_data.csv
│   ├── sample.json
│
├── module_1_json_dict/              # 🔹 JSON & Python dict basics
│   ├── 1json_dict.py
│   ├── 2nested_json.py
│   ├── 3json_load.py
│
├── module_2_file_handling/          # 🔹 File handling (CSV/JSON/NDJSON)
│   ├── 1_read_csv.py
│   ├── 2_read_fhir_json.py
│   ├── 3_validate_fhir_patients.py
│   ├── 4_match_patients.py
│   ├── 5_read_ndjson.py
│   ├── 6_convert_csv_to_fhir_ndjson.py
│   ├── 7_ndjson_to_bundle.py
│   └── 8_bundle_to_ndjson.py
│
├── module_3_fhir_resource/          # 🔹 Using `fhir.resources` package
│   ├── create_patient_resource.py
│   ├── create_patient_coverage_eob_bundle.py
│   ├── intro.txt
│   ├── parse_fhir_response.py
│   └── validate_patient_resource.py
│
├── module_4_use_cases/              # 🔹 Real-world workflows
│   └── 1_process_csv_to_fhir_bundle.py
│
├── output/                          # 🔹 Processed/validated/generated FHIR output
│   ├── converted_patients.ndjson
│   ├── error_log.json
│   ├── extracted_patients.ndjson
│   ├── fhir_patient.json
│   ├── linked_bundle.json
│   ├── patient_bundle.json
│   ├── updated_sample.json
│   └── valid_bundle.json
│__ docs/                            # related documets 
├── requirements.txt                 # 📦 Python dependencies
└── README.md                        # 📘 Project documentation

## 📁 Folder Structure

- `input/`: Raw CSV/JSON files
- `output/`: Validated and converted FHIR resources
- `error_output/`: Rows/resources that failed validation
- `docs/`: Word documents and theory material
- `module_*/`: Python scripts for each concept

## 📦 Python Libraries Used

| Library     | Purpose                                 | Install         |
|-------------|-----------------------------------------|-----------------|
| `csv`       | Parse CSV files                         | Built-in        |
| `json`      | Read/write JSON/NDJSON                  | Built-in        |
| `uuid`      | Generate UUIDs for FHIR IDs             | Built-in        |
| `requests`  | POST bundles to FHIR server             | `pip install requests` |
| `fhir.resources`  | FHIR Resources as Model Class           | `pip install fhir.resources` |
----------------------------------------------------------------------------------------------------

https://pypi.org/project/fhir.resources/

## 🔧 Setup

```bash
pip install -r requirements.txt

---
