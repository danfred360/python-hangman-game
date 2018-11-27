import random

def run():
    fname = getfName()
    words = getWords(fname)
    # print(words)

# asks person to choose category
def getfName():
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

def getWords(fname):
    f = open(fname, 'r')
    ans = []
    for i in range(0, countLines(fname)):
        ans.append(f.readline())
    return ans

# returns number of lines in a txt file fname
def countLines(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    f.close()
    return i + 1

run()
