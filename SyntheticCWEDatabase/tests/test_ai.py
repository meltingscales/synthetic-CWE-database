from ollama import chat

from SyntheticCWEDatabase.config import config
from SyntheticCWEDatabase.aihelper import AIHelper
import unittest
import os


@unittest.skipIf(
    os.getenv("SKIP_AI_TESTS") == "true",
    "Skipping AI tests due to environment variable SKIP_AI_TESTS=true",
)
class TestAI(unittest.TestCase):

    def setUp(self):

        # self.ai_helper = AIHelper(model_name="deepseek-r1:1.5b")
        # self.ai_helper = AIHelper(model_name="llama3.2:1b")
        self.ai_helper = AIHelper(model_name=config["MODEL_NAME"])

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
