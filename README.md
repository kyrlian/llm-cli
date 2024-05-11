# LLM CLIs, UIs, and wrappers for common engines <!-- omit in toc -->

## TOC <!-- omit in toc -->

- [Text CLIs](#text-clis)
- [Graphical UIs](#graphical-uis)
- [Engines](#engines)
- [Install](#install)
  - [Hugging Face](#hugging-face)
  - [Ollama](#ollama)
  - [Curses on windows](#curses-on-windows)
  - [llama.cpp](#llamacpp)
- [Run](#run)
- [Use in REPL](#use-in-repl)
- [Tests](#tests)
- [Old](#old)
- [Ressources](#ressources)


## Text CLIs

Display a prompt for the user to type text, and when the user types enter, send the text to hg inference api, and display the result. 
Loop until the user types 'quit' or 'exit' or 'bye'.

- [command line version: cli_simple.py](./cli_simple.py)
- [curses version to edit full prompt](./cli_curses.py) - requires [windows-curses](https://pypi.org/project/windows-curses/) on windows
- [textual version to edit full prompt](./cli_textual.py) - requires [textual](https://github.com/Textualize/textual)

## Graphical UIs
- [tkinter version to edit full prompt](./cli_tkinter.py) - requires [tkinter](https://docs.python.org/3/library/tkinter.html)
- [gradio version with prompt suggestions](./cli_gradio.py) - requires [gradio](https://www.gradio.app/)

## Engines
- [Online Hugging Face inference](./engine_hg.py) - requires [an hugging Face token](#hugging-face)
- [Local with Ollama](./engine_ollama.py) - requires [ollama](#ollama)
- [Local with Hugging Face pipeline and TinyLlama](./engine_pipeline.py) - requires [pytorch](https://pytorch.org/get-started/locally/)
- [Local with LlamaCpp and TinyLlama](./engine_local.py) - requires [llama.cpp](#llamacpp)
 

## Install

Install requirements
```sh
pip install -r requirements
```

### Hugging Face 
To use Hugging Face inference, create a [hugging face token](https://huggingface.co/settings/tokens), then create a .env file with your HUGGINGFACEHUB_API_TOKEN:
```sh
HUGGINGFACEHUB_API_TOKEN="hf_xxxxX"
```

### Ollama

To use Ollama, first install [ollama](https://ollama.com/) and download a model.
```sh
ollama serve
ollama list
ollama pull llama3
```

### Curses on windows
To use [cli_curses.py] on windows, you'll need [windows-curses](https://pypi.org/project/windows-curses/)

```sh
pip install windows-curses
```


### llama.cpp
To use llama.cpp see [llama-cpp-python](https://llama-cpp-python.readthedocs.io/en/latest/) and [llama.cpp](https://github.com/ggerganov/llama.cpp#build). For exemple for NVIDIA CUDA:
Install [CUDA toolkit](https://developer.nvidia.com/cuda-downloads) with `CUDA/Runtime/Librairies`, `CUDA/Development/Compiler` and `CUDA/Development/Visual Studio Integration`, and run:

```sh
$env:CMAKE_ARGS = "-DLLAMA_CUBLAS=ON"
$env:CMAKE_GENERATOR_TOOLSET="cuda=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3"
pip install llama-cpp-python  --upgrade --force-reinstall --no-cache-dir
```

## Run

All cli can be run directly

```sh
python.exe .\cli\cli_curses.py
```

All engines can be run directly to test them
```sh
python.exe .\cli\engines\engine_ollama.py
```

## Use in REPL
```sh
ipython.exe .\cli\repl.py
```

## Tests
- [run stable LM localy](./test/test-local-stable-lm.py)
- [run tinyLlama localy](./test/test-local-tinyllama.py)
- [various tests](./test/)

## Old
- [old version using requests](./old/hgcli-requests.py)
- [openAI API cli using requests](./old/openaicli.py)
- 
## Ressources
- [langchain - getting started](https://python.langchain.com/en/latest/modules/models/llms/getting_started.html)
- [HuggingFace text-generation models](https://huggingface.co/models?pipeline_tag=text-generation)
- [HuggingFace text2text-generation models](https://huggingface.co/models?pipeline_tag=text2text-generation)
- [Stable LM](https://github.com/Stability-AI/StableLM)
- [Stable LM on HugginFace](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)
- [Ollama](https://ollama.com/)
- [gradio](https://www.gradio.app/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [Textual](https://textual.textualize.io/)
- [Llama.cpp](https://github.com/ggerganov/llama.cpp)