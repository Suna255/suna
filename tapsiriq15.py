## thisset = {1, "salam" , 52 , True, "0"} setinin uzunluqunu teyin etmek 
a= {1, "salam" , 52 , True, "0"}
print(len(a))
print(a)

## thisset = {1, "salam" , 52 , True, "0"} setine 0 ve false deyerleri daxil edib uzunlugunu cap etmek 
a= {1, "salam" , 52 , True, "0"}
a.add(0)
a.add(False)
print(len(a))

## her-hansi iki seti birlesdirmek
a= {1, "salam" , 52 , True, "0"}
b={2,True,'hello',5,8,False}
c=a.union(b)
print(c)

## setden element silmek 
a= {1, "salam" , 52 , True, "0"}
a.remove(1)
print(a)

## setin daxilindeki butun elementleri silmek 
a= {1, "salam" , 52 , True, "0"}
a.clear()
print(a)

## setdeki butun elementleri cap etmek 
a= {1, "salam" , 52 , True, "0"}
print(a)