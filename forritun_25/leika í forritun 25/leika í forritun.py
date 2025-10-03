#leika

#guessing game

aftur = True
while aftur:
    
    import random
    n = random.randrange(1,10)
    guess = int(input("Veldu númer: "))
    while n!= guess:
        if guess < n:
            print("Of lágt")
            guess = int(input("Veldu annað númer: "))
        elif guess > n:
            print ("Of hátt")
            guess = int(input("Veldu annað númer: "))
        else:
           break
        print("Þú giskaðirð rétt!")
