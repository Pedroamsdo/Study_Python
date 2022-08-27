pair = [1, 1]
while(pair[0] > 0 and pair[1] > 0):
    pair = list(map(int, input().split()))
    if((pair[0] == pair[1]) and pair[0] > 0 and pair[1] > 0):
        print(f'{pair[0]} Sum={pair[0]}')
    elif(pair[0] > 0 and pair[1] > 0):
        aux = []
        origin = min(pair)
        end = max(pair)
        count = end - origin - 1
        aux.append(origin)
        for i in range(count):
            aux.append(origin + i + 1)
        aux.append(end)
        sumOfValues = sum(aux)
        aux2 = ['Sum=', str(sumOfValues)]
        strValues = ''.join(aux2)
        auxString = list(map(str, aux))
        auxString.append(strValues)
        sequence = ' '.join(auxString)
        print(sequence)
