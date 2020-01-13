def add1(a, b):
    print("RESULT IS")
    print(a + b + a)
    print("END OF RESULT")


def sub1(a, b):
    print("RESULT IS")
    print(a - b)
    print("END OF RESULT")


add1(10, 20)
sub1(10, 20)


# MY DECORATOR

def myDec(func):
    def decorated_func(x, y):
        print("RESULT IS")
        func(x, y)
        print("END OF RESULT")

    return decorated_func


@myDec
def add2(a, b):
    print(a + b)


add2(10, 20)


# How  @mydec works
def add3(a, b):
    print(a + b)


f = myDec(add3)
# f => Decorated func

f(100, 200)


def myDecX(func):
    def decorated_func(*x, **y):
        print("RESULT IS")
        func(*x, **y)
        print("END OF RESULT")

    return decorated_func


@myDecX
def add4(a, b, c):
    print(a + b + c)


add4(10, 20, 30)
