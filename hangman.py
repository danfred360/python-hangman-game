'''
shit to do:
- complete figures array
'''


import random

class Game:
    def __init__(self):
        # gets filename
        self.fname = self.getfName()
        # gets word
        self.word = self.getWord(self.fname)
        # gets difficulty
        self.tries = self.getDiff()
        self.attempts = 0

        self.blank = ''
        for i in self.word:
            if i == ' ':
                self.blank += ' '
            else:
                self.blank += '_'
        print(self.blank)
        print(self.word)
        while self.tries > 0:
            g = self.guess(self.word)
            if g == 'null':
                self.wrong(self.attempts)
                self.tries -= 1
                self.attempts += 1
            else:
                print('Good guess!')
                l = list(self.blank)
                for k in g[0]:
                    l[k] = g[1]
                s = ''
                for i in l:
                    s += i
                self.blank = s
                print(self.blank)
                try:
                    if self.blank.index('_') == -1:
                        pass
                except ValueError:
                    break
        if self.tries <= 0:
            print('You lose!')
            print('The word was {}'.format(self.word))
            return
        else:
            print('You won!')
            print('The word was {}'.format(self.word))
            return

    def wrong(self, num):
        print('Nope')
        figures = [
        ['____________________',
        '   |  /             ',
        '   | /              ',
        '   |/               ',
        '   |                ',
        '   |                ',
        '   |                ',
        '___|________________'],
        ['____________________',
        '  |  /    |         ',
        '  | /    (_)       ',
        '  |/               ',
        '  |                ',
        '  |                ',
        '  |                ',
    '    ___|________________'],
        ['____________________ ',
         '|  /    |            ',
         '| /    (_)           ',
         '|/      |            ',
         '|       |            ',
         '|                    ',
         '|                    ',
      '___|________________    '],
  ['     ____________________ ',
         '|  /    |           ',
         '| /    (_)          ',
         '|/     /|\          ',
         '|     / | \         ',
         '|                   ',
         '|                   ',
     ' ___|________________   '],['-'],['-'],['-']]



        for i in figures[num]:
            print(i)
    # gets players guess. Returns null if wrong, or index of the char
    def guess(self, word):
        word = list(word)
        x = self.getLetter()
        ans = []
        try:
            if word.index(x) == -1:
                pass
        except ValueError:
            return 'null'
        while True:
            try:
                if word.index(x) == -1:
                    pass
            except ValueError:
                return [ans, x]
            ans.append(word.index(x))
            word[word.index(x)] = '.'

    def getLetter(self):
        while True:
            x = input('Enter a letter. --> ')
            if len(x) == 1 and x.isalpha():
                return x
            else:
                print('Input not accepted, try again.')

    # player selects difiiculty, returns an integer for number of tries
    def getDiff(self):
        print('Select difficulty.')
        print('Enter 1 for easy, 2 for normal, or 3 for hard.')
        while True:
            x = input('--> ')
            if x == '1':
                return 7
            elif x == '2':
                return 5
            elif x == '3':
                return 3
            else:
                print('Answer not accepted. Try again.')


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
while True:
    temp = Game()
    print('Would you like to play again?')
    while True:
        x = input('y or n --> ')
        if x == 'n':
            print('Press enter to exit.')
            x = input('--> ')
            exit()
        elif x == 'y':
            break
        else:
            print('Sorry, answer not accepted. Try again.')
