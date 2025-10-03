#verkefni 13

aftur = True
while  aftur:

    svar = str(input("Viltu reikna summu(s), mismun(m), Margfeldi(M), deilingu(d) eða veldi(v)? "))
    if svar == "s" or svar == "S":
        s = int(input("Hvaða tölu viltu reikna? "))
        for i in range (1,21):
            print (s,"+",i,"=",s+i)

    elif svar == "m":
        m = int(input("Hvaða tölu viltu reikna? "))
        for i in range (1,21):
            print (m,"-",i,"=",m-i)

    elif svar == "M":
        M = int(input("Hvaða tölu viltu reikna? "))
        for i in range (1,21):
            print (M,"*",i,"=",M*i)

    elif svar == "d" or svar == "D":
        d = int(input("Hvaða tölu viltu reikna? "))
        for i in range (1,21):
            print (d,"/",i,"=",d//i)

    elif svar == "v" or svar == "V":
        v = int(input("Hvaða tölu viltu reikna? "))
        for i in range (1,21):
            print (v,"í veldinu",i,"=",v**i)

    else:
        print ("Villa")

    sv=str(input("Viltu prófa aftur? (j/n) "))
    if sv == "n" or sv == "N":
        aftur = False

    if sv == "j" or sv == "J":
        aftur = True
