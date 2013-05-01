# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i =  0
    out = ''
    for char in secretWord:
        for i in lettersGuessed:
            if i == char:                
                out += char
                break            
        if char != i:
            out += '_ '
    if out == secretWord:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    i =  0
    out = ''
    for char in secretWord:
        for i in lettersGuessed:
            if i == char:                
                out += char
                break            
        if char != i:
            out += '_ '
    return out



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    ans=string.ascii_lowercase 
    for char in lettersGuessed: 
        if char in ans: 
            ans=ans.replace(char,'') 
    return ans
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    line='-------------'
    lettersGuessed=[]
    history=[]
    letterin='na'
    goodguess=''
    guesses=8
    guessesmade = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    def victory():
        if isWordGuessed(secretWord, lettersGuessed)==True:
            print(line)
            print('Congratulations, you won!')
            return True
        else:
            return False
    def truethat():
        if letterin in secretWord:
            return True
    def guess():  
        if letterin in goodguess:
            return "Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed))
        elif letterin in guessesmade:
            return "Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed))
        elif letterin in secretWord:
            truethat()
            return 'Good guess: '+str(getGuessedWord(secretWord, lettersGuessed))
        else:
            return 'Oops! That letter is not in my word: '+str(getGuessedWord(secretWord, lettersGuessed))
    def mistakesMade():
        if letterin not in secretWord:
            return True
        else:
            return False
    def loss():
        if guesses<=0:
            return True
        else:
            return False
    while victory()==False:
        if truethat()==True:
            goodguess+=letterin
        print(line)
        print('You have '+str(guesses)+' guesses left.')
        print('Available Letters: '+str(getAvailableLetters(lettersGuessed)))
        letterin=raw_input('Please guess a letter: ')
        letterin=letterin.lower()                             
        guess()
        if mistakesMade()==True:
            guesses-=1
            if letterin in lettersGuessed:
                guesses += 1
            if loss() == True:
                print 'Oops! That letter is not in my word: '+str(getGuessedWord(secretWord, lettersGuessed))
                print(line)
                print('Sorry, you ran out of guesses. The word was '+str(secretWord)+'.')
                break
        lettersGuessed+=[letterin]
        print(guess())
        guessesmade+=[letterin]




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

