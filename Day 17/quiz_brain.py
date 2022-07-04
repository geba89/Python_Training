class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
    
    def next_question(self):
        question = self.question_list[self.question_number]
        question_answer = input(f"Q{self.question_number}. : {question.text} True or False?: ").lower()        
        self.question_number += 1
        if question_answer == question.answer.lower():
            return True
        return False
    
    def still_has_questions(self):
        if self.question_number > len(self.question_list):
            return False
        return True

    def check_answer(self, answer):
        if answer:
            print("Correct! Let's move to next one!")
        else:
            print("Ahh incorrect. Sorry!")
