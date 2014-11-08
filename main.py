import HtmlValidator
import RandomWord
import BingSearchResults
import ServerSniffer
import random

testCount = 10
bingAccountKey = BingSearchResults.getAccountKey()
wordlist = RandomWord.loadWordList('/wordlist/wordlist.txt')

for x in range(0, testCount):

	word = RandomWord.getRandomWord(wordlist)

	searchUrls = BingSearchResults.parseSearchResults( BingSearchResults.getSearchResults(str(word), bingAccountKey) )

	testUrl = random.choice(searchUrls)
	server = ServerSniffer.sniffHeaders(testUrl)
	validStatus = HtmlValidator.getValidStatus(testUrl)

	print('Testing URL {0}\n Server: {1}\n validStatus: {2}'.format(testUrl, server, validStatus[0]))

	if (validStatus[0] == 'invalid'):
		print('Errors: {0} / Warnings: {1}'.format(validStatus[1], validStatus[2]))

	print('\n\n')
