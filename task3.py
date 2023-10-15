list1 = []
while True:
    num = int(input("Введіть число"))
    if num == 0:
        break
    list1.append(num)
sum = sum(list1)
print("Сума: ", sum)
quantity = len(list1)
avrg = sum/quantity
print("Середнє значення: ", avrg)
max=max(list1)
min=min(list1)
print("Максимальне значення:",max,"\nМінімальне значення: ", min)
unprd=0
for num in list1:
        if num%2==0:
         unprd=unprd+1
print("Кількість непарних чисел: ", unprd)

