# write python code that : display a prompt for the user to type text, and when the user types enter, send the text to gpt chat api, and display the result. if the api response has more text, loop to display more tokens until the response is complete. Then display the prompt again. Loop until the user types 'quit' or 'exit' or 'bye'.

#pip install openai
import os
import openai

from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.
openai.api_key = os.environ.get("openai_api_key")

engine="text-davinci-003"
nbtokenstoforward=1024
nbtokenstorequest=1024

def call_api(prompt):
    response = openai.Completion.create(
        model=engine,
        prompt=prompt,
        max_tokens=nbtokenstorequest,
        temperature=0,
        n=1,
        stop=None
    )
    text = response["choices"][0]["text"]
    print(text)
    finish = response["choices"][0]["finish_reason"]
    return text, finish

def get_response(prompt):
    finish = ""
    fulltext = ""
    while finish != "stop":
        #print("continuing...")
        text, finish = call_api(prompt)
        fulltext += text
        prompt = fulltext[-nbtokenstoforward:]
    return fulltext

while True:
    user_input = input("> ")
    if user_input in ["quit", "exit", "bye"]:
        break
    response = get_response(user_input)
    #print(response)