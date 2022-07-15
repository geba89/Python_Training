from tkinter import *
from turtle import width


window = Tk()
button = Button()
input_field = Entry()
label = Label()
label2 = Label()

def convert():
    global input_field
    global label2

    miles = float(input_field.get())
    label2['text'] = f"{miles * 1.8}"

window.minsize(250, 100)
window.maxsize(600, 600)

label.grid(columnspan=2, row=0,)
label['text'] = "Please enter miles to convert to KM"
input_field['width'] = 20
input_field.grid(column=0, row=1)
button['text'] = "Convert"
button['command'] = convert
button.grid(column=1, row=1)
label2.grid(columnspan=2, row=2)




window.mainloop()

