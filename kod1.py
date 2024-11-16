a=input('Metn daxil edin')
boyuksozler="".join (a.lower().split())
tersmetn=boyuksozler[::-1]
if boyuksozler==tersmetn:
    print('bu soz polonormdu')
else :
    print('bu soz polonorm deyil')