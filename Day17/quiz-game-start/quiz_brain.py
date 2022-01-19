class QuizBrain:


    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}:{current_q.text} (True/False):")
        self.check_answer(user_answer, current_q.ans)
    def still_has_questions(self):
         return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
         if user_answer.lower() == correct_answer.lower():
             print("You got it right")
             self.score += 1
         else :
             print("you are wrong")
         if self.question_number == len(self.question_list):
             print(f"the corect answer was: {correct_answer}")
             print(f"Your current score is {self.score}/{self.question_number}")
             print("\n")
