from xmlrpc.client import ServerProxy
s = ServerProxy('http://localhost:8081')

def toggle_NOAA():
    try:
        current = s.get_NOAA_gain()

        new_val = 0 if current == 1 else 1

        s.set_NOAA_gain(new_val)

        return "unmuted" if new_val == 1 else "muted"

    except Exception:
        print("ERROR")

#import tkinter as tk
#from PyQt5.QtWidgets import QApplication

#import sip

#class NOAAtab:
    #def __init__(self, root):
     #   self.top = tk.Toplevel(root)
      #  self.top.title("NOAA")

       # self.embed_frame = tk.Frame(self.top, width=1200, height=800, bg="black")
        #self.embed_frame.pack(fill="both", expand=True)


        #self.embed_frame.update_idletasks()
        #win_id = self.embed_frame.winfo_id()

        #self.tb = freq(162400000)    
        #self.tb.start()               #
        #self.tb.embed_into(win_id)     
        #self.tb.show()  