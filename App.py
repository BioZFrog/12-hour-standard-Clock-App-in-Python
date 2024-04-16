from tkinter import *
from tkinter.ttk import * 
import time
from time import strftime
from PIL import Image, ImageTk

# Creating & Designing Screen
root = Tk()
root.title("Clock")
time_color = "orange"
background_color = "black"
label = Label(root, font = ("ds-digital", 80), background = background_color, foreground = time_color)
label.pack(anchor="center")

# Starting Format
print("--------___------------------12 Hour Clock App in Python------------------___--------")

print("Generating Clock....\n")
time.sleep(3)

# Window Icon
ico = Image.open("H.jpg")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Time 
def time():
    string = strftime(f"%I:%M:%S %p") # 12-hour-standard. Use (f"%H:%M:%S %p") for 24-hour-standard
    label.config(text=string)
    label.after(1000, time)

# Running App
time()
mainloop()
