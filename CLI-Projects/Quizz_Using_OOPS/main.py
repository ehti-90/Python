from data import question_data
from question import QuestionsBank
from quizzbrain import brain

# Here we load data in the QuestionBank Class 
length = len(question_data)

q_bank =[]

for i in range(length):
    new_question = QuestionsBank(question_data[i]["text"],question_data[i]["answer"] ) 
    # creating object and input data
    q_bank.append(new_question) # appending the question objects into list

quizz = brain(q_bank)

while quizz.still_has_question():   #   if data has questions show next
    quizz.next_question()   #   check_answer method will be check inside .next_question

quizz.score_report()