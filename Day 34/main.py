from numpy import pad
from question_model import Question
import data
from quiz_brain import QuizBrain
import html
import ui


question_data = data.data()
questions = question_data.get_questions()

question_bank = []
for question in questions:
    question_text = question["question"]
    question_text = html.unescape(question_text)
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = ui.QuizUI(quiz)