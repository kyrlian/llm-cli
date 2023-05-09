#!pyhon3

import os
import sys
from dotenv import load_dotenv, find_dotenv
import curses
from curses.textpad import Textbox
from langchain.llms import HuggingFaceHub

load_dotenv(find_dotenv())  # take environment variables from .env.
assert os.environ.get("HUGGINGFACEHUB_API_TOKEN") is not None


def initllm(model_id="bigscience/bloom"):
    return HuggingFaceHub(repo_id=model_id, model_kwargs={"temperature": 0.1, "max_length": 64})

def getresponse(llm, input):
    generated_text = llm(input)
    print(generated_text)
    return generated_text

def getinfo(llm):
    args = llm.model_kwargs
    return f"{llm.repo_id}:{args['temperature']}"

def cursesmain(stdscr, firstinput):
    #init llm
    model_id = "bigscience/bloom"
    llm = initllm(model_id)
    curses.use_default_colors()
    screenwin = stdscr.derwin(0, 0)
    screenwin.border()
    screenwin.addstr(
        0, 2, "Complete the prompt, type ESC to send, Ctrl-C to quit."
    )
    screenwin.addstr(screenwin.getmaxyx()[0] - 1, 2, getinfo(llm))
    inputwin = screenwin.derwin(
        screenwin.getmaxyx()[0] - 2, screenwin.getmaxyx()[1] - 2, 1, 1
    )
    textbox = Textbox(inputwin, insert_mode=True)

    def validator(ch):  # handle key input
        if ch == 27:
            return curses.ascii.BEL  # Control-G to exit
        elif ch in (curses.KEY_BACKSPACE, curses.ascii.DEL, curses.ascii.BS, 127):
            return curses.KEY_BACKSPACE
        return ch

    def getuserinput(prompt):
        inputwin.addstr(0, 0, prompt)
        inputwin.refresh()
         # give input to user and return box content
        return textbox.edit(validator).strip() 

    screenwin.refresh()

    #handle initial prompt if any
    if firstinput != "":
        generatedprompt = getresponse(llm, firstinput)
    else:
        generatedprompt=""
    #loop
    while True:
        editedprompt = getuserinput(generatedprompt)
        generatedprompt = getresponse(llm, editedprompt)

if __name__ == "__main__":
    args = sys.argv[1:]
    firstinput=""
    if len(args) > 0:
        firstinput=args[0]
    curses.wrapper(cursesmain, firstinput)

