# Core Data Types
# Numbers
# Strings
'''
List
Tuple
'''

"""
Dictionary
Set
"""

# Numbers
a = 10 #int
b = 12.5 #float
c = 0x12 #hex
d = 0b1010 #bin
e = 0o12 #oct

print('Hello')
print('a')
print('RESULT = ', a, b, c, d, e)
print('RESULT = ', a, b, c, d, e, sep='|') 
print('RESULT = ', a, b, c, d, e, sep='|', end='.') #file=, flush=
print('Test')

f = int(20)
print(f)

print(a)    # will print object it's holding
print(id(a))    # will print reference
print(type(a))
print(type(a).__name__)

"""
Immutable: Numbers, Strings, Tuple
Mutable: List, Set, Dictionary
"""

a = 100
print(a)
print(id(a))

b = a
print(b) # copies reference
print(id(b)) # so, b and a both refer to same object

a = 200
b = 300

# sys.getRefCount -> To get count of references in an object
