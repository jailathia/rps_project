import cv2
from keras.models import load_model
import numpy as np
import random
import time   

class RPS:

    def __init__(self):
        self.options = ['rock', 'paper', 'scissors', 'nothing']
        self.user_wins = 0
        self.computer_wins = 0
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    def get_computer_choice(self):
        self.computer_choice = random.choice(self.options[0:3])
        return self.computer_choice

    def countdown_timer(self):
        input("Press Enter to continue...")
        time_left = 3
        while time_left > 0:
            print("picture will be taken in " + str(time_left) + " seconds")
            cv2.waitKey(1000)
            time_left -= 1
        print("Start!")
    
    def get_prediction(self):
        
        end_time = time.time() + 1
        while time.time() < end_time: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            
            max_index = np.argmax(prediction[0])
            
            # here the option with the highest percentage is chosen
            self.user_choice = self.options[max_index]
            
            
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break 
        
        print("You showed " +  self.user_choice)

        return self.user_choice

    def get_winner(self):
        computer_choice = self.get_computer_choice()
        user_choice = self.get_prediction()
        while user_choice == 'nothing':
            print("Please try again")
            self.countdown_timer()
            user_choice = self.get_prediction()

        if computer_choice == user_choice:
            print("You both chose " + user_choice + ". This is a draw")
            return "draw"
        elif ((self.options.index(computer_choice))-(self.options.index(user_choice))) % 3 == 1:
            print(f"You chose {user_choice} and the computer chose {computer_choice}. You lose")
            self.computer_wins += 1
        else:
            print(f"You chose {user_choice} and the computer chose {computer_choice}. You win")
            self.user_wins += 1


def play():
    game = RPS()
    
    while game.user_wins < 3 or game.computer_wins < 3:
        game.countdown_timer()
        game.get_winner()
    # After the loop release the cap object
    game.cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    if game.user_wins == 3:
        print("Congratulations! You have won 3 times and therefore won the match")
    else:
        print("The computer has won 3 times and therefore won the match")


if __name__ == '__main__':
    play()