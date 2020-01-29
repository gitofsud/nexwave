# POSITIONAL Args with DEFAULT Values
def add(a, b=10):
    return a + b


r = add(10)
print('r =', r)


def get_ips(file_path, mode='r'):
    F = open(file_path, mode)
    if file_path.endswith('.csv'):
        ips = [line.split(',')[0] for line in F if line if line[:3].isdigit()]
        return ips
    else:
        ips = [line.split()[0] for line in F]
        return ips


r = get_ips(r"C:\Users\lab365\Desktop\python\bin\log_report.csv")
print(r)
