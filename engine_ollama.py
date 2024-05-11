import requests
import json

# Ollama exposes port 11434 by default

class engine_ollama():
    def __init__(self, model_id="llama3",port = 11434):  
        self.model = model_id
        self.url = f"http://localhost:{port}/api/generate"
        self.headers = {"Content-Type": "application/json"}

    def generate(self,prompt):
        data = {"model": self.model, "stream": False, "prompt": prompt}
        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        if response.status_code == 200:
            response_txt = response.text
            data = json.loads(response_txt)
            actual_response = data["response"]
            return actual_response
        else:
            print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    en = engine_ollama()
    en.generate("Who is obama?")