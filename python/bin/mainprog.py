import lib.project.net.addmodule

print(lib.project.net.addmodule.msg)
print(lib.project.net.addmodule.add(10, 20))

line = '-' * 40
print(line)

# 2nd way
import sys
print(sys.path)
# sys.path.append(r'C:\Users\lab365\Desktop\python\lib\addmodule.py')

# 3rd way - Import statement using alias
import lib.project.net.addmodule as a
print(a.msg)
print(a.add(10, 20))
print(line)

# 4th way
from lib.project.net.addmodule import msg, add
print(msg)
print(add(20, 30))

from lib.project.net.addmodule import msg as m, add as a
print(m)
print(a)

from lib.project.net.addmodule import *
print(msg)
print(add(10, 20))
