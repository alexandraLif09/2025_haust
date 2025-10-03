svar=int(input("sláðu inn tölu: "))

if svar<10:
    print ("talan er einn stafur")
elif svar<100:
    print ("talan er tveir stafir")
elif svar<1000:
    print("talan er þrír stafir")
elif svar ==2000:
    print("þú slóst inn töluna 2000")
else:
    print ("talan er stærri en þrír stafir")
