a={
    "yas" :20 ,
    "name" :"Nuray",
    "ixtisas": "praqramci"
}
#deyeri deyismek ucun
a["yas"]=23
print(a)

a.update({"yas":23})
print(a)

a["mekan"]="London"
print(a)

#a.pop()
#print(a)

#a.popitem()
print(a)

#a.clear()
print(a)

for i in a:
    print(a)

b=a.copy()
print(b)

b=a.copy("mekan")
print(b)