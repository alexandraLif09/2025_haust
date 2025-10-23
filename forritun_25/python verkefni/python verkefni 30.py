#Verkefni 30

listi1 = ["hundur", "köttur", "hestur", "kanína", "svín", "rotta", "ormur", "refur", "ljón", "hæna"]    #býr til lista með 10 dýrum
listi2 = []     #bý til tóman lista
teljari1=0
teljari_stafir=0

for i in range (0,5):   #gerir þetta 5 sinnum
    listi2.append(str(input("Sláðu inn nýja dýrategund: ")))    #bætir 5 nýjum dýrum í lista 2

for x in listi1:    #gerir þetta jafn oft og fjöldi dýra á lista 1 (10 sinnum). x verður heiti á dýri
    for y in listi2:    #gerir jafn oft og fjöldi dýra á lista 2 (5 sinnum). y verður heiti á dýri
        if x == y:  #ef dýr á lista 1 er það sama og á lista 2
            teljari1+=1     #hækkar teljarann um 1
print ("Sama dýrið kom", teljari1, "sinnum fyrir í báðum listunum") #prentar út niðurstöðuna

for dyr in listi1:  #les í gegnum allann listann 
    teljari_stafir+=len(dyr)    #telur stafafjöldan í hverju dýri og bötir því við niðurstöðina
print ("Það eru", teljari_stafir,"stafir í dýralistanum")   #prentar út niðurstöðuna

