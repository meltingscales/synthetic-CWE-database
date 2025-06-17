from SyntheticCWEDatabase.aihelper import AIHelper
import unittest
import os


@unittest.skipIf(os.getenv("SKIP_AI_TESTS") == "true", "Skipping AI tests")
class TestAI(unittest.TestCase):

    def setUp(self):

        self.ai_helper = AIHelper(model_name="llama3.2:1b")

    def test_simple_ollama_call(self):
        response = self.ai_helper.client.chat("Hello, how are you?")
        print(response)
        self.assertIsNotNone(response)
        self.assertContains(response, "Hello")

    def test_generate_vulnerable_code_cwe_79(self):
        vulnerable_code = self.ai_helper.generate_vulnerable_code(
            79,
            "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')",
            "php",
        )
        print(vulnerable_code)

        self.assertIsNotNone(vulnerable_code)

        self.assertContains(vulnerable_code, "<?php")

    def test_generate_secure_code_cwe_79(self):
        secure_code = self.ai_helper.generate_secure_code(
            79,
            "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')",
            "php",
        )
        print(secure_code)

        self.assertIsNotNone(secure_code)

        self.assertContains(secure_code, "<?php")
        self.assertNotContains(secure_code, "echo $_GET['username'];")

    def test_generate_payload_cwe_79(self):
        payload = self.ai_helper.generate_payload(
            79,
            "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')",
            "php",
        )
        print(payload)

        self.assertIsNotNone(payload)
        self.assertContains(payload, "script")
