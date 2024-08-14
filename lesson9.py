a=[1,2,3,4,5,6,7,8,9]
for i in a:
     print(i)

for i in range(len(a)):
    print(a[i])

i = 0
while  i < len(a):
     print(a[i])
     i = i+1
b=[]    
#for x in a:
#     if 'a' in x:
#          b.append(x)
#print(b)

thislist=[1,2,3,4,5,6,7,8,9]
theylist=[]
for i in thislist:
     if  i<5:
          theylist.append(i)
          print(theylist)
