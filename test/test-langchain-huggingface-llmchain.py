# https://python.langchain.com/en/latest/ecosystem/huggingface.html
# https://python.langchain.com/en/latest/modules/models/llms/integrations/huggingface_hub.html

# pip install huggingface_hub

from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

import os
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.
#hg libs expects HUGGINGFACEHUB_API_TOKEN
hg_api_key = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
assert hg_api_key is not None

repo_id = "google/flan-t5-xl" # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options

llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0, "max_length":64})

template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "Who won the FIFA World Cup in the year 1994? "

print(llm_chain.run(question))