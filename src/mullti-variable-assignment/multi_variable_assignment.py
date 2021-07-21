# https://note.nkmk.me/en/python-multi-variables-values/

# You can assign multiple values to multiple variables by separating variables and values with commas ,.
a, b = 100, 200
print(a)
# 100
print(b)
# 200

# You can assign the same value to multiple variables by using = consecutively.
a = b = 100
print(a)
# 100
print(b)
# 200

# You can assign to more than three variables. Moreover, it is also possible to assign to different types.
a, b, c = 0.1, 100, 'string'
print(a)
# 0.1
print(b)
# 100
print(c)

# If the number of variables on the left and the number of values on the right do not match, a ValueError will occur,
# but you can assign the rest as a list by appending * to the variable name.

# a, b = 100, 200, 300
# ValueError: too many values to unpack (expected 2)

# a, b, c = 100, 200
# ValueError: not enough values to unpack (expected 3, got 2)
a, *b = 100, 200, 300
print(a)
print(type(a))
# 100
# <class 'int'>
print(b)
print(type(b))
# [200, 300]
# <class 'list'>

*a, b = 100, 200, 300
print(a)
print(type(a))
# [100, 200]
# <class 'list'>
print(b)
print(type(b))
# 300
# <class 'int'>

# If there is one variable on the left side, it is assigned as a tuple.
a = 100, 200
print(a)
print(type(a))
# (100, 200)
# <class 'tuple'>

# Even three or more can be written in the same way.
a = b = c = 'string'
print(a)
# string
print(b)
# string
print(c)
# string

# Rather than immutable objects such as int, float and str, mutable objects such as list and dict be careful when assigning.
# If you use = consecutively, the same object is assigned to all variables,
# so if you change the value of element or add a new element, the other will also change.
a = b = [0, 1, 2]
print(a is b)
# True
a[0] = 100
print(a)
# [100, 1, 2]
print(b)
# [100, 1, 2]

# Same as below.
b = [0, 1, 2]
a = b
print(a is b)
# True
a[0] = 100
print(a)
# [100, 1, 2]
print(b)
# [100, 1, 2]

# If you want to process them separately, you need to assign them to each.
a = [0, 1, 2]
b = [0, 1, 2]
print(a is b)
# False
a[0] = 100
print(a)
# [100, 1, 2]
print(b)
# [0, 1, 2]
