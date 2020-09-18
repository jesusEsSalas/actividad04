def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)

limite = int(input("Establezca un límite para calcular e: "))
n = 0
e = 0
while n < limite:
    e += 1/factorial(n)
    n += 1

print("e:",e)