from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def append_password_file(new_entry):
    try:
        with open('Day 29/mypass.json', 'r') as file:        
            all_data = json.load(file)
            all_data.update(new_entry)
        
        with open('Day 29/mypass.json', 'w') as file:        
            json.dump(all_data, file, indent=True)
        
    except FileNotFoundError:
        with open('Day 29/mypass.json', 'w') as file:        
            json.dump(new_entry, file, indent=True)
        
    

def create_entry():
    website = web_input.get()
    email_address = email_input.get()
    password = pass_input.get()
    if website == "" or email_address == "" or password == "":
        messagebox.showerror(title="Failed.", message="Please fill all fields.")
        return

    new_entry = {website : {"email" : email_address, "password" : password}}    
    append_password_file(new_entry)

    messagebox.showinfo(title="Success", message="Password added!")

    web_input.delete(0, END)
    pass_input.delete(0, END)

def search_password():
    with open('Day 29/mypass.json', 'r') as file:
        try:
            all_data = json.load(file)
            website_data = all_data[web_input.get()]
            password = website_data["password"]
            email = website_data["email"]
            messagebox.showinfo(title="Webiste Data", message=f"Password: {password}\n Email: {email}")
        except KeyError:
            messagebox.showwarning(title="No Data", message=f"No data for {web_input.get()} found.")
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

web_input = Entry(width=24)
web_input.grid(row=1, column=1)

email_input = Entry(width=44)
email_input.insert(0,"geba89@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

pass_input = Entry(width=24)
pass_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=41, command=create_entry)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=16, command=search_password)
search_button.grid(row=1, column=2)

window.mainloop()