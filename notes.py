import tkinter as tk
from tkPDFViewer import tkPDFViewer as pdf  
from tkinter import*



class notestab(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent) 
        self.title("notes")
        self.geometry("700x600")

        label = tk.Label(self, text='*Active Case Notes*', fg="#006699", font= ("Arial", 20))
        label.pack(pady=10)

        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(self, pdf_location="blank.pdf", width=700, height=600)
        v2.pack()
