import math
import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
count_down_bool = False
timer_running = False
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def setup_timer():
    global reps
    global timer_running    
    if not timer_running:
        return
    reps += 1
    if reps % 8 == 0:
        add_mark()
        label.config(text="Break", fg=PINK)
        timer(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        add_mark()
        label.config(text="Break", fg=PINK)
        timer(SHORT_BREAK_MIN * 60)
    else:
        window.lift()
        label.config(text="Work", fg=RED)
        timer(WORK_MIN * 60)

def timer(minutes):
    if not timer_running:
        return
    min = math.floor(minutes/60)
    secs = minutes % 60
    if secs < 10 :
        secs = "0" + str(secs)
    canvas.itemconfig(canvas_timer, text=f"{min}:{secs}")
    if minutes > 0:        
        window.after(1000, timer, minutes -1)   
    else:
        setup_timer()        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global count_down_bool  
    global timer_running  
    if count > -1:
        canvas.itemconfig(canvas_timer, text=count)
        count_down_bool = True
        window.after(1000, count_down, count -1)           
    else:
        count_down_bool = False
        timer_running = True
        setup_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)



label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
label.grid(column=1, row=0)

pomodoro_image = tkinter.PhotoImage(file='Day 28/tomato.png')
canvas = tkinter.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=pomodoro_image)
canvas_timer = canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

def add_mark():
    global check_text
    check_text = check_text + "✓"
    check_mark['text'] = check_text

def reset_mark():
    if count_down_bool:
        return
    global check_text
    global timer_running
    global reps
    reps = 0
    label.config(text="Timer", fg=GREEN)
    timer_running = False
    check_text = ''
    check_mark['text'] = check_text
    canvas.itemconfig(canvas_timer, text="00:00")

def trigger_count_down():
    count_down(5)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0, borderwidth=0, activebackground=YELLOW, activeforeground="white")
reset_button['command'] = reset_mark
reset_button.grid(column=2, row=2)

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0, borderwidth=0, activebackground=YELLOW, activeforeground="white")
start_button['command'] = trigger_count_down
start_button.grid(column=0, row=2)

check_text = ''
check_mark = tkinter.Label(text=check_text, font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(column=1, row=3)

window.mainloop()


