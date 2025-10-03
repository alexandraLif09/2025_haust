#verkefni 11

aftur = True
while aftur:

    svar = str(input("Viltu reikna margfeldi eða veldi? (m/v): "))
    if svar == "m" or svar == "M":
        m = int(input("Hvaða töflu viltu reikna? "))
        for i in range (1,11):
            print (m,"x",i,"=",m*i)
         
    elif svar == "v" or svar == "V":
        svar = int(input("Hvaða tölu viltu fá í veldi? "))
        for i in range (1,11):
            print (svar,"í veldinu",i,"=",svar**i)

    sv=str(input("Viltu prófa aftur? (j/n) "))
    if sv == "n" or sv == "N":
        aftur = False

    if sv == "j" or sv == "J":
        aftur = True
print ("forritið búið")
