#1
x=3
y=4
if x * y > 10:
    print("Product is large")
else:
    print("Product is small")

#2
a='Python'
if 'y' in a:
    print('Found')
else:
    print('Not fround')

#3
name='Alice'
age=25
print(name,age)

#4
def greet():
    return 'Hi!'
print(greet())

#5
#val='20.5'
#print(int(val))

#6
print(2**3)

#7
a='Python'
b='rocks'
print(a,b,sep='---')

#8
a=[1,2,3]
b=2 in a
print(b)

#9
a='12'
b='8'
#print(a*b)

#10
a='7'
b='3'
print(a*int(b))

#11
x='10'
y=5
print(x*y)

#12
x=5
if x>3:
    print('yes')
else:
    print('no')

#13
x=[1,2,3]
x[0]=10
print(x)

#14
x='Python'
print(x.upper())

#15
x=[5,10,15]
x.append(20)
print(x)

#16
x=10
y=3
print(x%y)

#17
a='12'
b='8'
#print(a*b)

#18
print(5+3)
#19
print(10//2)

#20
x='Hello'+'World'
print(x)

#21
x=3
y="3"
print(x+int(y))

#22
a='11'
b='5'
#print(a*b)

#23
total=0
for i in range(5):
    total+=i
    print(total)

#24
x=5
print(x>3 and x<10)

#25
x='Java'
y='is'
z='cool'
print(x,y,z)

#26
a=[1,2,3,4,5]
b=a[2]=26
print(b)

#27
for i in range(3):
   print(i)

#28
count=0
while count<3:
    print(count)
    count+=1

#29
name='Python'
print(name.upper())

#30
squares=[x**2 for x in range(3)]
print(squares)

#31
x='Hello'
#print(int(x))

#32
x='15'
y=3
#print(x+y)

#33
x=10
y="2"
#print(x**y)

#34
text='apple'
count=3
#print(text/count)

#35
a=[5,10,15]
#print(a[4])

#36
x=5
y='5'
#print(x+y)

#37
a='Hello'
b=2
print(a*b)

#38
x=4.5
y=2
print(x*y)

#39
a='3'
b=int(a)+5
print(b)

#40
a='6'
print(a+a)

#41
a=(1,2)
#a[0]+=1

#42
x='apple'
y=2
#print(x+y)

#43
a=7
b=3
print(a%b)

#44
x=4
if x*2==8:
    print('Match')
else:
    print('Mismatch')

#45
num=7
if num %2==0:
    print('Even')
else:
    print('Odd')

#46
x=15
if x >20:
    print('Greater')
else:
    print('Smaller or Equal')

#47
score=85
if score >=50:
    print('pass')
else:
    print('fail')

#48
y=12
if y <10:
    print('below')
elif y == 12:
    print('equal')
else:
    print('above')

#49
num=10
if num >5:
    print('high')
else:
    print('low')

#50
temp=30
if temp>40:
    print('hot')
elif temp>20:
    print('warm')
else:
    print('cold')

#51
age =18
if age >=18:
    print('adult')
else:
    print('minor')

#52
number=-5
if number>0:
    print('positive')
elif number<0:
    print('negative')
else:
    print('zero')

#53
x=10
if x %5==0:
    print('divisible')
else:
    print('not divisible')

#54
x='coding'
if len(x)>5:
    print('long word')
else:
    print('short word')

#55
x=20
if x >10:
    if x <30:
        print('between 10 and 30')
    else:
        print('above 30')
else:
    print('below 10')

#56
text='programming'
print('gram' in text)

#57
fruit='apple'
#if fruit.startswith('a'):
  #  print('starts with a')
#else:
   # print('doesn't start with a)

#58
x=100
if x >50 and x < 150:
    print('in range')
else:
    print('out of range')

#59
num=10
if num>0:
    print('positive')
elif num <0:
    print('negative')
else:
    print('zero')

#60
x=1
while x <10:
    x*=2
print(x)

#61
n=5
factorial=1
for i in range (1, n+1):
    factorial*=i
print(factorial)


#62
a=3
b=2
if a>b:
    print('a is greater')
else:
    print('b is greater')

#63
value=True
print(not value)

#64
arr=[5,10,15]
arr.insert(1,7)
print(arr)

#65
text='python'
print(text[1:4])

#66
def greet():
    return 'Hi'
print(greet())

#67
a='hello'
b='world'
print(a+b)

#68
a=10
b='20'
#print(a+b)

#69
a='python'
b=3
print(a*b)

#70
a=10
b=0
#print(a//b)

#71
a=[1,2,3]
print(a.index(2))

#72
a=[1,2,3,4]
print(a.pop(2))

#73
a=[1,2,3,4]
print(a.pop())

#74
a=[1,2,3]
a.insert(1,4)
print(a)

#75
x=2
y=3
print(x**y)

#76
a=7
b=2
print(a//b)

#77
language='codinglsfun'
print(language[::-1])

#78
marks=[10,15,20]
marks[1]=12
print(marks)

#79
name='pythonrocks'
#name[5]='s'
#print(name)

#80
count=10
step='5'
print(count+int(step))

#81
total=15
total+=5
print(total)

#82
a=5
b=0
c=[]
if a and b or c:
    print('yes')
else:
    print('no')

#83
a=(5,10,15,20,25)
b=slice(1,4)
print(a[b])


#84
x=10
y=20
x,y=y,x
print(x,y)

#85
x,y=2,10
x*=y*x+1
print(x)

#85
number=(4,7,19,2,89,45,72,22)

sorted_num=sorted(number)
print(type(sorted_num))

#86
x=10
def test():
    global x
    x=20
test()
print(x)

#87
