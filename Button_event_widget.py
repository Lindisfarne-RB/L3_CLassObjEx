from tkinter import *

'''THIS IS FOR EVENTS
all keypress are trigerring the events, all tkinter events https://www.tutorialspoint.com/list-of-all-tkinter-events
https://docs.python.org/3/library/tkinter.html#bindings-and-events
tkinter passes an argument internally - which is event
event.x and event.y are cordinates of the button
'''
def clickme(event):
    print(f"you clicked on the button at {event.x} , {event.y}")

root = Tk()
root.title("Events in Tkinter")
root.geometry("600x400")

widget = Button(root, text="Click me please")
widget.pack()

widget.bind('<Button-1>', clickme)
widget.bind('<Double-1>', quit)

root.mainloop()