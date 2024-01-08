
import torch
from transformers import pipeline

class tinyllama_engine():
    def __init__(self, model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):  
        pipe = pipeline("text-generation", model=model_id, torch_dtype=torch.bfloat16, device_map="auto")
        self.model = pipe

    def generate(self, input):
        outputs = self.model(input, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
        generated_text = outputs[0]["generated_text"]
        print(f"DEBUG:tinyllama_engine:generate:generated_text: {generated_text}")
        return generated_text

    def getinfo(self):
        return f"{self.model.repo_id}"
    