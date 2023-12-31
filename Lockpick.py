# Importing necessary libraries
import pyautogui
import time

# Displaying a message indicating the script is starting
print("Opening Lockpick.py")

# List of pixel locations representing pins on the lock
pinLocations = [746, 831, 917, 1002, 1088, 1173]

# Displaying a countdown message before starting the main loop
for sleep in range(3):
    print(f"Starting in {3 - sleep}")
    time.sleep(1)

# Looping through each pin location
for pin in pinLocations:
    # Checking if the color at a specific location indicates an ongoing robbery
    if pyautogui.pixel(675, 540) != (255, 201, 3):
        print("Robbery not detected")
        break
    
    # Displaying the current pin being processed
    print(f"Pin {pinLocations.index(pin)}")

    # Flag indicating whether the pin has been clicked or not
    pinNotClicked = True

    # Looping until the pin is successfully clicked
    while pinNotClicked:
        # Checking if the pixels at two specific locations on the pin are similar and have a certain color intensity
        if pyautogui.pixel(pin, 539) == pyautogui.pixel(pin, 541) > (50, 50, 50):
            pyautogui.click()
            print("Clicked")
            pinNotClicked = False
            time.sleep(0.5)
