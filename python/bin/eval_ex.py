a = '10'
b = int(a)
c = eval(a)

print(a, b, c)

d = '[10, 20, 30]'
e = 'Hello'
f = list(e)
print(f)

g = list(d)
h = eval(d)
print(g, h, sep="\n")

i = 10
j = 20
k = eval('i + j')
print('k =', k)
