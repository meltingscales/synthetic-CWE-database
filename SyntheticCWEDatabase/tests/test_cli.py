import sys
import unittest
from unittest.mock import patch
import os
from SyntheticCWEDatabase.cli import cli_main
import json


class TestCLI(unittest.TestCase):
    def test_cli_with_args(self):
        # Mock sys.argv to simulate command-line arguments
        with patch.object(
            sys,
            "argv",
            [
                "SyntheticCWEDatabase",
                "--generate-data",
                "--cwe-id",
                "79",
                "--language",
                "php",
                "--dummy-ai",
                "--number-of-cwes",
                "1",
            ],
        ):
            # Call your CLI's main function
            cli_main()
            # Assert expected behavior, e.g., output, file changes, database updates
            self.assertTrue(
                os.path.exists("ephemeral-data/generated-cwes/CWE-79/cwe-manifest.json")
            )

            obj = json.load(
                open("ephemeral-data/generated-cwes/CWE-79/cwe-manifest.json")
            )
            self.assertEqual(obj["cwe-id"], 79)

        # destroy the generated data
        with patch.object(
            sys, "argv", ["SyntheticCWEDatabase", "--destroy-generated-data"]
        ):
            cli_main()
            self.assertFalse(
                os.path.exists("ephemeral-data/generated-cwes/CWE-79/cwe-manifest.json")
            )
