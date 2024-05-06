from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:

    questionObject = Question(question=data["text"], answer=data["answer"])
    question_bank.append(questionObject)

quizBrainObject = QuizBrain(question_bank)
currentScore = 0

while quizBrainObject.still_has_question():
    quizBrainObject.next_question()

print("You've completed the quiz")
print(f"Your final score was {quizBrainObject.score}/{quizBrainObject.question_number}")
