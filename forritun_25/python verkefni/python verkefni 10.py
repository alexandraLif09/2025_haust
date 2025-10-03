#verkefni 10

aftur = True
while aftur:

    tafla = int(input("Hvaða töflu viltu reikna? "))
    for i in range (1,11):
        print (tafla,"x",i,"=",tafla*i)

    sv= str(input("Viltu prófa aftur? (j/n) "))
    if sv == "n" or sv == "N":
        aftur = False
