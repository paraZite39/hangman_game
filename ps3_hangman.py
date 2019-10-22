import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return set(list(secretWord)).issubset(lettersGuessed)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter
        else:
            result += '_ '
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet.remove(letter)
    
    return ''.join(alphabet)


def checkLetter(letter, secretWord):
    return letter in list(secretWord)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * lets user know the length of secretWord

    * one guess / round (while loop)
    
    * guess counter
    '''
    guessedLetters = []
    guesses = 8
    print('Hello there, player!')
    print('I am thinking of a ' + str(len(secretWord)) + ' letter word.')
    
    while True:
        print('************************')
        print('You have ' + str(guesses) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(guessedLetters))
        
        letter = input('Please, guess a letter:')
        
        if(not letter in guessedLetters):
            guessedLetters += letter
            if(checkLetter(letter, secretWord)):
                print("Great job: " + getGuessedWord(secretWord, guessedLetters))
            else:
                print("Sorry, wrong letter. Word: " + getGuessedWord(secretWord, guessedLetters))
                guesses -= 1
        else:
            print("Sorry, you already picked that letter!")
        
        if(guesses == 0):
            print("The word was " + secretWord)
            break
        if (isWordGuessed(secretWord, guessedLetters)):
            print("Congratulations!")
            break
        

