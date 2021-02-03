digits = [100, -50, 10, -25, 90, -35, 90]
backup = [100, -50, 10, -25, 90, -35, 90]

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
        print('сумма всех чисел массива =', digit)
        break
    else:
        continue