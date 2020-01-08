x = 10


def f1():
    def f2():
        global x
        global y
        x = 200
        y = 40
        print('F2 =', x)
    f2()
    print('F1 =', x)


f1()
print('Global =', x, y)

print(dir(__builtins__))
