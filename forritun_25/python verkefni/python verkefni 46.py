#Verkefni 46

def valmynd():
    print("....................................")
    print()
    print('1: Bæta vöru á innkaupalistann')
    print('2: Eyða vöru af innkaupalistanum')
    print('3: Prenta innkaupalista')
    print('4: Hætta')
    print()
    print("....................................")


def baeda():
    aftur = True
    while aftur:
        listi.append(str(input("Hvaða vöru viltu bæta inná innkaupalistann? ")))
        svar = str(input("Viltu bæta við annari vöru? (j/n) "))
        if svar == "n" or svar == "N":
            aftur = False

def eyda():
    aftur = True
    while aftur:
        svar = False
        vara = (str(input("Hvaða vöru viltu eyða af innkaupalistanum? " )))
        for i in range(0, len(listi)):
            if listi[i] == vara:
                del listi[i]
                svar = True
        if svar == False:
            print ("Vara fannst ekki")
        sv = str(input("Viltu eyða annari vöru (j/n) "))
        if sv == "n" or sv == "N":
            aftur = False

def prenta():
    print("Þetta er innkaupalistinn:")
    for l in listi:
        print(l)


listi = []
aftur = True
while aftur:
    valmynd()
    val = int(input("Veldu tölu frá 1 - 4: "))
    if val == 1:
        baeda()
    elif val == 2:
        eyda()
    elif val == 3:
        prenta()
    elif val == 4:
        aftur = False
    else:
        print ("Þú valdir ekki rétt")
print ("Forritið búið")
