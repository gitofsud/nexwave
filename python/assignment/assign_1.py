list1 = [1, 3, 5, 16, 8]
list2 = [6, 5, 9, 4, 13, 12]

joined_list = list1
joined_list.extend([x for x in list2 if x not in list1])

# joined_list = list(set(list1 + list2))
print(joined_list)


def search(dev_id):
    if dev_id in joined_list:
        print('Found at index: {}'.format(joined_list.index(dev_id)))
    else:
        for i in joined_list:
            if i > dev_id:
                print('Value not found, so for next highest value')
                print('Index: {}, Value: {}'.format(joined_list.index(i), i))
                break
        else:
            print('Not Found')


search(int(input('Enter Device ID: ')))
search(int(input('Enter Device ID: ')))
search(int(input('Enter Device ID: ')))
