#Function
def rest():
    global energy
    if energy == 100:
        print("You don’t need to rest again")
    elif energy == 90:
        energy +=10
    elif energy < 100:
        energy += 20
def menufarm():
    global energy, happiness
    for k in range(0, 1000):
        print("1.Socialize")
        print("2.Harvest")
        print("3.rest")
        print("4.return to main menu ")
        x = int(input("chose : "))
        if x == 1:
            socialize()
        elif x == 2:
            if energy == 0:
                print("You don’t have enough energy… You need to rest for a while…")
            elif happiness == 0:
                print("You don’t have enough happiness… You need to meet your neighbors…")
            elif energy == 0 and happiness == 0:
                print("You don’t have enough happiness… You need to meet your neighbors…")
                print("You don’t have enough energy… You need to rest for a while…")
            else:
                energy -= 10
                happiness -= 10
                print("Harvesting the farm ....")
                print("happines decrease 10 point and energy decrease 10 point")
        elif x == 3:
            rest()
        elif x == 4:
            menugender()
        print("welcome : ", nama)
        print("Energy : ", energy)
        print("Happiness : ", happiness)
def menugender():
    global energy, happiness
    print("Mini Console Harvestmoon")
    print("=" * 25)
    print("sellect gender")
    print("1.Male")
    print("2.female")
    print("3.exit")
    e = 0
    a = int(input("choose : "))
    if a == 1:
        loopnama()
        menufarm()
    elif a == 2:
        loopnama()
        menufarm()
    elif a == 3:
        e = 1
        print("program is closed")
def loopnama():
    global nama
    nama = str(input("enter name "))
    if len(nama) < 3 and len(nama) > 20:
        for j in range(0, 1000):
            nama = str(input("enter name "))
    print("wellcome : ", nama)
    print("Energy : ", energy)
    print("Happiness : ", happiness)
def socialize():
    global energy, happiness
    if energy == 0:
        print("You don’t have enough energy...")
        print("You need to rest for a while...")
    elif energy == 90:
        print("Meet neighbors.....")
        print("Happiness increase 20 points and energy decrease 10 points")
        happiness += 10
        energy -= 10
    else:
        if happiness == 100:
            print("Happiness is full and energy decrease 10 points")
            energy -= 10
        elif happiness < 100:
            if happiness == 90:
                print("Meet neighbors.....")
                print("Happiness increase 20 points and energy decrease 10 points")
                happiness += 10
                energy -= 10
            else:
                print("Meet neighbors.....")
                print("Happiness increase 20 points and energy decrease 10 points")
                happiness += 20
                energy -= 10
#Variables
energy = 100
happiness= 100
#Tampilan
menugender()

