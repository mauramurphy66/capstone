import tkinter as tk
import os
import time
from tkinter import ttk, messagebox
import sys
import threading
from tkinter import Toplevel 
from tkinter import*
import matplotlib.pyplot as plt
from freq import freq
#from tkPDFViewer import tkPDFViewer as pdf  
#from ais import aistab
#from vhf import vhftab
#from uhf import uhftab
#from dsc import dsctab
#from playback import playbacktab
#from settings import settingstab
#from notes import notestab


root = tk.Tk() # creates main window
root.title("Coast Guard Sensor Network Audio") #sets title
root.geometry("2900x1900") #sets window size

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

def main(): 

    tk.Label(root, text="Frequency (Hz):").pack(pady=5) #creates widget for user to enter frequency
    freq_var = tk.StringVar(value="87.9e6")  #creates variable to store frequency as string and sets intial value 87.9e6
    freq_entry = ttk.Entry(root, textvariable=freq_var, width=20) # Creates entry box 
    freq_entry.pack(pady=5) 

    def set_frequency(): #defines function 
        val = freq_var.get() #reads the frequency from entry box
        send_command(f"freq={val}") #sends frequecny as a command by a pipe

    ttk.Button(root, text="Set Frequency", command=set_frequency).pack(pady=10) #create set frequency button

    tk.Label(root, text="Sample Rate:").pack(pady=5) #creates sample rate widget
    samp_var = tk.StringVar(value="2e6") #set inital sample rate
    samp_entry = ttk.Entry(root, textvariable=samp_var, width=20) #creates entry box
    samp_entry.pack(pady=5)

    def set_samp_rate(): #defines function
        val = samp_var.get() #reads sample rate
        send_command(f"samp_rate={val}") #sends sample rate as a command

    ttk.Button(root, text="set Sample Rate", command=set_samp_rate).pack(pady=10) #makes set sample rate button


#create the graph that can plot radio freq graph
    def plot_graph():#creates ploting function
        x = [161, 161.5, 162, 162.5, 163, 163.5, 164, 164.5] #defines x axis values
        y = [0, -20, -40, -60, -80, -100, -120, -140] #defines y axis values

        plt.figure(figsize=(9, 6))   #creates the figure where display will be
        plt.plot(x, y, marker= 'o', color= 'blue')    #creates plot
        plt.xlabel('Frequency (MHz)') #labels x, y and main graph
        plt.ylabel('Relative Gain')
        plt.title('Radio Frequency Graph')  
        plt.grid(True)  #includes grid
        plt.tight_layout() #helps auto adjust the view
        plt.show() #displays graph 

    ttk.Button(root, text="Show Graph", command=plot_graph).pack(pady=20) #creates show graph button that one pressed displays graph

    root.mainloop()

if __name__ == "__main__":
    main()

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



