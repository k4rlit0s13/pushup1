def minNum(samDaily, kellyDaily, difference):
    if kellyDaily <= samDaily:
        return -1
    return -(-difference // (kellyDaily - samDaily))  # División redondeando hacia arriba

# Ejemplo de uso
print(minNum(3, 5, 5))  # Salida: 3
print(minNum(4, 4, 10)) # Salida: -1
print(minNum(2, 6, 8))  # Salida: 2
