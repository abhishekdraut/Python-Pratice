import functools
result = functools.reduce(lambda x, y: x+y, range(0, 6))
print(result)
