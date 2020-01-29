s = 'python'

for a in s:
    print('a =', a)

b = 'java'
L = [10, 20, 30]

for b in L:
    print('b =', b)

print('Now a and b = ', a, b)

D = {'A': 10, 'B': 20}

for k in D:
    print('k = ', k)

line = '-' * 40
print(line)

for k in D.keys():
    print('Key = ', k, 'Value =', D[k])

print(line)

for v in D.values():
    print('v =', v)

print(line)

for i in D.items():
    print('i =', i, i[0], i[1])

print(line)

for i, j in D.items():
    print(i, j)

print(line)

hosts = ['h1', 'h2', 'h3']
ips = ['ip1', 'ip2']

z = zip(hosts, ips) # Can be iterated only once

print(z)
print(list(z))  # Iterating over z and print them as list

for h, p in zip(hosts, ips):    # We use zip again because z has already been iterated
    print(h, p)

for h, p in z:  # It will work only if iteration over the zip file is not already done, so nothing will print now as iteration is done above
    print(h, p)

print(line)

# for(i=2; i<10; i+2)
r1 = range(10)
r2 = range(1, 10)
r3 = range(1, 10, 2)
print(list(r1), list(r2), list(r3), sep="\n")
print(line)

r4 = range(10, 1, -1)
for i in range(2, 10, 2):
    print("i =", i)

print(line)

for h in range(0, len(hosts)):
    print(hosts[h])

for h in hosts[::2]:
    print('h =', h)

print(line)

comp = ['IBM', 'DEL1', 'SAP', 'DEL2']
for c in comp:
    if c.startswith('DEL'):
        print('FOUND')

print("NEW FOR")

for c in comp:
    if c.startswith('DEL'):
        print("FOUND")
        break

# Using flag

flag = False
for c in comp:
    if c.startswith('DEL'):
        print("FOUND")
        flag = True

if not flag:
    print('NOT FOUND')

# FOR ELSE
for c in comp:
    if c.startswith('DEL'):
        print("FOUND")
        break
else:
    print("NOT FOUND")

print(line)

for i in comp:
    if i.startswith('DEL'):
        print('Some logic')
    print('Last statement of FOR')

print(line)

for i in comp:
    if not i.startswith('DEL'):
        continue
    if i.startswith('DEL'):
        print('Some logic')
    print('Last statement of FOR')


