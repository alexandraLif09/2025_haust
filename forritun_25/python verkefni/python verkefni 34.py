#Verkefni 34

print ("'''''''''''Liður 1'''''''''''")
nafn = str(input("Hvaða nafn viltu leita að? "))
satt = False
file = open("nofn_v34.txt")
for line in file:
    word = line.strip()
    if nafn in word:    #Ef nafnið sem við slóum inn er í línunni sem er lesin
        print ("Nafnið", nafn, "er í skránni")
        satt = True
if satt == False:   #Ef hún hefur ekki fundið orðið
    print ("Nafnið fannst ekki í skránni")

print ("'''''''''''Liður 2'''''''''''")
teljari_max = 0     #teljari sem geymir lengsta orðið
teljari_min = 1000  #teljari sem telur stysta orðið
file = open("nofn_v34.txt")
for line in file:
    word = line.strip()
    if len(word) > teljari_max: #Ef að orðið er stærra en talan í teljari_max
        teljari_max = len(word)
    if len(word) < teljari_min: #Ef að orðið er minna en talan í teljari_max
        teljari_min = len(word)
print ("Lengsta nafnið er", teljari_max, "stafir á lengd")
print ("stysta nafnið er", teljari_min, "stafir á lengd")

print ("'''''''''''Liður 2'''''''''''")
file = open("nofn_v34.txt")
for line in file:
    word = line.strip()
    if len(word) == teljari_max:
        print ("Þetta er lengsta orðið", word)
    elif len(word) == teljari_min:
        print ("Þetta er stysta orðið", word)
