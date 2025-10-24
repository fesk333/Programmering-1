
while True:
    print("Vill du fortsätta? J/N")
    x = str(input("A: "))
    x = x.lower()
    if "j" in x:
        print("Vilken uppgift? fråga 1-10 (och ex 1.1 för nivå 2)")
        z = float(input("A: "))
        if z == 1:
            print("Uppgift 1")
            for i in range(11):
                print(i)

        elif z == 2:
            print("Uppgift 2")
            while True:
                g = int(input("Skriv ett tal"))

                if g == 0:
                    print("Talet är noll, stänger av. . .")
                    break
                else:
                    print("Talet är inte lika med noll")

        elif z == 3:
            print("Uppgift 3")
            print("Skriv in fem heltal separat")
            resultat = 0
            for i in range(5):
                tal = int(input("Tal: "))
                resultat += tal
            print(f"Resultat: {resultat}")
        elif z == 4:
            print("Uppgift 4")
            while True:
                inp = str(input("Skriv lösernordet: "))
                print("Hint: det är hemligt")
                if "hemligt" in inp:
                    print("Rätt")
                    break
                else:
                    print("Fel")
        elif z == 5:
            print("Uppgift 5")
            for i in range(21):
                if i%2 == 0:
                    print(i)
        elif z == 6:
            print("Uppgift 6")
            for i in range(10):
                print(10-i)

        elif z == 7:
            print("Uppgift 7")
            while True:
                e = int(input("Ge mig ett negativt tal "))
                if e < 0:
                    print("Yippie")
                    break
                else:
                    print("Awww")
        elif z == 8:
            print("Uppgift 8")
            produkt = 1
            for i in range(1,6):
                produkt = produkt * i
            print(produkt)
            
        elif z == 9:
            print("Uppgift 9")
            rad = int(input("Hur många rader? "))
            teckenrad = ""
            for r in range(rad):
                for i in range(r+2):
                    teckenrad = "*" * i
                print(teckenrad)
                    

        elif z == 10:
            print("Uppgift 10")
            tal = []
            heltal = 0
            for i in range(10):
                e = int(input("Ge mig ett heltal"))
                tal.append(e)
            print(tal)
            for f in range(len(tal)):
                if tal[f]%2 == 0:
                    heltal += 1
            print(f"Mängden heltal: {heltal}")

        elif z == 1.1:
            print("Uppgift 1.1")
            for i in range(10,31):
                print(i)
            for i in range(21):
                print(200-i)
            for i in range(9):
                print(1000+i*50)
        elif z == 1.2:
            print("Uppgift 1.2")
            v = 0
            while True:
            
                q = str(input("Vill du fortsätta? j/n"))
                if "j" in q:
                    f = int(input("Ge mig ett heltal"))
                    if f%2 == 0:
                        print("Det är ett heltal")
                        if f > v:
                            v = f
                    else:
                        print("Det är inte ett heltal")
                elif "n" in q:
                    print(f"största värde: {v}")
                    break
        
        elif z == 1.3:
            print("Uppgift 1.3")
            for i in range(101):
                if i%3 == 0 and i%5 == 0:
                    print("FizzBuzz")
                elif i%3 == 0:
                    print("Fizz")
                elif i%5 == 0:
                    print("Buzz")
                else:
                    print(i)
        elif z == 1.4:
            while True:
                print("Välj en av följande alternativ.")
                print("1. Subtrahera ett tal med ett annat")
                print("2. Dividera ett tal med ett annat")
                print("3. Avsluta programmet")
                e = int(input("A: "))
                if e == 1 or e == 2:
                    f = int(input("Första tal: "))
                    a = int(input("Andra tal: ")) 
                    if e == 1:
                        print(f"Total: {f-a}")
                    elif e == 2:
                        print(f"Total: {f/a}")
                elif e == 3:
                    break
                else:
                    print("Fel input, försök igen")
        elif z == 1.5:
            z = []
            e = int(input("Skriv ett heltal: "))
            g = [e]
            result = [int(digit) for digit in str(g[0])]  
            string = ""
            for i in result:
                if i != 9:
                    f = i+1
                elif i == 9:
                    f = 0
                z.append(f)
            for number in (z):
                string += str(number)
            print(string)
        elif z == 1.6:
            e = str(input("Mening: "))
            g = int(input("Steg till höger: "))
            f=[]
            for letter in e:
                f.append(letter)
            mening = ""
            for letter in range(len(f)):
                mening += " "*g
                mening += f[letter]
                print(mening)
                mening = ""
        elif z == 1.7:
            e = str(input("Mening: "))
            f = str(input("Första bokstav: "))
            a = str(input("Andra bokstav: "))
            s = ""
            if len(a) > 1 or len(f) > 1:
                print("Fel input")
                break
            s += a
            s += f
            if s in e:
                print("Det fanns i meningen")
            else:
                print("Det fanns inte i meningen")
        elif z == 1.8:
            e = int(input("Sidlängd: "))
            print("")
            for i in range(e):
                if i > 0:
                    print("*"*i)
        elif z == 1.9:
            xg = int(input("Hur många X per grupp? "))
            og = int(input("Hur många O per grupp? "))

            om = int(input("Hur många O mönster per rad? "))
            r = int(input("Hur många rader?"))
            bar = ""

            for i in range(r):
                
                for oz in range(om):
                    if oz == 0:
                        bar += ("X"*xg+"-"+"O"*og)
                    elif oz != 0:
                        bar += ("-"+"X"*xg+"-"+"O"*og)
                
                print(bar + ("-"+"X"*xg))
                bar = ""
            
    elif "n" in x:
        break
    else:
        print("dunno what u are sayin")