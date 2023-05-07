# LLM-CLI

Display a prompt for the user to type text, and when the user types enter, send the text to gpt chat api, and display the result. 
If the api response has more text, loop to display more tokens until the response is complete. Then display the prompt again. 
Loop until the user types 'quit' or 'exit' or 'bye'.

- [current version: hgcli.py](./hgcli.py)
- [run stable LM localy](./stable-lm.py)
- [tests](./test/)
- 
Old:
- [old version using requests](./old/hgcli-requests.py)
- [openAI API cli using requests](./old/openaicli.py)

Ressources:
- [langchain - getting started](https://python.langchain.com/en/latest/modules/models/llms/getting_started.html)
- [HuggingFace text-generation models](https://huggingface.co/models?pipeline_tag=text-generation)
- [HuggingFace text2text-generation models](https://huggingface.co/models?pipeline_tag=text2text-generation)
- [Stable LM](https://github.com/Stability-AI/StableLM)
- [Stable LM on HugginFace](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)