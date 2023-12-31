# V1 Released 31/12/23

import tkinter as tk
from tkinter import scrolledtext
import time
import numpy as np
import pyautogui

class LockpickScript:
    def __init__(self, app):
        self.app = app
        # List of pixel locations representing pins on the lock
        self.pinLocations = [746, 831, 917, 1002, 1088, 1173]

    def run(self):
        # Displaying a countdown message before starting the main loop
        for sleep in range(3):
            self.app.update_output(f"Starting in {3 - sleep}\n")
            time.sleep(1)

        # Looping through each pin location
        for pin in self.pinLocations:
            # Checking if the color at a specific location indicates an ongoing robbery
            if pyautogui.pixel(675, 540) != (255, 201, 3):
                self.app.update_output("Robbery not detected\n")
                break
            
            # Displaying the current pin being processed
            self.app.update_output(f"Pin {self.pinLocations.index(pin)}\n")

            # Flag indicating whether the pin has been clicked or not
            pinNotClicked = True

            # Looping until the pin is successfully clicked
            while pinNotClicked:
                # Checking if the pixels at two specific locations on the pin are similar and have a certain color intensity
                if pyautogui.pixel(pin, 539) == pyautogui.pixel(pin, 541) > (50, 50, 50):
                    pyautogui.click()
                    self.app.update_output("Clicked\n")
                    pinNotClicked = False
                    time.sleep(0.5)

        # Displaying a message when the main loop exits
        self.app.update_output("Exiting...\n")

class ATMRobberyScript:
    def __init__(self, app):
        self.app = app
        # List of RGB color values representing different colours
        self.colours = [
            (255,85,85), # 9ef
            (255,110,85), # c7f
            (255,136,85), # 358
            (255,162,85), # ed1
            (255,187,85), # cda
            (255,213,85), # ce2
            (255,238,85), # 073
            (247,255,85), # bd9
            (221,255,85), # 8b9
            (196,255,85), # 09a
            (170,255,85), # d52
            (145,255,85), # 6bd
            (119,255,85), # 5bc
            (93,255,85), # 21a
            (85,255,102), # 350
            (85,255,128), # 1a1
            (85,255,153), # ffe
            (85,255,179), # bd6
            (85,255,204), # 573
            (85,255,230), # f84
            (85,255,255), # cdd
            (85,230,255), # e82
            (85,204,255), # 9a4
            (85,179,255), # 2c3
            (85,153,255), # 33b
            (85,128,255), # 09c
            (85,102,255), # cea
            (93,85,255), # ebe
            (119,85,255), # c6f
            (145,85,255), # 630
            (170,85,255), # e8d
            (196,85,255), # 08c
            (221,85,253), # caf
            (247,85,255), # f46
            (255,85,238), # 707
            (255,85,213), # 2b5
            (255,85,187), # 6dc
            (255,85,162), # cc1
            (255,85,136), # 375
            (255,85,110), # 9fe
            ]

        # List of pixel locations to click based on the colours
        self.locations = [
            [655,428],
            [655,462],
            [655,492],
            [655,525],
            [655,555],
            [655,590],
            [655,625],
            [655,655],
            [655,690],
            [655,722],
            [820,428],
            [820,462],
            [820,492],
            [820,525],
            [820,555],
            [820,590],
            [820,625],
            [820,655],
            [820,690],
            [820,722],
            [980,428],
            [980,462],
            [980,492],
            [980,525],
            [980,555],
            [980,590],
            [980,625],
            [980,655],
            [980,690],
            [980,722],
            [1145,428],
            [1145,462],
            [1145,492],
            [1145,525],
            [1145,555],
            [1145,590],
            [1145,625],
            [1145,655],
            [1145,690],
            [1145,722],
        ]
    
    # Finds closest colour in the list if colour does not match exactly
    def findClosestInList(self, targetColour):
        targetArray = np.array(targetColour)
        coloursArray = np.array(self.colours)
        differences = np.abs(coloursArray - targetArray)
        if np.any(differences > 10):
            output = None
        else:
            distances = np.linalg.norm(differences, axis=1)
            output = np.argmin(distances)
        return output

    def run(self):
        # Displaying a countdown message before starting the main loop
        for sleep in range(5):
            self.app.update_output(f"Starting in {5 - sleep}\n")
            time.sleep(1)

        # Setting up variables for error handling
        errors = 0
        errorLimit = 2
        waitTime = 1

        # Main ATM hacking loop
        while not errors >= errorLimit :
            target = None
            
            # Looping through a specific range of pixels to find the target colour
            for pixel in range(1040, 1090):
                if pyautogui.pixel(pixel, 355) in self.colours:
                    self.app.update_output("Found target code\n")
                    target = self.colours.index(pyautogui.pixel(pixel, 355))
                    break
                # If exact colour not in list, attempt to find the closest colour in the list
                elif errors != 0:
                    target = self.findClosestInList(pyautogui.pixel(pixel, 355))
                    
            # Handling cases where the target colour is not found
            if target == None:
                self.app.update_output("Target code not found\n")
                errors += 1
                self.app.update_output(f"Attempts left: {2 - errors}\n")
                time.sleep(waitTime)
            else:
                # Clicking on the specified location if the target colour is found
                notClicked = True
                while notClicked:
                    # Click if specified location matches colour
                    if pyautogui.pixel(self.locations[target][0],self.locations[target][1]) == self.colours[target]:
                        pyautogui.click()
                        self.app.update_output("Clicked\n")
                        notClicked = False
                time.sleep(0.5)

        # Displaying a message when the main loop exits
        self.app.update_output("Exiting...\n")

