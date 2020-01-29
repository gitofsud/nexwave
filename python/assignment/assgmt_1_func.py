'''
>>> L = [10, 20, 30]
>>> dev_id_search(20, L)
'dev id found , dev-id=20index=1'
'''


def dev_id_search(dev_id, dev_list):



def main():
    l1 = [1, 3, 5, 16, 8]
    l2 = [6, 5, 9, 4, 13, 12]
    l3 = l1 + l2
    s = set(l3)
    l4 = list(s)
    l4.sort()

    while True:
        i = input('enter device id:')
        i = eval(i)
        r = dev_id_search(i, l4)
        print('search result =', r)
        ch = input('do you want to quit (y/n)?')
        if ch == 'y':
            break


if __name__ == '__main__':
    # main()
    import doctest

    doctest.testmod()
