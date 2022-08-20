from tkinter import *

root = Tk()

def login():
    id = txt_id.get()

txt_id = Entry(root)
txt_id.grid(row=0,column=1)
txt_pw = Entry(root, show="*")
txt_pw.grid(row=1,column=1)

label_id = Label(root, text='ID:')
label_id.grid(row=0,column=0)
label_pw = Label(root, text="Password:")
label_pw.grid(row=1,column=0)

button_login = Button(root, text="login", command=login)
button_login.grid(row=2,column=1)
root.mainloop()