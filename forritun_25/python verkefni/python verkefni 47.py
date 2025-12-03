#Verkefni 47

listi = []
svar = int(input("Hvað viltu slá inn margar tölur? "))
for i in range(0, svar):
    listi.append(int(input("Sláðu inn tölu: ")))

#Aðferð 1

summa = 0
for tala in listi:
    summa += tala
print ("Meðaltal talnanna er: ", round(summa/len(listi), 2))


#Aðferð 2
medaltal = sum(listi)/len(listi)
print ("Meðaltal talnanna er: ", round(medaltal, 2))
