#1
x='python'
#print(y)


#2
a=[1,2,3]
b=a
b[0]=5
print(a)
print(b)


#3
a=[1,2,3]
b=a
b.append(4)
print(a)


#4
print(type(5/2))
print(type(5//2))


#5
x1=[10,11,12,13,14]
x2=x1[::-1].append(15)
print(x2)

#6
s=[x**2
   for x in range(3)]
print(s)

#7
def greet(name):
 return 'hello, '+ name 
print(greet('Alice'))

#8
s=[x for x in
   range(5)if x % 2==0]
print(s)

#9
s={1,2,2,3}
print(len(s))

#10
x='Suna'
print('x')