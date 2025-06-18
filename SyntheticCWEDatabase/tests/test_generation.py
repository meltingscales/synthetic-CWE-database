import random
from SyntheticCWEDatabase.cwec_xml_helper import CWECXMLHelper
from SyntheticCWEDatabase.cwe_data_generator import generate_one_cwe
import unittest
import os
import shutil
from SyntheticCWEDatabase.aihelper import AIHelper, AIHelperDummy
from SyntheticCWEDatabase.config import config


class TestGeneration(unittest.TestCase):

    def setUp(self):
        self.cwec_xml_file_path = "ephemeral-data/cwe/cwec_latest.xml"
        self.cwec_xml_helper = CWECXMLHelper(self.cwec_xml_file_path)
        self.test_cwes_to_generate = [
            79,  # CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
            119,  # CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer
            120,  # CWE-120: Buffer Copy without Checking Size of Input ('Classic Buffer Overflow')
            121,  # CWE-121: Stack-based Buffer Overflow
            122,  # CWE-122: Heap-based Buffer Overflow
            123,  # CWE-123: Write-what-where Condition
            124,  # CWE-124: Buffer Copy without Checking Destination Size
            125,  # CWE-125: Out-of-bounds Read
            126,  # CWE-126: Buffer Over-read
        ]

        self.ai_helper = AIHelper(model_name=config["MODEL_NAME"])

        if config["USE_DUMMY_AI"] == "true":
            self.ai_helper = AIHelperDummy(model_name="dummy")

        # delete the generated-cwes folder if it exists
        try:
            shutil.rmtree("ephemeral-data/generated-cwes")
        except FileNotFoundError:
            pass

    def test_small_generation(self):

        # for all cwes in our list,
        for cwe_id in self.test_cwes_to_generate:

            # between 2 and 5 code examples per cwe
            for _ in range(random.randint(2, 5)):
                generate_one_cwe(cwe_id, "php", self.ai_helper)

            # assert that a folder has been created with the name of the cwe
            self.assertTrue(
                os.path.exists(f"ephemeral-data/generated-cwes/CWE-{cwe_id}")
            )

    def test_large_generation(self):
        pass

    def test_large_generation_with_multiple_cwes(self):
        pass
