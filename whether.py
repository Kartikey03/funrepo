import time
import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('300x200')

# Create a label for the loading message
loading_label = ttk.Label(root, text='Loading...')
loading_label.pack(pady=20)

# Create a progress bar
progress = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
progress.pack(pady=10)

# Function to simulate loading

def load():
    for i in range(1, 101):
        progress['value'] = i
        loading_label['text'] = f'Generating whether report'
        loading_label['text'] = f'Please Wait'

        root.update_idletasks()
        time.sleep(0.05)  # Add a delay of 50 milliseconds between each iteration# Call the load function after a delay
    root.destroy()
root.after(1000, load)
tk.mainloop()