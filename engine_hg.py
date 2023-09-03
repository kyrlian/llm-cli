
from langchain.llms import HuggingFaceHub
import os
from dotenv import load_dotenv, find_dotenv

class hg_engine():
    def __init__(self, model_id="bigscience/bloom"):  
        load_dotenv(find_dotenv())  # take environment variables from .env.
        assert os.environ.get("HUGGINGFACEHUB_API_TOKEN") is not None
        self.model_id = model_id
        self.model = HuggingFaceHub(repo_id=model_id, model_kwargs={"temperature": 0.1, "max_length": 64})

    def generate(self, input):
        generated_text = self.model(input)
        print(generated_text)
        return generated_text

    def getinfo(self):
        args = self.model.model_kwargs
        return f"{self.model.repo_id}:{args['temperature']}"