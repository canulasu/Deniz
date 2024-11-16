import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color_code = colorchooser.askcolor(title="Pick Colour")[1]
    if color_code:
        color_label.config(text=f"Hex Code: {color_code}")

root = tk.Tk()
root.title("Colour Picker")

clr_button = tk.Button(root, text="Pick Colour", command=choose_color)
clr_button.pack(pady=20)

color_label = tk.Label(root, text="Selected Color: None", width=30, height=2)
color_label.pack(pady=20)

root.mainloop()