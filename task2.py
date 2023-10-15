n=int(input("Введіть число: "))
result=[]
for num in range(1, n+1):
    sqr=num**2
    lastnum=sqr%10
    if lastnum==num:
        result.append(num)
print(result)
