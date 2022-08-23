n = int(input())
for i in range(n):
    number = int(input())
    if(number == 0):
        print('NULL')
    elif(number % 2 == 0):
        if(number < 0):
            print('EVEN NEGATIVE')
        if(number > 0):
            print('EVEN POSITIVE')
    elif(number % 2 != 0):
        if(number < 0):
            print('ODD NEGATIVE')
        if(number > 0):
            print('ODD POSITIVE')
