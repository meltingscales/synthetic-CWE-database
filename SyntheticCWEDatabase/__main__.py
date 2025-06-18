import os
import argparse
from SyntheticCWEDatabase.cwe_data_generator import generate_one_cwe
from SyntheticCWEDatabase.aihelper import AIHelper
from SyntheticCWEDatabase.save_to_mongodb import save_to_mongodb


def main():
    parser = argparse.ArgumentParser(description="Synthetic CWE Database")

    # they want to generate data
    parser.add_argument("--generate-data", action="store_true", help="Generate CWE data")
    parser.add_argument("--cwe-id", type=int, help="CWE ID to generate")
    parser.add_argument("--language", type=str, help="Language to generate")
    parser.add_argument("--ai-model", type=str, help="AI model to use")

    # they want to save data to mongodb
    parser.add_argument("--save-to-mongodb", action="store_true", help="Save data to MongoDB")

    args = parser.parse_args()

    if args.generate_data:
        generate_one_cwe(args.cwe_id, args.language, AIHelper(model_name=args.ai_model))
        return

    if args.save_to_mongodb:
        save_to_mongodb()

if __name__ == "__main__":
    main()
