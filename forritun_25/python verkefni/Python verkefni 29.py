#verkefni 29

nafn = str(input("Sláðu inn nafn: "))
listi = []      #Býr til tómann listi

for i in range (0, len(nafn)):   #gerir jafn oft og nafnið er langt
    if nafn[i] == " ":  #ef hún finnur eyðu
        listi.append(i) #þá skrifar hún í listann hvar eyðan er númer hvað

if len(listi) == 1:     #ef það er ein eyða í nafninu (þá eru tvö nöfn)
    print ("Fornafnið er:", nafn[:listi[0]])    #prentar frá byrjun að eyðu 
    print ("Eftirnafnið er:", nafn[listi[0]+1:])        #prentar frá eyðu til enda

elif len(listi) == 2:     #ef það eru tvær eyður
    print ("Fornafnið er:", nafn[:listi[0]])
    print("Miðjuunafnið er:", nafn[listi[0]+1:listi[1]])    
    print("Eftirunafnið er:", nafn[listi[1]+1:])
