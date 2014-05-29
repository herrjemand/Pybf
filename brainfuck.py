def brainfuck(b):
	"""
	Pybfi - Python Brainfuck interpreter
	By Herr Niemand 2014 
	Version 0.09
	Origin: https://github.com/herrniemand/python_brainfuck

	arguments:
		(string)b - brainfuck code

	help: http://c2.com/cgi/wiki?BrainfuckLanguage

	Copyrights NobodyAtAll. 
	All right reserved, preserved, precooked and prepared to rage agaings the machines!
	"""
	i = x = 0
	s = buff = ''
	arr = [0 for n in range(0,30000)]
	l = len(b)
	while x < l:
		n = b[x]
		if s == '' or n == ']':
			if n == '>': i += 1
			if n == '<': i -= 1
			if n == '+': arr[i] = (arr[i] + 1)%255
			if n == '-': arr[i] = (arr[i] - 1)%255
			if n == '.': buff += chr(arr[i])
			if n == ',': pass
			if n == '[': s = 'k'

			if n == ']':
				while arr[i] > 0:
					for z in s[0:]:
						if z == '>': i += 1
						if z == '<': i -= 1
						if z == '+': arr[i] = (arr[i] + 1)%255
						if z == '-': arr[i] = (arr[i] - 1)%255
						if z == '.': buff += chr(arr[i])
				s = ''
		else:
			s += n

		x += 1
	return buff