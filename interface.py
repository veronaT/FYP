import tkinter as tk
from PIL import Image, ImageTk

import ent

root = tk.Tk()

"""building canvas"""

canvas = tk.Canvas(root, width=400, height=300)
canvas.grid(columnspan=3)

banner = Image.open('banner.png')
banner = ImageTk.PhotoImage(banner)
banner_Label = tk.Label(image=banner)
banner_Label.image = banner
banner_Label.grid(column=1, row=0)

text = tk.Label(root, text="Select a .dat file less than 10mb")

root.mainloop()
