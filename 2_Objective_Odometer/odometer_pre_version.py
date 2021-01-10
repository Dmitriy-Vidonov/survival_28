massiv = [10, 1, 20, 2, 20, 3]
chet_massiv = []
nechet_massiv = []

sum = 0
avg = 0

# распределяем массивы по четности и нечетности индекса элемента массива
for i in range(len(massiv)):
    if i % 2 == 0:
        chet_massiv.append(massiv[i])
        sum += massiv[i]
    else:
        nechet_massiv.append(massiv[i])

# находим среднее значение эл-тов нечетного массива
avg = sum / len(chet_massiv)

print('chet =', chet_massiv)
print('nechet =', nechet_massiv)
print('последний элемент нечетного массива, t, время =', nechet_massiv[len(nechet_massiv)-1])
print('среднее значение четного массива, V, скорость =', avg)
print('километраж =', avg * nechet_massiv[len(nechet_massiv)-1])
