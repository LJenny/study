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