#Newspaper app
from datetime import date
from tkinter import *

#function to space out text, put linebreak after every 100 char
def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i%100==0 and i!=0:
            final_text +="\n"
    return final_text

#Newspaper program
root = Tk()
root.title("News Paper ")
root.geometry("1000x800")

texts = []
photos=[]
for i in range (0,3):
    with open (f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))
    image = PhotoImage(file=f"{i+1}.png")

   # image = image.resize((225,225), image.ANTIALIAS)#Photoimage resize not working
    #Todo: resize these images
    photos.append(image)

f0 = Frame (root, width=800, height=70)
Label(f0, text="Today's Newspaper" , font="lucida 33 ").pack()
today_date = date.today()
Label(f0, text=today_date , font="lucida 13 ").pack()
f0.pack()

f1 = Frame(root, width=900 , height=200, pady=14)
Label(f1, text=texts[0], padx=22, pady=22).pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")

f2 = Frame(root, width=900 , height=200, pady=14, padx=22)
Label(f2, text=texts[1], padx=22, pady=22).pack(side="right")
Label(f2, image=photos[1], anchor="e", padx=22).pack()
f2.pack(anchor="w")

f3 = Frame(root, width=900 , height=200, pady=14)
Label(f3, text=texts[2], padx=22, pady=22).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")

root.mainloop()

# image_label = Label(root, image=image)
# image_label.pack()
'''message_label = Label(root, textvariable=message_text, wraplength=250)
message_label.pack()

# Create a PhotoImage()
neutral_image = PhotoImage(file="neutral.png")

# Create a new Label using the PhotoImage and pack it into the GUI
image_label = Label(root, image=neutral_image)
image_label.pack()'''