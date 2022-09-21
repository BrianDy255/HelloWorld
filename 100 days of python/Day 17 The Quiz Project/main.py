from question_model import Question
from quiz_brain import QuizBrain
from opentDB import question_data

question_bank = []

for question in question_data:
    get_question = question['question']
    get_answer = question['correct_answer']
    question_object = Question(get_question,get_answer)
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"You're final score is {quiz.score}/{quiz.question_number}")
