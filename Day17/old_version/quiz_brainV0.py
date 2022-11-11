import self


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_choice = ""
        self.score = 0

    def still_has_question(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        # same evaluated by computer
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_anwser = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(user_anwser, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you are correct")
            self.score += 1

        else:
            print("you are wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is :{self.score}/{self.question_number}")
        print("\n")
