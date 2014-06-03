"""Python Brainfuck interpretor recursive"""
def brainfuckr(b, ii=0, iarr=[0 for n in range(0,30000)],ibuff=''):
	i,arr,buff = 0,[0 for n in range(0,30000)],''
	l,x = len(b),0
	s = ''
	# s = '' if b[0] != 'k' else 'r' #FOR RECURSION VERSION
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

				# buff += brainfuckr(s,i,arr) #FOR RECURSION VERSION
				s = ''

		elif:
			s += n

		x += 1
	return buff


# print(brainfuck(' +++++++++++++++++++++++++++++++++++++++++++++\
#  +++++++++++++++++++++++++++.+++++++++++++++++\
#  ++++++++++++.+++++++..+++.-------------------\
#  ---------------------------------------------\
#  ---------------.+++++++++++++++++++++++++++++\
#  ++++++++++++++++++++++++++.++++++++++++++++++\
#  ++++++.+++.------.--------.------------------\
#  ---------------------------------------------\
#  ----.-----------------------.'))

print(brainfuck('++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++\
 .>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.\
 ------.--------.>+.>.'))


