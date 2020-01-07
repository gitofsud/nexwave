a = 0

while a < 10:
    print('a =', a)
    a += 2

s = 'python'
b = 0
while b < len(s):
    print('b =', s[b])
    b += 1

L = ['FN', 'LN', 'ADR', 'a1', 'FN', 'ADR', 'a2', 'FN']

i = 0
while i < len(L):
    if L[i] == 'ADR':
        i += 1
        print(L[i])
        i += 1
    else:
        i += 1

j = 0
while j < len(L):
    if L[j].startswith('a'):
        print('FOUND')
        break
    else:
        j += 1
else:
    print('NF')

k = 0
while k < len(L):
    if not L[k].startswith('a'):
        k = k + 1
        continue
    print(L[k])
    k = k + 1
    print('Last Statment of While')

cart = []
while True:
    i = input('Enter Item: ')
    cart.append(i)
    ch = input('Quit (y/n)? : ')
    if ch == 'y':
        print('Cart = ', cart)
        break

