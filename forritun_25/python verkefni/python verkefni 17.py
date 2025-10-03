#Verkefni 17
postnumer = {101: "Reykjavík",102: "Reykjavík",103: "Reykjavík",104: "Reykjavík",105: "Reykjavík",107: "Reykjavík",108: "Reykjavík",109: "Reykjavík",110: "Reykjavík",112: "Reykjavík",113: "Reykjavík",116: "Reykjavík",170: "Seltjarnarnes",172: "Seltjarnarnes",190: "Vogar",200: "Kópavogur",201: "Kópavogur",202: "Kópavogur",203: "Kópavogur",210: "Garðabær",112: "Garðabær",220: "Hafnarfjörður",221: "Hafnarfjörður",222: "Hafnarfjörður",225: "Álftanes",230: "Reykjanesbær",232: "Reykjanesbær",233: "Reykjanesbær",235: "Reykjanesbær",240: "Grindavík",245: "Sandgerði",250: "Garður",260: "Reykjanesbær",270: "Mosfellsbær",271: "Mosfellsbær",276: "Mosfellsbær"}

aftur = True
while aftur:

    post = int(input("Sláðu inn póstnúmer: "))

    if post in postnumer:
        print (postnumer[post])
    else:
        print("Póstnúmer ekki til!")

    sv = str(input("Viltu spila aftur? (j/n): "))
    if sv == "n" or sv == "N":
        aftur = False
print ("Forritið er hætt")

    
