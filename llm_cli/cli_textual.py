#!python3

# https://textual.textualize.io/widgets/input/

import sys
from textual.app import App, ComposeResult
from textual.widgets import Input, Log
from llm_cli.engines.engine_ollama import Engine


class InputApp(App):
    def __init__(self, *args, engine, prompt, **kwargs):
        self.engine = engine
        self.prompt = prompt
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Input(id="input", placeholder="?", value=self.prompt)
        yield Log(id="debug")

    def on_ready(self) -> None:
        self.write_debug("Ready!")

    def on_input_submitted(self, message: Input.Submitted):
        if message.input.id == "input":
            prompt = message.value
            self.write_debug(f"prompt: {prompt}")
            answer = self.engine.generate(prompt)  # call LLM
            self.write_debug(f"answer: {answer}")
            self.query_one("#input", Input).insert_text_at_cursor(" " + answer)

    def write_debug(self, msg):
        self.query_one("#debug", Log).write_line(f"DEBUG:{msg}")

def main():
    args = sys.argv[1:]
    engine = Engine("llama3.1")
    app = InputApp(engine=engine, prompt=(args[0] if len(args) > 0 else ""))
    app.run()

if __name__ == "__main__":
    main()
