#Verkefni 36

svar = str(input("Skráðu inn eftirnafn: "))   #Slær inn eftirnafn sem á að leita að
file = open("nofn (3).txt")     #opnar skrá
listi = []          #Býr til tóman lista
for line in file:   #les í gegnum allar línurnar í textaskránni
    word = line.strip()     #eyðir stýriskránni úr línu (t.d. enter merkjum)
    listi = word.split(" ")     #splittar nöfnum upp og setur þau í listann (bil aðganag)
    if svar == listi[-1]:    #ef seinasta nafnið í listanum er jafntog nafnið sem við slóum inn
        print (word)    #þá prentar hún nafnið
