# Only generate a small number of CWEs for testing
test_cwes_to_generate = [
    79,
    119,
    120,
    121,
    122,
    123,
    124,
    125,
    126,
]

from config import cwec_xml_file_path


for cwe in test_cwes_to_generate:
    print(f"Generating CWE-{cwe}")

    pass
