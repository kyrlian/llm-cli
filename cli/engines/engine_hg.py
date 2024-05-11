import os
from dotenv import load_dotenv, find_dotenv
from huggingface_hub import InferenceClient

class Engine:
    def __init__(self, model_id="bigscience/bloom"):
        load_dotenv(find_dotenv())  # take environment variables from .env.
        hf_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
        assert hf_token is not None
        # print(f"DEBUG:hf_token:'{hf_token}'")
        self.model_id = model_id
        self.client = InferenceClient(token=hf_token,model=self.model_id)

    def generate(self, input):
        generated_text = self.client.text_generation(input)
        # print(f"DEBUG:hg_engine:generate:generated_text: '{generated_text}'")
        return generated_text

if __name__ == "__main__":
    en = Engine()
    print(en.generate("Who is obama?"))
