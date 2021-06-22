version = 0.1 # version number

def interpret(string):
	for element in string:
		element == 'h' if print('h', end='') else print('', end='')
	getInp()

def getInp():
	i = input('\nh> ')
	interpret(i)

print('HLang Interpreter ' + str(version))
getInp()
