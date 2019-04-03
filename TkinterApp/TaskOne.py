from tkinter import  *

window =Tk()

kilo_text = StringVar()
grams_text = StringVar()
pounds_text = StringVar()
ounces_text = StringVar()



text_kg = Label(window, text = "Kg")
text_kg.grid(row =0, column =0)

entry_kilo = Entry(window, textvariable =kilo_text)
entry_kilo.grid(row =0, column =1)

def convert_to_pounds(kg):
    return float(kg * 2.20462)

def convert_to_ounces(kg):
    return float(kg * 35.274)

def convert_to_grams(kg):
    return float(kg*1000)

def refresh():
    entry_grams.delete(0, END)
    entry_pounds.delete(0, END)
    entry_ounces.delete(0, END)

def convert_kilo():
    refresh()
    kg = float(kilo_text.get())
    grams = convert_to_grams(kg)
    pounds = convert_to_pounds(kg)
    ounces = convert_to_ounces(kg)
    entry_grams.insert(END, grams)
    entry_pounds.insert(END, pounds)
    entry_ounces.insert(END, ounces)


button_convert = Button(window, text = "Convert", command = convert_kilo)
button_convert.grid(row = 0, column = 2)


entry_grams = Entry(window, textvariable = grams_text)
entry_grams.grid(row =1, column =0)

entry_pounds = Entry(window, textvariable = pounds_text)
entry_pounds.grid(row =1, column =1)

entry_ounces = Entry(window, textvariable = ounces_text)
entry_ounces.grid(row =1, column =2)


window.mainloop()