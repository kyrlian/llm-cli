from rich import pretty
pretty.install()

from engine_hg import hg_engine

hg = hg_engine()
print(f"Loaded hg_engine as 'hg'")