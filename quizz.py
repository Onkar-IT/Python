def new_game():
    gusses=[]
    correct_gusses=0
    question_num=1

    for key in questions:
        print("___________________________________________________________________________")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess =input("Enter (A,B,C and D) : ").upper()
        guess = guess.upper()
        gusses.append(guess)
        correct_gusses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_gusses,gusses)


def check_answer(answer,guess):

        if answer == guess:
            print("CORRECT")
            return 1
        else:
            print("WRONG")
            return 0
def display_score(correct_gusses,gusses):
    print("__________________________________________")
    print("RESULTS")
    print("__________________________________________")

    print("Answers : ",end="")
    for i in questions:
        print(questions.get(i),end="")
    print()

    print("Gusses : ", end="")
    for i in gusses:
        print(i, end="")
    print()

    score= int((correct_gusses/len(questions))*100)
    print("Your score is :"+str(score)+"%")

def play_again():
    response=input("Do you want to play again ? (YES/NO)")
    response=response.upper()
    if response=="Y":
        return True
    else:
        return False

questions={"1.what is 1+1 ?":"A",
           "2.do u like pyhton ?":"A",
            "3.do u like java ?":"B"}  #you can edit the question and the answer option from this 

options=[["A.2","B.11","C.Don't know","D.Both A & B"],
["A.YES","B.NO","C.May Be","D.Don't Know"],
["A.YES","B.NO","C.May Be","D.Don't Know"]] #you can change the options accourding to your question and option 

new_game()

while play_again():
    new_game()

print("Thanks for playing")