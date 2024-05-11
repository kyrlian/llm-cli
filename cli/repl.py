from rich import pretty
pretty.install()

from engines.engine_hg import Engine

hg = Engine()
print(f"Loaded engine_hg as 'hg'")