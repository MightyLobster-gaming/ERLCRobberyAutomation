# ERLCRobberyAutomation

Script Runner
Script Runner is a simple Python application that provides a graphical interface to run various scripts. It utilizes Tkinter for the GUI and subprocess to execute Python scripts.

Installation
Clone the repository:

``Copy code
git clone https:`//github.com/yourusername/script-runner.git
Navigate to the project directory:``

``
Copy code
cd script-runner
Create and activate a virtual environment (optional but recommended):``

Copy code
python -m venv venv
source venv/bin/activate  # On Unix/Linux
# or
.\venv\Scripts\activate  # On Windows
Install the required packages:

The application requires Python 3.x. Install the required packages using the following command:

bash
Copy code
pip install -r requirements.txt
Usage
Run the program:

Navigate to the project directory and run the following command:

bash
Copy code
python script_runner.py
Using the application:

Upon launching the application, you'll see a graphical interface with several buttons:

Run Lockpick Script: Executes the "lockpick.py" script.
Run ATM Robbery Script: Executes the "atmrobbery.py" script.
Safe: Executes the "safe.py" script.
Quit: Closes the application.
The output window displays the printed output of the executed scripts. The window is read-only and displays messages from the executed scripts.

You can modify the script names in the code to run your custom scripts.

Notes
This application was built and tested on a Windows platform.
Make sure to adjust script names or paths as per your script fil
