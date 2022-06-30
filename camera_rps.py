from typing_extensions import Self
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
        self.user_score = 0
        self.computer_score = 0
        pass


    def open_camera(self):
    
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            self.prediction = model.predict(data)
            cv2.imshow('frame', frame)

            while self.user_score <3 and self.computer_score <3:
                self.timer()
                print(self.prediction)
                user_choice = self.get_prediction()
                print(user_choice)
                computer_choice = self.get_computer_choice()
                print(computer_choice)
                self.get_winner(computer_choice,user_choice)
                if self.user_score == 3: 
                    print('You have won! What a hero')
                    exit
                elif self.computer_score == 3:
                    print('You lost the game! Doofus')
                    exit

            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        
    def timer(self):
        countdown_timer = 3
        while countdown_timer>0:
            print(f"Show you hand in {countdown_timer} seconds")
            sleep(1)
            countdown_timer -= 1
        print('GO!')

    def get_prediction(self):
        if self.prediction[0][0] > 0.5:
            user_choice = 'rock'
        elif self.prediction[0][1] > 0.5:
            user_choice = 'paper'
        elif self.prediction[0][2] > 0.5:
            user_choice = 'scissors'
        elif self.prediction[0][3] > 0.5:
            user_choice = 'nothing'
        else:
            user_choice = 'No user choice detected'
        return user_choice

    def get_computer_choice(self):
        choice_list = ['Rock','Paper','Scissors']
        computer_choice = random.choice(choice_list).lower()
        #print(computer_choice)
        return computer_choice

    def get_winner(self,computer_choice,user_choice):
        #while self.user_score <=3 and self.computer_score <=3:
    
            if computer_choice == user_choice:
                print('It\'s a tie')
            elif computer_choice == 'rock':
                if user_choice == 'paper':
                    print('You won! Paper beats Rock')
                    self.user_score +=1
                else:
                    print('You lose! Rock beats Scissors')
                    self.computer_score += 1
            elif computer_choice == 'scissors':
                if user_choice == 'rock':
                    print('You won! Rock beats Scissors')
                    self.user_score +=1
                else:
                    print('You lose! Scissors beats Paper') 
                    self.computer_score += 1 
            elif computer_choice == 'paper':
                if user_choice == 'scissors':
                    print('You won! Scissors beats Paper')
                    self.user_score +=1
                else:
                    print('You lose! Paper beats Rock')
                    self.computer_score += 1
            print(f"You have {self.user_score} points, the computer has {self.computer_score}")
    
        

    def play():
        
        game = Rock_Paper_Scissors()
        game.open_camera()
       

if __name__ ==  '__main__':
    choice_list = ['Rock','Paper','Scissors','Nothing']
    
    Rock_Paper_Scissors.play()



    

