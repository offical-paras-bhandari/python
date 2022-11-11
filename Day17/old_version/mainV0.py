from question_modelV0 import Question
from dataV0 import question_data
from quiz_brainV0 import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # save data in new_question and send data in class Question
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("you have completed the quiz")
print(f"your final score was:{quiz.score}/{quiz.question_number}")