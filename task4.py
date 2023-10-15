num = 0
n = int(input("Введіть число N: "))
while True:
    sqrnum = num ** 2
    if sqrnum < n:
        print(sqrnum)
    else:
        break

    num += 1

