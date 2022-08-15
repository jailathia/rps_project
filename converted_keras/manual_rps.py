import random

def get_computer_choice():
    # we are using the convention that 1, 2 and 3 are rock, paper and scissors respectively
    computer_choice = random.choice(["1", "2", "3"])

    return computer_choice

def get_user_choice():
    
    while True:
        user_choice = input("Choose from: \n 1. rock \n 2. paper \n 3. scissors \n Enter the corresponding number: ")
        if user_choice not in ["1", "2", "3"]:
            print("Please choose 1, 2 or 3")
        else:
            break
    
    return user_choice

def get_winner(computer_choice,user_choice):

    result = ["win", "lose", "draw"]
    if computer_choice == user_choice:
        print("Draw")
        return result[2]
    elif user_choice == "1":
        if computer_choice == "2":
            print("Paper beats rock. Computer wins.")
            return result[1]
        else:
            print("Rock beats scissors. User wins.")
            return result[0]