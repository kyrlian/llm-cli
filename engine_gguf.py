
from huggingface_hub import hf_hub_download
from langchain.llms import LlamaCpp

MODELS_PATH = "E:\genai\local_models"

class engine_gguf():
    
    def __init__(self):  
        # https://github.com/PromtEngineer/localGPT/blob/main/load_models.py
        # https://python.langchain.com/docs/integrations/llms/llamacpp
        model_id="TheBloke/TinyLlama-1.1B-python-v0.1-GGUF"
        model_basename="tinyllama-1.1b-python-v0.1.Q5_K_M.gguf"
        model_path = hf_hub_download(
            repo_id=model_id,
            filename=model_basename,
            resume_download=True,
            cache_dir=MODELS_PATH,
        )
        kwargs = {
            "model_path": model_path,
            "n_ctx": 4096,
            "max_tokens": 4096,
            "n_batch": 512,  # set this based on your GPU & CPU RAM
            "n_gpu_layers" : 100,  # Llama-2-70B has 83 layers
        }
        self.llm = LlamaCpp(**kwargs)

    def generate(self, input):
        generated_text = self.llm(input)
        # print(f"DEBUG:local_engine:generate:generated_text: '{generated_text}'")
        return generated_text
    