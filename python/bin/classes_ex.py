class Account1:
    def addUser(self, n):
        self.name = n

    def viewUser(self):
        return self.name

    bank = 'ICICI'

    @classmethod
    def bankRules(cls, area):
        return 'Bank Rules' + area

    @staticmethod
    def bankInfo():
        return 'Bank Info'

    def __init__(self):
        print('SB LOGIC HERE')

class Account2(Account1):
    def Addadhar(self,a):
        self.adhar=a
    def Viewadhar(self):
        return self.adhar

    def viewUser(self):
        return 'welcome'+self.name

    def __init__(self):
        super().__init__() # or Account1.__init__(self)
        print('CA LOGIC HERE')

class RBI:
    def Viewrules(self):
        return 'rbi rules'

class Account3(Account2,RBI):
    pass

class Govt:
    def Viewrules(self):
        return 'govt rules'

class Account4(Account3,Govt):
    pass

class Account5(Account3):
    def __init__(self):
        self.gov=Govt()

class Account6:
    def __init__(self,n):
        self.name=n
    def __add__(self, x):
        return self.name + x.name
    def __str__(self):
        return self.name
    def __len__(self):
        return len(self.name)
    def __iter__(self):
        self.count=0
        return self

    def __next__(self):
        c = self.count
        if c<len(self.name):
            self.count+=1
            return self.name[c]
        else:
            raise StopIteration

from abc import ABC,abstractmethod
class Acccount (ABC):
    def addUser(self, a):
        self.name = a

    @abstractmethod
    def viewUser(self):
        pass

class MyAccount(Acccount):
    def viewUser(self):
        return 'hello'+self.name

cust1 = Account1()
cust2 = Account1()
cust1.addUser('C1')
cust2.addUser('C2')
print(cust1.viewUser())
print(cust2.viewUser())
print(Account1.bank)
print(cust1.name)
print(Account1.bankRules('BLR'))
print(Account1.bankInfo())
print(Account1.viewUser(cust2))



cust3=Account2()
cust3.addUser('C3')
print(cust3.viewUser())
print(Account2.bank)
print(Account2.bankRules('BLR'))
print(Account2.bankInfo())
cust3.Addadhar('a1')
print(cust3.Viewadhar())


cust4=Account3()
print(cust4.Viewrules())
cust4.addUser('c4')

cust5=Account4()
print(cust5.Viewrules())
print(Govt.Viewrules(cust5))


cust6=Account5()
print(cust6.Viewrules())
print(cust6.gov.Viewrules())

cust7=Account6('abc')
cust8=Account6('xyz')
result=cust7+cust8
print(result)
print('cust7=',cust7)
print('length=',len(cust7))
for i in cust7:
    print('i=',i)

#a=Acccount()
b=MyAccount()
b.addUser('B')
print(b.viewUser())