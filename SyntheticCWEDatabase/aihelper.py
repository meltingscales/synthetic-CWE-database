from ollama import chat
from ollama import ChatResponse
from ollama import Client


class AIHelper:
    def __init__(self, model_name: str, model_api_url: str = None):
        self.model_name = model_name
        if not self.model_name:
            raise ValueError("model_name cannot be empty")

        self.client = Client()
        self.model_api_url = model_api_url
        if self.model_api_url:
            self.client = Client(host=model_api_url)

    def generate(self, prompt: str):
        response: ChatResponse = self.client.chat(
            model=self.model_name, messages=[{"role": "user", "content": prompt}]
        )
        return response.message.content

    @staticmethod
    def fetch_prompt(prompt_name: str):
        with open(f"prompts/{prompt_name}.txt", "r") as f:
            return f.read()

    def generate_vulnerable_code(
        self, cwe_id: int, cwe_description: str, language: str
    ):
        prompt = self.fetch_prompt("generate_vulnerable_code")
        prompt = prompt.replace("{{CWE_ID}}", str(cwe_id))
        prompt = prompt.replace("{{CWE_DESCRIPTION}}", cwe_description)
        prompt = prompt.replace("{{LANGUAGE}}", language)
        return self.generate(prompt)

    def generate_secure_code(self, cwe_id: int, cwe_description: str, language: str):
        prompt = self.fetch_prompt("generate_secure_code")
        prompt = prompt.replace("{{CWE_ID}}", str(cwe_id))
        prompt = prompt.replace("{{CWE_DESCRIPTION}}", cwe_description)
        prompt = prompt.replace("{{LANGUAGE}}", language)
        return self.generate(prompt)

    def generate_payload(self, cwe_id: int, cwe_description: str, language: str):
        prompt = self.fetch_prompt("generate_payload")
        prompt = prompt.replace("{{CWE_ID}}", str(cwe_id))
        prompt = prompt.replace("{{CWE_DESCRIPTION}}", cwe_description)
        prompt = prompt.replace("{{LANGUAGE}}", language)
        return self.generate(prompt)


class AIHelperDummy(AIHelper):
    """Class used to test AIHelper without actually using an AI model."""

    def __init__(self, model_name: str):
        super().__init__(model_name)

    def generate(self, prompt: str):
        return f"""{self.__class__.__name__} Example response:
{prompt}"""

    def generate_vulnerable_code(
        self, cwe_id: int, cwe_description: str, language: str
    ):
        return f"""{self.__class__.__name__} Example vulnerable code:
{cwe_id} {cwe_description} {language}"""

    def generate_secure_code(self, cwe_id: int, cwe_description: str, language: str):
        return f"""{self.__class__.__name__} Example secure code:
{cwe_id} {cwe_description} {language}"""

    def generate_payload(self, cwe_id: int, cwe_description: str, language: str):
        return f"""{self.__class__.__name__} Example payload:
{cwe_id} {cwe_description} {language}"""
