# a good resource tkinter  -  https://dafarry.github.io/tkinterbook/
#tk docs tutorial - very gppd

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
    # 1.0 means delete from  first line and 0th character to end

def openFile():
    global file
    file =askopenfilename(defaultextension = ".txt",
                          filetypes = [("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()



def cut ():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad" , "Notepad by me" )
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile =
                                 'Untitled.txt', defaultextension = ".txt",
                          filetypes = [("All Files", "*.*"),
                                    ("Text Documents", "*.txt")] )
        if file == "":
            file = None
        else:
            #Save as a new File
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File saved")
    else:
        f = open(file, "w") #save the file
        f.write(TextArea.get(1.0, END))
        f.close()


def saveAsFile():
    pass
def quitApp():
    root.destroy()



if __name__ == '__main__':
    root = Tk()
    root.title("Untitled Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("644x788")
    #Add textarea
    TextArea = Text(root , font = "lucida 13")
    file = None
    TextArea.pack(fill = BOTH, expand=True)

    #Lets add menubar
    MenuBar = Menu(root)

    #File menu starts
    FileMenu = Menu (MenuBar, tearoff=0)
    #To open new File
    FileMenu.add_command(label = "New" ,  command = newFile)

    #To open already existing file
    FileMenu.add_command(label="Open File",  command=openFile)

    #To save the current File
    FileMenu.add_command(label="Save", command=saveFile)

    # To save As the current File
    FileMenu.add_command(label="Save As", command=saveAsFile)

    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    #file menu ends

    # Edit menu starts
    EditMenu = Menu(MenuBar, tearoff=0)

    # To cut
    EditMenu.add_command(label="Cut", command=cut)
    # To copy
    EditMenu.add_command(label="Copy", command=copy)

    # To paste the current File
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label = "Edit", menu=EditMenu)
    # edit menu ends

    # Help menu starts
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help" , menu= HelpMenu)
    # Help menu ends



    #adding scroll bar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.config(menu=MenuBar)

    root.mainloop()
