from tkinter import *
from tkinter import messagebox
import csv
import random
import pandas as p

BACKGROUND_COLOR = "#B1DDC6"

translation = False
pair = True
french_word = ""
english_word = ""
cancel_id = ''
data = {}

with open('Day 31/data/french_words.csv', mode="r") as input:
    reader = csv.reader(input)
    data = {rows[0]:rows[1] for rows in reader}

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flashy")

card_back = PhotoImage(file='Day 31/images/card_back.png')
card_front = PhotoImage(file='Day 31/images/card_front.png')
button_correct_image = PhotoImage(file='Day 31/images/right.png')
button_wrong_image = PhotoImage(file='Day 31/images/wrong.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
top_text = canvas.create_text(400, 150, text="LANGUAGE", font=("Ariel", 40, "italic"))
bottom_text = canvas.create_text(400, 263, text="WORD", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

def delete_item():
    del data[french_word]
    with open('Day 31/data/french_words.csv', 'w') as f:
        for key in data.keys():
            f.write("%s, %s\n" % (key, data[key].strip()))

def correct_click():
    global translation
    translation = True 
    delete_item()
    window.after_cancel(cancel_id)
    swap_cards()

def wrong_click():
    window.after_cancel(cancel_id)
    swap_cards()

button_wrong = Button(image=button_wrong_image, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR, command=wrong_click)
button_wrong.grid(row=1, column=0)

button_correct = Button(image=button_correct_image, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR, command=correct_click)
button_correct.grid(row=1, column=1)



def swap_cards():
    global cancel_id
    change_image()
    cancel_id = window.after(3000, swap_cards)  

def change_image():
    global translation
    if translation:
        set_pair()
        canvas.itemconfig(canvas_image, image=card_front)
        canvas.itemconfig(top_text, text="French")
        canvas.itemconfig(bottom_text, text=french_word)
        translation = False
        
    else:
        canvas.itemconfig(canvas_image, image=card_back)   
        canvas.itemconfig(top_text, text="English")    
        canvas.itemconfig(bottom_text, text=english_word) 
        translation = True

def set_pair():
    global pair
    global french_word
    global english_word
    try:
        french_word, english_word = random.choice(list(data.items()))   
    except IndexError:
        messagebox.showinfo(title="Flashy", message="All words completed!")
        window.destroy()

set_pair()
canvas.itemconfig(canvas_image, image=card_front)
canvas.itemconfig(top_text, text="French")
canvas.itemconfig(bottom_text, text=french_word)
translation = False
cancel_id = window.after(3000, swap_cards) 

window.mainloop()

