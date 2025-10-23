#Verkefni 26

from random import randint
aftur = True
while aftur:            #Til að spila aftur
    strakur = str(input("Strákur: "))     #Slær inn strákanafn
    stelpa = str(input("Stelpa: "))         #slær inn stelpunafn
    tala = randint(90,100)     #Velur random tölu frá 0-100
    #output
    print("Það eru", str(tala)+"% líkur á að", strakur, "og", stelpa, "byrji saman")    #Prentar líkurnar og prentar random töluna sem tölvan valdi
    kk = len(strakur)//2        #finnur lengdina á nafninu og deilir með 2
    kvk = len (stelpa)//2       #finnur lengdina á nafninu og deilir með 2
    print ("Barnið þeirra mun heita:", strakur[0:kk]+stelpa[kvk:])  #Prentar fyrripartinn af stráka nafnini og seinnipartinn af stelpu nafni
    
    sv = str(input("Viltu prófa aftur? (j/n): "))
    if sv == "n" or sv == "N":
        aftur = False
print ("Takk fyrir að spila!")
