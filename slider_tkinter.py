from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.geometry("455x233")
root.title("Slider Tutorial")

def getdollar():
    print(f"We hve credited {myslider2.get()} dollar in your acc")
    tmsg.showinfo("Amount credited",f"we credited {myslider2.get()} $ in your acc")



Label(root, text="How many dollars you want").pack()
myslider = Scale(root, from_ = 0 , to=455) # vertical
myslider2 = Scale(root,  from_ = 0 , to=100, orient = HORIZONTAL)
#myslider.pack()
myslider3 = Scale(root,  from_ = 10 , to=500, orient = HORIZONTAL, tickinterval=5)
myslider3.set(15)
#myslider.pack()
myslider2.pack()
myslider3.pack()


Button(root, text="Come...Get Dollars!!!", pady=10, command=getdollar).pack()
# reading the value from slider

root.mainloop()