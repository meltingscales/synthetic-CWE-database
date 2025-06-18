import os
from dotenv import dotenv_values

cwec_output_folder = "ephemeral-data/cwe"
cwec_xml_file_name = "cwec_latest.xml"

cwec_xml_file_path = os.path.join(cwec_output_folder, cwec_xml_file_name)

generated_cwes_output_folder = "ephemeral-data/generated-cwes"

# expected environment variables
expected_env_vars = [
    "MONGODB_URL",
    "MONGODB_USERNAME",
    "MONGODB_PASSWORD",
    "USE_DUMMY_AI",
    "MODEL_NAME",
    "MODEL_API_URL",
    "MODEL_API_TOKEN",
]

# highest priority to .secret.env, then .shared.env, then environment variables
config_source_files = [
    ".shared.env",  # shared development variables
    ".secret.env",  # sensitive variables
]

# config is a dictionary that will be populated with the values from the files and environment variables
config = dict()

# load config from files
for config_source_file in config_source_files:
    config.update(dotenv_values(config_source_file))

# override loaded values with environment variables
config.update(os.environ)

for env_var in expected_env_vars:
    if env_var not in config:
        raise ValueError(
            f"Environment variable {env_var} is not set. Please check your .shared.env and .secret.env files."
        )
