#1
#list ve tuple ikiside deyisenleri gosterir.Ferqleri ise liste deyisen elave edeib silmek olur.Tuple ise olmur.list []
#tuple ().

#2
## tup_1 = ("alma" , 4 , True , 32 , "salam" , 0) tupleinda almadan 32 e qeder elementleri cap etmek 
tup_1=('alma', 4, True, 32, 'salam',0)
print(tup_1[0:3])

#3
## tup_1 = ("alma" , 4 , True , 32 , "salam" , 0) tupleinda sondan 3 elementi cap etmek 
tup_1=('alma', 4, True, 32, 'salam',0)
print(tup_1[-3:])

#4
# ## tup_1 = ("alma" , 4 , True , 32 , "salam" , 0) tupleinda sonuncu elementi cap etmek
tup_1=('alma', 4, True, 32, 'salam',0)
print(tup_1[-1])

#5
## tup_1 = ("alma" , 4 , True , 32 , "salam" , 0) tuplenin uzunlugunu 2 e vurmaq 
tup_1=('alma', 4, True, 32, 'salam',0)
print(len(tup_1)*2)