def sort(array):
    aux = []
    for i in range(len(array)):
        minValue = min(array)
        index = array.index(minValue)
        aux.append(minValue)
        array.pop(index)
    return aux


def selectionSort():
    array = input('Array separataded with ",": ').split(',')
    array_int = list(map(int, array))
    sortedArray = sort(array_int)
    print(sortedArray)


selectionSort()
