from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.window.title("Quizzzzzzler")

        self.canvas = Canvas(height=250, width=300, highlightthickness=0, background="white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas_text = self.canvas.create_text(150, 125, text="Question Text", width=250)
        
        self.true_image = PhotoImage(file='Day 34/images/true.png')
        self.false_image = PhotoImage(file='Day 34/images/false.png')
        self.button_true = Button(image=self.true_image, command=self.button_press_true)
        self.button_true.grid(row=2, column=1, padx=20, pady=20)
        self.button_false = Button(image=self.false_image, command=self.button_press_false)
        self.button_false.grid(row=2, column=0, padx=20, pady=20)

        self.score = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}", background=THEME_COLOR, foreground="white")
        self.score.grid(row=0, column=1, padx=20, pady=20)

        self.change_question()

        self.window.mainloop()


    def change_question(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=question)
    
    def button_press_true(self):
        self.give_feedback(self.quiz.check_answer("True"))        

    def button_press_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def update_score_text(self):
        self.score["text"] = f"Score: {self.quiz.score}/{self.quiz.question_number}"

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(300, self.reset_canvas)

    def reset_canvas(self):
        self.canvas.config(background="white")
        self.update_score_text()
        if self.quiz.still_has_questions():
            self.change_question()
        else:
            messagebox.showinfo(title="End of quiz", message=f"You had {self.quiz.score} correct answers out of {self.quiz.question_number} questions")
            self.window.destroy()

