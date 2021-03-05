mydict = {2:9, 5:-3, 3:12, 7:3, 4:20,
1:9, 6:9, 11:3, 13:6}
def fill(mydict, n):
	for i in range(n + 1):
		if i not in mydict.keys():
			mydict[i] = '!!'
	return mydict

#def no_dup(mydict):
#	for elem in mydict.values():
#		if list(mydict.values).count(elem) > 1:
#			del 
#	return mydict

def summarize(n):
	s = 0
	while (n > 0) and (n != s):
		s += n % 10
		n //= 10
		if (n == 0) and (s // 10 > 0):
			n = s
			s = 0
	return s

def salt_lang(string):
	lst = ['а', 'я', 'и', 'ю', 'ы', 'о', 'э', 'е', 'у']
	for c in string:
		if c in lst:
			string = string.replace(c, f'{c}c{c}')

	return string

print(fill(mydict, 20))
#print(no_dup(mydict))
print(summarize(152))
print(salt_lang('Привееет! Как дела?'))