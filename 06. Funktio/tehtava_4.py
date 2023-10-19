def listSum(list):
    sum = 0

    for x in list:
        sum += float(x)

    return sum


numberList = [2, 3, 4, 5, 7, 8, 9, 6, 5]

print(listSum(numberList))
