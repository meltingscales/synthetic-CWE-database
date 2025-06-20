from pymongo import MongoClient
from SyntheticCWEDatabase.config import config

import os
import json
import logging


class MongoHelper:
    def __init__(self):
        self.client = MongoClient(
            config["MONGODB_URL"],
            username=config["MONGODB_USERNAME"],
            password=config["MONGODB_PASSWORD"],
        )
        self.db = self.client["SyntheticCWEDatabase"]
        self.collection = self.db["code_examples"]

    def save_one_code_folder(self, path: str):
        obj = json.load(open(os.path.join(path, "code-manifest.json")))

        # check if the code-example-uuid already exists
        if self.lookup_one_code_folder(obj["code-example-uuid"]):
            logging.info(f"Code example {obj['code-example-uuid']} already exists, skipping")
            return

        self.collection.insert_one(obj)

    def lookup_one_code_folder(self, code_example_uuid: str):
        return self.collection.find_one({"code-example-uuid": code_example_uuid})


if __name__ == "__main__":

    guid = "bf36e10b-7582-4b57-889c-34b13eaa649d"
    mongo_helper = MongoHelper()
    mongo_helper.save_one_code_folder(f"./ephemeral-data/generated-cwes/CWE-79/{guid}.code/")
    print(mongo_helper.lookup_one_code_folder(f"{guid}") is not None)
