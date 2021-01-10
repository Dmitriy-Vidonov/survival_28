massiv = [20,2,30,6,10,7]
chet_massiv = []
nechet_massiv = []
time_massiv = []
km = 0

# распределяем массивы по четности и нечетности индекса элемента массива
for i in range(len(massiv)):
    if i % 2 == 0:
        chet_massiv.append(massiv[i])
    else:
        nechet_massiv.append(massiv[i])

# преобразовывем нечетный массив во временной
for i in range(len(nechet_massiv)):
    if i == 0:
        time_massiv.append(nechet_massiv[i])
    else:
        time_massiv.append(nechet_massiv[i] - nechet_massiv[i-1])

# рассчитываем километраж
for i in range(len(time_massiv)):
    km += chet_massiv[i] * time_massiv[i]
    
print('chet =', chet_massiv)
print('nechet =', nechet_massiv)
print('временной массив =', time_massiv)
print('километраж =', km)
