from tkinter import *
import tkinter.messagebox as tmsg

def order():
    tmsg.showinfo("Order Received", f"We have received your order for {varstr.get()}. Thank you for ordering ")

root = Tk()

root.geometry("455x433")
root.title("Radio Button Tutorial")


var = IntVar()
varstr = StringVar()
varstr.set("Radio")
Label(root, text="What would you like to have Sir?",font="lucida 19 bold",  justify=LEFT , padx=14).pack()
radio =Radiobutton(root, text="Burger", padx=14, variable=varstr, value="Burger").pack(anchor='w')
radio =Radiobutton(root, text="Pizza", padx=14, variable=varstr, value="Pizza").pack(anchor='w')
radio =Radiobutton(root, text="Tacos", padx=14, variable=varstr, value="Tacos").pack(anchor='w')
radio =Radiobutton(root, text="Butter Chicken", padx=14, variable=varstr, value="Butter Chicken").pack(anchor='w')

Label(root , text= "--------------").pack()

# this can be done using a list retriving values from a list
listop=['Banana','Cherries','Grapes','Orange','Apple']

for i in range(len(listop)):
    radio = Radiobutton(root, text= listop[i], padx=14, variable=varstr, value=i).pack(anchor='w')

Button(text="Order Now", command=order).pack()
root.mainloop()