class SafeRobberyScript:
    def __init__(self, app):
        self.app = app

    def run(self):
        self.app.update_output("Currently in development\n")
        # Displaying a message when the main loop exits
        self.app.update_output("Exiting...\n")

class AutoRobbery:
    def __init__(self, root):
        self.root = root
        self.root.title("ERLC Auto Robbery\n")

        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.output_text.pack(padx=10, pady=10)

        # Set the ScrolledText widget as read-only
        self.output_text.configure(state=tk.DISABLED)

        # Add a modified welcome message
        self.update_output("Welcome to ERLC Auto Robbery\nPlease select a robbery to complete:\n")

        # Variable to track execution status
        self.is_running = False

        lockpick_button = tk.Button(root, text="Run Lockpick Script", command=self.run_lockpick_script)
        lockpick_button.pack(pady=5)

        atmrobbery_button = tk.Button(root, text="Run ATM Robbery Script", command=self.run_atm_robbery_script)
        atmrobbery_button.pack(pady=5)

        safe_button = tk.Button(root, text="Run Safe Robbery Script", command=self.run_safe_script)
        safe_button.pack(pady=5)

        quit_button = tk.Button(root, text="Quit", command=self.root.destroy)
        quit_button.pack(pady=5)

        # Set the window to stay on top
        self.set_window_always_on_top()

    def set_window_always_on_top(self):
        self.root.wm_attributes("-topmost", 1)
        self.root.after(100, self.set_window_always_on_top)

    def run_lockpick_script(self):
        self.run_script(LockpickScript(self), "Lockpick Script")

    def run_atm_robbery_script(self):
        self.run_script(ATMRobberyScript(self), "ATM Robbery Script")

    def run_safe_script(self):
        self.run_script(SafeRobberyScript(self), "Safe Robbery Script")

    def run_script(self, script_instance, script_name):
        # Check if a script is already running
        if self.is_running:
            self.update_output("Another script is currently running. Please wait until it finishes.\n")
            return

        # Set the execution status to True
        self.is_running = True

        # Clear the output text before running a new script
        self.clear_output()

        # Add a script name header to the output
        self.update_output(f"Running {script_name}:\n")

        try:
            # Call the script's run method
            script_instance.run()
        except Exception as e:
            self.update_output(f"Error: {e}\n")

        # Set the execution status to False when the script finishes
        self.is_running = False

    def update_output(self, text):
        # Ensure that the ScrolledText widget is in NORMAL state before modifying its content
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        # Set the ScrolledText widget back to read-only state
        self.output_text.configure(state=tk.DISABLED)

        # Update the GUI immediately
        self.root.update_idletasks()

    def clear_output(self):
        # Ensure that the ScrolledText widget is in NORMAL state before clearing its content
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        # Set the ScrolledText widget back to read-only state
        self.output_text.configure(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoRobbery(root)
    root.mainloop()
