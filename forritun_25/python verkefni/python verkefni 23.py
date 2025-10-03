#Verkefni 23

nofn = ["vigdís", "litzy", "ragna", "unnur", "elísabeth", "alex", "karen", "jana", "sibba", "heiðrún"]
strengur = "Háfjallaveiki"

nofn.sort ()
print ("nöfnin eru:", end=" ")
for n in nofn:
    print (n,end=" ")
print ()

print (nofn[5:8])

print (nofn[-4:])

print (strengur[2:7])

print (strengur[-5:])

print (strengur[0:2]+strengur[-5:])
