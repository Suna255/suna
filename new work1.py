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
#print(s)

#9
#s={1,2,2,3}
print(len(s))

#10
x='Suna'
print('x')

#11
s=[]
s.append(9)
print(s)

#12
result=0
for i in range(5):
    result += 2 * i
print(result)

#13
list1=[1,2,3]
list2=list1
list2.append(4)
print(list1)

#14
def func(*args):
 print(len(args))
func(1,2,3,4)

#15
nums=[10,20,30]
nums[1]=25
print(nums)

#16
data= {"x":10,
       "y":20,"z":30}
print(len(data))
      
#17
s="Machine Learning"
print('Learn' in s)

#18
#def func(a,b):
 #return a/0
#print(func(4,2))

#19
a={1,2,3}
#a[0]=4
print(a)

#20
x='python'
#print(y)

#21
s=[1,2,3]
s+4