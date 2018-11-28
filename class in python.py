class User:
    pass
obj1=User()

obj1.firstName='rumman'
obj1.lastName='islam nur'
print(obj1.firstName)
#-----------------------------------------
class UserInfo:
    def __init__(self):
        print("constractor")
        pass
obj2=UserInfo()


#===================
class x:
    name='a'
    name2='b'
    def show(self):
        print(self.name, self.name2)
x=x()
x.show()


#----------------------------------------------
print('\n------------------------')
class UserInfo1:
    def __init__(self,firstName,lastName):
        self.fName=firstName
        self.lName=lastName
        print("constractor "+self.fName)
        pass
obj3=UserInfo1('rumman','islam')
print(obj3.lName)