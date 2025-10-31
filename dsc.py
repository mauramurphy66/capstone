import tkinter as tk
class dsctab(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent) 
        self.title("DSC")
        self.geometry("700x600")

        label = tk.Label(self, text='*Digital Selective calling under development*', fg="#006699", font= ("Arial", 20))
        label.pack(pady=10)