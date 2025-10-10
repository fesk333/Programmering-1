e = int(input("Hur många minuter? "))
z = int(input("Hur många sekunder? "))

total = e * 60 + z

if total > 165 and total < 260:
    print("Du får spela låten ")
else:
    print("Du får inte spela låten ")