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
result = sum_many(4, 5, 6)
print(result)

def testKwargs(*args, **kwargs):
	print(args)
	print(kwargs)
testKwargs(1, 2, 3, name='foo', age=3)

def sum_and_mul(a, b=10):
	return a+b, a*b
print(sum_and_mul(2,3))
print(sum_and_mul(2))

a = 1
def vartest():
	global a
	a = a+1
vartest()
print(a)

sum = lambda a, b: a+b
print(sum(3, 4))

myList = [lambda a,b:a+b, lambda a,b:a*b]
print(myList)
print(myList[0](1,2))
print(myList[1](3,4))

def is_odd(a):
	if(a % 2 == 0):
		print("even")
	else:
		print("odd")
is_odd(1)

def avg(*args):
	sum = 0
	for i in args:
		sum = sum + i
	print(sum/len(args))
avg(1,2,3,4,5)