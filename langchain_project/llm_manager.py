import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

class LLMManager:
    def __init__(self):
        self.llm = self._create_llm()

    def _create_llm(self):
        return ChatOpenAI(
            temperature=0.7,
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1",
            model="openrouter/free",
            max_tokens=1000
        )

    def simple_question(self, question: str) -> str:
        response = self.llm.invoke(question)
        return response.content

    def formatted_response(self, template: str, **kwargs) -> str:
        prompt = PromptTemplate(
            input_variables=list(kwargs.keys()),
            template=template
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        return chain.run(**kwargs)

llm_manager = LLMManager()