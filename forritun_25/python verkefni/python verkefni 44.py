#Verkefni 44

file = open("verk44.txt")

listi = []

for line in file:
    word = line.strip(" ")
    listi = line.split(";")
print (listi)
print (word)
