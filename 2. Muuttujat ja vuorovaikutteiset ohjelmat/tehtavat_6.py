import random

kolmenumeroinenKoodi = []
neljänumeroinenKoodi = []

i = 0

while i < 4:
    i += 1
    neljänumeroinenKoodi.append(random.randint(1, 6))

    if i <= 3:
        kolmenumeroinenKoodi.append(random.randint(0, 9))



print(''.join(map(str,kolmenumeroinenKoodi)))
print(''.join(map(str,neljänumeroinenKoodi)))


