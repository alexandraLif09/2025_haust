#Verkefni 24

lond = ["japan", "filippseyjar", "bretland", "kólumbía", "spánn", "venesúla", "gvatemala", "danmörk", "noregur", "slóvenía"]

fleiri = int(input("Hvað viltu  bæta við mörgum löndum? (minnst 5)): "))
print ("veit ekki hvað á að gera hér")

lond.sort ()
print ("Nöfnin eru:", end=" ")
for l in lond:
    print (l, end=" ")
print ()

print ("Löndin eru", len(lond))


