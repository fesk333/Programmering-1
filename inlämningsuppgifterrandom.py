import random


deck = {
    "Hearts": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
    "Diamonds": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
    "Clubs": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
    "Spades": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
}

colors = ["Röd", "Blå", "Grön", "Gul", "Orange", "Lila", "Rosa", "Brun", "Grå", "Svart", 
          "Vit", "Turkos", "Indigo", "Korall", "Magenta", "Lime", "Navy", "Teal", "Beige", "Guld"]

while True:
    e = int(input("Välj uppgift 1-5, 0 för att avsluta: "))
    if e == 0:
        break
    elif e == 1:
        while True:
            f = str(input("Vill du dra ett kort? (j/n): ").lower())
            if f == "j" and deck is not None:
                suit = random.choice(list(deck.keys()))
                rank = random.choice(deck[suit])
                print(f"Du drog: {rank} of {suit}")
                deck[suit].remove(rank)
            if deck is None:
                print("Inga kort kvar")
                break
            elif f == "n":
                break
    elif e == 2:
        spelare = int(input("Antal spelare: "))
        spelande = []
        for i in range(spelare):
            spelande.append(random.randint(1, 101))
        print(spelande)
        print(f"Högsta poäng: {max(spelande)}")

    elif e == 3:
        färger = int(input("Hur många färger vill du ha? "))
        for i in range(färger):
            print(random.choice(colors))
    
    elif e == 4:
        dagar = int(input("Hur många dagar vill du simulera vädret? "))
        väderdagar = {

        }
        for i in range(dagar):
            random.randint(-20, 40)
            väderdagar[f"Dag {i+1}"] = random.randint(-20, 40)
        
        for dag, temp in väderdagar.items():
            print(f"{dag}: {temp}°C")
        print(f"Genomsnittliga temperaturen: {sum(väderdagar.values())/dagar}°C")
    
    elif e == 5:

        tävlare = int(input("Antal tävlande: "))
        resultat = {}
        for i in range(tävlare):
            nr = random.randint(1,1001)
            if i == 1000:
                break
            while nr in resultat.values():
                nr = random.randint(1,1001)
            resultat[f"Tävlande {i+1}"] = nr
        
        for r in resultat.items():
            print(f"{r[0]}: {r[1]}")
    else:
        print("Felaktigt val, försök igen.")