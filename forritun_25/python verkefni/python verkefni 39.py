#Verkefni 39

listi1 = ["Vigdís", "Alex", "Tristan", "Helena", "Katrín"]
listi2 = ["Erlings", "Hlyns", "Stefáns", "Hlífs", "Leifs"]

for i in range (0, len(listi1)):
    for x in range (0, len(listi2)):
        print (listi1[i], listi2[x])

print ("...............................")

for i in listi1:
    for x in listi2:
        print (i, x)
