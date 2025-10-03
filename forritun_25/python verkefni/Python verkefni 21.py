#Verkefni 21

from random import randint
aftur = True
while aftur:

    for i in range (1):
        tala = randint(1,4)

        if tala == 1:
            print ("Það verður rok og rigning á morgun")
        elif tala == 2:
            print ("Það verður sól og blíða á morgun")
        elif tala == 3:
            print ("Það verður þurrt en kalt á morgun")
        elif tala == 4:
            print ("Það verður logn með smá skúrum á morgun")
        else:
            print ("villa")
        
        sv=str(input("Viltu nýja veðurspá? (j/n) "))
        if sv == "n" or sv == "N":
                aftur = False
                print ("Forritið Búið")
