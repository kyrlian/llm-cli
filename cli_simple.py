#!pyhon3

import sys
from engine_hg import hg_engine

def main(firstinput):
    # init llm
    engine = hg_engine()
    # input-generate loop
    res = ""
    if firstinput != "":
        res = engine.generate(firstinput)
    while True:
        user_input = input(f"{engine.model_id}> ").strip()
        if user_input in ["quit", "exit", "bye"]:
            break
        if user_input in ["reset"]:
            res = ""
            user_input = input("> ").strip()
        res = engine.generate(res + " " + user_input)


if __name__ == "__main__":
    args = sys.argv[1:] 
    main(args[0] if len(args) > 0 else "")
    