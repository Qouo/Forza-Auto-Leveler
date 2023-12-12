# TODO -- add image of what the car level 50 should look like for the program to stop.

import time
import pyautogui
import logging
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

# Configure logging
logging.basicConfig(filename='key_press.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def press_key():
    # Simulate pressing the "D" key
    pyautogui.press('d')

    # Log the key press
    logging.info('"D" key pressed at %s', time.strftime('%Y-%m-%d %H:%M:%S'))

def check_game_level():
    # Capture the screen
    screenshot = pyautogui.screenshot()

    # Load the template image from the bundled data
    template_data = open("level_50_template.png", "rb").read()
    template_image = Image.open(BytesIO(template_data))

    # Convert the template image to a NumPy array
    template = np.array(template_image)

    # Convert the screenshot to a NumPy array
    screenshot_np = np.array(screenshot)

    # Convert the screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

    # Set a threshold for matching
    threshold = 0.8
    loc = np.where(result >= threshold)

    # Check if any matches are found
    return len(loc[0]) > 0

if __name__ == "__main__":
    # Run the script while the game level is not 50
    while not check_game_level():
        press_key()
        time.sleep(300)  # 300 seconds = 5 minutes

    print("Game reached level 50. Stopping the script.")
