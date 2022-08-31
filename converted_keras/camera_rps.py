import cv2
from keras.models import load_model
import numpy as np
import random

options = ['rock', 'paper', 'scissors', 'nothing']

class RPS:

    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.user_choice = ""
        self.computer_choice = ""

    def get_computer_choice(self):
        self.computer_choice = random.choice(options.remove('nothing'))
        return self.computer_choice

    
    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            
            # here the option with the highest percentage is chosen
            self.user_choice = options[np.argmax(prediction[0])]
            print("You showed " +  self.user_choice)
            
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows() 
        
        
        return self.user_choice

    def get_winner(self):
        if self.computer_choice == self.user_choice:
            print("You both chose " + self.user_choice + ". This is a draw")
            return "draw"
        elif ((options.index(self.computer_choice))-(options.index(self.user_choice))) % 3 == 1:
            print("The computer chose " + self.computer_choice + " and you chose " + self.user_choice ". You lose")
            return "loss"
        else:
            print("The computer chose " + self.computer_choice + " and you chose " + self.user_choice ". You win")
            return "win"

    def play_once(self)
        while self.user_choice not in options.remove('nothing'):
            self.user_choice = self.get_prediction
            return self.user_choice
        

def play():
    game = RPS()
    while True:
        game.play_once()

