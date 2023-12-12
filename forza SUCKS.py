import time
import pyautogui
import logging
import threading
import tkinter as tk
from tkinter import font

# Configure logging
logging.basicConfig(filename='key_press.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Global variable to control the loop
running = False

def press_key():
    while running:
        # Simulate pressing the "D" key
        pyautogui.press('d')

        # Log the key press
        logging.info('"D" key pressed at %s', time.strftime('%Y-%m-%d %H:%M:%S'))

        # Sleep for 5 minutes
        time.sleep(300)  # 300 seconds = 5 minutes

def start():
    global running
    if not running:
        running = True
        # Log that the program has started
        logging.info('Program started at %s', time.strftime('%Y-%m-%d %H:%M:%S'))
        # Start a new thread for the key press function
        threading.Thread(target=press_key).start()

def stop():
    global running
    running = False
    # Log that the program has stopped
    logging.info('Program stopped at %s', time.strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Forza Sucks")

    # Comic Sans font
    comic_sans_font = font.Font(family="Comic Sans MS", size=12)

    # Program name label
    program_label = tk.Label(root, text="Forza FUCKING sucks", font=comic_sans_font)
    program_label.pack(pady=10)

    # Start button
    start_button = tk.Button(root, text="Start", command=start)
    start_button.pack(pady=10)

    # Stop button
    stop_button = tk.Button(root, text="Stop", command=stop)
    stop_button.pack(pady=10)

    # Run the main loop
    root.mainloop()
