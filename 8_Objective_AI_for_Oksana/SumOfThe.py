def SumOfThe(N: int, data: int) -> int: 

    digits = data
    backup = data

    digit = 0
    sum = 0

    for x in range(len(digits)):
        digits = []
        for z in range(len(backup)):
            digits.append(backup[z])
        sum = 0
        digit = digits[x]
        digits.pop(x)
        for y in range(len(digits)):
            sum += digits[y]
        if sum == digit:
            break
        else:
            continue

    return digit