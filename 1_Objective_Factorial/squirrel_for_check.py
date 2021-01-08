def squirrel(N):
    
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