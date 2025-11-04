#Verkefni 33

print ("'''''''''''Liður 1'''''''''''")
file = open("words (1).txt")
teljari = 0 
for line in file:
    word = line.strip()
    for stafur in word:
        if stafur == 'e':
            teljari -= 1
        else:
            teljari += 1
print ("Stafurinn E er ekki í", teljari, "orðum")
