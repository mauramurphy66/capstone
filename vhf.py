import tkinter as tk
from PyQt5.QtWidgets import QApplication
import sip
#from freq import freq


class vhftab:
    def __init__(self, root):
        self.top = tk.Toplevel(root)
        self.top.title("VHF Radio")

        self.embed_frame = tk.Frame(self.top, width=1200, height=800, bg="black")
        self.embed_frame.pack(fill="both", expand=True)


        self.embed_frame.update_idletasks()
        win_id = self.embed_frame.winfo_id()

        #Start GNU Radio flowgraph
       # self.tb = freq()    
        self.tb.start()               
        self.tb.embed_into(win_id)     
        self.tb.show()         

#import tkinter as tk
#class vhftab(tk.Toplevel):
 #   def __init__(self, parent):
  #      super().__init__(parent) 
   #     self.title("VHF")
    #    self.geometry("700x600")
#   label = tk.Label(self, text='*vhf tab under development*', fg="#006699", font= ("Arial", 20))
 #       label.pack(pady=10)
#       from freq import freq