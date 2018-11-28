

def Info(x,y):
    return x/y
print( Info(20,10) )
#print( Info(4,0)) #gives error

#so we use try catch

def Info1(x,y):
    try:
        result= x/y
    except Exception as e :
        return "This is an error message! ",e
    finally:
        print('success')
    return result
print( Info1(4,0) )