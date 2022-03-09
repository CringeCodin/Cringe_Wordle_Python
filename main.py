import random
from termcolor import cprint
from ast import literal_eval

def isUniqueString(string):
	uniqueCharSet = set()
	for char in string:
		if char in uniqueCharSet:
			return False
		uniqueCharSet.add(char)
	return True

possibleGuessWordsIsolated = []
possibleCorrectWords = []

wordsFile = open("wordlist.txt")
#GET WORDS HERE

wordsFile.close()
possibleGuessWords = []
for word in possibleGuessWordsIsolated:
	possibleGuessWords.append(word)
for word in possibleCorrectWords:
	possibleGuessWords.append(word)


guesses = 6
numOfGuesses = 0

correctWord = "placeholder"
wordGuessed = False

def restart():
	global wordGuessed
	global correctWord
	# correctWord = random.choice(possibleCorrectWords)
	correctWord = "robot"
	wordGuessed = False
def guess():
	global numOfGuesses
	playerGuess = 0
	while not playerGuess in possibleGuessWords or not len(playerGuess) == 5:
		playerGuess = input(f"Guess {numOfGuesses + 1}: ")
		if not len(playerGuess) == 5:
			cprint("Not 5 letters long", "red")
		elif not playerGuess in possibleGuessWords:
			cprint("Not an acceptable word", "red")
		else:
			evaluate(playerGuess)
			numOfGuesses += 1
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
		print(f"Correct! The word was {correctWord}")
		wordGuessed = True
	elif correctLetters != 5 and numOfGuesses == 6:
		print(f"You lose! The word was {correctWord}")

restart()
for i in range(guesses):
	if not wordGuessed:
		guess()
	else:
		break