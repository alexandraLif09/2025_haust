#verkefni 7

#input
from random import randint
tala = (randint(1,10))
gisk = int(input("Giskaðu á tölu frá 0 - 10: "))

#output
if gisk == tala:
    print("þú giskaðir rétt, talan er: ",tala)
elif gisk < tala:
    print ("þú giskaðir á of lága tölu, rétt tala er: ",tala)
elif gisk > tala:
    print ("þú giskaðir á of háa tölu, rétt tala er: ",tala)
