#verkefni 4

#input
aldur=int(input("Hvað ertu gömul/gamall á þessu ári? "))

#output
if aldur <= 12:
    print ("þú ert barn")

elif aldur >= 20:
    print ("þú ert fullorðin(n)")

else:
    print ("þú ert unglingur")

    
print("þú ert fædd(ur) árið ",2025-aldur,)
