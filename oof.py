import random

class Game:
    def __init__(self):
        self.figures = [
        ['____________________',
        '   |  /             ',
        '   | /              ',
        '   |/               ',
        '   |                ',
        '   |                ',
        '   |                ',
        '___|________________']]
        # gets filename
        self.fname = self.getfName()
        # gets word
        self.word = self.getWord(self.fname)
        # gets difficulty
        self.tries = self.getDiff()
        self.attempts = 0
        while True:
            g = self.guess(self.word)
            if g == 'null':
                self.wrong(attempts)
                self.tries -= 1
                self.attempts += 1

    def wrong(self, num):
        for i in self.figures[num]:
            print(i)
    # gets players guess. Returns null if wrong, or index of the char
    def guess(self, word):
        x = getLetter()
        if word.index(x) == -1 and word.index(capitalize(x)) == -1:
            return 'null'
        elif word.index(x) != -1:
            return index


    def getLetter(self):
        while True:
            x = ('Enter a letter. --> ')
            if len(x) == 1 and x.isalpha():
                return x
            print('Input not accepted, try again.')

    # player selects difiiculty, returns an integer for number of tries
    def getDiff(self):
        print('Select difficulty.')
        print('Enter 1 for easy, 2 for normal, or 3 for hard.')
        while True:
            x = input('--> ')
            if x == '1' or x == '2' or x == '3':
                break
            print('Answer not accepted. Try again.')
        if x == '1':
            return 7
        if x == '2':
            return 5
        if x == '3':
            return 3

    # asks person to choose category
    def getfName(self):
        print('Which chatagory would you like to play?')
        print('Enter 1 for countries, 2 for states, or 3 for baby animals.')
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

    # returns an array of words from fname
    def getWord(self, fname):
        f = open(fname, 'r')
        ans = []
        for i in range(0, self.countLines(fname)):
            l = list(f.readline())
            l.pop(len(l) - 1)
            l.pop(len(l) - 1)
            l.pop(len(l) - 1)
            x = ''
            for i in l:
                x += i
            ans.append(x)
        x = random.randint(0, len(ans) -1)
        return ans[x]

    # returns number of lines in a txt file fname
    def countLines(self, fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        f.close()
        return i + 1

temp = Game()
