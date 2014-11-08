import time

def createLog():
	f = open('log/'+time.strftime('%Y%m%d%H%M%S')+'.log', 'w')
	return f

def writeLog(data, f):
	f.write(data)

f = createLog()
writeLog('hello\n', f)