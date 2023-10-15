list1 = []
num = int(input("Введіть число: "))
while num > 0:
    a = num % 10
    list1.append(a)
    num//=10
list1.append(num)
if len(list1) == len(set(list1)):
    print("Ні")
else:
    print("Так")
