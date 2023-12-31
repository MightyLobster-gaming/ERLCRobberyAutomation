# Importing necessary libraries
import pyautogui
import time
import numpy as np

print("Opening ATMRobbery.py")

# List of RGB color values representing different colours
colours = [
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
locations = [
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
def findClosestInList(targetColour):
    targetArray = np.array(targetColour)
    coloursArray = np.array(colours)
    differences = np.abs(coloursArray - targetArray)
    if np.any(differences > 10):
        output = None
    else:
        distances = np.linalg.norm(differences, axis=1)
        output = np.argmin(distances)
    return output

# Displaying a countdown message before starting the main loop
for sleep in range(5):
    print(f"Starting in {5 - sleep}")
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
        if pyautogui.pixel(pixel, 355) in colours:
            print("Found target code")
            target = colours.index(pyautogui.pixel(pixel, 355))
            break
        # If exact colour not in list, attempt to find the closest colour in the list
        elif errors != 0:
            target = findClosestInList(pyautogui.pixel(pixel, 355))
            
    # Handling cases where the target colour is not found
    if target == None:
        print("Target code not found")
        errors += 1
        print(f"Attempts left: {2 - errors}")
        time.sleep(waitTime)
    else:
        # Clicking on the specified location if the target colour is found
        notClicked = True
        while notClicked:
            # Click if specified location matches colour
            if pyautogui.pixel(locations[target][0],locations[target][1]) == colours[target]:
                pyautogui.click()
                print("Clicked")
                notClicked = False
        time.sleep(0.5)

# Displaying a message when the main loop exits
print("Exiting...")