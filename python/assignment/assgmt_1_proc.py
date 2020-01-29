'''
this is a pogram related to indexing of number using procedural programming
'''



l1 = [1, 3, 5, 16, 8]
l2 = [6, 5, 9, 4, 13, 12]
l3=l1+l2
s=set(l3)
l4=list(s)
l4.sort()

while True:
    in_val = input('enter device id:')
    in_val=int(in_val)
    if in_val in l4:
        print('device id found, id=',in_val,'its index:',l4.index(in_val))
    elif in_val>max(l4):
        print('not found')
    else:
        for i in l4:
            if i>in_val:
                print('val=',i,'ind=',l4.index(i))
                break

    ch=input('do you want to quit (y/n)?')
    if ch=='y':
        break

