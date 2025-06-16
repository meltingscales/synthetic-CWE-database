"""This script fetches the latest Common Weakness Enumeration (CWE) data from the official CWE website 
and saves it to a local file.
It is designed to be run periodically to keep the local CWE data up-to-date.
"""

import requests
from zipfile import ZipFile
from io import BytesIO
import os

output_folder = 'ephemeral-data/cwe'
cwec_xml_file_name = 'cwec_latest.xml'
cwec_xml_file = os.path.join(output_folder, cwec_xml_file_name)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def download_cwes_xml():
    cwec_url='https://cwe.mitre.org/data/xml/cwec_latest.xml.zip'

    # download zip into memory and unzip
    response = requests.get(cwec_url)
    zip_file = ZipFile(BytesIO(response.content))
    zip_file.extractall(output_folder)
    zip_file.close()

    # rename the file to cwec_latest.xml
    os.rename(os.path.join(output_folder, os.listdir(output_folder)[0]), os.path.join(output_folder, 'cwec_latest.xml'))


# only download if the file doesn't exist
if not os.path.exists(os.path.join(output_folder, cwec_xml_file_name)):
    download_cwes_xml()

# read the first xml file we find
xml_file = os.path.join(output_folder, os.listdir(output_folder)[0])
with open(xml_file, 'r') as file:
    xml_data = file.read()
    print(len(xml_data))