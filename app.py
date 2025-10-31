#code copied straight from:https://wiki.gnuradio.org/index.php?title=GNU_Radio_Flowgraph_Embedded_in_Python_Applications
#only change made changed "fm_receiver" to "freq"

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
# First Import your flowgraph
from freq import freq

class FM(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Simple FM Example")

        # Instantiate FM Receiver App
        self.tb = freq()
        self.setMinimumSize(700, 500)

        # State variable
        self.listening = False 

        # Layout
        layout = QVBoxLayout()

        # Button
        self.button = QPushButton("Start Listening")
        self.button.clicked.connect(self.toggle_listening)  # connect click event
        layout.addWidget(self.button)

        self.setLayout(layout)

    def toggle_listening(self):
        """Toggle listening state and update button text."""
        self.listening = not self.listening

        if self.listening:
            self.button.setText("Stop Listening")
            print("Listening started...")
            self.tb.start()
        else:
            self.button.setText("Start Listening")
            print("Listening stopped.")
            self.tb.stop()
            self.tb.wait()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FM()
    window.show()
    sys.exit(app.exec_())