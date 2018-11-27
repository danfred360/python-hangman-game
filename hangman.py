import random


class Game:S
    def __init__(self):
        self.fname = self.getfName()
        self.words = self.getWords(fname)
        print(words)

    # asks person to choose category
    def getfName(self):
        print('Which chatagory would you like to play?')
        print('Press 1 for countries, 2 for states, or 3 for baby animals.')
        while True:
            choice = input('--> ')
            if choice == '1' or choice == '2' or choice == '3':
                break
            print('Answer not accepted. Try again.')
        fname = ''
        if choice == '1':
            fname = 'countries.txt'
        if choice == '2':
            fname = 'states.txt'
        if choice == '3':
            fname = 'babyanimals.txt'
        return fname

    def getWords(self, fname):
        f = open(fname, 'r')
        ans = []
        while i != '':
            ans.append(f.readline())
        return ans

    temp = Game()
