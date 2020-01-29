l = [str(x) + "\n" for x in dir(__builtins__)]

f = open('abc.txt', 'w')
f.writelines(l)
f.close()