from tkinter import *
import playground

window  = Tk()

window.minsize(500, 300)
window.title("First GUI")

my_label = Label(text="Hello World", font=("Arial", 20, "normal"))
my_label.pack()
my_label["text"] = "Hello !!!!"
my_label.config(text = "Hello?")
input = Entry()
counter = 0
def button_clicked():

    global counter
    global my_label
    global input
    counter += 1
    my_label.config(text=f"You clicked button {counter} times!")
    print(input.get())

button = Button(text="Click Me!", command=button_clicked)
button.pack()



input.pack()
input['width'] = 10

window.mainloop()
