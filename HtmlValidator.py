import urllib.request
import urllib.parse
import re

requestUrl = urllib.parse.quote('http://www.planetcjd.co.uk', '')

html = urllib.request.urlopen('http://validator.w3.org/check?uri=' + requestUrl + '%2F&charset=%28detect+automatically%29&doctype=Inline')

validStatusRegex = re.search(r".*Errors found while checking this document.*", html.read().decode('utf-8'), re.MULTILINE)

if (validStatusRegex):
	print('invalid')
else:	
	print('valid')
