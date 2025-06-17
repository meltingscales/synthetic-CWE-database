from SyntheticCWEDatabase.cwecxmlhelper import CWECXMLHelper
from SyntheticCWEDatabase.config import cwec_xml_file_path, generated_cwes_output_folder

import os
import json


def generate_one_cwe(cwe_id: int, language: str):

    # TODO generate manifest correctly, respecting it if it already exists
    # TODO make helper methods to set up files and folders

    print(f"Generating CWE-{cwe_id}")

    helper = CWECXMLHelper(cwec_xml_file_path)

    xml = helper.get_cwe_by_id(cwe_id)

    # create a folder for the cwe
    cwe_folder = os.path.join(generated_cwes_output_folder, f"CWE-{cwe_id}")
    os.makedirs(cwe_folder, exist_ok=True)

    # determine what number of code examples have already been generated
    existing_code_examples = os.listdir(cwe_folder)
    existing_code_examples_count = len(existing_code_examples)

    # generate the code example
    code_example_number = existing_code_examples_count + 1
    code_example_folder = os.path.join(cwe_folder, f"{code_example_number}.code")
    os.makedirs(code_example_folder, exist_ok=True)

    # populate the code example folder with dummy data for now
    # create a vulnerable folder
    vulnerable_folder = os.path.join(code_example_folder, "vulnerable")
    os.makedirs(vulnerable_folder, exist_ok=True)

    # create a secure folder
    secure_folder = os.path.join(code_example_folder, "secure")
    os.makedirs(secure_folder, exist_ok=True)

    # create a payload folder
    payload_folder = os.path.join(code_example_folder, "payload")
    os.makedirs(payload_folder, exist_ok=True)

    # create a manifest file
    manifest_file = os.path.join(cwe_folder, "cwe-manifest.json")
    with open(manifest_file, "w") as f:
        json.dump(
            {
                "cwe-id": cwe_id,
                "title": xml.get("Name"),
                "generated-code-folders": [code_example_folder],
            },
            f,
        )

    # create a vulnerable file
    vulnerable_file = os.path.join(vulnerable_folder, "index.php")
    with open(vulnerable_file, "w") as f:
        f.write("<?php echo $_GET['username']; ?>")

    # create a secure file
    secure_file = os.path.join(secure_folder, "index.php")
    with open(secure_file, "w") as f:
        f.write("<?php echo htmlspecialchars($_GET['username']); ?>")

    # create a payload file
    payload_file = os.path.join(payload_folder, "payload.txt")
    with open(payload_file, "w") as f:
        f.write(
            "<script language='javascript'>alert('You've been attacked!');</script>"
        )
