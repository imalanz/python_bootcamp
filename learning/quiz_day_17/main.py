from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    text = question['text']
    answer = question['answer']
    question_bank.append(Question(text, answer))

quiz = QuizzBrain(question_bank)
quiz.next_question()