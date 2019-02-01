for char in "UMSS":
    print(char)

for li in ["U","M","S","S"]:
    print(li)

T = ("Alejandrina", "Jimenez", "UMSS", 2019)
for t in T:
    print(T.index(t),t)

D = {"nombre":'Alejandrina','universidad':"UMSS"}
for k,v in D.items():
    print(k,v)
for k in D:
    print(k)