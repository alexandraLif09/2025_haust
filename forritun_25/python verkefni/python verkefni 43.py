#Verkefni 43

aftur = True
while aftur:
    FB = "Fjölbrautaskólinn í Breiðholti"
    MK = "Menntaskólinn í Kópavogi"

    print (FB[0:18]+MK[-10:])

    print("....................................")

    nafn = "Alexandra Líf Adolphsdóttir"

    for n in nafn:
        print(n, "+", end = " ")
    print()

    for i in range (len(nafn),0, -1):
        print (nafn[i-1], end="")
    print()

    print("....................................")
    skoli = str(input("Í hvaða skóla ertu í? "))
    while skoli != "FB":
        skoli = str(input("Í hvaða skóla ertu í? "))
        if skoli == "FB":
            print ("Rétt!")

    print("....................................")

    svar = str(input("viltu keyra forritið aftur? "))
    if svar == "já" or svar == "já" or svar == "JÁ":
        aftur = True
    else:
        aftur = False
print ("Forritið er búið")
