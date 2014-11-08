import HtmlValidator
import RandomWord
import BingSearchResults
import ServerSniffer
import random
import Logger

testCount = 10
bingAccountKey = BingSearchResults.getAccountKey()
wordlist = RandomWord.loadWordList('/wordlist/wordlist.txt')
log = Logger.createLog()

for x in range(0, testCount):

	word = RandomWord.getRandomWord(wordlist)

	searchUrls = BingSearchResults.parseSearchResults( BingSearchResults.getSearchResults(str(word), bingAccountKey) )

	testUrl = random.choice(searchUrls)
	server = ServerSniffer.sniffHeaders(testUrl)
	validStatus = HtmlValidator.getValidStatus(testUrl)

	print('Testing URL {0}\n Server: {1}\n validStatus: {2}'.format(testUrl, server, validStatus[0]))

	if (validStatus[0] == 'invalid'):
		print('Errors: {0} / Warnings: {1}'.format(validStatus[1], validStatus[2]))
		Logger.writeLog(testUrl + ',' + server + ',' + 'invalid' + ',' + validStatus[1] + ',' + validStatus[2] + '\n',log)
	else:
		Logger.writeLog(testUrl + ',' + server + ',' + 'valid\n',log)

	print('\n\n')
