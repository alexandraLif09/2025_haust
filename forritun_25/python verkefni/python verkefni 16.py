#Verkefni 16

#A)

for i in range (200, 149,-1):
    print (i)
    
print ("'''''''''''''''''''A'''''''''''''''''''")

#B)

for i in range (50,105,5):
    print (i)

print ("'''''''''''''''''''B'''''''''''''''''''")

#C)
aftur = True
while aftur:

    takn = str(input("Sláðu á lyklaborðið "))
    print ("Þú slóst",takn,"á lyklaborðið")

    if takn == "q" or takn == "Q":
        aftur = False
        
print ("'''''''''''''''''''C'''''''''''''''''''")

#D)
def aldur(fa):
    svar = (2025-fa)
    print ("Þú ert",svar,"gömul/gamall")
    
faedingarAr = int(input("Hvenær ertu fædd/ur?: "))
aldur (faedingarAr)

print ("'''''''''''''''''''D'''''''''''''''''''")
