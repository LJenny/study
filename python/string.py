"""
Author: Jenny
Data: 2018-04-16
1. String stduy
"""
head = "Python"
tail = " is fun!"
print("="*50)
print((head+tail)*2)
print("="*50)

a = "Life is too short, You need python."
print(a[19:])
print(a.count('o'))
print(a.find(','))
print(a.upper())
print(a.replace("Life", "Your leg"))
print(a.split())
print("="*50)

b = '20180416Sunny'
year = b[:4]
day = b[4:8]
weather = b[8:]
print(year + " " + day + " " + weather)
print("="*50)

number = 3
c = "I eat %d apples. I eat %s banana" % (number, "one")
d = "I eat {0} apples. I eat {number} banana".format(10, number="one")
print(c)
print(d)
print("="*50)

print("%-10syenare" % "hi")
print("{0:>20}".format("hi"))
print("{0:!<20}".format("hi"))
print("="*50)

pin = "9100101-2000000"
if pin[8] == '2':
	print('girl')
else:
	print('boy')
print("="*50)

e = 'a:b:c:d'
print(e.replace(":", "#"))
print('#'.join(e.split(':')))