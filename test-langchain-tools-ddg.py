# https://python.langchain.com/en/latest/modules/agents/tools/examples/ddg.html

# !pip install duckduckgo-search

from langchain.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

print(search.run("Obama's first name?"))
