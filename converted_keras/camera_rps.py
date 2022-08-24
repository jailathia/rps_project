import cv2
from keras.models import load_model
import numpy as np

options = ['rock', 'paper', 'scissors', 'nothing']

class RPS:

    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.user_choice = ""
        self.computer_choice = ""

    
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
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        confidence_percentage = prediction[0]
        print(confidence_percentage)
        if np.argmax(confidence_percentage) == 3:
            self.user_choice = options[3]
            print("No input detected. Please try again.")
        elif max(confidence_percentage) < 0.75:
            self.user_choice = options[3]
            print("No input detected. Please try again.")
        else:
            self.user_choice = options[np.argmax(confidence_percentage)]
            print("You showed " +  self.user_choice)
        return self.user_choice

