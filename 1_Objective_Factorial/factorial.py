def squirrel(N: int) -> int:
    try:
        factorial = 1
        count = 0
        for i in range(2, N+1):
            factorial *= i

        N = factorial
        first_digit = factorial
        while N > 0:
            N = N // 10
            count += 1

        for i in range(count-1):
            first_digit = first_digit // 10

        return first_digit
    except Exception as ex:
        print('Сбой в работе функции squirrel() - ' + str(ex))

print('функция - ', squirrel(100))


# черновики:

factorial = 1

n = 70

print('число', n)

# нашли факториал
for i in range(2, n+1):
    factorial *= i

print('факториал =', factorial)

# узнали, сколько разрядов есть в числе факториала
count = 0
N = factorial
while N > 0:
    N = N // 10
    count += 1

print('разрядов =', count)

# ищем первую цифру числа
first_digit = factorial
for i in range(count-1):
    first_digit = first_digit // 10


print('первое число факториала =', first_digit)
