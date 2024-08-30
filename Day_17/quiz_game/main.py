from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for registration in question_data:
    question_bank.append(Question(registration["text"], registration["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\nYour final score is: {quiz.score}/{len(quiz.question_list)}")
