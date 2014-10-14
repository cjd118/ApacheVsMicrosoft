import urllib.request
import urllib.parse
import re

def getValidStatus(requestUrl):

	requestUrl = urllib.parse.quote(requestUrl, '')

	html = urllib.request.urlopen('http://validator.w3.org/check?uri=' + requestUrl + '%2F&charset=%28detect+automatically%29&doctype=Inline')
	htmlData = html.read().decode('utf-8')

	invalidStatusRegex = re.search(r'.*Errors found while checking this document.*', htmlData, re.MULTILINE)

	if (invalidStatusRegex):
		errorCount = re.search(r'\d.*(?= Errors)', htmlData, re.MULTILINE)
		warningCount = re.search(r'(?<=, )\d.*(?= warning\()', htmlData, re.MULTILINE)

		return ('invalid', errorCount.group(0), warningCount.group(0))
	else:	
		return ('valid')

# test function
print(getValidStatus('http://www.microsoft.co.uk'))
