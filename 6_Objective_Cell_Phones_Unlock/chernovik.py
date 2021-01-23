import math

itog_number = 0

# def PatternUnlock(N: int, hits: int) -> str:

diag = math.sqrt(1 ** 2 + 1 ** 2) # 1.41...

sum = 7 + 2 * diag # 9.82..

rounded_sum = round(sum, 5) # округлять результат нужно до 5-ти цифр после запятой - 9.82843

print(rounded_sum) # 9.82843

# как сделать так, чтобы результат был целым числом без запятых
# print(int(round(sum, 5)*100000))

# как получить 100000
i = 10

while rounded_sum % i != 0:
    rounded_sum *= i
    i *= 10

print(i) # i = 100000

itog_number = int(round((i * sum), 0))

print(itog_number) # 982843

# далее предусмотреть исключение нолей из числа
# взять любое тестовое число, перегнать его в массив, исключая '0'
# потом этот массив преобразовать в строку

test_massiv = []
inverted_massiv = []

test_number = 10012

i = 10
el = 0

# формируем массив значений без "0"
while test_number != 0:
    el = test_number % i
    if el == 0:
        test_number = int(test_number/i)
    else:
        test_massiv.append(el)
        test_number = int(test_number/i)

# инвертируем полученный ранее массив в норм. вид
for x in range(len(test_massiv)-1, -1, -1):
    inverted_massiv.append(test_massiv[x])

# создаем строку из списка
# при добавлении эл-тов преобразуем int в str
stroka = ''.join(str(e) for e in inverted_massiv)

print(stroka)


# далее нужно прописать алгоритм расчета длины в зависимости от введенного кода
# типа свод правил продумать - как длина считается в зависимости от введенных чисел
# то есть алгоритм смотрит текущее число и следующее. и он должен понимать - как считать длину


# начнем с самого простого - что если обкатывать механику с самого примитивного. например небольшой массив

massiv = [1, 2, 3, 4, 5, 6]

inv_massiv = [6, 5, 4, 3, 2, 1]

current_element = [1, 2, 3, 4, 5, 7, 8]
next_element = [2, 7]

dlina = 0

# считаем длину диагонали. если 1 и след - 2, то +1. если 6 и след. 2 - то +1.41..
#for i in range(len(massiv)-1):
 #   if massiv[i] == current_element[0] and massiv[i + 1] == next_element[0]: 
  #      dlina += 1
   # elif massiv[i] == current_element[1] and massiv[i + 1] == next_element[0]:
    #    dlina += 1.41

#print('dlina =', dlina)

# напишем весь алго с 1 до 6 просто пока что
# 1 - сначала линейное движение
for i in range(len(massiv)-1):
    if massiv[i+1] > massiv[i]:
        dlina += 1

print('dlina = ', dlina)

print()
print('**********************')
print()

dlina = 0

# 2 - теперь обратное движение
for i in range(len(inv_massiv)-1):
    if inv_massiv[i+1] < inv_massiv[i]:
        dlina += 1

print('Длина в обратку -', dlina)

print()
print('**********************')
print()

# 3 - прямое простое движение но с числами не последовательно, но в одну сторону
massiv = [1, 5, 6]
dlina = 0

digit_counter = 0
for i in range(len(massiv)-1):
    if massiv[i+1] > massiv[i]:
        digit_counter = massiv[i]
        while massiv[i+1] > digit_counter:
            dlina += 1
            digit_counter += 1

print('digit_counter =', digit_counter)
print('dlina =', dlina)    

print()
print('**********************')
print()

# 4 - обратное простое движение с чимлами не последовательно, но в одну сторону
massiv = [6, 5, 1]
dlina = 0
digit_counter = 0

for i in range(len(massiv)-1):
    if massiv[i+1] < massiv[i]:
        digit_counter = massiv[i]
        while massiv[i+1] < digit_counter:
            dlina += 1
            digit_counter -= 1

print('digit_counter =', digit_counter)
print('dlina =', dlina)    

print()
print('**********************')
print()


# 5 - движение в любые стороны с непоследовательными числами. Напр. 1,5,5,3,6
massiv = [1, 5, 5, 3, 6]
dlina = 0
digit_counter = 0

for i in range(len(massiv)-1):
    
    # если след. цифра больше текущей:
    if massiv[i+1] > massiv[i]:
        digit_counter = massiv[i]
        while massiv[i+1] > digit_counter:
            dlina += 1
            digit_counter += 1
    
    # если след. цифра меньше текущей:
    elif massiv[i+1] < massiv[i]:
        digit_counter = massiv[i]
        while massiv[i+1] < digit_counter:
            dlina += 1
            digit_counter -= 1
    
    # если след. цифра равна текущей:
    elif massiv[i+1] == massiv[i]:
        continue        

print('dlina =', dlina)

print()
print('**********************')
print()

# 6 - добавить одно условие - что если по 6 будет 2 и длина между ними другая. Сначала в одну сторону
massiv = [1, 5, 3, 6, 2]
dlina = 0
digit_counter = 0

