from SyntheticCWEDatabase.cwec_xml_helper import CWECXMLHelper
import unittest


class TestCWECXMLHelper(unittest.TestCase):

    def setUp(self):
        self.cwec_xml_file_path = "ephemeral-data/cwe/cwec_latest.xml"
        self.cwec_xml_helper = CWECXMLHelper(self.cwec_xml_file_path)

    def test_get_cwe_by_id(self):

        cwec_xml_helper = CWECXMLHelper(self.cwec_xml_file_path)

        cwe_79 = cwec_xml_helper.get_cwe_by_id(79)

        print(cwe_79)

        self.assertIsNotNone(cwe_79)
        self.assertEqual(
            cwe_79.get("Name"),
            "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')",
        )
