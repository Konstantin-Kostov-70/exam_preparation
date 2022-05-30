import ast

a = "[1, 20, 3]"

print(type(a))
a = ast.literal_eval(a)

b = '2 , 5'
print(b)
b = ast.literal_eval(b)

c = 'True'
c = ast.literal_eval(c)
print(c)
print(type(c))

print(a)
print(b)
print(type(b))

print(type(a))
