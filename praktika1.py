#rows=5
#for i in range(rows ,0,-1):
   # for j in range (0,i ):
  #      print('* ', end="")
   # print("\3")




#alt alta verir
#rows=5
#for i in range(rows ,0,-1):
 #   for j in range (0,i ):
 #       print('* ', end="")
  #  print("\t")


import random
a=int(input('reqem daxil edin:'))
b=random.randrange(1,10)
while b!=a:
 if a>b:
  print('texminimiz boyukdur')
  a=int(input('reqem daxil edin:'))
 elif b>a:
  print('texminimiz boyukdur')
  a=int(input('reqem daxil edin:'))
 else:
  break
print('texmininiz dogrudur.')
