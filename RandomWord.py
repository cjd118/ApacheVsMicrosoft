import os
import random

def loadWordList(wordlist):

	dir = os.path.dirname(__file__)

	wordlist = open(dir + wordlist)
	wordlistContent = wordlist.readlines()

	return wordlistContent

def getRandomWord(wordlist):

	return random.choice(wordlist)