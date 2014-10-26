import urllib.request	
import urllib.parse
import os
import re
import xml.etree.ElementTree as ET

def getAccountKey():

	dir = os.path.dirname(__file__)

	keyFile = open(dir + '\\bing-account-key.txt')
	key = keyFile.read()

	return key	
	
def getSearchResults(term, accountKey):

	password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None, 'https://api.datamarket.azure.com', accountKey, accountKey)

	handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
	opener = urllib.request.build_opener(handler)

	searchResults = opener.open('https://api.datamarket.azure.com/Bing/Search/v1/Composite?Sources=%27web%27&Query=%27' + term + '%27')

	SearchResultsData = searchResults.read().decode('utf-8')

	usefulData = re.search(r'(?<= \/\>)\<entry.*entry\>(?=\<\/feed\>\<)', SearchResultsData, re.MULTILINE)
	usefulDataNoNamespaces = re.sub(r'd:|m:','',usefulData.group(0),0,re.MULTILINE)

	return '<root>' + usefulDataNoNamespaces + '</root>'

def parseSearchResults(xml):

	root = ET.fromstring(xml)
	urls = []

	for entry in root.findall('entry'):
		for contentElement in entry.find('content').find('properties'):
			if (contentElement.tag == 'Url'):
				urls.append(contentElement.text)

	return urls;

key = getAccountKey()
fetchedResults = getSearchResults('xbox', key)
urls = parseSearchResults(fetchedResults)

print (urls)

