#verkefni 8

#input

dýr = str(input("Átt þú gæludýr? "))

#output
if dýr == "já" or dýr == "ja" or dýr == "Já" or dýr == "Ja" or dýr == "JA" or dýr == "JÁ":
    print ("Þú átt gæludýr")

elif dýr == "nei" or dýr == "Nei" or dýr =="NEI":
    print ("Þú átt ekki gæludýr")

else:
    print ("Villa. Reyndu aftur")
