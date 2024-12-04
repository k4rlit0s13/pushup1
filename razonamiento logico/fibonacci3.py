def primeros_fibonacci(m):
    a, b = 0, 1
    for _ in range(m):
        print(a, end=" ")
        a, b = b, a + b
        
m = int(input("Ingrese la cantidad de números de Fibonacci: "))
primeros_fibonacci(m)
