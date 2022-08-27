def findNumbers(min, max):
    numbersBetwenn = max - min - 1
    aux = []
    for i in range(numbersBetwenn):
        aux.append(min + i + 1)
    dividingNumbers = []
    for element in aux:
        if((element % 5 == 2) or (element % 5 == 3)):
            dividingNumbers.append(element)
    return dividingNumbers


def main():
    numbers = []
    numbers.append(int(input()))
    numbers.append(int(input()))
    origin = min(numbers)
    end = max(numbers)
    if(origin != end):
        request = findNumbers(origin, end)
        for element in request:
            print(element)


main()
