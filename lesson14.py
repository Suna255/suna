a={4,6,3,8,1,2,9}
print(a)
b={True,5,'hello',False,7}
print(b)
a={2,5,7,9}
for i in a:
    print(i)

print(5 not in  a)
a.add(8)
print(a)

a={4,6,3,8,1,2,9}
b={True,5,'hello',False,7}
a.update(b)
print(a)
a.remove(6)
print(a)
c=a.union(b)
print(c)