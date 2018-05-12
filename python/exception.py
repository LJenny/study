try:
	a = [1, 2]
	print(a[3])
	4 / 0
except (ZeroDivisionError, IndexError) as e:
	pass
except ZeroDivisionError as e:
	print(e)
except IndexError as e:
	print("I am index error")
	print(e)
else:
	print("ok")
finally:
	print("I'm finally")

class Bird:
	def fly(self):
		raise NotImplementedError

class Eagle(Bird):
	#pass  # error!!
	def fly(self):
		print("very fast")

eagle = Eagle()
eagle.fly()

class MyError(Exception):
	def __init__(self, msg):
		self.msg = msg
	def __str__(self):
		#return "It can't accept the nick!!"
		return self.msg

def say_nick(nick):
	if nick == 'pull':
		raise MyError("It can't accept the nick~")
	print(nick)

try:
	say_nick("push")
	say_nick("pull")
#except MyError:
#	print("Don't ust pull")
except MyError as e:
	print(e)  # use error message