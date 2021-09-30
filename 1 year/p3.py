def alll(a):
	if type(a) == list:
		for elem in a:
			if (elem == False) or (elem == 0) or (elem == []):
				return False
	return True

	if type(a) == dict:
		for k, v in a:
			if (v == False) or (v == 0) or (v == []):
				return False
	return True

def anny(a):
	if type(a) == list:
		k = 0
		for elem in a:
			if (elem == False) or (elem == 0) or (elem == []):
				k += 1
		if k == len(a):
			return False
		return True

	if type(a) == dict:
		k = 0
		for k, v in a:
			if (v == False) or (v == 0) or (v == []):
				k += 1
		if k == len(a):
			return False
		return True

print(alll([1,2,3,[1]]))