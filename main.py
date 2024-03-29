from data import question_data
import random
class Question:
    def __init__(self, question,answer):
        self.question=question
        self.answer=answer

cont=True
score=0
q="a"
a="b"

def generateRandomQuestion():
    global q,a
    questionNumber=random.randint(0,len(question_data)-1)
    print("original answer: "+question_data[questionNumber]["answer"])
    q=question_data[questionNumber]["text"]
    a=question_data[questionNumber]["answer"]


while cont==True:
    generateRandomQuestion()
    new_q=Question(q,a)
    ans=input(new_q.question)
    print("your answer: "+ans)
    if ans.lower()==new_q.answer.lower():
        score+=1
        print(f"your score: {score},\n continue variable: {cont}")
        cont=True
    else:
        cont=False
        break
print(f"final score {score}")
