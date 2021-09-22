alphabates = ['a', 'b', 'c', 'd', 'd', 'f']


def isvovel(alphabates):
    vovels = ['a', 'e', 'i', 'o', 'u']
    if alphabates in vovels:
        a = print("hoiiii")
        return a
    else:
        return False


result = filter(isvovel, alphabates)
print(type(result))
result = list(result)
print(result)
