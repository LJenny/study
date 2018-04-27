def sum(a, b):
	return a + b

def safe_sum(a, b):
	if type(a) != type(b):
		print("not to add")
		return
	else:
		return sum(a, b)

