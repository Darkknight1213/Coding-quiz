from data import question_data
from question_model import Question
from quiz_brain import Brain

question_bank = []

for i in question_data:
    obj = Question(i["text"], i["answer"])
    question_bank.append(obj)

number_of_questions = int(input("How many questions you want to attend: "))

question = Brain(question_bank, number_of_questions)
while question.still_has_qs():
    question.next_question()
print("Congratulations, You've completed the Quiz")
print(f"your score is {question.score}/{number_of_questions}")