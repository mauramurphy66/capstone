
import tkinter as tk
import os
import time
from tkinter import ttk, messagebox
import sys
import threading
from tkinter import Toplevel 
from tkinter import*
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from ais import aistab
from vhf import vhftab
from dsc import dsctab
from playback import playbacktab
from settings import settingstab
from all import MultiController
from NOAA import toggle_NOAA
from channel16 import toggle_Channel16
from channel13 import toggle_Channel13
#from NOAA import NOAAtab
#from channel16 import channel16
#from freq import freq
#from tkPDFViewer import tkPDFViewer as pdf  
#from channel13 import channel13
#from channel16 import Channel16Controller



background_color = "#FFFFFF" 
button_bg = "#006699"        
button_fg = "#E03C31"  

root = tk.Tk() # creates main window
root.title("Coast Guard Sensor Network Audio Home") #sets title
root.geometry("2900x1900") #sets window size
root.configure(bg=background_color)
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

canvas = Canvas()
canvas.create_rectangle(00,600,600,00, fill ="#006699",width = 6)


canvas.pack()

canvas.create_text(
    185, 50,             
    text="WELCOME",
    fill="#FFFFFF",
    font=("Courier", 40, "bold")
)
canvas.create_text(
    185, 140,   
    text="COAST GUARD AUDIO",
    fill="#FFFFFF",
    font=("Courier", 20, "bold")
)
canvas.create_text(
    185, 180,   
    text="TRANSMISSION HOMEPAGE",
    fill="#FFFFFF",
    font=("Courier", 20, "bold")
)



image_path1 = "cyber_logo.jpg"

try:
    original_image1 = Image.open(image_path1)
    resized1 = original_image1.resize((150, 150))
    logo_img1 = ImageTk.PhotoImage(resized1)

    logo_label1 = tk.Label(root, image=logo_img1, bg=background_color)
    logo_label1.image = logo_img1
    logo_label1.pack(pady=10)
    logo_label1.place(x=0, y=10)

except:
    print("Error")

image_path2 = "ee_logo.jpg"

try:
    original_image2 = Image.open(image_path2)
    resized2 = original_image2.resize((150, 150))
    logo_img2 = ImageTk.PhotoImage(resized2)

    logo_label2 = tk.Label(root, image=logo_img2, bg=background_color)
    logo_label2.image = logo_img2
    logo_label2.pack(pady=10)
    logo_label2.place(x=1115, y=10)

except:
    print("Error")

path = r"\\.\pipe\gnuradio_ctrl" #path that communicates between python and gnu radio will have to change if trying to run in linux to something like "/tmp/gnuradio_ctr"

def send_command(cmd: str): #defines function that sends commands to GNU radio through named pipe
    if not os.path.exists(path): #check if pipe exists
        print(f"Pipe not found") #returns message for error handling
        return #exit function 
        
    try:
        with open(path, "w") as fifo:  # opens the pipe in write mode
            fifo.write(cmd + "\n")  # send the command
            print(f"Sent: {cmd}")
    except Exception as e:  # handle errors if something goes wrong
        print(f"ERROR")

        style = ttk.Style() # style configuration
        style.theme_use("default")
        style = ttk.Style() # style configuration



def open_new_16():
    state = toggle_Channel16()
def open_new_13():
    state = toggle_Channel13()
def open_new_NOAA():
    state = toggle_NOAA()
def open_new_vhf():
    vhftab(root)
def open_new_all():
    all = MultiController()
    all.run_flowgraph()
def open_new_DSC():
    dsctab(root)
def open_new_AIS():  
    aistab(root)
def open_new_Playback():
    playbacktab(root)
def open_new_Settings():
    settingstab(root)


buttons = [
   
    ("Start Radio", open_new_all),
    ("Channel 16", open_new_16),
    ("Channel 13", open_new_13),
    ("NOAA", open_new_NOAA),
    ("VHF", open_new_vhf),
    ("DSC", open_new_DSC),
    ("AIS", open_new_AIS),
    ("Playback", open_new_Playback),
    ("Settings", open_new_Settings)
]
for i, (text, command) in enumerate(buttons):
    row = i % 3
    col = i // 3
    btn = tk.Button(
        button_frame,
        text=text,
        command=command,
        font=("Arial", 20),
        fg="#FFFFFF",
        bg="#006699",
        width=10,
        height=1
    )
    btn.grid(row=row, column=col, padx=20, pady=10)



       

def main(): 
   root.mainloop()

if __name__ == "__main__":
    main()



