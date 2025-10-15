
while True:
    print("Vilken uppgift? 4.1, 4.2, 4.3, 4.4, 4.1.f, 4.2.f, 4.3.f, 4.4.f, 4.5.f" )
    upg = str(input())

    if upg == "4.1":
        while True:
            print("Vilket är världens folkrikaste land?")
            svar = str(input("Svar: "))
            if svar.lower() == "kina":
                print("Rätt!")
                break
            else:
                print("Fel, försök igen!")
                continue
    elif upg == "4.2":
        E = 50
        while E != 0:
            print(E)
            E -= 1
    elif upg == "4.3":
        while True:
            print("2. Omvandla kilometer till meter")
            print("3. Avsluta programmet")
            val = str(input("Svar: "))
            if "1" in val:
                meter = float(input("Ange antal meter: "))
                km = meter / 1000
                print(f"{meter} meter är {km} kilometer.")
                print("")
                continue
            elif "2" in val:
                km = float(input("Ange antal kilometer: "))
                meter = km * 1000
                print(f"{km} kilometer är {meter} meter.")
                print("")
                continue
            if "3" in val:
                break
            else:
                print("Felaktigt val, försök igen.")
                print("")
                continue
    elif upg == "4.4":
        while True:
            print("Ge ett heltal: (0 avslutar)")
            Num = int(input())
            if Num == 0:
                break
            elif Num % 2 == 0:
                print("Talet är jämnt:")
            elif Num % 2 != 0:
                print("Talet är udda:")
            else:
                print("Jag vet inte, fråga en matematiker.")
    
    elif upg == "4.1.f":
        for i in range(40, 81):
            print(i)
    
    elif upg == "4.2.f":
        for i in range(20):
            print(1495 - i*5)
    
    elif upg == "4.3.f":
        E = "Detta är ett meddelande"
        for i in E:
            print(i)
        print(E[::-1])
    elif upg == "4.4.f":
        NS = input("Skriv ett tal: ")
        NS.replace(" ", "")
        Sum = 0
        tab = []
        for i in NS:
            tab.append(i)
        for i in tab:
            try:
                Sum += int(i)
            except ValueError:
                pass
        print(Sum)
    elif upg == "4.5.f":
        NS = input("Skriv ett tal: ")
        tab = []
        for i in NS:
            tab.append(i)
        if "3" in tab and "7" in tab:
            print("Talet innehåller 3 och 7")
        elif "3" in tab and "7" not in tab:
            print("Talet innehåller en 3:a")
        elif "7" in tab and "3" not in tab:
            print("Talet innehåller en 7:a")
        else:
            print("Talet innehåller varken 3 eller 7")

    forts = str(input("Vill du fortsätta? (j/n): "))
    if forts.lower() == "j":
        continue
    elif forts.lower() == "n":
        print("Hejdå!")
        break
    else:
        print("Svara med j/n")
        continue