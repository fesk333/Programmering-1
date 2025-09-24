import time
import keyboard
import os
import random


# Used to clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Inputs and interface
print("Welcome to Python (made with Python)")
Snake_character = input("Choose a single character for your snake: ")
Snake_character = Snake_character[0]
Fruit_character = input("Choose a single character for your fruit: ")
Fruit_character = Fruit_character[0]
Speed = float(input("Choose a speed for your snake (lower is faster): "))
Map_width = int(input("Choose a width for your map: "))
Map_height = int(input("Choose a height for your map: "))


# Values and loops
#----------------------------------------------------------------------------#
map = []
snake = []

for i in range(Map_height):
    map.append("#" * (Map_width))

Snake_x = 3
Snake_y = 5

Fruit_x = 7
Fruit_y = 3

Shop_x = None
Shop_y = None
Shop = False
banned = []

event = None
items = ["Landmine defuser", "Teleporter", "Plow", "Inversor"]

snake = [(Snake_x, Snake_y)]
snake_body = 1
snake_history = []

Landmine_x = []
Landmine_y = []
Landmine_count = 5

Snake_direction = "right"
previous_direction = "right"

# loop value
l=0

#----------------------------------------------------------------------------#

while True:
    # Checks if the loop isnt the first, to start other values
    if l > 0:
        for i in range(Map_height):
            # Creates a "blank" slate, which characters can be added
            map[i] = ""
            row = ""

            # A loop through each row and column
            for j in range(Map_width):
                
                # Checks if the X and Y coordinate matches up, and if it does, it will add that character
                # Else it will just add the background (#) 

                if fullsnake_x.count(j) > 0 and fullsnake_y.count(i) > 0 and (j, i) in fullsnake:
                    row += Snake_character
                
                elif j == Fruit_x and i == Fruit_y:
                    row += Fruit_character
                
                elif j == Shop_x and i == Shop_y:
                    row += "S"
                
                elif Landmine_x.count(j) > 0 and Landmine_y.count(i) > 0 and (j, i) in zip(Landmine_x, Landmine_y):
                    row += "X"
                else:
                    row += "#"
                    
            map[i] = row

    l += 1

    # Map logic
    # If the X and Y coordinate is out of boundry, the you will lose unless you have an inversor
    if Snake_y > (Map_height-1) or Snake_y < 0 or Snake_x > (Map_width -1) or Snake_x < 0:
        if "Inversor" in items:
            items.remove("Inversor")
            event = "You inversed to the other side of the map!"
            if Snake_y > (Map_height-1):
                Snake_y = 1
            elif Snake_y < 0:
                Snake_y = (Map_height-1) 

            if Snake_x > (Map_width -1):
                Snake_x = 1
            elif Snake_x > 0:
                Snake_x = (Map_width -1)
            inversed = True
        else:
            clear()
            print("You hit a wall! Game Over!")
            break

    # If the snakes X and Y matches the fruits, the fruit will reappear elsewhere with different values
    # Also adds to the length of the snake
    if Snake_x == Fruit_x and Snake_y == Fruit_y:
        Fruit_y = random.randint(0, Map_height - 1)
        Fruit_x = random.randint(0, Map_width - 1)
        snake_body += 1
    
    if Fruit_x == Shop_x and Fruit_y == Shop_y or (Fruit_x, Fruit_y) in zip(Landmine_x, Landmine_y):
        Fruit_y = random.randint(0, Map_height - 1)
        Fruit_x = random.randint(0, Map_width - 1)
    if (Fruit_x, Fruit_y) in snake_history:
        Fruit_y = random.randint(0, Map_height - 1)
        Fruit_x = random.randint(0, Map_width - 1)
    
    # You will win if the snake is as long as the map, minus the landmines and shop
    if len(snake) == (Map_width * Map_height) - (len(Landmine_x) + len(Shop_x)):
        clear()
        print("You win!")
        break

    # The snake will die if it hits itself, unless it has a plow
    if (Snake_x, Snake_y) in snake_history:
        if "Plow" in items:
            items.remove("Plow")
            event = "You used a plow to break through yourself!"

            for i in (snake_history):
                if i == (Snake_x, Snake_y):
                    snake_history.remove(i)
                    break
                
        else:
            clear()
            print("You hit yourself! Game Over!")
            break
    
    # Has a 10% to spawn a landmine each loop
    if random.randint(1, 10) == 1 and len(Landmine_x) < Landmine_count:
        Landmine_x.append(random.randint(0, Map_width - 1))
        Landmine_y.append(random.randint(0, Map_height - 1))

    # The snake will die if it hits a landmine, unless it has a landmine defuser
    for i in range(len(Landmine_x)):
        if Snake_x == Landmine_x[i] and Snake_y == Landmine_y[i]:
            if "Landmine defuser" in items:
                Landmine_x.pop(i)
                Landmine_y.pop(i)
                items.remove("Landmine defuser")
                event = "You defused a landmine!"
                break
            else:
                clear()
                print("You hit a landmine! Game Over!")
                quit()

    # If the snake has a certain length, a shop will appear
    if snake_body%5 == 1 and Shop == False and snake_body not in banned and snake_body > 1:
        Shop = True
        Shop_x = random.randint(0, Map_width - 1)
        Shop_y = random.randint(0, Map_height - 1)
        event = "Shop appeared"

    # If the snake hits the shop, the game will pause and a menu will appear
    if Snake_x == Shop_x and Snake_y == Shop_y:
        Shop_x, Shop_y = None, None
        Shop = False
        # Banned a certain length of a snake body, so that shops will not spawn all the time
        banned.append(snake_body)
        clear()
        money = random.randint(0, 3)
        # Microtransactions
        gewag = input("Please enter you visa card number: ")
        gewgs = input("Please enter your pin: ")

        while money > 0:
            # Gives the user 0 to 3 money which the snake can spend on upgrades
            g = 5000
            print(f"Current balance: {str(money)} dorrar")
            print("")
            money -= 1
            print("Please select an upgrade or item: ")
            print("1. Speed up")
            print("2. Speed down")
            print("3. Change snake character")
            print("4. Change fruit character")
            print("5. Random item")
            print("6. Exit the shop")
            print("")
            print("")
            g = int(input("Choice: "))
            if 1 or 2 or 3 or 4 or 5 in g:


                if g == 1:
                    Speed -= 0.01
                    break
                if g == 2:
                    Speed += 0.01
                    break
                if g == 3:
                    Snake_character = input("Choose a single character for your snake: ")
                    Snake_character = Snake_character[0]
                    break
                if g == 4:
                    Fruit_character = input("Choose a single character for your fruit: ")
                    Fruit_character = Fruit_character[0]
                    break
                if g == 5:
                    if random.randint(1, 4) == 1:
                        items.append("Landmine defuser")
                        event = "You got a landmine defuser!"
                        break
                    elif random.randint(1, 4) == 2:
                        items.append("Teleporter")
                        event = "You got a teleporter!"
                        break
                    elif random.randint(1, 4) == 3:
                        items.append("Plow")
                        event = "You got a plow!"
                        break
                    elif random.randint(1, 4) == 4:
                        items.append("Inversor")
                        event = "You got an inversor!"
                if keyboard.is_pressed('o'):
                    break
            elif g == 6:
                break
            else:
                if g == 5000:
                    g = int(input("Choice: "))               
        

        
    # A key that can be held to exit
    if keyboard.is_pressed('p'):
        break

    # Displays the map in the terminal
    for w in map: 
        print(w)

    # Checks what direction the snake should go
    if keyboard.is_pressed('d'):
        Snake_direction = "right"
    if keyboard.is_pressed('a'):
        Snake_direction = "left"
    if keyboard.is_pressed('w'):
        Snake_direction = "up"
    if keyboard.is_pressed('s'):
        Snake_direction = "down"  

    y = 0
    x = 0

    # The snake history checks the previous places the snake has traveled with the amount tracked depends on snake body
    for i in range(len(snake)):
        snake_history.append((Snake_x, Snake_y))
        if len(snake_history) > snake_body:
            snake_history.pop(0)

    # Teleports the snake forwards an extra step
    if keyboard.is_pressed('q') and "Teleporter" in items:
        boost = True
        items.remove("Teleporter")
        event = "Teleporter activated!"
    else:
        boost = False

    # Compares the previous direction with the current, and if the direction is the opposite, it will stay the same
    # This is so that the snake can't go into itself
    if previous_direction == "right" and Snake_direction == "left":
        Snake_direction = "right"
    if previous_direction == "left" and Snake_direction == "right":
        Snake_direction = "left"
    if previous_direction == "up" and Snake_direction == "down":
        Snake_direction = "up"
    if previous_direction == "down" and Snake_direction == "up":
        Snake_direction = "down"
    
    # Checks the direction, and adds to the snakes X or Y Value depending on the direction
    elif Snake_direction == "right":
        Snake_x += 1
        x = 1
        previous_direction = "right"
        if boost == True:
            Snake_x += 1
            boost = False
    elif Snake_direction == "left":
        Snake_x -= 1
        x = -1
        previous_direction = "left"
        if boost == True:
            Snake_x -= 1
            boost = False
    elif Snake_direction == "up":
        Snake_y -= 1
        y = -1
        previous_direction = "up"
        if boost == True:
            Snake_y -= 1
            boost = False
    elif Snake_direction == "down":
        Snake_y += 1
        y = 1
        previous_direction = "down"
        if boost == True:
            Snake_y += 1
            boost = False
    
    # Updates the snakes coordinates
    snake = [(Snake_x, Snake_y)]

    # The snake is the head, whilst the snake_history is the body
    fullsnake = snake_history + snake

    # Lists out the previous positions and current position for the full snake
    # Makes it into X and Y coordinates
    fullsnake_x = []
    fullsnake_y = []
    for part in fullsnake:
        fullsnake_x.append(part[0])
        fullsnake_y.append(part[1])

    # Shows the interface
    print("Hold 'p' to quit")
    print(f"Items: {items}")
    if event != None:
        print("Event: " + event)

    # Makes the game pause, which it relies on
    # Otherwise the game would run too fast, and would be impossible to play
    time.sleep(Speed)
    # Clears the map for the next printing of the map
    clear()