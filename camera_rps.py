import cv2
from keras.models import load_model
import numpy as np
import time
from time import sleep
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

from ast import If
import random

class Rock_Paper_Scissors:

    def __init__(self):
        #self.computer_choice = random.choice(self.choice_list)
        pass

    def get_computer_choice(self):
        choice_list = ['Rock','Paper','Scissors']
        computer_choice = random.choice(choice_list).lower()
        #print(computer_choice)
        return computer_choice


    def get_user_choice(self):
    
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
        
        #determine the user choice from the values given by the model
        if prediction[0][0] > 0.5:
            user_choice = 'rock'
        elif prediction[0][1] > 0.5:
            user_choice = 'paper'
        elif prediction[0][2] > 0.5:
            user_choice = 'scissors'
        elif prediction[0][3] > 0.5:
            user_choice = 'nothing'
        
        #print(user_choice)
        return user_choice

    def get_winner(self,computer_choice,user_choice):
        user_score=0
        computer_score=0
        if computer_choice == user_choice:
           print('It\'s a tie')
        elif computer_choice == 'rock':
            if user_choice == 'paper':
                print('You won! Paper beats Rock')
                user_score +=1
            else:
                print('You lose! Rock beats Scissors')
                computer_score += 1
        elif computer_choice == 'scissors':
            if user_choice == 'rock':
                print('You won! Rock beats Scissors')
                user_score +=1
            else:
                print('You lose! Scissors beats Paper') 
                computer_score += 1 
        elif computer_choice == 'paper':
            if user_choice == 'scissors':
                print('You won! Scissors beats Paper')
                user_score +=1
            else:
                print('You lose! Paper beats Rock')
                computer_score += 1
        print(f"You have {user_score} points, the computer has {computer_score}")

def play():

    timer()
    game = Rock_Paper_Scissors()
    computer_choice = game.get_computer_choice()
    user_choice = game.get_user_choice()
    game.get_winner(computer_choice,user_choice)

def timer():
    countdown_timer = 3
    while countdown_timer>0:
        print(f"Show you hand in {countdown_timer} seconds")
        sleep(1)
        countdown_timer -= 1
    print('GO!')

if __name__ ==  '__main__':
    choice_list = ['Rock','Paper','Scissors','Nothing']
        
    play()



    
