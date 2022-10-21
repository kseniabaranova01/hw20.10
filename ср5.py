def func():
    n = int(input('Введите ваше число'))
    k = int(input("выберите систему счисления (2 или 8)"))
    if (k!= 2) and (k!= 8): print ("неккоректные значения")
    otvet = ""
    while n>=1:
        i= str(n%k)
        otvet = otvet+i
        n=n//k
    otvet=otvet[::-1]
    return otvet

print(func())
