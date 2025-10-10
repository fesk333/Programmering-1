e = int(input("Hur många timmar vill du hyra bilen? "))
pris = e * 80
if e > 950:
    print("Du får endast hyra bilen för 950 kr")
if e <= 950:
    print(f"Det kostar {pris} kr att hyra bilen")