# Old extra code below: 

    #tk.Label(root, text="Frequency (Hz):").pack(pady=5) #creates widget for user to enter frequency
   # freq_var = tk.StringVar(value="87.9e6")  #creates variable to store frequency as string and sets intial value 87.9e6
    #freq_entry = ttk.Entry(root, textvariable=freq_var, width=20) # Creates entry box 
    #freq_entry.pack(pady=5) 

   # def set_frequency(): #defines function 
       # val = freq_var.get() #reads the frequency from entry box
        #send_command(f"freq={val}") #sends frequecny as a command by a pipe

   # ttk.Button(root, background = button_bg, foreground = button_fg, text="Set Frequency", command=set_frequency).pack(pady=10) #create set frequency button

   # tk.Label(root, text="Sample Rate:").pack(pady=5) #creates sample rate widget
  #  samp_var = tk.StringVar(value="2e6") #set inital sample rate
   # samp_entry = ttk.Entry(root, textvariable=samp_var, width=20) #creates entry box
   # samp_entry.pack(pady=5)

    #def set_samp_rate(): #defines function
       # val = samp_var.get() #reads sample rate
        #send_command(f"samp_rate={val}") #sends sample rate as a command

   # ttk.Button(root, background = button_bg, foreground = button_fg, text="Set Sample Rate", command=set_samp_rate).pack(pady=10) #makes set sample rate button


#create the graph that can plot radio freq graph
   # def plot_graph():#creates ploting function
        #x = [161, 161.5, 162, 162.5, 163, 163.5, 164, 164.5] #defines x axis values
        #y = [0, -20, -40, -60, -80, -100, -120, -140] #defines y axis values

       # plt.figure(figsize=(9, 6))   #creates the figure where display will be
        #plt.plot(x, y, marker= 'o', color= 'blue')    #creates plot
        #plt.xlabel('Frequency (MHz)') #labels x, y and main graph
        #plt.ylabel('Relative Gain')
        #plt.title('Radio Frequency Graph')  
        #plt.grid(True)  #includes grid
        #plt.tight_layout() #helps auto adjust the view
        #plt.show() #displays graph 

   # ttk.Button(root, text="Show Graph", command=plot_graph).pack(pady=20) #creates show graph button that one pressed displays graph


#def open_new_AIS():  
 #   aistab(root)
#def open_new_vhf():
  #  vhftab(root)
#def open_new_uhf():
 #   uhftab(root)
#def open_new_DSC():
 #   dsctab(root)
#def open_new_Playback():
 #   playbacktab(root)
#def open_new_Settings():
 #   settingstab(root)
#def open_new_notes():
 #   notestab(root)



#label = tk.Label(root, text='Welcome to the Coast Guard Sensor Network', fg="#006699", font= ("Arial", 20))
#label.pack(pady=10)

#button = tk.Button(root, text='AIS', command=open_new_AIS, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
#button.pack(pady=10)

#button = tk.Button(root, text='VHF', command=open_new_vhf, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
#button.pack(pady=10)

#button = tk.Button(root, text='UHF', command=open_new_uhf,  font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
#button.pack(pady=10)

#button = tk.Button(root, text='DSC', command=open_new_DSC, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
#button.pack(pady=10)

#button = tk.Button(root, text='Playback', command=open_new_Playback, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
#button.pack(pady=10)

#button = tk.Button(root, text='Settings', command=open_new_Settings, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
#button.pack(pady=10)

#button = tk.Button(root, text='Active Case Notes', command=open_new_notes, font= ("Arial", 20), fg="#FFFFFF", bg="#006699")
#button.pack(pady=10)


#def open_new_16():
 #   def launch():
  #      ch16 = channel16(root)
#
 #       try:
  #          ch16.tb.set_frequency(156800000) #set frequency for channel 16
   #    except:
    #       print("Warning: Could not set frequency yet (flowgraph might not be initialized).")

        # Start GNU Radio flowgraph
     #   ch16.tb.start()

        # Embed PyQt window inside Tkinter frame
    #    ch16.embed_into(ch16.embed_frame.winfo_id())

        # Keep the PyQt GUI responsive inside Tkinter
    #    def qt_loop():
       #     from PyQt5 import Qt
       #     Qt.QApplication.processEvents()
        #    ch16.top.after(20, qt_loop)

     #   qt_loop()

   # import threading
   # threading.Thread(target=launch, daemon=True).start()

#canvas.create_rectangle(210,10,10,210,outline ="#E03C31",fill ="#E03C31",width =4)