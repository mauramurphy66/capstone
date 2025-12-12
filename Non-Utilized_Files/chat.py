import tkinter as tk
from tkinter import Toplevel 
#from tkPDFViewer import tkPDFViewer as pdf  

root = tk.Tk()
root.title("Coast Guard Sensor Network Home") 
root.geometry("300x200")  # set window size

def open_new_AIS():
    new_window = Toplevel(root)  
    new_window.title("AIS")
    new_window.geometry("350x150")  
def open_new_R21():
    new_window = Toplevel(root) 
    new_window.title("Rescue 21")
    new_window.geometry("350x150")  
def open_new_PAWSS():
    new_window = Toplevel(root)  
    new_window.title("PAWSS")
    new_window.geometry("350x150")  
def open_new_DSC():
    new_window = Toplevel(root) 
    new_window.title("DSC")
    new_window.geometry("350x150")  
def open_new_Playback():
    new_window = Toplevel(root) 
    new_window.title("Playback")
    new_window.geometry("350x150")  
def open_new_Settings():
    new_window = Toplevel(root)  
    new_window.title("Settings")
    new_window.geometry("350x150")  
	



label = tk.Label(root, text='Welcome to the Coast Guard Sensor Network', fg="#006699", font= ("Arial", 20))
label.pack(pady=10)

button = tk.Button(root, text='AIS', command=open_new_AIS, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
button.pack(pady=10)

button = tk.Button(root, text='Rescue 21', command=open_new_R21, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
button.pack(pady=10)

button = tk.Button(root, text='PAWSS', command=open_new_PAWSS, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
button.pack(pady=10)

button = tk.Button(root, text='DSC', command=open_new_DSC, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
button.pack(pady=10)

button = tk.Button(root, text='Playback', command=open_new_Playback, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
button.pack(pady=10)

button = tk.Button(root, text='Settings', command=open_new_Settings, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
button.pack(pady=10)



#pdf_view = pdf.ShowPdf()
#pdf_display = pdf_view.pdf_view(root, pdf_location="chart.pdf", width=100, height=100)
#pdf_display.pack(expand=True, fill='both')

root.mainloop()
