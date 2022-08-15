import random

def get_computer_choice(comp_choice, self)

    self.comp_choice = random.choice(["rock", "paper", "scissors"])

    return comp_choice

def get_user_choice(user_choice, self)
    while True
        user_choice = input("Choose from: \n 1. rock \n 2. paper \n 3. scissors \n Type the corresponding number: ")
        if user_choice not in ["1", "2", "3"]
            print("Please enter 1, 2 or 3")
        else:
            break
    
    self.user_choice = user_choice
    
    return user_choice
