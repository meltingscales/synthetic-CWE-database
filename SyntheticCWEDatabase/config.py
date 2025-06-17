import os
from dotenv import dotenv_values

cwec_output_folder = "ephemeral-data/cwe"
cwec_xml_file_name = "cwec_latest.xml"

cwec_xml_file_path = os.path.join(cwec_output_folder, cwec_xml_file_name)

generated_cwes_output_folder = "ephemeral-data/generated-cwes"

config = {
    **dotenv_values(".shared.env"),  # load shared development variables
    **dotenv_values(".secret.env"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}
