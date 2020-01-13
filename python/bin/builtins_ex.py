# Map
L = [100, 200, 300, 400]


def sub(i):
    return i - 10


r1 = map(sub, L)
print(list(r1))


# Filter
def filt(j):
    return j > 100


r2 = filter(filt, L)
print(list(r2))

# Reduce
import functools as fc


def red(p, q):
    return p + q


r3 = fc.reduce(red, L)
M = ['W', 'E', 'L']
r4 = fc.reduce(red, M)
print(r3, r4)

# Lambda Functions

# 1. Does not have a function name
# 2. Function body should have one line

r5 = map(lambda i: i - 10, L)
r6 = filter(lambda j: j > 100, L)
r7 = fc.reduce(lambda p, q: p + q, L)
print(list(r5), list(r6), r7, sep='\n')

f = lambda a, b: a + b
r8 = f(10, 20)
print('r8 =', r8)

L = [(lambda i: i * i)(a) for a in range(10)]
print('L =', L)

Keys = ['A', 'B']
Values = [10, 20]
D = {k: (lambda i: i + i)(v) for k, v in zip(Keys, Values)}
print('D =', D)
