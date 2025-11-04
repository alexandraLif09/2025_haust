#Verkefni 32
#hluti 1
print ("'''''''''''Liður 1'''''''''''")
file = open("words (1).txt")

for line in file:   #fyrir hverja línu í skránni
    word = line.strip() #eyðir öllum aukamerkjum t.d. Enter
    if len(word)>20:     #ef lengdin á nafninu er lengra en 20 stafir
        print (word)    #þá prentast það út

#hluti 2
print ("'''''''''''Liður 2'''''''''''")
file = open("words (1).txt")
nafn = str(input("Sláðu inn nafn sem þú vilt leita að: "))  #slá inn leitarstreng
for line in file:  #fyrir hverja línu í skránni
    word = line.strip() #eyðir öllum aukamerkjum t.d. Enter
    if nafn in word:    #ef nafnið er í word
        print(word)


#hluti 3

print ("'''''''''''Liður 3'''''''''''")
file = open("words (1).txt")
leita = str(input("Sláðu inn nafn sem þú vilt leita að: ")) #slá inn leitarstreng
teljari = 0
for line in file:   #fyrir hverja línu í skránni 
    word = line.strip()     #eyðir öllum auka merkjum t.d. Enter
    for stafur in word:     #fer í gegnum orðið staf fyrir staf
        if stafur == leita: #ef stafurinn er sá sami og í leit
            teljari += 1    # þá hækkar teljari um 1
print ("Stafurinn fannst",teljari,"sinnum í skránni")   #prentar út niðurstöðu
