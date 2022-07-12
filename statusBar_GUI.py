from tkinter import *

def upload():
    statusvar.set("Busy.....")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")


root =Tk()
root.geometry("455x233")
root.title("Status Bar Lesson")

#there is no widget status bat - we will use label and border to make it look like stats bar

statusvar = StringVar()
statusvar.set("Ready ")
sbar =  Label (root, textvariable=statusvar, relief = SUNKEN,
               anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload" , command=upload).pack()
root.mainloop()