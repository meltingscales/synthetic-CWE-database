from SyntheticCWEDatabase.cwecxmlhelper import CWECXMLHelper
from SyntheticCWEDatabase.cwe_data_generator import generate_one_cwe
import unittest
import os
import shutil


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

    def tearDown(self):
        # delete the generated-cwes folder
        try:
            shutil.rmtree("ephemeral-data/generated-cwes")
        except FileNotFoundError:
            pass

    def test_small_generation(self):
        for cwe_id in self.test_cwes_to_generate:
            generate_one_cwe(cwe_id, "php")

            # assert that a folder has been created with the name of the cwe
            self.assertTrue(
                os.path.exists(f"ephemeral-data/generated-cwes/CWE-{cwe_id}")
            )

    def test_large_generation(self):
        pass

    def test_large_generation_with_multiple_cwes(self):
        pass
