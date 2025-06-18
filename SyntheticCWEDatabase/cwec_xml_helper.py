import xml.etree.ElementTree as ET


class CWECXMLHelper(object):

    def __init__(self, cwec_xml_file_path: str) -> None:
        self.xml_path = cwec_xml_file_path
        self.xml_tree = ET.parse(cwec_xml_file_path)
        # Define namespace map for cleaner XPath queries
        self.ns = {"cwe": "http://cwe.mitre.org/cwe-7"}

    def get_cwe_by_id(self, cwe_id: int) -> ET.Element:
        return self.xml_tree.find(
            ".//cwe:Weakness[@ID='{}']".format(cwe_id), namespaces=self.ns
        )

    def get_cwe_by_name(self, cwe_name: str) -> ET.Element:
        return self.xml_tree.find(
            ".//cwe:Weakness[@Name='{}']".format(cwe_name), namespaces=self.ns
        )

    def get_cwe_by_name_and_id(self, cwe_name: str, cwe_id: int) -> ET.Element:
        return self.xml_tree.find(
            ".//cwe:Weakness[@Name='{}'][@ID='{}']".format(cwe_name, cwe_id),
            namespaces=self.ns,
        )
