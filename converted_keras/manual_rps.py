import random

def get_computer_choice(comp_choice, self)

    self.comp_choice = random.choice(["rock", "paper", "scissors"])

    return comp_choice

def get_user_choice(user_choice, self)

    self.user_choice = input("Choose from: \n 1. rock \n 2. paper \n 3. scissors \n Type the corresponding number: ")

    return user_choice
