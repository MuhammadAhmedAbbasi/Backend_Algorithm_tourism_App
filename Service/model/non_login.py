from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from typing import Dict
from Service.config import (
    QWEN_NONLOGIN_MODEL,
    QWEN_NONLOGIN_BASE_URL,
    BEST_ROUTE_PROMPT,
    TRAFFIC_INFO_PROMPT,
    CULINARY_PROMPT,
    CULTURAL_PROMPT,
    SIGHTSEEING_PROMPT
)

class NonLogin():
    def __init__(self):
        self.start_model()
        self.prompts()
        self.initialize()
        
    def start_model(self):
        self.model = OllamaLLM(
            model=QWEN_NONLOGIN_MODEL,
            base_url=QWEN_NONLOGIN_BASE_URL
        )
        
    def prompts(self):
        self.prompt_best_route = ChatPromptTemplate.from_template(BEST_ROUTE_PROMPT)
        self.prompt_Traffic_information = ChatPromptTemplate.from_template(TRAFFIC_INFO_PROMPT)
        self.prompt_culinary_specialities = ChatPromptTemplate.from_template(CULINARY_PROMPT)
        self.prompt_cultural_introduction = ChatPromptTemplate.from_template(CULTURAL_PROMPT)
        self.prompt_Sightseeing_tours = ChatPromptTemplate.from_template(SIGHTSEEING_PROMPT)

    def initialize(self):
        self.chain_cultural_introduction = self.prompt_cultural_introduction | self.model
        self.chain_best_route = self.prompt_best_route | self.model
        self.chain_prompt_Sightseeing_tours = self.prompt_Sightseeing_tours | self.model
        self.chain_culinary_specialities = self.prompt_culinary_specialities | self.model
        self.chain_Traffic_information = self.prompt_Traffic_information | self.model
        
    def invoke(self, place, info):
        if info == "文化介绍":
            return self.chain_cultural_introduction.invoke({"info": info, "place": place})
        elif info == "最佳路线":
            return self.chain_best_route.invoke({"info": info, "place": place})
        elif info == "景点游览":
            return self.chain_prompt_Sightseeing_tours.invoke({"info": info, "place": place})
        elif info == "特色美食":
            return self.chain_culinary_specialities.invoke({"info": info, "place": place})
        elif info == "交通信息":
            return self.chain_Traffic_information.invoke({"info": info, "place": place})
        else:
            return self.chain_cultural_introduction.invoke({"info": info, "place": place})