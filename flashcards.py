class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaninig = meaning

    def __str__(self):

        # we will return a string
        return self.word + ' ( '+self.meaninig+' )'

flash = []
print('Welcome to flashcard application')

# the following loop will be replaced until user stops to add the flashcards
while(True):  # in order to take input several times we are using a loop here
    word = input('Enter the name you want to add to flashcard : ')
    meaning = input('Enter the meaning of the word : ')

    flash.append(flashcard(word, meaning))
    option  = int(input('Enter 0, if you want to add another flashcar otherwise enter 1 : '))

    if (option):  # this means if option is true
        break    

# printing all the flashcards
print('\nYour flashcards')
for i in flash:
    print('>', i)   