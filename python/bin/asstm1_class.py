class search:
    def __init__(self,l1,l2):
        r=l1+l2
        r=set(r)
        r=list(r)
        self.l=r

    def dev_id_search(self,dev_id):
        dev_list=self.l
        if dev_id in dev_list:
            return 'dev id found , dev-id=' + str(dev_id) + 'index=' + str(dev_list.index(dev_id))
        elif dev_id > max(dev_list):
            return 'not found'
        else:
            for i in dev_list:
                if i > dev_id:
                    return 'val=' + str(i) + '   ind=' + str(dev_list.index(i))

def main():
    l1 = [1, 3, 5, 16, 8]
    l2 = [6, 5, 9, 4, 13, 12]
    a=search(l1,l2)
    r=a.dev_id_search(10)
    print(r)

if __name__ == '__main__':
    main()