from SyntheticCWEDatabase.cwec_xml_helper import CWECXMLHelper
from SyntheticCWEDatabase.config import (
    cwec_xml_file_path,
    generated_cwes_output_folder,
    config,
)
from SyntheticCWEDatabase.aihelper import AIHelper, AIHelperDummy

import os
import json
import uuid


def generate_one_cwe(cwe_id: int, language: str):

    # TODO make helper methods to set up files and folders

    print(f"Generating CWE-{cwe_id}")

    xml_helper = CWECXMLHelper(cwec_xml_file_path)
    ai_helper = AIHelper(model_name=config["MODEL_NAME"])

    cwe_xml = xml_helper.get_cwe_by_id(cwe_id)

    # create a folder for the cwe
    cwe_folder = os.path.join(generated_cwes_output_folder, f"CWE-{cwe_id}")
    os.makedirs(cwe_folder, exist_ok=True)

    # generate the code example
    code_example_uuid = str(uuid.uuid4())
    code_example_folder = os.path.join(cwe_folder, f"{code_example_uuid}.code")
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

    # create a manifest file if it doesn't exist, otherwise update it
    cwe_manifest_file = os.path.join(cwe_folder, "cwe-manifest.json")
    if os.path.exists(cwe_manifest_file):
        with open(cwe_manifest_file, "r") as f:
            cwe_manifest = json.load(f)
    else:
        cwe_manifest = {
            "generated-code-folders": [],
            "cwe-id": cwe_id,
            "title": cwe_xml.get("Name"),
        }

    cwe_manifest["generated-code-folders"].append(
        {
            "id": code_example_uuid,
            "path": code_example_folder,
        }
    )

    with open(cwe_manifest_file, "w") as f:
        json.dump(
            cwe_manifest,
            f,
        )

    # create a vulnerable file
    # TODO generate the vulnerable file with the AI
    vulnerable_file = os.path.join(vulnerable_folder, "index.php")
    with open(vulnerable_file, "w") as f:
        f.write("<?php echo $_GET['username']; ?>")

    # create a secure file
    # TODO generate the secure file with the AI
    secure_file = os.path.join(secure_folder, "index.php")
    with open(secure_file, "w") as f:
        f.write("<?php echo htmlspecialchars($_GET['username']); ?>")

    # create a payload file
    # TODO generate the payload file with the AI
    payload_file = os.path.join(payload_folder, "payload.txt")
    with open(payload_file, "w") as f:
        f.write(
            "<script language='javascript'>alert('You've been attacked!');</script>"
        )

    # create a code-manifest.json file
    # no need to check if it exists, we'll always create it
    code_manifest_file = os.path.join(code_example_folder, "code-manifest.json")
    with open(code_manifest_file, "w") as f:
        json.dump(
            {
                "code-example-uuid": code_example_uuid,
                "cwe-id": cwe_id,
                "language": language,
                "generated-files": [
                    {
                        "type": "vulnerable-code",
                        "path": vulnerable_file,
                    },
                    {
                        "type": "secure-code",
                        "path": secure_file,
                    },
                    {
                        "type": "payload",
                        "path": payload_file,
                    },
                ],
                "validated-by-human": False,
                "human-validation-notes": None,
            },
            f,
        )
