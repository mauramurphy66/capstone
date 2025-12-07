import tkinter as tk
class alltab(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent) 
        self.title("All")
        self.geometry("700x600")

        label = tk.Label(self, text='*all tab under development*', fg="#006699", font= ("Arial", 20))
        label.pack(pady=10)