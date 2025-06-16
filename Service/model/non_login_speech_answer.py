from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from typing import Dict
from Service.config import (
    QWEN_SPEECH_MODEL,
    QWEN_SPEECH_BASE_URL,
    SPEECH_PROMPT
)

class NonLoginSpeechAnswer():
    def __init__(self):
        self.start_model()
        self.prompts()
        self.initialize()
        
    def start_model(self):
        self.model = OllamaLLM(
            model=QWEN_SPEECH_MODEL, 
            base_url=QWEN_SPEECH_BASE_URL
        )
        
    def prompts(self):
        self.prompt = ChatPromptTemplate.from_template(SPEECH_PROMPT)
        
    def initialize(self):
        self.chain = self.prompt | self.model
        
    def invoke(self, answer):
        return self.chain.invoke({"question": answer})