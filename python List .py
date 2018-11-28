#list

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[2:3])

for alist in thislist:
    print(alist)

print('---------------only number add------------\n')
sum=0
number=[10,5,30,'rumman',15]
for anum in number:
    if type(anum)==int :
        sum+=anum
print(sum)

print('--------------- add- list-----------\n')
number1=[10,5,30,'rumman',15]
print(number1)
number1[1]=20
print(number1)

#add
number1.append("rana")
print(number1)

#postition onujayi add
number1.insert(2,10)
print(number1)
#delete
del number1[0]
print(number1)

#list theke kono item out kore niye asa and delete
print('--------------- -----------\n')
row=[10,5,3,5,4]
row1=row.pop()#last item
print(row)
print(row1)
#value delete
row.remove(10)
print(row)

print('---------------String to list convert -----------\n')
import  re
car="famous car, dhaka ,bangladesh"
car_info=re.split(',',car)
print(car_info)

#join list as a string
car_info_join=' '.join(car_info)
print(car_info_join)

#lenth
print(len(car_info))
sortList=['a','b','c']
print(sorted(sortList))
sortList.reverse()
print(sortList)

if 'b' in sortList:
    print ('found')