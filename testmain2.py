
def calculate(string, numbers_and_operators, Result):

    numbers_and_operators = []
    Result = 0

    for char in string:
        try:
            char = int(char)
        except ValueError:
            pass

        numbers_and_operators.append(char)
    
    if isinstance(numbers_and_operators, str) == False:
        numbers_and_operators.append("+")
    
    e = True
    def is_number(numbers_and_operators, e):
        for i in range(len(numbers_and_operators)-1):
            try:
                if isinstance(numbers_and_operators[i], int) and isinstance(numbers_and_operators[i+1], int):
                    r = numbers_and_operators[i] * 10 + numbers_and_operators[i+1]
                    numbers_and_operators.pop(i)
                    numbers_and_operators.pop(i)
                    numbers_and_operators.insert(i, r)
                    e = True
                    break
                else:
                    e = False
            except IndexError:
                pass
    
        return numbers_and_operators, e

        
    while e == True:
        for z in range(len(numbers_and_operators)):
            numbers_and_operators = is_number(numbers_and_operators, e)[0]
            e = is_number(numbers_and_operators, e)[1]


    Result += numbers_and_operators[0]
    divmul = True

    if "+" not in numbers_and_operators and "-" not in numbers_and_operators and "*" not in numbers_and_operators and "/" not in numbers_and_operators:
        Result = numbers_and_operators[0]
        
        #return numbers_and_operators, Result

  

    def divisionmultiplication(numbers_and_operators, divmul):

        for i in range(len(numbers_and_operators)-1):
            divmul = False

            try:
                if numbers_and_operators[i] == "*":
                    numbers_and_operators[i] = numbers_and_operators[i-1] * numbers_and_operators[i+1]
                    numbers_and_operators.pop(i+1)
                    numbers_and_operators.pop(i-1)
                    
                    i -= 1
                    divmul = True

                if numbers_and_operators[i] == "/":
                    numbers_and_operators[i] = numbers_and_operators[i-1] / numbers_and_operators[i+1]
                    numbers_and_operators.pop(i+1)
                    numbers_and_operators.pop(i-1)
                    i -= 1
                    divmul = True

            except IndexError:
                pass

        return numbers_and_operators, divmul
    
    if "*" in numbers_and_operators or "/" in numbers_and_operators:
        
        if "+" not in numbers_and_operators and "-" not in numbers_and_operators:
            numbers_and_operators.insert(0, 0)
            numbers_and_operators.insert(1, "+")
        
        while divmul == True:
            for z in range(len(numbers_and_operators)):
                numbers_and_operators = divisionmultiplication(numbers_and_operators, divmul)[0]
                divmul = divisionmultiplication(numbers_and_operators, divmul)[1]
                if divmul == False:
                    break

    for i in range(len(numbers_and_operators)-1):
        try:
            if numbers_and_operators[i] == "+":
                Result += numbers_and_operators[i+1]
            if numbers_and_operators[i] == "-":
                Result -= numbers_and_operators[i+1]
        except IndexError:
            pass
    
    
    
    return numbers_and_operators, Result