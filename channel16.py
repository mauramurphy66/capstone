from xmlrpc.client import ServerProxy
s = ServerProxy('http://localhost:8081')

def toggle_Channel16():
    try:
        current = s.get_CH16_gain()

        new_val = 0 if current == 1 else 1

        s.set_CH16_gain(new_val)

        return "unmuted" if new_val == 1 else "muted"

    except Exception:
        print("ERROR")

#import subprocess
#import sys
#import os

#class Channel16Controller:
 #   """
  #  Launches the Channel 16 GNU Radio flowgraph in a separate process.
   # """

    #def __init__(self):
#   self.flowgraph_filename = "freq.py"
#
 #       self.flowgraph_path = os.path.join(
  #          os.path.dirname(__file__),
   #         self.flowgraph_filename
    #    )
#
 #      
  #      if not os.path.exists(self.flowgraph_path):
   #         raise FileNotFoundError(
    #            f"Channel 16 flowgraph not found at:\n{self.flowgraph_path}"
     #       )

    #def run_flowgraph(self):
     #   """
      #  Launch the flowgraph in a separate process so Tkinter GUI is not blocked.
       # """
       # python_exec = sys.executable  # Use the current Conda environment
        #subprocess.Popen([python_exec, self.flowgraph_path])



#import tkinter as tk
#import sip
#from PyQt5 import QtWidgets, QtCore
#from freq import freq

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.12.0




#class channel16:
 #   def __init__(self, root):
  #      self.top = tk.Toplevel(root)
   #     self.top.title("Channel 16")
#
      #  self.embed_frame = tk.Frame(self.top, width=1200, height=800, bg="black")
       # self.embed_frame.pack(fill="both", expand=True)
#
 #       self.embed_frame.update_idletasks()
  #      self.win_id = self.embed_frame.winfo_id()
#
 #        Ensure QApplication exists
   #     self.qapp = QtWidgets.QApplication.instance()
    #    if self.qapp is None:
     #       self.qapp = QtWidgets.QApplication([])
#
        # Create GNU Radio Qt widget
 #       self.tb = freq()
  #      self.tb.set_frequency(156800000)
#
        # Embed properly
 #       self.embed_into()

        # Start flowgraph
  #      self.tb.start()

        # Keep Qt events flowing
   #     self.qt_event_loop()

   # def embed_into(self):
    #    """Embed QWidget (GNU Radio GUI) inside Tk widget."""
        # Convert Tk's window ID into a Qt widget
     #   parent_qt_widget = sip.wrapinstance(int(self.win_id), QtWidgets.QWidget)

        # Reparent GNU Radio QWidget into Tkinter window
      #  self.tb.setParent(parent_qt_widget)
       # self.tb.setWindowFlags(QtCore.Qt.Widget)

        # Show inside Tk
        #self.tb.show()

   # def qt_event_loop(self):
    #    self.qapp.processEvents()
     #   self.top.after(20, self.qt_event_loop)

