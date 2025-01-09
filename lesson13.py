Suna=('apple', 4, 'banans', True,33,77)
list1=list(Suna)
print(list1)
list1.append('salam')
print(list1)
Suna=tuple(list1)
print(Suna)

tuple1=('apple', 4, 'banans', True,33,77)
tuple2=('salam',7,False)
print(tuple1+tuple2)
#print(tuple1*tuple2)
s=tuple1 *2
print(s)

fruits=('apple','mango','papaya','pineapple','cherry')
(green,tropic, *red)=fruits
print(green)
print(tropic)
print(red)

tuple1=('apple', 4, 'banans', True,33,77)
for i in tuple1:
    print(i)

tuple1=('apple', 4, 'banans', True,33,77)
