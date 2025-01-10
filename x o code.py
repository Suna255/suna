rows=8
cols=8
for i in range(rows):
    for j in range(cols):
        if (i+j)%2==0:
            print('X', end=" ")
        else:
            print('O',end=" ")
    print()