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

window.minsize(200, 200)

label.pack()
label['text'] = "Please enter miles to convert to KM"
input_field['width'] = 20
input_field.pack()
button['text'] = "Convert"
button['command'] = convert
button.pack()
label2.pack()




window.mainloop()

