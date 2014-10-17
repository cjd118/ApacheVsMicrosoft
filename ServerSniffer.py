import urllib.request

def sniffHeaders(requestUrl):

	page = urllib.request.urlopen(requestUrl)
	headers = dict(page.info())
	server = headers.get('Server')

	if server.find('IIS') > -1 :
		server = 'IIS'
	elif server.find('Apache') > -1:
		server = 'Apache'
	else: 
		server = 'Unknown'

	return server
