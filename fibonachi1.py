def fibonacci(n):
    if n < 0:
        return "El número debe ser un entero no negativo."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
try:
    n = int(input("Ingrese un número entero n para calcular el n-ésimo número de Fibonacci: "))
    resultado = fibonacci(n)
    print(f"El {n}-ésimo número de Fibonacci es: {resultado}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
