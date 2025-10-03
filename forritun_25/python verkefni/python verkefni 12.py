#Verkefni 12

from random import randint
aftur=True
while aftur:
    for i in range (1,14):
        tala = randint(1,3)
        
        if tala == 3:
            print ("leikur",i,"=> X")
        else:
            print ("Leikur",i,"=>",tala)

    sv=str(input("Viltu prófa aftur? (j/n) "))
    if sv == "n" or sv == "N":
        aftur = False
print ("Forritið búið")
