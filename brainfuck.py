def brainfuck(b):
	"""
	Pybfi - Python Brainfuck interpreter(OLD)
	By Herr Niemand 2014 
	Version 0.10.0
	Origin: https://github.com/herrniemand/python_brainfuck

	arguments:
		(string)b - brainfuck code

	help: http://c2.com/cgi/wiki?BrainfuckLanguage

	Copyrights Herr Niemand. 
	All right reserved, preserved, precooked and prepared to rage agaings the machines!
	GPLv2
	"""
	i = x = 0
	s = buff = ''
	arr = [0 for n in range(0,30000)]#30000 memory cells
	l = len(b)
	while x < l:
		n = b[x]
		if (s == '' or n == ']') and not n.isalpha():
			if n == '>': i += 1
			elif n == '<': i -= 1
			elif n == '+': arr[i] = (arr[i] + 1)%255
			elif n == '-': arr[i] = (arr[i] - 1)%255
			elif n == '.': buff += chr(arr[i])
			elif n == ',': s = 'c'
			elif n == '[': s = 'w'
			elif n == ']' and s == 'w':
				while arr[i] > 0:
					for z in s[0:]:
						if z == '>': i += 1
						if z == '<': i -= 1
						if z == '+': arr[i] = (arr[i] + 1)%255
						if z == '-': arr[i] = (arr[i] - 1)%255
						if z == '.': buff += chr(arr[i])
				s = ''
			else: 
				raise SyntaxError("Missing [.")

		elif s == 'w': s += n
		elif s == 'c': 
			arr[i] = ord(n)
			s = '' 

		x += 1
		if x == l and s != '': raise SyntaxError("Missing ].")

	return buff