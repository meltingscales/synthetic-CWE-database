import unittest
from SyntheticCWEDatabase.config import config
from ollama import Client


class TestRawOllama(unittest.TestCase):
    def setUp(self):
        pass

    def testSimple(self):

        url = config["MODEL_API_URL"]
        model_name = config["MODEL_NAME"]
        print(url, model_name)

        client = Client(url)

        response = client.chat(
            model_name,
            messages=[
                {
                    "role": "user",
                    "content": "Generate a command injection payload that sleeps for 5 seconds. Output only the payload. Write it for Linux bash.",
                }
            ],
        )

        print(response)

        raw_output = response.message.content

        print(raw_output)

        self.assertIn("; sleep", raw_output)
