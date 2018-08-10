from tkinter import *
import tkinter.messagebox


def doNothing():
    print("True")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project...",command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# ***** Tool Bar ******
toolbar = Frame(root, bg="blue")

insertButton = Button(toolbar,text="Insert Image", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP,fill=X)

# **** status bar *****

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
