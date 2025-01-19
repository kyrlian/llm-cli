import requests

# InstructLab exposes port 8000 by default
# https://github.com/instructlab/instructlab
# http://127.0.0.1:8000/docs

# model is


class Engine:
    def __init__(self, model_id="models/merlinite-7b-lab-Q4_K_M.gguf", port=8000):
        self.model = model_id
        self.url = f"http://localhost:{port}/v1"
        self.headers = {"Content-Type": "application/json"}

    def list(self)->list:
        response = requests.get(f"{self.url}/models", headers=self.headers)
        if response.status_code == 200:
            response_json = response.json()
            models = response_json["data"]
            modelnames = [m["id"] for m in models]
            return modelnames
        else:
            print("Error:", response.status_code, response.text)
            return []

    def generate(self, prompt, model=None):
        if model is None:
            model = self.model
        data = {
            "prompt": prompt,
            "model": model,
            "suffix": None,
            "max_tokens": 100,
            "temperature": 0.8,
            "top_p": 0.95,
            "top_k": 40,
            "stop": ["§"],
        }
        response = requests.post(
            f"{self.url}/completions", headers=self.headers, json=data
        )
        if response.status_code == 200:
            response_json = response.json()
            actual_response = response_json["choices"][0]["text"]
            return actual_response
        else:
            print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    en = Engine()
    print("list: " , ", ".join(en.list()))
    print("generate: " , en.generate("Who is obama?"))
