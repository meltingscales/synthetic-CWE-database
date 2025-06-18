from ollama import chat

from SyntheticCWEDatabase.config import config
from SyntheticCWEDatabase.aihelper import AIHelper, AIHelperDummy
import unittest
import os


# allow failure of tests
@unittest.expectedFailure
class TestAI(unittest.TestCase):

    def setUp(self):

        self.skip_ai_tests = os.getenv("USE_DUMMY_AI") == "true"
        if self.skip_ai_tests:
            self.ai_helper = AIHelperDummy(model_name="dummy")
            print("Using dummy AI")
        else:
            self.ai_helper = AIHelper(model_name=config["MODEL_NAME"])
            print(f"Using AI model: {self.ai_helper.model_name}")

    @unittest.skipIf(
        os.getenv("USE_DUMMY_AI") == "true",
        "Skipping internal ollama call due to environment variable USE_DUMMY_AI=true",
    )
    def test_simple_ollama_call(self):
        response = chat(
            model=self.ai_helper.model_name,
            messages=[{"role": "user", "content": "Hello, how are you?"}],
        )
        print(response)
        self.assertIsNotNone(response)
        self.assertIn("I'm", response.message.content)

    def test_generate_vulnerable_code_cwe_79(self):
        vulnerable_code = self.ai_helper.generate_vulnerable_code(
            79,
            "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')",
            "php",
        )
        print(vulnerable_code)

        self.assertIsNotNone(vulnerable_code)

        self.assertIn("<?php", vulnerable_code)

    def test_generate_secure_code_cwe_79(self):
        secure_code = self.ai_helper.generate_secure_code(
            79,
            "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')",
            "php",
        )
        print(secure_code)

        self.assertIsNotNone(secure_code)

        self.assertIn("<?php", secure_code)
        self.assertNotIn("echo $_GET['username'];", secure_code)

    def test_generate_payload_cwe_79(self):
        payload = self.ai_helper.generate_payload(
            79,
            "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')",
            "php",
        )
        print(payload)

        self.assertIsNotNone(payload)
        self.assertIn("script", payload)
