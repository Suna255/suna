operator=input('Operator daxil edin:')
num1=float(input('Birinci ededi daxil edin:'))
num2=float(input('ikinci ededi daxil edin:'))
if operator=='+':
    netice=num1+num2
elif operator=='-':
    netice=num1-num2
elif operator=='*':
     netice=num1*num2
elif operator=='/':
    netice=num1/num2
else:
    print('operatoru duzgun daxil etmemisiz!')
print('Sizin neticeniz:', netice)