#Verkefni 42
from random import randint
lond = ["Iceland", "Portúgal", "England", "Svíðþjóð", "Danmörk", "Noregur", "Thýskaland", "Mexíkó", "Frakkland", "Italía"]
print ("þetta eru löndin sem þér stendur til boða aða fara til", end = " ")
for land in lond:
    print(land, "og", end=" ")
print()

print ("...........................................................")

svar = 0
while svar<5:
    svar = int(input("Hvað viltu bæta inn mörgum löndum? (min 5): "))
for i in range(0, svar):
    lond.append(str(input("Sláðu inn nýtt land sem þig langar til: ")))

print ("...........................................................")

lond.sort()

print ("Þetta eru löndin sem þú getur farið til í stafrófsröð:")
for land in lond:
    print (land)

print ("...........................................................")


print ("Þú ferð til", lond[randint(0, len(lond))], "og þú verður þar í", randint(1, 10), "vikur")
