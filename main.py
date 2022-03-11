import sys
import random
from termcolor import cprint

def isUniqueString(string):
	uniqueCharSet = set()
	for char in string:
		if char in uniqueCharSet:
			return False
		uniqueCharSet.add(char)
	return True


wordsFile = open("wordlist.txt")


possibleWords = []
nonUniqueWords = []

for line in wordsFile:
	if isUniqueString(line.rstrip("\n")):
		possibleWords.append(line.rstrip("\n"))
	else:
		nonUniqueWords.append(line.rstrip("\n"))	
wordsFile.close()

guesses = 6
numOfGuesses = 0

correctWord = "placeholder"
wordGuessed = False

def restart():
	global wordGuessed
	global correctWord
	try:
		correctWord = random.choice(possibleWords)
	except IndexError:
		cprint("List empty.", "red")	
		sys.exit()
	wordGuessed = False
def guess():
	global numOfGuesses
	playerGuess = 0
	while not playerGuess in possibleWords or not len(playerGuess) == 5:
		playerGuess = input(f"Guess {numOfGuesses + 1}: ")
		if not len(playerGuess) == 5:
			cprint("Not 5 letters long", "red")
		elif not playerGuess in possibleWords:
			cprint("Not an acceptable word", "red")
		else:
			numOfGuesses += 1
			evaluate(playerGuess)
def evaluate(guess):
	global wordGuessed
	correctLetters = 0
	for index in range(5):
		letter = guess[index]
		if not letter in correctWord:
			if index != 4:
				print(letter, end="")
			else:
				print(letter)
		elif letter in correctWord and correctWord.find(letter) != index:
			if index != 4:
				cprint(letter, "yellow", end="")
			else:
				cprint(letter, "yellow")	
		else:
			if index != 4:
				cprint(letter, "green", end="")
			else:
				cprint(letter, "green")	
			correctLetters += 1
	if correctLetters == 5:
		cprint(f"Correct! The word was {correctWord}", "green")
		wordGuessed = True
	elif correctLetters != 5 and numOfGuesses == 6:
		cprint(f"You lose! The word was {correctWord}", "red")

restart()
for i in range(guesses):
	if not wordGuessed:
		guess()
	else:
		break


"""
HOW TO DO MULTIPLE LETTERS

Idea 1: Iterate over word trying to find correct letters while
keeping track of how many times each letter occurs using a dict

Then try and find yellows then everything else is grey

we could use a list storing the colors of each letter and then 
iterate over each letter in the guess and then the list, ie
correct is "beans"
guess is "never"
colorlist is ["white", "white", "white", "white", "white"]


iterate over guess and check whether index we're on is equal to
the index in the correct one
if it is we change value in colorlist

N, B
not equal
E, E
equal, change colorlist[1] to green
V, A
not equal
E, N
not equal
R, S
not equal

colorlist is now ["white", "green", "white", "white", "white"]

now let's iterate over both again

NB
n is in beans, and the index of n in beans (4) does not already 
equal guess[4], so change colorlist[0] to yellow
EE
ignore because colorlist[1] is not white
VA
v is not in beans
EN
e is in beans, but when we head to the earliest point it occurs, 
we already have it in colorlist

we can now iterate over beans inside this iteration to try and
find an unmatched e

there isn't any, so colorlist[3] is still white
RS
no r in beans


never
beans

final colorlist is ["yellow", "green", "white", "white", "white"]

for idx, i in enumerate((guess, colorlist)):
	if idx != 4:
		cprint(i[0], i[1], end="")
	else:
		cprint(i[0], i[1])
"""