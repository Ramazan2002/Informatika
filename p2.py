def f19(n):
	a = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4:'Апрель', 5:'Май', 6:'Июнь', 7:'Июль', 8:'Август', 9:'Сентябрь', 10:'Октябрь', 11:'Ноябрь', 12:'Декабрь'}
	return a[n]

def f20(n):
	a = {(1, 2, 12): 'Зима', (3, 4, 5): 'Весна', (6, 7, 8): 'Лето', (9, 10, 11): 'Осень'}
	for elem in a.values():
		if elem in a.keys():
			return elem


def f21(n):
	a = {k: k ** 3 for k in range(1, n + 1)}
	return a

def f21_1(a):
	s = 1
	for elem in a.values():
		s *= elem
	return s

def f22(a, b):
	c = {}
	for i in range(len(a)):
		c[a[i]] = b[i]
	return c

def f23(a):
	a = {a[elem]: a.get(elem) for elem in a}
	return a

print(f19(int(input())))
print(f20(int(input())))
print(f21(int(input())))
print(f21_1({1: 5, 2: 7, 3: 8}))
print(f22([1,2,3], [4, 8, 6]))
print(f23({1:435, 2: 4}))