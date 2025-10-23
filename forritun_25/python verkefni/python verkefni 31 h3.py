#Verkefni 31    hluti 3

def fall(s1, s2):   #s1 fær gildið úr breytunni strengur1 og s2 fær úr breytunni strengur2
    listi = []  #Býr til tóman lista
    for stafur in s1:   #Les hvern staf í s1 (strengi)
        if stafur in s2:    #Ef hún finnur stafinn í hinum strengnum (s2)
            listi.append(stafur) #Þá skrifar hún stafinn í listann
    print (listi)   #Prentar út alla stafina sem koma fyrir í báðum strengjum
    print (list(set(listi)))    #Ef stafurinn kemur tvisvar fyrir þá prentar hún bara einu sinni stafinn

#Hérna byrjar forritið
strengur1 = str(input("Sláðu inn streng 1: "))
strengur2 = str(input("Sláðu inn streng 2: "))
fall(strengur1,strengur2)  #Kallar í fallið og sendir breyturnar upp í fallið
