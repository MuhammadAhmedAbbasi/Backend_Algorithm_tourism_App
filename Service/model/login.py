from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from typing import Dict
from Service.config import (
    QWEN_MODEL_NAME,
    QWEN_BASE_URL,
    TRAVEL_PROMPT,
    FOOD_PROMPT,
    ACCOMMODATION_PROMPT,
    SUMMARY_PROMPT
)

class Login():
    def __init__(self):
        self.start_model()
        self.prompts()
        self.initialize()

    def start_model(self):
        self.model = OllamaLLM(model=QWEN_MODEL_NAME, base_url=QWEN_BASE_URL)

    def prompts(self):
        # Using prompts from config (content remains identical)
        self.prompt_travel = ChatPromptTemplate.from_template(TRAVEL_PROMPT)
        self.prompt_food = ChatPromptTemplate.from_template(FOOD_PROMPT)
        self.prompt_accommodation = ChatPromptTemplate.from_template(ACCOMMODATION_PROMPT)
        self.prompt_summary = ChatPromptTemplate.from_template(SUMMARY_PROMPT)

    def initialize(self):
        self.chain_travel = self.prompt_travel | self.model
        self.chain_food = self.prompt_food | self.model
        self.chain_accommodation = self.prompt_accommodation | self.model
        self.chain_summary = self.prompt_summary | self.model

    def invoke(self, category: str, data: Dict):
        if category == "travel":
            return self.chain_travel.invoke(data)
        elif category == "food":
            return self.chain_food.invoke(data)
        elif category == "accommodation":
            return self.chain_accommodation.invoke(data)
        elif category == "summary":
            return self.chain_summary.invoke(data)
        else:
            return "无效类别，请选择 'travel'、'food' 或 'accommodation'。"