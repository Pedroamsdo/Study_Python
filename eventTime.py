def justNumber(beginning):
    number = ''.join(
        caractere for caractere in beginning if caractere.isdigit())
    return int(number)


def confirmation(hourB, hourF):
    if (hourB == hourF):
        return 0
    else:
        return -1


def durationOfEvent(dayB, hourB, dayF, hourF):
    secondsB = 3600*hourB[0] + 60*hourB[1] + hourB[2]
    secondsF = 3600*hourF[0] + 60*hourF[1] + hourF[2]
    dayDuration = dayF - dayB + confirmation(hourB, hourF)
    if dayDuration < 0:
        dayDuration = 0
    if(hourF[0] - hourB[0] > 0):
        eventH = int((secondsF - secondsB)/3600)
        eventM = int(((secondsF - secondsB) % 3600)/60)
        eventS = int(((secondsF - secondsB) % 3600) % 60)
    elif(hourF[0] - hourB[0] < 0):
        dif = abs(secondsF - secondsB)
        eventH = int((86400 - dif)/3600)
        eventM = int(((86400 - dif) % 3600)/60)
        eventS = int(((86400 - dif) % 3600) % 60)
    elif(hourF[0] - hourB[0] == 0):
        if(hourF[1] - hourB[1] < 0):
            dif = abs(secondsF - secondsB)
            eventH = int((86400 - dif)/3600)
            eventM = int(((86400 - dif) % 3600)/60)
            eventS = int(((86400 - dif) % 3600) % 60)
        else:
            eventH = int((secondsF - secondsB)/3600)
            eventM = int(((secondsF - secondsB) % 3600)/60)
            eventS = int(((secondsF - secondsB) % 3600) % 60)
    print(f'{dayDuration} dia (s)')
    print(f'{eventH} hora (s)')
    print(f'{eventM} minuto (s)')
    print(f'{eventS} segundo (s)')


def event():
    beginning = input()
    beginningNumber = justNumber(beginning)
    hourb = input()
    hourBeginning = list(map(int, hourb.split(':')))
    end = input()
    endNumber = justNumber(end)
    hourf = input()
    hourFinal = list(map(int, hourf.split(':')))
    durationOfEvent(beginningNumber, hourBeginning, endNumber, hourFinal)


event()
