def choose(obj):
	if isinstance(obj, list):
		return sum(obj)
	elif isinstance(obj, dict):
		return {k: v for v, k in obj.items()}
	elif isinstance(obj, tuple):
		r = 1
		for elem in obj:
			r *= elem
		return r
	elif isinstance(obj, int):
		return 0
	elif isinstance(obj, float):
		return obj
	elif isinstance(obj, set):
		x = set()
		for elem in obj:
			x.add(elem*elem)
		return x
print(choose((1,2,3,4)))