#Verkefni 35

svar = str(input("Skráðu inn fornafn: "))
file = open("nofn (3).txt")
listi = []
for line in file:
    word = line.strip()
    listi = word.split(" ")
    if listi[0] == svar:
        print (word)
