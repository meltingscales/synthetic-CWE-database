from SyntheticCWEDatabase.config import *
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    # for testing xml parsing

    # import the xml file
    cwec_xml_tree = ET.parse(cwec_xml_file_path)

    # get the root element
    root = cwec_xml_tree.getroot()

    # print the root element
    print(root)

    # get the first child of the root element
    first_child = root[0]

    # print the first child
    print(first_child)

    print(root.find(".//{*}Weaknesses"))
