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


def generate_one_cwe(cwe_id: int, language: str, ai_helper: AIHelper):
    print(f"Generating CWE-{cwe_id}")

    xml_helper = CWECXMLHelper(cwec_xml_file_path)

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
            "manifest-path": os.path.join(code_example_folder, "code-manifest.json"),
        }
    )

    with open(cwe_manifest_file, "w") as f:
        json.dump(
            cwe_manifest,
            f,
            indent=4,
        )

    # create a vulnerable file
    vulnerable_file = os.path.join(vulnerable_folder, "vulnerable-code.txt")
    vulnerable_file_content = ai_helper.generate_vulnerable_code(
        cwe_id,
        cwe_xml.get("Name"),
        language,
    )
    with open(vulnerable_file, "w") as f:
        f.write(vulnerable_file_content)

    # create a secure file
    secure_file_content = ai_helper.generate_secure_code(
        cwe_id,
        cwe_xml.get("Name"),
        language,
    )
    secure_file = os.path.join(secure_folder, "secure-code.txt")
    with open(secure_file, "w") as f:
        f.write(secure_file_content)

    # create a payload file
    payload_file = os.path.join(payload_folder, "payload.txt")
    payload_file_content = ai_helper.generate_payload(
        cwe_id,
        cwe_xml.get("Name"),
        language,
    )
    with open(payload_file, "w") as f:
        f.write(payload_file_content)

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
                        "model-name": ai_helper.model_name,
                        "validated-by-human": {
                            "reviewed-by-human": False,
                            "notes": None,
                            "valid": None,
                        },
                        "file-content": vulnerable_file_content,
                    },
                    {
                        "type": "secure-code",
                        "path": secure_file,
                        "model-name": ai_helper.model_name,
                        "validated-by-human": {
                            "reviewed-by-human": False,
                            "notes": None,
                            "valid": None,
                        },
                        "file-content": secure_file_content,
                    },
                    {
                        "type": "payload",
                        "path": payload_file,
                        "model-name": ai_helper.model_name,
                        "validated-by-human": {
                            "reviewed-by-human": False,
                            "notes": None,
                            "valid": None,
                        },
                        "file-content": payload_file_content,
                    },
                ],
            },
            f,
            indent=4,
        )
