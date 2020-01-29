a = 10

# IF

if a == 10:
    print('a eq 10')

if a > 10:
    print('a gt 10')

if a < 10:
    print("a lt 10")

# ELIF

if a == 10:
    print('a eq 10')
elif a > 10:
    print('a gt 10')
elif a < 10:
    print("a lt 10")

# ELSE

if a == 10:
    print('a eq 10')
elif a > 10:
    print('a gt 10')
else:
    print("a lt 10")

# Examples

s = "python"

if 'th' in s:
    print('Substring found')

if not s.startswith('java'):
    print("Not java")

if s != 'c++':
    print("Not C++")

if s[1:3] == 'yt':
    print('yt found')

L1 = [10, 20]
L2 = L1
L3 = L1.copy()

if 20 in L1:
    print('20 found')

if L1 is L2:    # is -> compares id
    print('Both refers to same object')

if id(L1) == id(L2):
    print('Both refers to same object')

if L1 == L3: # Checks if content is same, id may not be same
    print('Contents are same')

D = {'A': 10, 'B': 20}

if 'B' in D:
    print('Key - B found')

if 'B' in D.keys():
    print('Key - B found')

if 10 in D.values():
    print('Value - 10 found')

if ('A', 10) in D.items(): # [('A', 10), ('B', 20)]
    print('Item found')

if a == 10:
    pass

# () and or not