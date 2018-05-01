def sum(a, b):
	return a + b

def safe_sum(a, b):
	if type(a) != type(b):
		print("not to add")
		return
	else:
		return sum(a, b)


# 대화형 인터프리터나 다른 모듈에서 불러서 사용할 때는 수행되지 않음
if __name__ == "__main__":
	print(safe_sum('a', 1))
	print(safe_sum(1, 4))
	print(sum(10, 10.4))

PI = 3.141592

class Math:
	def solv(self, r):
		return PI * (r ** 2)
