def add():
    a = 10
    b = 20
    c = a + b
    print('c =', c)

add()

def get_ips():
    F = open(r'C:\Users\lab365\Desktop\python\log\server_log.txt')
    ips = [line.split()[0] for line in F if line[:3].isdigit()]
    print('ips =', ips)

get_ips()

print('ips =', ips) # Name Error will occur