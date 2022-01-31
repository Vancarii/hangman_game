# ~ Yecheng Wang
# ~ February 26th 2020
# ~ Hangman Game
# ~ Creating a Hangman Game

# important module imports including our own 'HangingMan'
import string
import random
from MyHMGraphics import Bowman 
from MyHMGraphics import Welcome

import os

## ~-~-~-~-~-~-~-~-~-~-~ Functions -~-~-----------------

# ~ Displays the underscores the same length of the word chosen
def DisplayUnderscore(sWord,sUnderscores):
    for char in sWord:
	sUnderscores.append("_")
    for index in sUnderscores:
	print index , 
    print ""
    return
   
# ~ Takes the secret word and the guessed letter and see if anything matches by
# ~ iterating through the word
# ~ if the guessed letter matches any letter in the word, reveal it
# ~ Display the next animation if there is no match
# ~ Return the values of how many errors there are (iErr) and the underscore counter (iUCounter)
# ~ 	This helps make sure the user hasn't lost or won the game
def GuessChecker(sWord,sGuess,sUnderscores, iErr, iUCounter):
    bFound = False
    for char in sGuess:
	iIndex = 0
	os.system('cls')
	for letter in sWord:
	    if char == letter:
		sUnderscores[iIndex] = char
		sGuessedWords.append(sGuess)
		bFound = True
		iUCounter -= 1
	    iIndex +=1

	if not bFound:
	    iErr += 1
	    sGuessedWords.append(sGuess)
    print Bowman[iErr]
    
    for char in sUnderscores:
	print char + ' ',
    return iErr, iUCounter

## ~-~-~-~-~-~-~-~-~-~-~ MAIN PROGRAM -----~-~-----------------
## ~-~-~-~-~-~-~-~-~-~-~ Initialization -~-~-----------------

# ~ Splash Screen
os.system('color b ')

print Welcome
print "TO YECHENG'S GAME!\n"
os.system('pause')
os.system('cls')

print 'RULES:\nGuess different letters to figure out what the secret word is.\nif you get it right, the letter will be revealed.'
print 'If your guess is not in the word, the archer will begin to shoot his arrow.\n'
print "YOUR OBJECTIVE:"
print 'Try to guess the word either one letter at a time or try guessing the whole word.'
print "Make sure you don't let the archer break the heart or else you lose!\n"

os.system('pause')
os.system('cls')

sUnderscores = []

## Take file and split into easy and hard 
# ~ Create two seperate strings for easy and hard words
sEasyWords = ""
sHardWords = ""

# ~ Open the dictionary file and read it
fDictionaryFile = open("Dictionary.txt", "r")
sWordFile = fDictionaryFile.read()

## Split the long string of text into a list of words (strings)
sAnswer = sWordFile.split("~")

# ~ Split the long string of words into easy and hard words depending on length
for Word in sAnswer:
    if len(Word) < 6:
	sEasyWords += Word + ", "
	sEasy = sEasyWords.split(", ")
    elif len(Word) >= 6:
	sHardWords += Word + ", "
	sHard = sHardWords.split(", ")

## ~-~-~-~-~-~-~-~-~-~-~ MAIN LOOP -----~-~-----------------

bContPlaying = True

# ~ Large loop allows for the player to continue playing after they have finished a game
while bContPlaying:
    iErrors = 0

    # ~ Have this list so that it stores all guessed letters so there wont have a repeat
    sGuessedWords = []

    # ~ ask for the level of difficulty that the user would like to play
    # ~ checks input validation
    strValidInput = False
    
    while not strValidInput:
	iInputDifficulty = str(raw_input("Choose the level of difficulty that you would like to play then click enter(e / h): "))
	iInputDifficulty = iInputDifficulty.lower()
	if iInputDifficulty == 'e' or iInputDifficulty == 'h':
	    if iInputDifficulty == "e":
		sWord = random.choice(sEasy)
		os.system('cls')
	    if iInputDifficulty == "h":
		sWord = random.choice(sHard)
		os.system('cls')
	    strValidInput = True
	else:
	    os.system('cls')
	    print('please enter either e or h')
    
    
    print Bowman[0]
    
    # ~ Calls the display underscore function 
    iUnderscoreCounter = len(sWord)
    DisplayUnderscore(sWord,sUnderscores)
    
    # ~ Loop that checks if the user won or lost 
    # ~ If not, have the user input guesses 
    # ~ if the guess is longer than 1 letter, treat it like a guess for the word
    # ~ if the word matches, then you win, else, you lose 
    # ~ Tell the user whether they win or lose
    while iErrors < 8 and iUnderscoreCounter > 0:
	sGuess = str(raw_input("Guess: "))
	if sGuess not in sGuessedWords:
	    if sGuess.isalpha() == True:
		if len(sGuess) == 1:
		    iErrors, iUnderscoreCounter = GuessChecker(sWord,sGuess,sUnderscores, iErrors, iUnderscoreCounter)
		else:
		    if sGuess == sWord:
			iUnderscoreCounter = 0
		    else:
			iErrors = 8
	    else:
		print "Please enter only letters"
	else:
	    print "Please enter a new letter"
    else:
	if iErrors == 8:
	    os.system('cls')
	    print Bowman[8]
	    print "You broke my heart :( The Word was", sWord.upper()
	elif iUnderscoreCounter == 0:
	    print "You Win!!!"
	    
	CheckContPlay = str(raw_input("\nWould you like to continue playing? (y or n): "))
	CheckContPlay = CheckContPlay.lower()
	    
	while CheckContPlay <> 'y' and CheckContPlay <> 'n':
	    CheckContPlay = str(raw_input("\nPlease enter either y or n: "))
	    CheckContPlay = CheckContPlay.lower()
	else:
	    if CheckContPlay == 'n':
		print '\nTHANKS FOR PLAYING!!'
		bContPlaying = False
	    elif CheckContPlay == 'y':
		bContPlaying = True
		os.system('cls')
		sUnderscores = []
		iUnderscoreCounter = 0

fDictionaryFile.close()








 





