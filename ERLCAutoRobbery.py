import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading
import win32gui
import win32con
import os

class ScriptRunnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Script Runner")

        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.output_text.pack(padx=10, pady=10)

        self.update_output("Welcome to Script Runner\n")

        lockpick_button = tk.Button(root, text="Run Lockpick Script", command=lambda: self.run_script("Lockpick.py"))
        lockpick_button.pack(pady=5)

        atmrobbery_button = tk.Button(root, text="Run ATM Robbery Script", command=lambda: self.run_script("ATM.py"))
        atmrobbery_button.pack(pady=5)

        safe_button = tk.Button(root, text="Run Safe Cracking Script", command=lambda: self.run_script("Safe.py"))
        safe_button.pack(pady=5)

        quit_button = tk.Button(root, text="Quit", command=self.root.destroy)
        quit_button.pack(pady=5)

        # Set the window to stay on top
        self.root.after(1, self.set_window_always_on_top)

    def set_window_always_on_top(self):
        hwnd = win32gui.GetForegroundWindow()
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    def run_script(self, script_name):
        # Clear the output text before running a new script
        self.clear_output()

        try:
            # Set the environment variable to suppress the debugger warning
            env = os.environ.copy()
            env["PYDEVD_DISABLE_FILE_VALIDATION"] = "1"

            process = subprocess.Popen(
                ["python", script_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True,
                errors="ignore",  # Ignore encoding errors in subprocess
                env=env,  # Pass the modified environment
            )

            # Create a separate thread to read and update the GUI
            threading.Thread(target=self.update_output_thread, args=(process,), daemon=True).start()
        except subprocess.CalledProcessError as e:
            self.update_output(e.output)

    def update_output_thread(self, process):
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                self.update_output(output)

    def update_output(self, text):
        # Ensure that the ScrolledText widget is in NORMAL state before modifying its content
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        # Set the ScrolledText widget back to read-only state
        self.output_text.configure(state=tk.DISABLED)

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptRunnerApp(root)
    root.mainloop()
