#Verkefni 18

aftur = True
while aftur:

    linur = int(input("Hvað viltu skrifa margar línur?: "))
    for i in range(0,linur):
        print ("X" * 30)

    sv = str(input("Viltu spila aftur? (j/n): "))
    if sv == "n" or sv == "N":
        aftur = False
print ("Forritið er hætt")
