from tkinter import *

def update():
    print("Updating the GUI")
    root.geometry(f"{height.get()}x{width.get()}")

root = Tk()
root.geometry("344x233")
root.title("Window Resizer")
width = StringVar()
height = StringVar()

Entry (root, textvariable=width).pack()
Entry (root, textvariable=height).pack()
Button(root, text="Apply",  command=update).pack()
root.mainloop()
