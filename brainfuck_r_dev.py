class Pybfi:
	def __init__(self):
		self.__mem = [0 for n in range(0,1024*32)]
		self.__i = 0
		self.__buffer = ''

	def fuck(self, b):
		"""
		Pybfir - Python Brainfuck interpreter Recursive
		By Herr Niemand 2014 
		Version 0.13.2
		Origin: https://github.com/herrniemand/python_brainfuck

		arguments:
			(string)b - brainfuck code

		help: http://c2.com/cgi/wiki?BrainfuckLanguage

		Copyrights Herr Niemand. 
		All right reserved, preserved, precooked and prepared to rage agaings the machines!
		GPLv2
		"""
		try:
			x = br = 0
			s = ''
			l = len(b)
			while x < l:
				n = b[x]
				# print(n)
				if (not br or n in '][') and not n.isalpha():
					if n == '>': self.__i += 1
					elif n == '<': self.__i -= 1
					elif n == '+': self.__mem[self.__i] = (self.__mem[self.__i] + 1)%255
					elif n == '-': self.__mem[self.__i] = (self.__mem[self.__i] - 1)%255
					elif n == '.': self.__buffer += chr(self.__mem[self.__i])
					elif n == ',':	
						while True:
							try:
								z = ord(input("Please enter a character: "))
								if z < 256: 
									self.__mem[self.__i] = z
									break
								else: raise ValueError
							except ValueError:
								print(chr(z) + ' is not a valid ascii character!')
						
					elif n == '[': 
						if br: s += n
						br += 1


					elif n == ']' and br:
						br -= 1
						if not br:
							print(s)
							while self.__mem[self.__i]:
								self.fuck(s)
							s = ''
						else: s += n

				elif br: s += n
				x += 1
				# if x == l and s != '': raise SyntaxError("Missing ].")

			return self.__buffer

		except Exception as e:
			print(e.__class__.__name__,':',str(e).capitalize())
			print('i:   ', self.__i)
			#print('mem: ',self.__mem)


# x = Pybfi().fuck
# print(x('+[>,>++++[<++++++++>-]<.<]'))