import random

def computer_choice():
    return random.choice([1, -1, 0])

def user_choice():
    youstr = (input("Enter your key : "))
    mydict = {
        "s" : 1,
        "w" : -1,
        "g" : 0
    }
    if youstr not in mydict:
        print("Invalid Choice!")
        return None
    return mydict[youstr]

def play_game():
    reverseDict = {
        1 : "Snake",
        -1 : "Water",
        0 : "Gun"
    }
    computer = computer_choice()
    you = user_choice()
    if you is None:
        return
    
    print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]} ")

    result ={
        (1,-1) : "You lose",
        (-1, 1) : "You win",
        (0, 1) : "You lose",
        (1, 0) : "You win",
        (0, 1) :"You lose",
        (0, -1) : "You win",
        (-1, 0) : "You lose"
     }

    if computer == you :
        print("Its a draw..")
    else :   
        print(result.get((computer, you), "Something went wrong!"))


while True:
    play_game()
    if input ("Try again? y/n :").lower() != "y":
        break