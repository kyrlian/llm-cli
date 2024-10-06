#!pyhon3

import sys
from llm_cli.engines.engine_hg import Engine


def simple_cli(firstinput):
    # init llm
    engine = Engine()
    # input-generate loop
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
        print(f":{res}")

def main():
    args = sys.argv[1:]
    simple_cli(args[0] if len(args) > 0 else "")

if __name__ == "__main__":
    main()