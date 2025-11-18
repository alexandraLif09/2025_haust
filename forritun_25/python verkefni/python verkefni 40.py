#verkefni 40

listie = []
listi3a = []

file = open("nofn (3).txt")     
listi = []         
for line in file:   
    word = line.strip()     
    if "e" in word.lower():
        listie.append(word)
    if "a" in word[2]:
        listi3a.append(word)
        (len(word) > 2)

print("Nöfnin sem innihalda stafinn e eru:", len(listie))
print (listi3a)
print ("Fjöldi nafna sem eru með a sem þriðja staf er:", len(listi3a))
