#Verkefni 19

aftur = True
while aftur:

    tala = int(input("Sláðu inn mánuð í tölustöfum (1-12): "))

    if tala==1:
        print ("Janúar")
    elif tala==2:
        print ("Febrúar")
    elif tala==3:
        print ("Mars")
    elif tala==4:
        print ("Apríl")
    elif tala==5:
        print ("Maí")
    elif tala==6:
        print ("Júní")
    elif tala==7:
        print ("Júlí")
    elif tala==8:
        print ("Ágúst")
    elif tala==9:
        print ("September")
    elif tala==10:
        print ("Október")
    elif tala==11:
        print ("Nóvember")
    elif tala==12:
        print ("Desember")
    else:
        print ("Villa")
    
    

    sv = str(input("Viltu spila aftur? (j/n): "))
    if sv == "n" or sv == "N":
        aftur = False
print ("Forritið er hætt")
