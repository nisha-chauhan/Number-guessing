import random
from logo import Logo
Easy_level_turn=10
Hard_level_turn=2

def set_difficulty():
    level= input("Type 'easy' for easy level and 'hard' for hard level\n")
    if level== "easy":
        return Easy_level_turn
    else:
        return Hard_level_turn
    
def check_answer(guess,turns,answer):
    if guess<answer:
        print("To Low")
        return turns - 1
    elif guess>answer:
        print("To High")
        return turns - 1
    else:
        print("You got the ANSWER ,You won ")
        exit()
        
        

# #( "first we have to print some statements")
def game():
    
    print(Logo)
    print("Welcome To The Number Guessing Game")
    print("Guess a Number Between 10 To 100")
    answer=random.randint(1,100)
    turns=set_difficulty()
    guess=0
    while guess!="answer" :
        print(f"You have {turns} attempts left")
        guess= int(input("Make a guess "))
        turns=check_answer(guess,turns,answer)
        if turns==0:
            print("You run out of lives,So you loose")
            return
        elif guess!="answer" :
            print("Guess   again.")
game()
