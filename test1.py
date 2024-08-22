i=10
while i>0:
    if i in range(1,10,3):
         print(i)
    i=i-2

s={1,0}
lst=[10,20]
for i in s:
     lst.append(list(s)[i])
print(lst)
 
i=1
while i<10:
    if i in (i%2, i%3):
          print(i)
    i+=1

s={'a',True, 'b',2}
s1=[]
for i in s:
     s1.append(i)
print(s1)
