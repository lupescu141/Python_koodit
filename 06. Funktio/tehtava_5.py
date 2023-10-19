def listPariton(list):
    sum = []

    for x in list:
        if float(x) % 2 == 0:
            sum.append(x)

    return sum


numberList = [2, 3, 4, 5, 7, 8, 9, 6, 5]

print(numberList)
print(listPariton(numberList))
