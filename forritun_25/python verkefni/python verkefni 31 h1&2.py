#Verkefni 31    hluti 1 & 2

def hastafir(t):
    print (t.upper())

def lastafir(t):
    print (t.lower())


texti = str(input("Sláðu inn texta: "))
svar = str(input("Viltu breyta textanum í hástafi eða lástafi (h/l)? "))
if svar == "h":
    hastafir(texti)
elif svar == "l":
    lastafir(texti)
else:
    print ("Villa")
