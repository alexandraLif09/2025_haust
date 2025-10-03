#Verkefni 22

dyr = ["ljón", "köttur", "hestur", "dádýr", "kanína"]
print ("Fjöldi dýra í listanum mínum er: ",len(dyr))
print ("Þessi dýr eru", end=" ")
for d in dyr:
    print (d,end=" ")
print ()

def NyttDyr ():
    dyr.append (str(input("Sláðu inn nýtt dýr: ")))

NyttDyr ()
NyttDyr ()
NyttDyr ()

print ("Listinn minn lítur þá svona út:", dyr)

dyr.sort ()
for d in dyr:
    print (d)

print ("Svona er listinn raðaður í stafrófsröð: ")
for i in range (0,len(dyr)):
    print("Dýr nr", i+1,"á listanum er",dyr[i])
