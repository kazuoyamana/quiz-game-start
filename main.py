from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
	question_bank.append(Question(question["text"], question["answer"]))


question = QuizBrain(question_bank)


while question.still_has_questions():

	question.next_question()

