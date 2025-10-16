#Verkefni 28

aftur = True
while aftur:
    strengur =str(input("sláðu inn streng: "))  #Slá einn einhvern streng
    stafur = str(input("Sláðu inn staf sem þú vilt leita að: "))
    teljari = 0
    for i in strengur:      #Les í gegnum strenginn staf fyrir staf
        if i == stafur:     #Ef stafurinn er sá sami og leitarstafurinn
            teljari+= 1     #teljari hækkar um 1 sama og teljari=teljari+1

    #Prentar niðurstöðu
    print ("strengurinn er", strengur, "og stafurinn", stafur,"kemur", teljari,"fyrir í röðinni.")
    print (strengur[::-1])  #prentar út strenginn öfugt

    #Athuga hvort spilarar vilja byrja upp á nýtt
    breyta = str(input("Viltu spila aftur (j/n)? "))
    if breyta == "n" or breyta == "N":
        aftur = False
