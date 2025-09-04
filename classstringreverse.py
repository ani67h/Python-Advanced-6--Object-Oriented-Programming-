class string_reverse:

    def __init__(self, string = ""):
        self.string = string

    def input(self):
        self.string = input("Please enter a word and I will reverse it : ")

    def output(self):
        print("The reverse of the word that you have entered is ",self.string[::-1])   

rev = string_reverse()
rev.input()
rev.output()