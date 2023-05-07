#!pyhon3

from langchain.llms import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # take environment variables from .env.
assert os.environ.get("HUGGINGFACEHUB_API_TOKEN") is not None


def initllm(model_id="bigscience/bloom"):
    return HuggingFaceHub(repo_id=model_id, model_kwargs={"temperature": 0.1, "max_length": 64})


def get_response(llm, input):
    generated_text = llm(input)
    print(generated_text)
    return generated_text


def main(firstinput):
    model_id = "bigscience/bloom"
    llm = initllm(model_id)
    res = ""
    if firstinput != "":
        res = get_response(llm, firstinput)
    while True:
        user_input = input(f"{model_id}> ").strip()
        if user_input in ["quit", "exit", "bye"]:
            break
        if user_input in ["reset"]:
            res = ""
            user_input = input("> ").strip()
        res = get_response(llm, res + " " + user_input)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) > 0:
        main(args[0])
    else:
        main("")
