a=[1,2,3]
b=a[:]
b[0]=5
print(a)
print(b)  #cavab c

x1=[10,11,12,13,14]
x2=x1[::-1].append(15)
print(x2) #cavab c

print(type(5/2))
print(type(5//2)) #c

a=[1,2,3]
b=a
b.append(4)
print(a) #a

x=3
y='3'
print(x==y) #false

x=[1,2,3]
print(sum(x)) #b

print((4**2)%3) #1

print(10//3) #3

x=[0,1,2,3,4]
x[1:4]=[9,8,7]
print(x) #b

a=9
b=18
a=a+(b!=a)
print(a) #a


#1 
i=1
while i<=10:
    print(i)
    i+=1
#bizden 10 dongusunu istedi <= istifade etdim. bu isare i deyisenini 10 qeder dovr edecek.
#sonda ise her defe bir vahid artsin deye i+1 yazmisdim amma kod sehv oldu sonsuz 1 verdi cavabi.
#men ise ele kod yazmali idim ki 10 qeder reqemler bir bir arta arta yazilsin.
#buna gorede deyisen +
