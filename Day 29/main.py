from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def append_password_file(new_entry):
    file = open('Day 29/mypass.txt', 'a')
    file.write(new_entry)
    file.close()

def create_entry():
    website = web_input.get()
    email_address = email_input.get()
    password = pass_input.get()
    new_entry = f"{website} | {email_address} | {password} \n"
    append_password_file(new_entry)

    web_input.delete(0, END)
    pass_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

logo_image = PhotoImage(file='Day 29/logo.png')

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

web_input = Entry(width=44)
web_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=44)
email_input.insert(0,"geba89@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

pass_input = Entry(width=24)
pass_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=41, command=create_entry)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()