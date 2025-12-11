import tkinter as tk
from PyQt5.QtWidgets import QApplication
import sip
from freq import freq

class channel13:
    def __init__(self, root):
        self.top = tk.Toplevel(root)
        self.top.title("Channel 13")

        self.embed_frame = tk.Frame(self.top, width=1200, height=800, bg="black")
        self.embed_frame.pack(fill="both", expand=True)


        self.embed_frame.update_idletasks()
        win_id = self.embed_frame.winfo_id()

        #Start GNU Radio flowgraph
        self.tb = freq(156650000)    
        self.tb.start()               
        self.tb.embed_into(win_id)     
        self.tb.show()         
