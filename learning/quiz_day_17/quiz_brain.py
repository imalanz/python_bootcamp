from data import question_data

class QuizzBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number > len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        result = input(f"Q{self.question_number}: {current_question} (True/False): ")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
            print(f"your score is: {self.score}/{self.question_number}")
        else:
            print("Thats wrong")
