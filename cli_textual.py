#!python3

# https://textual.textualize.io/widgets/input/

import sys
from engine_hg import hg_engine
from textual.app import App, ComposeResult
from textual.widgets import Input, Log

class InputApp(App):
    def __init__(self, *args, engine, prompt, **kwargs):
        self.engine = engine
        self.prompt = prompt
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Input(id="input", placeholder="?", value=self.prompt)
        yield Log(id="debug")

    def on_ready(self) -> None:
        self.debug("Ready!")

    def on_input_submitted(self, message: Input.Submitted):
        if message.input.id == "input":
            prompt = message.value
            self.debug(f"prompt: {prompt}")
            answer = self.engine.generate(prompt)  # call LLM
            self.debug(f"answer: {answer}")
            self.query_one("#input", Input).insert_text_at_cursor(" " + answer)

    def debug(self, msg):
        self.query_one("#debug", Log).write_line(msg)


if __name__ == "__main__":
    args = sys.argv[1:]
    engine = hg_engine("bigscience/bloom")
    app = InputApp(engine=engine, prompt=(args[0] if len(args) > 0 else ""))
    app.run()