"""Create a class called QuizBrain.

Write an _init_() method.

Initialise the question_number to 0.

Initialise the question_list to an input."""

class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self):
            return self.question_number<len(self.question_list)

    """Retrieve the item at the current question_number from the question_list.

    Use the input() function to show the user the Question text and ask for the user's answer."""

    def nextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, u_answer, r_answer):
        if u_answer.lower() == r_answer.lower():
            self.score +=1
            print("Answer is correct")
        else:
            print("Choose the wrong answer")
        print(f"The correct answer is: {r_answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")
