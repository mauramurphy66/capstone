import tkinter as tk


from tkinter import *
from PIL import Image, ImageTk

class aistab(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("AIS")
        self.geometry("700x600")

        label1 = tk.Label(
            self,
            text='*AIS is not yet available within Tkinter Python Application*',
            fg="#006699",
            font=("Arial", 20)
        )
        label1.pack(pady=10)

        label2 = tk.Label(
            self,
            text='To view current AIS progress, please utilize the ArcGIS Display',
            fg="#006699",
            font=("Arial", 14)
        )

        label2.pack(pady=5)











#from tkPDFViewer import tkPDFViewer as pdf
#from tkinter import Scrollbar, RIGHT, Y 

       # v1 = pdf.ShowPdf()
       # v2 = v1.pdf_view(self, pdf_location=r"C:\Users\Maura\Downloads\capstone\chart.pdf", width=700, height=600)
       # v2.pack(expand=True, fill='both')



        #scrollbar = Scrollbar(self)
        #scrollbar.pack(side=RIGHT, fill=Y)
