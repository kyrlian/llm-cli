# LLM-CLI

Display a prompt for the user to type text, and when the user types enter, send the text to hg inference api, and display the result. 
Loop until the user types 'quit' or 'exit' or 'bye'.

## CLIs
- [command line version: hgcli.py](./cli_simple.py)
- [tkinter version to edit full prompt](./cli_tkinter.py) (requires tkinter)
- [curses version to edit full prompt](./cli_curses.py)
- [textual version to edit full prompt](./cli_textual.py)

## Engines
- [HuggingFace Hub](./engine_hg.py)
- [Local TinyLlama](./engine_local.py)
- 
## Tests
- [run stable LM localy](./test/test-local-stable-lm.py)
- [run tinyLlama localy](./test/test-local-tinyllama.py)
- [various tests](./test/)

## Old:
- [old version using requests](./old/hgcli-requests.py)
- [openAI API cli using requests](./old/openaicli.py)

## Install

Install requirements
```sh
pip install -r requirements
```

To use llama.cpp see [llama-cpp-python](https://llama-cpp-python.readthedocs.io/en/latest/) and [llama.cpp](https://github.com/ggerganov/llama.cpp#build). For exemple for NVIDIA CUDA:
Install [CUDA toolkit](https://developer.nvidia.com/cuda-downloads) with `CUDA/Runtime/Librairies`, `CUDA/Development/Compiler` and `CUDA/Development/Visual Studio Integration`, and run:

```sh
$env:CMAKE_ARGS = "-DLLAMA_CUBLAS=ON"
$env:CMAKE_GENERATOR_TOOLSET="cuda=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3"
pip install llama-cpp-python  --upgrade --force-reinstall --no-cache-dir
```

To use Hugging face inference, create a .env file with your HUGGINGFACEHUB_API_TOKEN
```sh
HUGGINGFACEHUB_API_TOKEN="hf_xxxxX"
```

## Run
```sh
python.exe .\hgcli.py
```

## Use in REPL
```sh
ipython.exe .\init_repl.py
```

## Ressources
- [langchain - getting started](https://python.langchain.com/en/latest/modules/models/llms/getting_started.html)
- [HuggingFace text-generation models](https://huggingface.co/models?pipeline_tag=text-generation)
- [HuggingFace text2text-generation models](https://huggingface.co/models?pipeline_tag=text2text-generation)
- [Stable LM](https://github.com/Stability-AI/StableLM)
- [Stable LM on HugginFace](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)