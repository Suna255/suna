## 1 thistuple = ("salam" , 42 ,True , "hi") tupllenin sonuna 21 reqemini elave etmek 
tuple1=("salam" , 42 ,True , "hi") 
Suna=list(tuple1)
Suna.append(21)
tuple1=tuple(Suna)
print(tuple1)

## 2 thistuple = ("salam" , 42 ,True , "hi") tuple-in ortasına alma sozunu elave etmek 
tuple2= ("salam" , 42 ,True , "hi")
Lale=list(tuple2)
Lale.insert(2,'alma')
tuple2=tuple(Lale)
print(tuple2)

## 3 thistuple = ("salam" , 42 ,True , "hi") birinci elementi sagol ile deyismek 
tuple3=("salam" , 42 ,True , "hi")
Resad=list(tuple3)
Resad[0]='sagol'
tuple3=tuple(Resad)
print(Resad)

## 4 thistuple = ("salam" , 42 ,True , "hi") True-ni silmek 
tuple4=("salam" , 42 ,True , "hi")
money=list(tuple4)
money.pop(2)
tuple4=tuple(money)
print(tuple4)

## 5 thistuple = ("salam" , 42 ,True , "hi" , False, 91 , 33 , "alma") tuple-ni ele 3 hisseye bolmek ki ilk hissede daha cox element olsun 
tuple5= ("salam" , 42 ,True , "hi" , False, 91 , 33 , "alma")
length=len(tuple5)
print(birinci)
print(second)
print(ucuncu)

## thistuple = ("salam" , 42 ,True , "hi") tuple-nin elementlerini ayri ayri cap etmek 
tuple6=("salam" , 42 ,True , "hi")
for suna in tuple6:
    print(suna)

## thistuple = ("salam" , 42 ,True , "hi") tuplenin elementlerini 4 defe tekrar eletdirmek (tuple icinde)
tuple7=("salam" , 42 ,True , "hi")
suna=tuple7*4
print(suna)