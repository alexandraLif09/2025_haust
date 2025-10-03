#verkefni 13

aftur = True
while  aftur:

    svar = str(input("Viltu reikna summu(s), mismun(m), Margfeldi(M), deilingu(d) eða veldi(v)? "))
    if svar == "s" or svar == "S":
        tala1 = int(input("Sláðu inn tölu 1: "))
        tala2 = int(input("Sláðu inn tölu 2: "))

        print ("Summa þessa talna er: ",tala1+tala2)

    elif svar == "m":
        tala1 = int(input("Sláðu inn tölu 1: "))
        tala2 = int(input("Sláðu inn tölu 2: "))

        print ("mismunur talnana er: ",tala1-tala2)

    elif svar == "M":
        tala1 = int(input("Sláðu inn tölu 1: "))
        tala2 = int(input("Sláðu inn tölu 2: "))

        print ("Margfeldi talnana er: ",tala1*tala2)

    elif svar == "d" or svar == "D":
        tala1 = int(input("Sláðu inn tölu 1: "))
        tala2 = int(input("Sláðu inn tölu 2: "))

        print ("deiling talnana er: ",tala1/tala2)

    elif svar == "v" or svar == "V":
        tala1 = int(input("Sláðu inn tölu 1: "))
        tala2 = int(input("Sláðu inn tölu 2: "))

        print ("veldi talnana er: ",tala1**tala2)

    else:
        print ("Villa")

    sv=str(input("Viltu prófa aftur? (j/n) "))
    if sv == "n" or sv == "N":
        aftur = False

    if sv == "j" or sv == "J":
        
        aftur = True

    
