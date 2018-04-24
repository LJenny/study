print("z","z""z")

for i in range(10):
	print(i, end=' ')

a = input("plz enter : ")
print(a)

input1 = input("fist:")
input2 = input("second:")

total = int(input1) + int(input2)
print("sum %d" % total)

b = "1,2,3,4,5"
numbers = b.split(",")
total = 0
for n in numbers:
	total += int(n)
print(total)

f = open("file.txt", 'w')
for i in range(1, 11):
	data = "line num : %d\n" % i
	f.write(data)
f.close()

f = open("file.txt", 'r')
while True:
	line = f.readline()
	if not line: break
	print(line)
f.close()

f = open("file.txt", 'r')
lines = f.readlines()
for line in lines:
	print(line)
f.close()

f = open("file.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("file.txt", 'a')
for i in range(11, 20):
	data = "new line num : %d" % i
	f.write(data)
f.close()

with open("file.txt", 'r') as d:
	data = d.read()
	print(data)
