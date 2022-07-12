from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("Title goes here")
# this prog is preparation for two small proj notepad and calculator

#use of icon , we can use custom.ico file, will change feather of tkinter
# u can download free icons form internet

root.wm_iconbitmap("1.ico")
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command=root.destroy).pack()

root.mainloop()