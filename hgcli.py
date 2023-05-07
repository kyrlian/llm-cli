#!pyhon3

from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
import os
import sys
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.
api_key = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
assert api_key is not None

def initllmchain(model_id = "bigscience/bloom"):
    llm = HuggingFaceHub(repo_id=model_id, model_kwargs={"temperature":0.1, "max_length":64})
    template = "{payload}"
    prompt = PromptTemplate(template=template, input_variables=["payload"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain

def get_response(llm_chain,input):
    generated_text=llm_chain.run(input)
    print(generated_text)
    return generated_text

def main(firstinput):
    model_id = "bigscience/bloom"
    llmchain = initllmchain(model_id)
    res=""
    if firstinput != "":
        res = get_response(llmchain,firstinput)
    while True:
        user_input = input(f"{model_id}> ").strip()
        if user_input in ["quit", "exit", "bye"]:
            break
        if user_input in ["reset"]:
            res=""
            user_input = input("> ").strip()
        res = get_response(llmchain, res + " " + user_input)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) > 0:
        main(args[0])
    else:
        main("")
