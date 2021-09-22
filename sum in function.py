def addition(*inputs):
    sum = 0
    for i in inputs:
        sum = i+sum

    return(sum)


like = addition(1, 2, 3, 4, 5)
print(like)

print(type(like))
