#Verkefni 20

aftur = True
while aftur:

    lengd = int(input("Sláðu inn lengd: "))
    breidd = int(input("Sláðu inn breidd: "))
    haed = int(input("Sláðu inn hæð: "))
    
    print ("Flatarmálið er", lengd*breidd)
    print ("Ummálið er", lengd+lengd+breidd+breidd)
    print ("Rúmmálið er", lengd*breidd*haed)

    sv = str(input("Viltu spila aftur (j/n)? "))
    if sv == "n" or sv == "N":
        aftur = False
print ("Forritið er hætt")
    
