#set duplicate item nay na
num_set=set()
num_set.add(20)
num_set.add(200)
num_set.add(30)
num_set.add(20)
print( num_set)

set_a={1,5,10,3,5}
set_b={11,5,100,31,5}

print('A - B =',set_a - set_b)
print('A | B =',set_a | set_b)
print('A & B =',set_a & set_b)
print('A ^ B =',set_a ^ set_b)

setCountry={'bangladesh', 'india', 'uk'}
country='india'
if country in setCountry:
    print(country.title(),'Exists')