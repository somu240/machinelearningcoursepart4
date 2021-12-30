

nums = [1,2,3,4,5,6]

print(list(map(lambda x: x**x,nums)))

nums = range(-5,5)

less_than_zero = list(filter(lambda x: x<0,nums))
print(less_than_zero)

from functools import reduce
product = reduce((lambda x, y: x+y), range(0,101))
print(product)