import tkinter as tk
#from tkPDFViewer import tkPDFViewer as pdf
#from tkinter import Scrollbar, RIGHT, Y 

from tkinter import *
from PIL import Image, ImageTk

class aistab(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("AIS")
        self.geometry("700x600")

        label = tk.Label(self, text='*AIS tab under development*', fg="#006699", font=("Arial", 20))
        label.pack(pady=10)

       # v1 = pdf.ShowPdf()
       # v2 = v1.pdf_view(self, pdf_location=r"C:\Users\Maura\Downloads\capstone\chart.pdf", width=700, height=600)
       # v2.pack(expand=True, fill='both')



        #scrollbar = Scrollbar(self)
        #scrollbar.pack(side=RIGHT, fill=Y)
