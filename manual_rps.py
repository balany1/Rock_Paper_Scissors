import random

class Rock_Paper_Scissors:

    def __init__(self,choice_list):
        #self.computer_choice = random.choice(self.choice_list)
        pass

    def get_computer_choice():
        choice_list = ['Rock','Paper','Scissors','Nothing']
        computer_choice = random.choice(choice_list)
        return computer_choice


    def get_user_choice():
        while True:

            user_choice = input('Please choose Rock, Paper or Scissors:').lower()
            if user_choice == 'rock' or user_choice == 'scissors' or user_choice == 'paper':
                return user_choice
            else:
                print('Please choose one of the options selected')
            



    if __name__ ==  '__main__':
        choice_list = ['Rock','Paper','Scissors','Nothing']
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        print(computer_choice)
        print(user_choice)