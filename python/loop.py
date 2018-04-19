"""
Author: Jenny
Data: 2018-04-19
3. if, while, for
"""
a = 1
print(type(a))
b = 1
print(a is b)

money = 2000
card = 1
if money >= 3000 or card:
	print("call taxi")
else:
	print("walk")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
	pass
elif card:
	print("walk")
else:
	print("walk")

c = [1, 9, 23, 46]
if 23 in c:
	print("lotto")

treeHit = 0
while treeHit < 10:
	treeHit = treeHit + 1
	print("treeHit : "+str(treeHit))
	if treeHit == 10:
		print("fall")

prompt = """
	1. Add
	2. Del
	3. List
	4. Quit

	Enter numer: """

number = 0
while number != 4:
	print(prompt)
	number = int(input())

d = 1
sumVal = 0
while d <= 100:
	sumVal += d
	d += 1
print(sumVal)

e = 0
while True:
	e += 1
	if (e > 5): break
	print('*' * e)
print("\n")
star = 7
space = 0
while star > 0:
	print(' ' * space + '*' * star)
	star -= 2
	space += 1

test_list = ['one', 'two', 'three']
for i in test_list:
	print(i)

f = [(1, 2), (3, 4), (5, 6)]
for (fir, last) in f:
	print(fir + last)

g = range(10)
print(g)

sum = 0
for i in range(1, 11):
	sum = sum + i
print(sum)