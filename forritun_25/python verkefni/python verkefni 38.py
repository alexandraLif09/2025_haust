#Verkefni 38

def summa():
    samtals = 0
    for i in range(0, len(listi)):
        samtals += listi[i]
    return samtals

def safntidni():
    summ = 0
    safn = []
    for i in range (0, len(listi)):
        summ += listi[i]
        safn.append(summ)
    return safn

def rada():
    listi.sort()
    return listi



listi = []
svar = int(input("Hvað villtu slá inn margar tölur? "))
for i in range(0, svar):
    listi.append(int(input("Sláðu inn tölu ")))
print (listi)
print ("Summan er: ", summa())
print ("Safntíðnin er: ", safntidni())
print ("listinn raðaður: ", rada())
