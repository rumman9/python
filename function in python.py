#function
def welcome():
    print("first function")
    for x in range(0,10):
        print("hi ",str(x))
#calling
welcome()

def welcome1(name,lname,middleName=" "):
    fname=name
    lastName=lname
    fullName=fname+' '+middleName+" "+lastName
    print("first function "+fullName)
welcome1("rana","islam", 's')
