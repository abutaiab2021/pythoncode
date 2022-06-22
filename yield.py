def fun_genarate():
    yield 1
    yield 2
    yield 3


for value in fun_genarate():
    print(value)
