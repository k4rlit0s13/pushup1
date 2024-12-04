def multiplicacion_rusa(multiplicador, multiplicando):
    resultado = 0
    while multiplicador > 0:
        if multiplicador % 2 != 0:
            resultado += multiplicando
        multiplicador //= 2
        multiplicando *= 2
    return resultado

multiplicador = int(input("Ingrese el multiplicador: "))
multiplicando = int(input("Ingrese el multiplicando: "))
print("Resultado:", multiplicacion_rusa(multiplicador, multiplicando))
