#Verkefni 41

file = open("nofn (3).txt")
listi1 = []
listi2 = []
for line in file:   
    word = line.strip()
    fjoldi = word.count(" ")
    if len(word) > 30:
        listi1.append(word)
    if fjoldi == 3:
        listi2.append(word)
        
print (listi1)
print (len(listi1))
print (listi2)
print (len(listi2))
