from tkinter import *

window = Tk()

window.title("Tkinter App")

b1 = Button(window, text = "Execute")
# TO add widgets to window - 1
# b1.pack()
#  2 - more flexibility
b1.grid(row = 0, column =0)

e1 = Entry(window)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column =2)

window.mainloop()