#!pyhon3

import sys
import curses
from curses.textpad import Textbox
from engines.engine_hg import Engine


def cursesmain(stdscr, firstinput):
    # init llm
    engine = Engine("bigscience/bloom")
    curses.use_default_colors()
    screenwin = stdscr.derwin(0, 0)
    screenwin.border()
    screenwin.addstr(0, 2, "Complete the prompt, type ESC to send, Ctrl-C to quit.")
    # screenwin.addstr(screenwin.getmaxyx()[0] - 1, 2, engine.getinfo())
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

    # handle initial prompt if any
    if firstinput != "":
        generatedprompt = engine.generate(firstinput)
    else:
        generatedprompt = ""
    # loop
    while True:
        editedprompt = getuserinput(generatedprompt)
        generatedprompt = engine.generate(editedprompt)


if __name__ == "__main__":
    args = sys.argv[1:]
    curses.wrapper(cursesmain, args[0] if len(args) > 0 else "")
