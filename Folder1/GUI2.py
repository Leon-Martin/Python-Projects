from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Hello')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like cats?')

if answer == 'yes':
    print(' :D ')

root.mainloop()
