theylist=[5,22,10,49,58,2,9,100,6,13] 
itislist=[]
for i in theylist:
    if i>10:
         itislist.append(i)
print(itislist)


list1234576576 = [2,4,6,8,10,12,14,16,18,20]
[print (i*2) for i in list1234576576]
print(list1234576576)


listm = [2,4,6,8,10,12,14,16,18,20]
theylist=[x*2 for x in listm]
print(theylist)


listold = [2,5,6,10,11,13,16]
listnew= [x //2  for x in listold]
print(listnew)


a = ["school","class","university","bachelor","book","student"]
b=[]
for x in a:
     if 'c' not in x:
        b.append(x)
     print(b)
