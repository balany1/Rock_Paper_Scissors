from ast import If
import random

class Rock_Paper_Scissors:

    def __init__(self,choice_list):
        #self.computer_choice = random.choice(self.choice_list)
        pass

    def get_computer_choice():
        choice_list = ['Rock','Paper','Scissors']
        computer_choice = random.choice(choice_list).lower()
        return computer_choice


    def get_user_choice():
        while True:

            user_choice = input('Please choose Rock, Paper or Scissors:').lower()
            if user_choice == 'rock' or user_choice == 'scissors' or user_choice == 'paper':
                return user_choice
            else:
                print('Please choose one of the options selected')

    def get_winner(computer_choice,user_choice):
        if computer_choice == user_choice:
           print('It\'s a tie')
        elif computer_choice == 'rock':
            if user_choice == 'paper':
                print('You won! Paper beats Rock')
            else:
                print('You lose! Rock beats Scissors')
        elif computer_choice == 'scissors':
            if user_choice == 'rock':
                print('You won! Rock beats Scissors')
            else:
                print('You lose! Scissors beats Paper')  
        elif computer_choice == 'paper':
            if user_choice == 'scissors':
                print('You won! Scissors beats Paper')
            else:
                print('You lose! Paper beats Rock')
              
            
    


    if __name__ ==  '__main__':
        choice_list = ['Rock','Paper','Scissors','Nothing']
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        get_winner(computer_choice,user_choice)