import subprocess
import sys
import os

class MultiController:
    """
    Launches the Channel 16 GNU Radio flowgraph in a separate process.
    """

    def __init__(self):
        # The exported flowgraph file from GRC
        self.flowgraph_filename = "Final_MultiChannel.py"

        # Absolute path to the flowgraph file
        self.flowgraph_path = os.path.join(
            os.path.dirname(__file__),
            self.flowgraph_filename
        )

        # Check file exists
        if not os.path.exists(self.flowgraph_path):
            raise FileNotFoundError(
                f"flowgraph not found at:\n{self.flowgraph_path}"
            )

    def run_flowgraph(self):
        """
        Launch the flowgraph in a separate process so Tkinter GUI is not blocked.
        """
        python_exec = sys.executable  # Use the current Conda environment
        subprocess.Popen([python_exec, self.flowgraph_path])


