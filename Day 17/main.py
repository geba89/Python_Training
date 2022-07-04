import question_model
from quiz_brain import QuizBrain
import data

answer = True
question_list = []
for question in data.question_data:
    new_question = question_model.Question(question["text"], question["answer"])
    question_list.append(new_question)

quiz = QuizBrain(question_list)

while answer and quiz.still_has_questions():

    answer = quiz.next_question()
    quiz.check_answer(answer)

if quiz.still_has_questions():
    print(f"Number of correct answers: {quiz.question_number -1}")
else:
    print("Congratulations! you won the game!")
print("Thank you for playing!")