import tkinter as tk
class playbacktab(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent) 
        self.title("Audio Playback")
        self.geometry("700x600")
        

        label = tk.Label(self, text='*playback feature under development*', fg="#006699", font= ("Arial", 20))
        label.pack(pady=10)