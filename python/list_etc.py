"""
Author: Jenny
Data: 2018-04-18
2. list, tuple, dictionary
"""
a = [1, 3, 5, 7, 9, 'List', ['apple', 'banana']]
print(a * 2)
print(str(a[0])+" "+a[5]+" "+a[6][1])
a[1:3] = [2, 4, 6]
print(a)
a[6:8] = []
del a[1]
print(a)
a.append(-12)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(-12))
a.insert(0, 99)
print(a)
a.remove(99)
print(a)
print(a.count(1))
b = [11, 22, 33]
a.extend(b)
print(a)

c = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
print(c[4]+" "+c[2])
print(len(c))
print(id(c))

print('*'*50)
t1 = (1,)
t2 = 1, 2, 3
print(t1)
print(t2)
print(t1[0])
print(t1+t2)

print('*'*50)
dic1 = {1: 'a', 3: 'c'}
dic1[2] = 'b'
dic1['name'] = 'Jenny'
print(dic1)
del dic1[2]
print(dic1)
print(dic1['name'])
print(dic1.keys())
for k in dic1.keys():
	print(k)
print(list(dic1.keys()))
print(list(dic1.values()))
print(list(dic1.items()))
print(dic1.get('name'))
print(dic1.get('no key'))
print(dic1.get('name', 'python'))
print('name' in dic1)
dic2 = {1:1, 2:2, 3:3}
print(min(dic2.values()))
print(max(dic2.values()))