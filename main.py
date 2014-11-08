import HtmlValidator
import RandomWord
import BingSearchResults
import ServerSniffer
import random
import Logger
import urllib.parse

testCount = 10
bingAccountKey = BingSearchResults.getAccountKey()
wordlist = RandomWord.loadWordList('/wordlist/wordlist.txt')
log = Logger.createLog()
scrapedDomains = set()

for x in range(0, testCount):

	try:

		word = RandomWord.getRandomWord(wordlist)

		searchUrls = BingSearchResults.parseSearchResults( BingSearchResults.getSearchResults(str(word), bingAccountKey) )

		testUrl = random.choice(searchUrls)

		#check domain hasn't already been scraped
		parsedTestUrl = urllib.parse.urlparse(testUrl)
		testDomain = parsedTestUrl.netloc

		print('Checking if domain {0} has already been scraped...'.format(testDomain))

		if (testDomain not in scrapedDomains):

			scrapedDomains.add(testDomain)

			server = ServerSniffer.sniffHeaders(testUrl)
			validStatus = HtmlValidator.getValidStatus(testUrl)

			print('Testing URL {0}\n Server: {1}\n validStatus: {2}'.format(testUrl, server, validStatus[0]))

			if (validStatus[0] == 'invalid'):
				print('Errors: {0} / Warnings: {1}'.format(validStatus[1], validStatus[2]))
				Logger.writeLog(testUrl + ',' + server + ',' + 'invalid' + ',' + validStatus[1] + ',' + validStatus[2] + '\n',log)
			else:
				Logger.writeLog(testUrl + ',' + server + ',' + 'valid\n',log)

			print('\n\n')

	except Exception:
		continue
