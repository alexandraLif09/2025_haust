#Verkefni 34

print ("'''''''''''Liður 1'''''''''''")
file = open("nofn_v34.txt")
nafn = str(input("Hvaða nafn viltu leita að? "))
for line in file:
    word = line.strip()
    for name in word:
        if nafn in word:
            print ("Nafnið er í skránni")
        else:
            print ("Nafnið er ekki í skránni")
