name="rumman islam nur"
age=20
print(name)

#vagfol and vagshesh ber korte
x=7
y=3
z=divmod (x, y)
print(z)

#----------------------power
p=2
q=p**4
r=pow(p,4)
print(q)
print('-------------------------\n')



list=[10, 5, 2, 3, 'rumman', 10]
print(list)
print(list[2:5])

#tuple shudu read kora jay
tuple=(10, 5, 2, 3, 'rumman', 10)
print(tuple.count(tuple))


#array marge
array1={'a': 10, 'b': 20}
array2={'c': 10, 'd': 20}
array1.update(array2)
print(array1)

#loop in pythn
for i in array1:
    print (i)
    print(array1[i])


# string print like array
rana="Rana sharkar"
print(rana[0],rana[2] ,rana[-1])

print("----------------\nCamel Case : "+rana.title())
print(rana.upper())
print(rana.lower())

#speace remove
print('-----------------\n')
s="    md       "
print('_'+s+'_')
print('_'+s.lstrip().rstrip()+'_')
print('_'+s.strip()+'_')


#word find
print('------------------\n')
findS="we live in an age"
print(findS.find('an'))
print(findS.find('gsdfds'))

print(findS.replace('an','ann'))
print(findS)


#string interpolation

person="{name} age is {age}"
print(person.format(name='rana',age=20))