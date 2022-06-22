from re import A


x = 100


def mainFunction():
    global x
    print(x)

    x = "Paramount Insurance Company Limited"
    print(x)

    y = 500
    print(y)


mainFunction()
print(x)
# print(y) wrong way


# another global variable example

def my_func():
    global a
    a = 10
    b = 20
    c = a+b
    print(c)


my_func()


def func():
    print(a)


func()

# /////
def outside_function():
    a = 20

    def inside_function():
        nonlocal a
        a = 30
        print("Inner function: ", a)
    inside_function()
    print("Outer function: ", a)


outside_function()
