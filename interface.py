import tkinter as tk
from PIL import Image, ImageTk

import ent

root = tk.Tk()

"""building canvas"""

canvas = tk.Canvas(root, width=400, height=300)
canvas.grid(columnspan=3)


text = tk.Label(root, text="Select a .dat file less than 10mb")


root.mainloop()
