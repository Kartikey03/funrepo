from tkinter import *
import time
import tkinter as tk
from tkinter import ttk
root=Tk()
root.geometry('500x200')
label1=Label(root, text="check weather outside your house")
label1.pack()

label2=Label(root, text="Enter your location: ")
label2.pack()

box=Entry(root, width=50)
box.pack()


def weather():
    root = Tk()
    root.geometry('300x200')

    # Create a label for the loading message
    loading_label = ttk.Label(root, text='Loading...')
    loading_label.pack(pady=20)

    # Create a progress bar
    progress = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
    progress.pack(pady=10)

    # Function to simulate loading
    def fuck():
        root=Tk()
        root.geometry('600x200')

        label=Label(root, text="Behen Ke Laude itna aalas bhi accha nhi h, chl apni gaand utha aur bhr jaake dekh.", font=('Arial Bold',10,"bold"))
        label.pack()
    def load():
        for i in range(1, 101):
            progress['value'] = i
            loading_label['text'] = f'Generating whether report'
            loading_label['text'] = f'Please Wait'

            root.update_idletasks()
            time.sleep(0.05)  # Add a delay of 50 milliseconds between each iteration# Call the load function after a delay
        root.destroy()
        fuck()
    
    root.after(1000, load)



bs= Button(root, text="Look for weather", font=('Arial Bold',10,"bold"), relief=GROOVE, fg='black', command=weather)
bs.pack()

def close():
    root.destroy()

bs= Button(root, text="Close", font=('Arial Bold',10,"bold"), relief=GROOVE, fg='black', command=close)
bs.pack()



root.mainloop()
