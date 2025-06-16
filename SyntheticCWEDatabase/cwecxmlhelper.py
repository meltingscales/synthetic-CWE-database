import xml.etree.ElementTree as ET


class CWECXMLHelper(object):

    def __init__(self, cwec_xml_file_path: str) -> None:
        self.cwec_xml_file_path = cwec_xml_file_path
        self.cwec_xml_data = open(cwec_xml_file_path, "r").read()
        self.cwec_xml_tree = ET.fromstring(self.cwec_xml_data)

    def get_cwe_by_id(self, cwe_id: int) -> ET.Element:
        return self.cwec_xml_tree.find(f"./Weakness[@ID='{cwe_id}']")

    def get_cwe_by_name(self, cwe_name: str) -> ET.Element:
        return self.cwec_xml_tree.find(f"./Weakness[@Name='{cwe_name}']")

    def get_cwe_by_name_and_id(self, cwe_name: str, cwe_id: int) -> ET.Element:
        return self.cwec_xml_tree.find(
            f"./Weakness[@Name='{cwe_name}'][@ID='{cwe_id}']"
        )
