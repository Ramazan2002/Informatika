def f1(a, x, y):
	return sum(a[x: y + 1])

def f1_1(a, x, y):
	k = 1
	for elem in a[x: y + 1]:
		k *= elem
	return k

print(f1([1, 2, 3, 10, 254], 1, 3))
print(f1_1([1, 2, 3, 10, 254], 1, 3))
def f2(a, x):
	lst = []
	for i in range(len(a)):
		if a[i] != x:
			lst.append(a[i])
	return lst

def f22(a, x):
	for elem in a:
		while x in a:
			a.remove(x)
	return a

def f3(a, x, y):
	a[x: y + 1] = a[x: y + 1][::-1]
	return a

def f4(a, x):
	lst = a[:]
	for i in range(len(a)):
		lst[(i+x) % len(a)] = a[i]
	return lst

def f5(*args):
	return sum(args, [])

def f6(a, b):
	if len(a) > len(b):
		for i in range(len(b)):
			a.insert(2 * i + 1, b[i])
	else:
		for i in range(len(a)):
			b.insert(2 * i + 1, b[i])
	return a

#def f8(a):
	#lst = []
	#for i in range(1, len(a)):
	#	lst += [a[i - 1], a[i]]
	#lst = tuple(lst)

print(f2([1, 2, 3, 1, 10, 254], 1))
print(f22([1, 2, 3, 1, 10, 254], 1))
print(f3([1, 2, 3, 10, 254], 0, 3))
print(f4([1, 2, 3], -2))
print(f5([1, 2, 3], [5, 2]))
print(f6([1, 1, 1, 1, 1, 1], [0, 0, 0]))
#print(f8([1, 2, 3, 4, 5, 6]))