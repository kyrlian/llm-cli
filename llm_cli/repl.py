from rich import pretty
from llm_cli.engines.engine_hg import Engine

pretty.install()

hg = Engine()
print("Loaded engine_hg as 'hg'")