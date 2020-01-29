F1 = open('log_report.txt', 'w')
F2 = open('log_report.csv', 'w')
F1.write('IP\tDATE\tPICS\tURL\n')
F2.writelines(['IP,', 'DATE,', 'PICS,', 'URL,\n'])
F3 = open(r'C:\Users\lab365\Desktop\python\log\server_log.txt')

for line in F3:
    if line[:3].isdigit():
        sp = line.split()
        ip = sp[0]
        dt = sp[3]
        dt1 = dt[1:12]
        dt2 = dt[1:dt.index(':')]
        # if sp[6].startswith('/pics')
        if 'pics' in sp[6]:
            im = sp[6] # /pics/5star2000.gif
            im1 = im[6:] # 1 - way
            im2 = im.split('/')[-1] # 2nd way
            im3 = im.lstrip('/pics/') # 3rd way
            im4 = im.replace('/pics/', '') # 4th way
        else:
            im1 = 'No Image'
        url = sp[10][1:-1]
        print(ip, dt2, im1, url, sep='\t', file=F1)
        print(ip, dt2, im1, url, sep=',', file=F2)

F1.close()
F2.close()
F3.close()
