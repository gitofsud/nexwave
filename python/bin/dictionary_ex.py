# dict -> class

D = {'course': 'python', 'dur':10, 'loc': 'Blr'}
print(D['course'])

# Unordered

# Add or Update
D['course'] = ['c++', 'java']
E = D.copy()

# Remove
r1 = D.pop('course')
print('pop =', r1, D)

del D['dur']
print('After del =', D)

r2 = D.popitem()
print(r2, D)

# Other methods
k = E.keys()
v = E.values()
i = E.items()

print(k, v, i, sep='\n')
