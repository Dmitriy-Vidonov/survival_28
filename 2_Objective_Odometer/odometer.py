def odometer(oksana):
    chet_massiv = []
    nechet_massiv = []
    sum = 0
    speed = 0
    for i in range(len(oksana)):
        if i % 2 == 0:
            chet_massiv.append(oksana[i])
            sum += oksana[i]
        else:
            nechet_massiv.append(oksana[i])
    speed = sum / len(chet_massiv)
    
    return speed * nechet_massiv[len(nechet_massiv)-1]