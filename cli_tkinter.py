#!pyhon3

import sys
import tkinter as tk
from engine_hg import hg_engine
from engine_tinyllama import tinyllama_engine

class CliWindow(tk.Frame):
    def __init__(self, parent, initialprompt):
        # self.model = hg_engine()
        self.model = tinyllama_engine()
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
            answer = self.model.generate(prompt)
            print(f"answer:{answer}")
            self.textboxprompt.insert(tk.END, "\n" + answer)


if __name__ == "__main__":
    args = sys.argv[1:]
    root = tk.Tk()
    trackwin = CliWindow(root, args[0] if len(args) > 0 else "")
    root.mainloop()

