#Verkefni 27

from random import randint
aftur = True
while aftur:        #Keyrir á meðan breytan aftur er True
    samtals1 = 0    #Samtals stig fyrir spilara 1
    samtals2 = 0    #Samtals stig fyrir spilara 2
    running = True  #Breyta sem er True á meðan spilari vill spila áfram
    spilari1 = 'j'  #Breyta sem er j ef spilari 1 vill halda áfram að spila
    spilari2 = 'j'  #Breyta sem er j ef spilari 2 vill halda áfram að spila

    while running == True:
        if spilari1 == 'j':     #Ef spilari 1 er j þá heldur hún áfram
            tala1 = randint(1,13)   #Velur tölu frá 1 - 13
            samtals1 = samtals1 + tala1     #Leggu töluna við samtals stig
            print ("Spilari 1 fékk: ",tala1)    #Prentar út hvaða tölu spilari 1 fékk

        if spilari1 == 'j':     #Ef spilari 2 er j þá heldur hún áfram
            tala2 = randint(1,13)   #Velur tölu frá 1 - 13
            samtals1 = samtals2 + tala2     #Leggu töluna við samtals stig
            print ("Spilari 1 fékk: ",tala2)    #Prentar út hvaða tölu spilari 2 fékk

        print ("Spilari 1 er nú kominn með ",tala1)     #prentar út hvaða tölu spilari 1 er með samtals
        print ("Spilari 2 er nú kominn með ",tala2)     #prentar út hvaða tölu spilari 2 er með samtal

        if samtals1<21 and samtals2<=21:
            if spilari1 == "j":     #Ef spilari1 er =j þá gerir hún næstu línu
                spilari1 = str(input("Vill spilari 1 draga aftur? "))   #Spyr hvort spilari 1 vilji draga nýtt spil og setur í breytuna svar1
            if spilari2 == "j":     #Ef spilari2 er =j þá gerir hún næstu línu
                spilari2 = str(input("Vill spilari 2 draga aftur? "))   #Spyr hvort spilari 2 vilji draga nýtt spil og setur í breytuna svar2

        #Athugar hvort einhver sé kominn yfir 21 og er sprunginn

        #Ef báðir springa
        if samtals1>21 and samtals2>21:
            print ("BúmmBúmm báðir sprungu. jafntefli")
            running = False     #Til að stoppa spilið þar sem það er búið
        #Ef spilari 1 springur
        elif samtals1>21:
            print ("Spilari 1 sprak. Spilari 2 vann")
            running = False     #Til að stoppa spilið þar sem það er búið
        #Ef spilari 2 sprengur
        elif samtals2>21:
            print ("Spilari 2 sprakk. Spilari 1 vann")
            running = False     #Til að stoppa spilið þar sem það er búið

        #Ef báðir vilja ekki draga fleiri spil
        if spilari1 == "n" and spilari2 == "n":

            #Jafntefli
            if samtals1 == samtals2:
                print ("Jafntefli")
                running = False     #Til að stoppa spilið þar sem það er búið

            #Ef spilari1 er með hærri tölu
            elif samtals1>samtals2:
                print ("Spilari 1 vann")
                running = False     #Til að stoppa spilið þar sem það er búið

            #Ef spilari2 er með hærri tölu
            elif samtals1<samtals2:
                print ("Spilari 2 vann")
                running = False     #Til að stoppa spilið þar sem það er búið

        #Athugar hvort spilarar vilja byrja upp á nýtt
        breyta = str(input("Viltu spila aftur (j/n)? "))
        if breyta == "n" or breyta == "N":
            aftur = False

print ("Takk fyrir að spila")
