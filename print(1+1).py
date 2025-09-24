# List of all previous answers
g = []

# A definition that calculates depending on what method
def calc(f, s, c):

    t = None
    if "+" in c:
        t = f + s
    elif "-" in c:
        t = f - s
    elif "*" in c:
        t = f * s
    elif "/" in c:
        t = f / s

    return t

# A Loop for the calculator
H = True
while H == True:

    if len(g) > 0:
        print(f"Previous calculations: {g}")
    
    ip = str(input("Would you like to calculate? (Y/N)"))

    if "y" in ip or "Y" in ip:
            
            # Takes in answers for the user

            f = float(input("first number: "))
            s = float(input("second number: "))

            c = str(input("Calculation method (+,-,*,/): "))
            if len(c) > 1:
                print("Only one method at a time")
                exit()
            
            # Calculates the total

            t = calc(f, s, c)

            # Checks if its even or odd
            if t != None:
                e = t%2
                if e == 0:
                    print(f"Result: {t}, even")
                else:
                    print(f"Result: {t}, odd")

                g.append(f"{str(f)} {str(c)} {str(s)} = {str(t)}")
            else:
                print("idk")
    
    
    elif "n" in ip or "N" in ip:
        print("Exiting...")
        H = False
        exit()
    
    else:
        print("I can't hear you, repeat")
    