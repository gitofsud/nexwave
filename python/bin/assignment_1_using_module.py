import assgmt_1_func as af

while True:
    i = input('Enter ID: ')
    i = eval(i)
    L = [10, 20, 30]
    r = af.dev_id_search(i, L)
    print('Result:', r)
    ch = input('Quit(y/n)? ')
    if ch == 'y':
        break
