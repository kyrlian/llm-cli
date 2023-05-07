# https://python.langchain.com/en/latest/ecosystem/huggingface.html
# https://python.langchain.com/en/latest/modules/models/llms/integrations/huggingface_hub.html

# pip install huggingface_hub

from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

import os
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.
assert os.environ.get("HUGGINGFACEHUB_API_TOKEN") is not None

# See https://huggingface.co/models?pipeline_tag=text-generation
llm = HuggingFaceHub(repo_id="bigscience/bloom" , model_kwargs={"temperature":0.1, "max_length":64})
print(llm("Who won the FIFA World Cup in the year 1994? "))