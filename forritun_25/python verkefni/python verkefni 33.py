#Verkefni 33

print ("'''''''''''Liður 1'''''''''''")
counter = 0     #telur hvað mörg orð inni halda EKKI stafinn E
ecounter = 0    #telur hvað mörg orð inni halda stafinn E
wordcounter = 0 #telur fjölda orða 
file = open("words (1).txt")
for line in file:
    word = line.strip()
    wordcounter += 1
    if 'e' not in word:
        counter += 1
    if 'e' in word:
        ecounter += 1

print ("Stafurinn e er ekki í", counter,"orðum")
print ("%.0f"%((ecounter/wordcounter)*100) + "% orða innihalda stafinn E")
print ("orðin eru", wordcounter, "í heildina")

print ("'''''''''''Liður 2'''''''''''")
leita = str(input("Sláðu inn einhverja bókstafi: "))
bcounter = 0
file = open("words (1).txt")
for line in file:
    word = line.strip()
    fann = False
    for stafur in leita:
        if stafur in word:
            fann = True
    if fann == False:
        bcounter += 1

print ("Orðin sem ekki innihaldastafina", leita, "eru", bcounter, "talsins")


print ("'''''''''''Liður 3'''''''''''")
stafir_counter = 0
file = open("words (1).txt")
for line in file:
    word = line.strip()
    for stafur in word:
        stafir_counter += 1
print ("Það eru", stafir_counter, "stafir í öllu skjalinu")
