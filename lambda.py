def myfun(n):
    return lambda a:a*n
x=myfun(2)
print(x(5))

print(map(lambda x:pow(x,3),L1))
list(map(lambda x:pow(x,3),L1))
