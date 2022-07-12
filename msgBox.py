#This program uses gui window ask for height and width resize the window of GUI


# menu /submenus in gui
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.geometry("733x566")
root.title("  My PyEditor")
def myfunc():
    print("------>>> ----->>>>>>")

def help():
    print("I wil help you")
    tmsg.showinfo("Help" , "Thank you for taking my help")
def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience good? " , "Did you use this GUI?")
    if value == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong, we will fix it"
    tmsg.showinfo("Experience", msg)

def smthng():
    ans = tmsg.askretrycancel("something 1", "something 2")
    if ans :
        print("Retry")
    else:
        print("Cancel -Bye")

# use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(lable="File", command=myfunc)
# mymenu.add_command(lable="Exit", command=quit)
# mymenu.add_command(lable="Edit", command=myfunc)
# root.config(menu = mymenu)

yourmenubar = Menu(root)

m1 = Menu(yourmenubar, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save Project", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu = yourmenubar)
yourmenubar.add_cascade(label="File", menu=m1)


m2 = Menu(yourmenubar, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)

yourmenubar.add_cascade(label="File", menu=m2)
root.config(menu = yourmenubar)


m3 = Menu(yourmenubar, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate us", command=rate)
m3.add_command(label="something", command=smthng )
yourmenubar.add_cascade(label="Help", menu=m3)

root.config(menu = yourmenubar)

root.mainloop()
