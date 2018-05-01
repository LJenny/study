import sys
import mod1

print(mod1.sum(2, 3))
print(mod1.safe_sum(2, '3'))

print(mod1.PI)
a = mod1.Math()
print(a.solv(3))

# print the directory installed python library.
print(sys.path)

# if you want to load a module, then you can append its path to sys.path.
# or use PYTHONPATH (환경변수) as 'set PYTHONPATH=C:/'
sys.path.append("C:/")
print(sys.path)