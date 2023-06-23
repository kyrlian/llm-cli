#!pyhon3

from langchain.llms import HuggingFaceHub
import os
import sys
from dotenv import load_dotenv, find_dotenv
import tkinter as tk
load_dotenv(find_dotenv())  # take environment variables from .env.
assert os.environ.get("HUGGINGFACEHUB_API_TOKEN") is not None

langchain_model = HuggingFaceHub(repo_id="bigscience/bloom", model_kwargs={"temperature": 0.1, "max_length": 64})

class CliWindow(tk.Frame):
    def __init__(self, parent, initialprompt):
        tk.Frame.__init__(self, parent)
        self.textboxprompt = tk.Text(self, width=50, height=5)
        self.textboxprompt.pack(expand=True, fill=tk.BOTH)
        self.textboxprompt.insert(tk.END, initialprompt)
        bottomframe = tk.Frame(self)
        bottomframe.pack(side=tk.BOTTOM)
        tk.Button(bottomframe, text="CLS", command=self.btnclean).pack(side=tk.LEFT)
        tk.Button(bottomframe, text="Send", command=self.btnsend).pack(side=tk.LEFT)
        self.pack()

    def resize(self, event):
        if self.width != event.width or self.height != event.height:
            print(f"{event.widget=}: {event.height=}, {event.width=}\n")
            self.textboxprompt.width

    def btnclean(self):
        self.textboxprompt.delete("1.0", tk.END)

    def btnsend(self):
        prompt = self.textboxprompt.get("1.0", tk.END).strip()
        if len(prompt) > 0:
            print(f"prompt:{prompt}")
            answer = langchain_model(prompt)
            print(f"answer:{answer}")
            self.textboxprompt.insert(tk.END, "\n" + answer)


if __name__ == "__main__":
    args = sys.argv[1:]
    initialprompt = ""
    if len(args) > 0:
        initialprompt = args[0]
    root = tk.Tk()
    trackwin = CliWindow(root, initialprompt)
    root.mainloop()

