def es_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

n = int(input("Ingrese un número: "))
print("it's Fibonacci" if es_fibonacci(n) else "No Fibonacci")
