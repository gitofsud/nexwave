# POSITIONAL Args
def add(a, b):
    return a + b


r = add(10, 20)
print('r =', r)


def get_ips(file_path, mode):
    F = open(file_path)
    if file_path.endswith('.csv'):
        ips = [line.split(',')[0] for line in F if line if line[:3].isdigit()]
        return ips
    else:
        ips = [line.split()[0] for line in F]
        return ips


r = get_ips(r"C:\Users\lab365\Desktop\python\bin\log_report.csv", 'r')
print(r)
