import math

def razryad(some_list) -> int:
    razryad = 0

    for i in range(len(some_list)-1):
        if len(some_list) == 1:
            razryad = 1
            break
        else:
            if i == 0:
                razryad += 10
            elif i > 0:
                razryad *= 10

    return razryad

def list_to_num(some_list) -> int:
    razr_number = razryad(some_list)
    
    some_digit = 0

    for i in range(len(some_list)):
        some_digit += int(some_list[i]) * razr_number
        razr_number /= 10

    return int(some_digit)

def BigMinus(s1: str, s2: str) -> str:
    s1 = list(s1) # перевели строку в список
    s2 = list(s2) # перевели строку в список

    s1 = list_to_num(s1)
    s2 = list_to_num(s2)

    return str(abs(s1 - s2))