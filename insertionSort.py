# Efficient for small data values.
# Good for datasets that ia already partially sorted.
def createArray(arraySize):
    array = []
    for index in range(arraySize):
        array.append(int(input(f'Valor do elemento {index}:')))
    return array


def sort(array):
    vectorSize = len(array) - 1
    for index in range(vectorSize):
        for index in range(vectorSize):
            if (array[index + 1] < array[index]) and (index != vectorSize):
                aux = array[index]
                array[index] = array[index + 1]
                array[index + 1] = aux
    return array


def insertionSort():
    arraySize = int(input('Size of array: '))
    array = createArray(arraySize)
    print(array)
    sortedArray = sort(array)
    print(sortedArray)


insertionSort()
