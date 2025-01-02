from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nextQuestion()

"""you're completed the quiz
    your final score/total questions attend"""
print("congratulation on completing the above quiz")
print(f"Your total score is: {quiz.score}/{quiz.question_number}")