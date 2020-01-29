# list -> class
L1 = list([10, 20, 30])
L2 = [10, 12.5, 'python', ['a', 'b']]
print(L1, L2, sep='\n')
print(L2[1])
print(L2[2][1])
print(L2[3][1])
print(L2[-1:1:-1])

# Add
L2.append(200)
print('append = ', L2)

L2.insert(2, 300)
print('Insert = ', L2)

L3 = [10, 20]
L4 = ['a', 'b']
L5 = L3 + L4
L6 = L3 * 10
print(L5, L6, sep='\n')

L3.extend(L4)
print('Extend = ', L3)

# Remove
r1 = L5.pop()
print('r1 =', r1, L5)
r2 = L5.pop(2)
print('r2 =', r2, L5)
r3 = L5.remove(20)
print('r3 =', r3, L5)

del L5[0]
print('After del=', L5)

# Update
print('L3 =', L3)
L3[1] = 'Java'
print('After update = ', L3)

# Some other methods
L6 = [10, 30, 20]
L6.sort()
print('Sort Asc =', L6)
L7 = ['z', 'a', 'b']
L7.sort(reverse=True)
print('Sort Desc =', L7)
L8 = [10, 'a', 20, 'b']
L8.reverse()
print('Reverse = ', L8)
L8.clear()
print('L8 =', L8)

# Copy
L = [10, ['a', 'b']]
M = L # Reference Copy
N = L.copy() # Shallow Copy

# Copy Module - copy(), deepcopy()
import copy
P = copy.deepcopy(L)
print(id(L[0]), id(P[0]))
print(id(L[1]), id(P[1]))

cp = copy.deepcopy
q = cp(L)
print(q)
