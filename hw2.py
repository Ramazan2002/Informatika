a = [1, 2, 3, 4, 2]
b = [2, 3, 1,2, 4]
c = (1, 2, 3,)
d = (6, 4, 5, 7,)

def f9(x):
	return True if len(x) == 0 else False

def f10(x):
	x = [x[i] for i in range(len(x)) if i % 2 == 0]
	return x

def f11(x, y):
	return True if sorted(x) == sorted(y) else False

def f12(x, y):
	return x + y

def f13(x, d):
	tup = []
	lst = []
	for i in range(len(x)):
		if x[i] >= d:
			lst.append(x[i])
		else:
			tup.append(x[i])
	return tuple(lst), tup

def f14(x):
	if x[:(len(x) + 1) // 2] == x[len(x) // 2::][::-1]:
		return True
	else:
		return False

def f15(x):
	y = [i for i in range(len(x)) if x[i] != 0]
	return y

def f16(x, y):
	return min(x, key = lambda x: abs(x - y))

def f17(x):
	y = sum(x[:3])
	for i in range(len(x) - 3):
		if sum(x[i:i + 3]) > y:
			y = sum(x[i:i + 3])
			z = x[i:i + 3]
		else:
			z = x[:3]
	return z

def f18(x):
	if len(x) % 2 == 0:
		x = x[:(len(x) + 1) // 2 - 1] + x[len(x) + 1 :len(x) // 2:-1 ][::-1]

	else:
		x = x[:len(x) // 2] + x[len(x):len(x) // 2:-1 ][::-1]
	return x


print(f9(a))
print(f10(a))
print(f11(a, b))
print(f12(c, d))
e, f = f13(a, 3)
print(e, f)
print(f14([1,2,3,2,1]))
print(f15([1, 0, 0, 4]))
print(f16(a, 2.1))
print(f17(a))
print(f18(a))