tp=10,3,'rana'
print(tp,type(tp))

#tuple seperate
x,y,z=tp  #value dorkar na thakle _ dite hoy
print(x,y,z ,sep=' | ')

#dictoranry key value parir
dic={}
dic[10]='rana'
dic['a']=10
print(dic['a'])

print('------------------------\n')
dic1={'rana':20,10:5}
print(dic1[10])
for k,v in dic1.items():
    print(k,v,sep='=>')
