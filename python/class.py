# 클래스 생성
class FourCal:
	# 초기화
	def __init__(self, first=0, second=0):
		self.first = first
		self.second = second
		self.value = 0
	def setData(self, first, second):
		self.first = first
		self.second = second
	def sum(self):
		return self.first + self.second
	def sub(self):
		return self.first - self.second
	def mul(self):
		return self.first * self.second
	def div(self):
		return self.first / self.second
	def add(self, val):
		self.value += val
		return self.value
	def minus(self, val):
		self.value -= val
		return self.value

a = FourCal(1, 1)
print(type(a))
#a.setData(4, 2)
print("first : %d" % a.first)
print("second : %d" % a.second)
print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())
print(a.add(5))
print(a.add(8))
print(a.minus(8))

# 클래스 상속
class MoreFourCal(FourCal):
	def pow(self):
		return self.first ** self.second
b = MoreFourCal(3, 3)
print(b.sum())
print(b.pow())

class SafeFourCal(FourCal):
	# 클래스 오버라이딩
	def div(self):
		if self.second == 0:
			return 0
		else:
			return self.first / self.second
c = SafeFourCal(4, 0)
print(c.div())

class MaxLimitCal(FourCal):
	def __init__(self):
		self.value = 200
	def add(self, val):
		if self.value >= 100:
			print("over 100")
			return
		else:
			self.value += val
		return self.value
e = MaxLimitCal()
print(e.add(4))
print(e.add(5))

data = "jenny|28|F"
tmp = data.split("|")
age = tmp[1]
print(age)

class Data:
	def __init__(self, data):
		tmp = data.split("|")
		self.name = tmp[0]
		self.age = tmp[1]
		self.sex = tmp[2]
	def print_age(self):
		print("age : %d" % int(self.age))
d = Data(data)
print(d.name)
d.print_age()