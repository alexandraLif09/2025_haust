#Verkefni 25

from random import randint     #nær í random fallið

aftur = True
while aftur:      #keyrir á meðan breytan (aftur) er True
        #       0         1        2          3         4
    nofn = ["margrét", "díana", "bríet", "isabella", "emma"]
    tala = randint(0,4)   #Velur random tölu  á bilinu 0-4
    #Prenta vinningshafa
    print ("Til hamingju", nofn[tala], "Þú hefur unnið milljón í happdrætti FB!")   #Prentar út hver vann
    print ("Þessir unnu ekkert: ", end="")
    for i in range (0,len(nofn)):   #Gerir jafn oft og listinn er langur (5 sinnum)
        if i != tala:      #Ef i er EKKI jafnt og tala
            print (nofn[i], end="")
            if i<len(nofn)-1:    #Gerir þetta ef að hún hefur ekki prentað síðasta nafnið
                print (",", end="")   #Prentar kommu


    print()   #fylir alltaf end=" "
    sv = str(input("Viltu draga aftur? (j/n): "))
    if sv == "n" or sv == "N":
        aftur = False

