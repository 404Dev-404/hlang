version = 0.0 # version number

def interpret(string):
	for element in string:
		if element == 'h':
			print('h', end='')
		elif element != 'h':
			print('', end='')
	getInp()

def getInp():
	i = input('\nh> ')
	interpret(i)

print('HLang Interpreter ' + str(version))
getInp()
