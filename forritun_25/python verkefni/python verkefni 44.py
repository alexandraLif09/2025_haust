#Verkefni 44

file = open("verk44.txt")
for line in file:
    listi = []
    word = line.strip()
    listi = line.split(";")
    print (listi[0])

print (".................................")

svar = str(input("Sláðu inn leitarorð: "))
k = False
file = open("verk44.txt")
for line in file:
    listi = []
    word = line.strip()
    listi = line.split(";")
    if svar == listi[0].strip():
        print ((listi[1]).strip())
        k = True
if k == False:
    print ("Fann ekki leitarorð")
