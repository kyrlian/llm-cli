# https://python.langchain.com/en/latest/modules/agents/getting_started.html

# pip install langchain

import os
from dotenv import load_dotenv, find_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import HuggingFaceHub

#init hg api key
load_dotenv(find_dotenv())  # take environment variables from .env.
assert os.environ.get("HUGGINGFACEHUB_API_TOKEN") is not None

#First, let’s load the language model we’re going to use to control the agent.

repo_id = "google/flan-t5-xl" # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0})

#Next, let’s load some tools to use. Note that the llm-math tool uses an LLM, so we need to pass that in.

tools = load_tools(["ddg-search", "llm-math"], llm=llm)

#Finally, let’s initialize an agent with the tools, the language model, and the type of agent we want to use.

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

#Now let’s test it out!

agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")