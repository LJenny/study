"""
Author: Jenny
Data: 2018-04-20
4. function
"""
def sum(a, b):
	return a+b
print(sum(3, 4))

def printSum(a, b):
	print("%d + %d = %d" % (a, b, (a+b)))
printSum(3, 4)

def sum_many(*args):
	sum = 0
	for i in args:
		sum = sum + i
	return sum
result = sum_many(1, 2, 3)
print(result)