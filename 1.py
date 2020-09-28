from tkinter import *
import random, string
from PIL import ImageTk,Image

import pyperclip
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")
Label(root, text = 'STRONG PASS GENERATOR' , font ='Times 17 bold').pack()
Label(root, text ='By Anubha Gupta', font ='arial 12 bold').pack(side = BOTTOM)
pass_label = Label(root, text = 'Pass Length', font = 'Times 15 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()
pass_str = StringVar()

def Generator():
    password = ''

   
    for x in range(0,pass_len.get()):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(root, text = "GENERATE PASSWORD" ,font='Times 14 bold', command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD',font='Times 14 bold', command = Copy_password).pack(pady=5)



canvas=Canvas(root,width=400,height=300)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\AnubhaG\\Desktop\\Python project\\image.jpg"))
canvas.create_image((0,0),anchor='nw',image=image)

canvas.pack()
root.mainloop()