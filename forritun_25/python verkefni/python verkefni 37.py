#Verkefni 37

def fornafn():
    file = open("nofn (3).txt")
    svar = str(input("Skráðu inn fornafn sem við viljum leita að: "))
    listi = []
    for line in file:
        word = line.strip()
        listi = word.split(" ")
        if listi[0] == svar:
            print(word)

def eftirnafn():
    file = open("nofn (3).txt")
    leita = input(str("Sláðu inn eftirnafn sem þú vilt finna: "))

    for line in file:
        word = line.strip()
        lengd = len(word) - len(leita)

        if leita == word[lengd:]:
            print(word)
            
def fe():
    file = open("nofn (3).txt")
    sv1 = str(input("Skráðu inn fornafn sem við viljum leita að: "))
    sv2 = str(input("Skráðu inn eftirnafn sem við viljum leita að: "))
    listi = []
    for line in file:
        satt = False
        word = line.strip()
        listi = word.split(" ")
        if listi[0] == sv1:
            satt = True
        if satt:
            if sv2 == listi[-1]:
                print("Nafnið", word, "fannst í skránni")
            
def valmynd():
    print("....................................")
    print()
    print('Veljið:')
    print('1: Finnið fornafn')
    print('2: Finnið eftirnafn')
    print('3: Finnið bæði fornafn og eftirnafn:')
    print('4 Hætta í forriti')
    print()
    print("....................................")

afram = True
while afram:
    valmynd()
    val = int(input("Veljið: "))
    if val == 1:
        fornafn()
    elif val == 2:
        eftirnafn()
    elif val == 3:
        fe()
    elif val == 4:
        afram = False
print("Forritið búið")
    

    
