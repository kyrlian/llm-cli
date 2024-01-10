
import torch
from transformers import pipeline

class engine_local():
    def __init__(self, model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):  
        pipe = pipeline("text-generation", model=model_id, torch_dtype=torch.bfloat16, device_map="auto")
        self.pipe = pipe

    def generate(self, input):
        outputs = self.pipe(input, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95, return_full_text=False)
        generated_text = outputs[0]["generated_text"]
        # print(f"DEBUG:local_engine:generate:generated_text: '{generated_text}'")
        return generated_text
