#Verkefni 24

lond = ["japan", "filippseyjar", "bretland", "kólumbía", "spánn", "venesúla", "gvatemala", "danmörk", "noregur", "slóvenía"]

num=0
while num<5:       #Gerir aftur og aftur þangað til notandinn slær inn 5 eða hærri tölu
    num = int(input("Hvað viltu bæta við mörgum löndum? (minnst 5)): "))

for i in range (0,num):
    lond.append (str(input("Sláðu inn nýtt land á listann: ")))

lond.sort ()        #raðar listanum í stafrófsröð
print ("Nöfnin eru:", *lond)     #prentar löndin í eina línu

print ("Löndin eru", len(lond))      #prentar hvað mörg lönd eru í listanum

#prentar þriðja hvert land í listanum
print ("Þriðja hvert land á listanum er:", end=" ")
for i in range (0,len(lond),3):
    print (lond[i], end=" ")
print ()

#prentar landið í miðjunni
print ("Landið í miðjunni er:", lond[(round(len(lond)/2)-1)])

#prentar fyrsta stafinn í öllum löndunum
print ("Fyrsti stafurinn í öllum nöfnum er:", end=" ")
for i in lond:
    print (i[0], end=" ")
print ()

#prentar fyrsta og seinata landið út og svo land nr 2 og næst síðasta og svo koll af kolli
z = round(len(lond)/2)
for i in range (0,z):
    print (lond[i], lond [-(i+1)], end=" ")
print ()
