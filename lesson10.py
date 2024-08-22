a=8
if a>1:
    print('a 1 den boyukdur')
else:
    print('a 1 den kicikdir')


a=8
if a>1:
    print('a 1 den boyukdur')
elif a == 1:
    print('a 1 e beraberdir')
else:
    print('a 1 den kicikdir')

+-b=40
if b>20:
    print('b 20 den boyukdur')
    if b>30:
        print('b 30 dan da boyukdur')


    list1=['apple','banana','cherry']
    for x in list1:
        print(x)
        if x == 'banana':
            break

        for x in list1:
            if x == 'banana':
                continue
            print(x)
            

adj=['red', 'big','tasty']
list3=['apple','banana','cherry']

for x in adj:
    for y in list3:
        print(x,y)