from tkinter import *

window = Tk()

window.title("Tkinter App")

def kmToMiles():
    print("Success : "+e1_val.get())
    miles = float(e1_val.get())*1.6
    t1.insert(END, miles)

# command  = funct without brackkets
b1 = Button(window, text = "Execute", command = kmToMiles)
# TO add widgets to window - 1
# b1.pack()
#  2 - more flexibility
b1.grid(row = 0, column =0)

# Stores value of e1
e1_val = StringVar()
e1 = Entry(window, textvariable = e1_val)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column =2)

window.mainloop()