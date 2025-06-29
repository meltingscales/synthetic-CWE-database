import os
import argparse
from SyntheticCWEDatabase.cwe_data_generator import generate_one_cwe
from SyntheticCWEDatabase.aihelper import AIHelper, AIHelperDummy
from SyntheticCWEDatabase.MongoHelper import MongoHelper
from SyntheticCWEDatabase.config import generated_cwes_output_folder
import shutil


def destroy_generated_data():
    # delete the generated-cwes folder
    try:
        shutil.rmtree(generated_cwes_output_folder)
        print(f"Deleted {generated_cwes_output_folder}")
    except FileNotFoundError:
        print(f"Folder {generated_cwes_output_folder} not found")
        pass


def cli_main():
    parser = argparse.ArgumentParser(description="Synthetic CWE Database")

    # they want to generate data
    parser.add_argument(
        "--generate-data", action="store_true", help="Generate CWE data"
    )
    parser.add_argument("--cwe-id", type=int, help="CWE ID to generate")
    parser.add_argument("--language", type=str, help="Language to generate")
    parser.add_argument("--ai-model", type=str, help="ollama AI model name to use")
    parser.add_argument("--dummy-ai", action="store_true", help="Use dummy AI")
    parser.add_argument(
        "--number-of-cwes", type=int, default=1, help="Number of CWEs to generate"
    )

    # they want to save data to mongodb
    parser.add_argument(
        "--save-to-mongodb", action="store_true", help="Save data to MongoDB"
    )

    # they want to destroy our generated data
    parser.add_argument(
        "--destroy-generated-data", action="store_true", help="Destroy generated data"
    )

    args = parser.parse_args()

    if args.generate_data:
        if args.dummy_ai:
            ai_helper = AIHelperDummy("dummy")
        else:
            ai_helper = AIHelper(model_name=args.ai_model)

        for _ in range(0, args.number_of_cwes):
            generate_one_cwe(args.cwe_id, args.language, ai_helper)

        return

    if args.save_to_mongodb:
        # save_all_to_mongodb()
        raise NotImplementedError("save_to_mongodb not implemented")
        return

    if args.destroy_generated_data:
        destroy_generated_data()
        return
