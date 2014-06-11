class Pybfir:
	"""
		Pybfir - Python Brainfuck interpreter Recursive
		By Herr Niemand 2014 
		Version 1.1.0
		Origin: https://github.com/herrniemand/python_brainfuck
		Samples: https://github.com/pablojorge/brainfuck
		help: http://c2.com/cgi/wiki?BrainfuckLanguage

		Copyrights Herr Niemand. 
		All right reserved, preserved, precooked and prepared to rage agaings the machines!
		GPLv2
	"""
	def __init__(self):
		self.__mem = [0 for n in range(0,1024*32)]
		self.__i = 0

	def run(self, b):
		"""
		.run:
			arguments:
				(string)b - brainfuck code.

			help: http://c2.com/cgi/wiki?BrainfuckLanguage
		"""
		x = br = 0
		s = ''
		l = len(b)
		while x < l:
			n = b[x]
			if not br or n in '][':
				if n == '>': self.__i += 1
				elif n == '<': 
					if self.__i > 0:self.__i -= 1 
					else: raise IndexError('Memory cell out of range')
				elif n == '+': self.__mem[self.__i] = (self.__mem[self.__i] + 1)%256
				elif n == '-': self.__mem[self.__i] = (self.__mem[self.__i] - 1)%256
				elif n == '.': print(chr(self.__mem[self.__i]), end='')
				elif n == ',':	
					while True:
						z = ''
						try:
							z = str(input('Please enter a character: '))
							if ord(z) < 256: 
								self.__mem[self.__i] = ord(z)
								break
							else: raise ValueError
						except: print(z + ' is not a valid input!')
					
				elif n == '[': 
					if br: s += n
					br += 1

				elif n == ']' and br:
					br -= 1
					if not br:
						while self.__mem[self.__i]: self.run(s)
						s = ''
					else: s += n

			elif br: s += n
			x += 1

	def load(self, filename):
		"""
		.load:
			arguments:
				(string)filename - file address.
		"""
		with open(filename) as f:
			self.run(f.read())