for i in range(len(massiv)-1):
    
    # если след. цифра больше текущей:
    if massiv[i+1] > massiv[i]:
        digit_counter = massiv[i]
        while massiv[i+1] > digit_counter:
            dlina += 1
            digit_counter += 1
    
    # если след. цифра меньше текущей:
    elif massiv[i+1] < massiv[i] and massiv[i+1] != 2 and massiv[i] != 6: 
        digit_counter = massiv[i]
        while massiv[i+1] < digit_counter:
            dlina += 1
            digit_counter -= 1
    
    # если след. цифра равна текущей:
    elif massiv[i+1] == massiv[i]:
        continue

    elif massiv[i+1] == 2 and massiv[i] == 6:
        dlina += 1.5       

print('dlina =', dlina)

print()
print('**********************')
print()


# 7 - так же, как 6-й, но с возможностью от 2 перейти к 6
massiv = [1, 5, 3, 6, 2, 6, 2, 6, 4, 2, 5]
dlina = 0
digit_counter = 0

for i in range(len(massiv)-1):
    
    if massiv[i+1] == massiv[i]: # если след. цифра равна текущей:
        continue

    elif massiv[i] == 6 and massiv[i+1] == 2: # если "6-2"
        dlina += 1.5       
    
    elif massiv[i] == 2 and massiv[i+1] == 6: # если "2-6"
        dlina += 1.5
        
    elif massiv[i] == 2 and massiv[i+1] != 6: # если 2 и не 6
        # либо след. число больше 2
        if massiv[i+1] > massiv[i]:
            digit_counter = massiv[i]
            while massiv[i+1] > digit_counter:
                dlina += 1
                digit_counter += 1
                
        # либо след. число меньше 2
        elif massiv[i+1] < massiv[i]:
            digit_counter = massiv[i]
            while massiv[i+1] < digit_counter:
                dlina += 1
                digit_counter -= 1
                
    elif massiv[i] == 6 and massiv[i+1] != 2: # если 6 и не 2    
        # либо след. число больше 6
        # заглушка - доработаем дальше
        
        # либо след. число меньше 6
        if massiv[i+1] < massiv[i]:
            digit_counter = massiv[i]
            while massiv[i+1] < digit_counter:
                dlina += 1
                digit_counter -= 1
            
    elif massiv[i+1] > massiv[i]: # если след. эл-т > текущего
        digit_counter = massiv[i]
        while massiv[i+1] > digit_counter:
            dlina += 1
            digit_counter += 1
            
    elif massiv[i+1] < massiv[i]: # если след. эл-т < текущего
        digit_counter = massiv[i]
        while massiv[i+1] < digit_counter:
            dlina += 1
            digit_counter -= 1
  
print('dlina =', dlina) # 22 - верный ответ

print()
print('**********************')
print()

# 8 - обработка линий до 7 и назад

massiv = [1, 5]
dlina = 0
digit_counter = 0

for i in range(len(massiv)-1):
    
    # если след. цифра равна текущей:
    if massiv[i+1] == massiv[i]:
        continue

    elif massiv[i] == 6 and massiv[i+1] == 2: # если "6-2"
        dlina += 1.5       
    
    elif massiv[i] == 2 and massiv[i+1] == 6: # если "2-6"
        dlina += 1.5
        
    elif massiv[i] == 2 and massiv[i+1] == 7: # если "2-7"
        dlina += 1.5
        
    elif massiv[i] == 7 and massiv[i+1] == 2: # если "7-2"
        dlina += 1.5
        
    elif massiv[i] == 6 and massiv[i+1] == 7: # если "6-7"
        dlina += 1.5 * 2
        
    elif massiv[i] == 7 and massiv[i+1] == 6: # если "7-6"
        dlina += 1.5 * 2
        
    elif massiv[i] == 2 and massiv[i+1] != 6: # если 2 и не 6
        # либо след. число больше 2
        if massiv[i+1] > massiv[i]:
            digit_counter = massiv[i]
            while massiv[i+1] > digit_counter:
                dlina += 1
                digit_counter += 1
                
        # либо след. число меньше 2
        elif massiv[i+1] < massiv[i]:
            digit_counter = massiv[i]
            while massiv[i+1] < digit_counter:
                dlina += 1
                digit_counter -= 1
                
    elif massiv[i] == 6 and massiv[i+1] != 2: # если 6 и не 2    
        # либо след. число больше 6
        # заглушка - доработаем дальше
        
        # либо след. число меньше 6
        if massiv[i+1] < massiv[i]:
            digit_counter = massiv[i]
            while massiv[i+1] < digit_counter:
                dlina += 1
                digit_counter -= 1
            
    elif massiv[i+1] > massiv[i]: # если след. эл-т > текущего
        digit_counter = massiv[i]
        while massiv[i+1] > digit_counter:
            dlina += 1
            digit_counter += 1
            
    elif massiv[i+1] < massiv[i]: # если след. эл-т < текущего
        digit_counter = massiv[i]
        while massiv[i+1] < digit_counter:
            dlina += 1
            digit_counter -= 1
  
print('dlina =', dlina)



