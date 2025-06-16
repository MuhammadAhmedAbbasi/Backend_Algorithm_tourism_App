from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from typing import Dict
from Service.config import (
    QWEN_MODEL_NAME,
    QWEN_BASE_URL,
    DESCRIPTION_PROMPT
)

class Description():
    def __init__(self):
        self.start_model()
        self.prompts()
        self.initialize()

    def start_model(self):
        self.model = OllamaLLM(model=QWEN_MODEL_NAME, base_url=QWEN_BASE_URL)

    def prompts(self):
        self.prompt_description = ChatPromptTemplate.from_template(DESCRIPTION_PROMPT)
        
    def initialize(self):
        self.chain_description = self.prompt_description | self.model

    def invoke(self, data: Dict):
        return self.chain_description.invoke(data)