#1
i=1
while i <10:
    if i in range(1,11,2):
        pass
    print(i)
    i=i+3
    #burda bizden 10 daxilinde i her defesinde 3 3 artmasini istiyirdi. cavab 1 3 7 oldu.
    #10 icinde 3 dene 3 var. bu sebebden dovr 3 defe olacaq.pass emri hec bir emeliyyat yerine yetirmir.

#2
i=1
while i <10:
    if i in range(2,11,3):
        break
    print(i)
    i=i+2
    print(i)
#yene bizden 10 daxilinde dovr istiyir.Burda break emri var.O dongunu dayandirmaq ucundur. ve bize i+2 verdiyi ucun.
#i deyiseni her dongude 2 vahid artir. amma cavabinda 3 ededi 2 sdefe tekrar edib anlamadim onu.

#3
i=1
while i <10:
    i+=1
    if i in range(1,11,3):
        break
    print(i)
    i=i+2
 #cavab 2,5,8 yene eyni qaydada bizden dovr gosterir ve 10 daxilinde olanlari 2 vahid artiraraq istiyir. 
#if bizde emeliyyati yerine yetirir amma asagidaki break hemin emeliyyati dayandirir.

#4
i=1
while i<10:
    if i in range(2,11,3):
        break
    i+=2
    print(i)
#cavab 5,3 alindi. yuxaridakilarla eynidir islemler.sadece bir ferqli meqam var bu defe i+=2 yazilib

#5
i=1
while i<10:
    if i in range(2,11,3):
        break
    print(i)
    i=i+2

#6
i=1
while i<10:
    if i in range(1,11,3):
        continue
    print(i)
    i=i+2
#continue esasen dongulerde (for,while) istifade olunur. bu emel iterasiyani dayandirir ve novbetiye kecir

#7
i=1
while i <10:
    if i in range(10,0,-1):
        print(i)
    i=i+3

#8
i=1
while i<10:
    if i in range(1,11,3)
        print(i)
    i=i+2