def odometer(oksana):
    chet_massiv = []
    nechet_massiv = []
    time_massiv = []
    km = 0

    for i in range(len(massiv)):
        if i % 2 == 0:
            chet_massiv.append(massiv[i])
        else:
            nechet_massiv.append(massiv[i])

    for i in range(len(nechet_massiv)):
        if i == 0:
            time_massiv.append(nechet_massiv[i])
        else:
            time_massiv.append(nechet_massiv[i] - nechet_massiv[i-1])

    for i in range(len(time_massiv)):
        km += chet_massiv[i] * time_massiv[i]

    return km #вывод
