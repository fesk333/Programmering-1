import testmain2

ja = ["j", "ja", "y", "yes", "1", "ok"]
nej = ["n", "nej", "no", "0"]

print("Välkommen till miniräknaren!!!!!")
i = 0

while True:
    if i == 0:
        extra = ""
    else:
        extra = " igen"

    i += 1
    print("")
    question = str(input(f"Vill du räkna ut något{extra}? (j/n): "))
    if question.lower() in nej:
        print("Okej, hejdå!")
        break
    elif question.lower() in ja:
        pass
    else:
        print("Svara med j/n")
        continue

    string = str(input("Räkna ut: "))
    string = string.replace(" ", "")


    numbers_and_operators = []
    Result = 0

    if __name__ == "__main__":
        Result, numbers_and_operators = testmain2.calculate(string, numbers_and_operators, Result)

    print(f"Summa: {numbers_and_operators}")
