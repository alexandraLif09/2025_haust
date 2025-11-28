#Verkefni 45

def valmynd():
    print("....................................")
    print()
    print('1: Samlagning')
    print('2: Frádráttur')
    print('3: Margföldun')
    print('4: Deiling')
    print('5: Hætta')
    print()
    print("....................................")

def samlag():
    tala1 = int(input("Sláðu inn tölu 1: "))
    tala2 = int(input("Sláðu inn tölu 2: "))
    summa = tala1 + tala2
    print("Summa þessara talna er: ", summa)

def frad():
    tala1 = int(input("Sláðu inn tölu 1: "))
    tala2 = int(input("Sláðu inn tölu 2: "))
    summa = tala1 - tala2
    print("Summa þessara talna er: ", summa)

def margf():
    tala1 = int(input("Sláðu inn tölu 1: "))
    tala2 = int(input("Sláðu inn tölu 2: "))
    summa = tala1 * tala2
    print("Summa þessara talna er: ", summa)

def deiling():
    tala1 = int(input("Sláðu inn tölu 1: "))
    tala2 = int(input("Sláðu inn tölu 2: "))
    summa = tala1 / tala2
    print("Summa þessara talna er: ", round(summa, 2))

aftur = True
while aftur:
    valmynd()
    val = int(input("Veldu tölu frá 1 - 5: "))
    if val == 1:
        samlag()
    elif val == 2:
        frad()
    elif val == 3:
        margf()
    elif val == 4:
        deiling()
    elif val == 5:
        aftur = False
print ("Forritið búið")
