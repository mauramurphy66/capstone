import tkinter as tk
from tkinter import ttk
import os
import matplotlib.pyplot as plt

# --- Color definitions ---
background_color = "#007AA5"  # Blue RGB(0, 122, 165)
button_bg = "#FFFFFF"         # White
button_fg = "#E03C31"         # CG Red (Pantone 179 C)

# --- Setup main window ---
root = tk.Tk()
root.title("Coast Guard Sensor Network Audio")
root.geometry("1900x1000")
root.configure(bg=background_color)

path = r"\\.\pipe\gnuradio_ctrl"

def send_command(cmd: str):
    """Send command to GNU Radio through named pipe"""
    if not os.path.exists(path):
        print("Pipe not found")
        return
    try:
        with open(path, "w") as fifo:
            fifo.write(cmd + "\n")
            print(f"Sent: {cmd}")
    except Exception as e:
        print(f"ERROR: {e}")

# --- Configure ttk style ---
style = ttk.Style()
style.theme_use("default")

style.configure(
    "Custom.TButton",
    background=button_bg,
    foreground=button_fg,
    font=("Helvetica", 14),
    borderwidth=2
)
style.map(
    "Custom.TButton",
    background=[("active", "#f0f0f0")],
    foreground=[("active", button_fg)]
)

style.configure("Custom.TEntry", fieldbackground="white", foreground="black")

# --- Main GUI function ---
def main():
    tk.Label(root, text="Frequency (Hz):", bg=background_color, fg="white").pack(pady=5)

    freq_var = tk.StringVar(value="87.9e6")
    freq_entry = ttk.Entry(root, textvariable=freq_var, width=20, style="Custom.TEntry")
    freq_entry.pack(pady=5)

    def set_frequency():
        val = freq_var.get()
        send_command(f"freq={val}")

    ttk.Button(root, text="Set Frequency", command=set_frequency, style="Custom.TButton").pack(pady=10)

    # Sample Rate
    tk.Label(root, text="Sample Rate:", bg=background_color, fg="white").pack(pady=5)
    samp_var = tk.StringVar(value="2e6")
    samp_entry = ttk.Entry(root, textvariable=samp_var, width=20, style="Custom.TEntry")
    samp_entry.pack(pady=5)

    def set_samp_rate():
        val = samp_var.get()
        send_command(f"samp_rate={val}")

    ttk.Button(root, text="Set Sample Rate", command=set_samp_rate, style="Custom.TButton").pack(pady=10)

    # Plot Graph Button
    def plot_graph():
        x = [161, 161.5, 162, 162.5, 163, 163.5, 164, 164.5]
        y = [0, -20, -40, -60, -80, -100, -120, -140]

        plt.figure(figsize=(9, 6))
        plt.plot(x, y, marker="o", color="blue")
        plt.xlabel("Frequency (MHz)")
        plt.ylabel("Relative Gain")
        plt.title("Radio Frequency Graph")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    ttk.Button(root, text="Show Graph", command=plot_graph, style="Custom.TButton").pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
