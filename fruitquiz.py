import random

class fruitquiz:
    # create a constructor
    def __init__(self):
        # create a dictionary of fruits as keys and color as value
        self.fruits = {'apple':'red',
                        'orange':'orange',
                        'watermelon':'green',
                        'banana':'yellow'}
        
        # function for the quiz, here a fruit will be chosen randomly
    def quiz(self):
        while(True):

            fruit, color = random.choice(list(self.fruits.items()))
            print('What is the color of {}'.format(fruit))
            user_answer = input()

            if(user_answer.lower() == color):
                print('Correct answer')
            else:
                print('Wrong answer')

            option = int(input('Enter 0, if you want to plat again otherwise enter 1 : '))
            if (option):
                break

print('Welcome to fruit quiz')
fq = fruitquiz()
fq.quiz()